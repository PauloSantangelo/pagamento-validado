import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.abspath("templates"))

@app.route("/")
def home():
    return render_template("payment_success.html")

if __name__ == "__main__":
    app.run(debug=True)
