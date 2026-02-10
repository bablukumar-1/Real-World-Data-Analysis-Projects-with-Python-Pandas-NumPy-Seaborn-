from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator as gt

app = Flask(__name__)

# ✅ CORS full allow
CORS(app, supports_credentials=True)

@app.route("/translate", methods=["POST", "OPTIONS"])
def translate():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.get_json()
    print("DATA:", data)

    text = data["text"]
    target = data["target"]

    result = gt(target=target).translate(text)
    print("RESULT:", result)

    return jsonify({"translated_text": result}), 200

if __name__ == "__main__":
    app.run(debug=True)
