from flask import Flask

app = Flask(__name_)

@app.route("/user")
def hello_admin():
    return "Hello An"

if__name_ == "__main_":
    app.run(debug=True)
