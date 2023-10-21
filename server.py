from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def process_data(data, model = {}):
    words = data.split(" ")
    for i, word in enumerate(words):
        print(i)
        if i == len(words) - 1:
            break
        
        if word not in model:
            model[word] = {}

        next_word = words[i + 1]
        if next_word not in model[word]:
            model[word][next_word] = 0

        model[word][next_word] += 1

    return model

def pick(model_entry):
    options = []
    for word, times in model_entry.items():
        options.extend([word] * times)

    return random.choice(options)

def generate(model, prompt, words = 10):
    output = [prompt]

    while output[-1] in model and len(output) < words:
        word = pick(model[output[-1]])
        output.append(word)

    return " ".join(output)


@app.route("/train", methods=["POST"])
def handle_train():
    model = request.json.get("model", {})
    text = request.json["text"]

    modified_model = process_data(text, model=model)

    return jsonify({
        "model": modified_model
    })

@app.route("/generate", methods=["POST"])
def handle_generate():
    model = request.json.get("model")
    prompt = request.json.get("prompt")

    return jsonify({
        "text": generate(model, prompt)
    })

@app.route("/ping", methods=["GET"])
def handle_ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)