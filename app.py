from flask import Flask

app = Flask(__name_)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

if__name_ == "__main_":
    app.run(debug=True)
