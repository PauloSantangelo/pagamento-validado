import os
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__, template_folder=os.path.abspath("templates"))

@app.route("/")
def home():
    return render_template("payment_success.html")

@app.route("/webhook", methods=["POST"])
def asaas_webhook():
    data = request.json  # Captura os dados recebidos do Asaas

    # Verifica se o pagamento foi confirmado
    if data.get("event") == "PAYMENT_CONFIRMED":
        payment_id = data.get("payment", {}).get("id")  # Captura o ID do pagamento
        print(f"Pagamento confirmado: {payment_id}")

        # Redireciona para a página de pagamento validado
        return redirect("https://pagamento-validado-paulo-santangelos-projects.vercel.app/")

    return jsonify({"status": "ignored"}), 200

if __name__ == "__main__":
    app.run(debug=True)
