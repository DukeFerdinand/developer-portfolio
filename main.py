from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return "Hello World!"


if __name__ == "__main__":
    print("App running")
    app.run()
