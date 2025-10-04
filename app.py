# from flask import Flask, render_template, request, jsonify
# import os
# import openai
# from openai.error import RateLimitError
# from dotenv import load_dotenv
# from flask import Flask, render_template, request, jsonify

# load_dotenv()

# app = Flask(__name__)

# # Load API key from environment variable
# openai.api_key = os.getenv("OPENAI_API_KEY")
# if not openai.api_key:
#     raise ValueError("Please set your OPENAI_API_KEY environment variable!")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/ask", methods=["POST"])
# def ask():
#     user_input = request.json.get("messag")
#     if not user_input:
#         return jsonify({"error": "No message provided."}), 400

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": user_input}]
#         )
#         answer = response['choices'][0]['message']['content']
#         return jsonify({"answer": answer})

#     except RateLimitError:
#         return jsonify({"answer": "⚠️ Quota exceeded! Please check your OpenAI plan."})
#     except Exception as e:
#         return jsonify({"answer": f"⚠️ Error: {str(e)}"})

# if __name__ == "__main__":
#     app.run(debug=True)
import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize the OpenAI client
# It automatically reads the OPENAI_API_KEY from the environment
try:
    client = OpenAI()
except Exception as e:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.") from e

@app.route("/")
def home():
    """Renders the main chat page."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handles the AI query from the frontend."""
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    try:
        # Modern syntax for the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        # Extract the answer from the response object
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})

    except RateLimitError:
        return jsonify({"answer": "⚠️ Quota exceeded! Please check your OpenAI plan."})
    except Exception as e:
        return jsonify({"answer": f"⚠️ An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)