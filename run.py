from config import Development
from flaskr import create_app
app = create_app(config=Development())

if __name__ == "__main__":
    app.run(port=1337)
