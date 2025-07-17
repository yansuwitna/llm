from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma:2b", user_input],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        response = result.stdout.strip()
    except Exception as e:
        response = f"Error: {e}"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
