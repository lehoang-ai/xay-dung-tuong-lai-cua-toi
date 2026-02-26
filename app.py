from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Bạn là AI hỗ trợ học sinh."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)