from flask import Flask, render_template, request, jsonify
import os
import openai
from openai.error import RateLimitError
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

load_dotenv()

app = Flask(__name__)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("Please set your OPENAI_API_KEY environment variable!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("messag")
    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"answer": answer})

    except RateLimitError:
        return jsonify({"answer": "⚠️ Quota exceeded! Please check your OpenAI plan."})
    except Exception as e:
        return jsonify({"answer": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
