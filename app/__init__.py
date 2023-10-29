from flask import Flask, request, jsonify

from . import markov

def create_app():
    app = Flask(__name__)

    @app.route("/train", methods=["POST"])
    def handle_train():
        model = request.json.get("model", {})
        text = request.json["text"]

        modified_model = markov.process_data(text, model=model)

        return jsonify({
            "model": modified_model
        })

    @app.route("/generate", methods=["POST"])
    def handle_generate():
        model = request.json.get("model")
        prompt = request.json.get("prompt")
        length = request.json.get("length", 16)

        return jsonify({
            "text": markov.generate(model, prompt, words=length)
        })

    @app.route("/ping", methods=["GET"])
    def handle_ping():
        return "pong"

    return app