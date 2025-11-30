from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    system_msg = data.get("system", "تو یک دستیار فارسی هستی.")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "خطا: " + str(e)})

if __name__ == "__main__":
    app.run(debug=True)
