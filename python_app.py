from flask import Flask
app = Flask(__name__)


#Adding some comments
@app.route('/')
def home():
    return "Hello Prethumnan!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
