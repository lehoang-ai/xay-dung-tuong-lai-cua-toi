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
            {"role": "system", "content": "Bạn là AI cố vấn tương lai. Nhiệm vụ của bạn là giúp học sinh xây dựng kế hoạch phát triển bản thân, định hướng nghề nghiệp và tạo lộ trình hành động cụ thể."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)