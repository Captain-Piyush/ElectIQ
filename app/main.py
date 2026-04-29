import os
import logging
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

system_instruction = (
    "You are ElectIQ, an interactive, non-partisan election process assistant. "
    "Your goal is to help citizens understand the democratic process, including voter "
    "registration, primaries, general elections, how votes are counted, and the electoral college. "
    "Be objective, clear, encouraging, and provide easy-to-understand explanations. "
    "If a question is outside the scope of elections or civic processes, politely steer the conversation back."
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    message = data["message"]
    
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=message
        )
        return jsonify({"response": response.text})
    except Exception as e:
        logger.error(f"Error communicating with Gemini API: {str(e)}")
        return jsonify({"error": "Failed to generate response."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
