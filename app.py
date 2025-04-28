import logging
from flask import Flask, render_template, request, jsonify
from services.openrouter_service import generate_email_response

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

@app.route('/')
def index():
    app.logger.info("rendering index page")
    return render_template('index.html')

@app.route("/generate", methods=['POST'])
def generate():
    try:
        data = request.get_json()
        user_email = data.get("email")
        tone = data.get("tone")

        if not user_email or not tone:
            app.logger.warning("missing email or tone in request")
            return jsonify({"response": "Email and tone fields are required."}), 400

        app.logger.info(f"generating email with tone {tone}")
        ai_reply = generate_email_response(user_email, tone)

        app.logger.info("Respond generated successfully")
        return jsonify({"response": ai_reply})

    except Exception as e:
        app.logger.error(f"Error generating response: {str(e)}", exc_info=True)
        return jsonify({"response": f"Error generating response: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
