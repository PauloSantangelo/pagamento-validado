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
    if data and data.get("event") == "PAYMENT_CONFIRMED":
        payment_id = data.get("payment", {}).get("id")  # Captura o ID do pagamento
        print(f"✅ Pagamento confirmado: {payment_id}")  # Log para depuração

        # Retorna URL de redirecionamento para a página de pagamento aprovado
        return jsonify({"status": "success", "message": "Pagamento confirmado", "redirect_url": "/" }), 200

    # Se não for um evento de pagamento confirmado, apenas ignora
    return jsonify({"status": "ignored", "message": "Evento não tratado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
