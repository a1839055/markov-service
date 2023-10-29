import random

import pytest

from app import create_app

def read_file(filename):
    with open(filename, "r") as f:
        return " ".join(f.readlines())

@pytest.fixture()
def app():
    app = create_app()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_train(client):
    text = read_file("sample-1.txt")

    response = client.post(
        "/train",
        json={
            "text": text
        }
    )

    model = response.json["model"]

    print(model)

    assert model["cat"]["is"] == 2
    assert model["is"]["big"] == 1
    assert model["is"]["orange"] == 1

def test_generate(client):
    random.seed(1)

    model = {
        "the": {
            "cat": 2,
        },
        "cat": {
            "is": 2
        },
        "is": {
            "big": 1,
            "orange": 1
        },
        "big": {
            "and": 1
        }
    }

    response = client.post(
        "/generate",
        json={
            "model": model,
            "prompt": "the"
        }
    )

    text = response.json.get("text")

    assert text == "the cat is orange"
    