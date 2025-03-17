from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def payment_success():
    return render_template("payment_success.html")

if __name__ == "__main__":
    app.run(debug=True)
