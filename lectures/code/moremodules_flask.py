from flask import Flask
app = Flask(__name__)

@app.route("/<name>")
@app.route("/")
def hello(name="World"):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True)  # only for debugging!