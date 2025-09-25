from os import environ
from app import create_app  

app = create_app()

if __name__ == "__main__":
    host = environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(environ.get("FLASK_RUN_PORT", 8000))
    debug = environ.get("FLASK_DEBUG", "1") != "0"
    app.run(host=host, port=port, debug=debug)