
from flask import Flask, request, jsonify, render_template
from gemini_chat import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message")

    try:
        reply = get_response(user_msg)
        return jsonify({"reply": reply})
    except Exception as e:
        # Return error message instead of crashing
        return jsonify({
            "reply": "Gemini API is not enabled for this API key yet.",
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
