import os

from waitress import serve

from app import create_app

if __name__ == "__main__":
    DEBUG = os.environ.get("DEBUG", False)
    PORT = os.environ.get("PORT", 8080)

    app = create_app()

    if DEBUG:
        app.run(host="0.0.0.0", port=PORT)
    else:
        serve(app, host="0.0.0.0", port=PORT)