from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hey this is new website which modified from old one"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
