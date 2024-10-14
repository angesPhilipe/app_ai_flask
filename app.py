from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"<marquee><h1>Hello Zizi content !!!!</h1></marquee>"



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)