import random

def process_data(data, model = {}):
    words = data.split(" ")
    for i, word in enumerate(words):
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