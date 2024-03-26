from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"student_number": "200556572"})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    # Logic to handle different intents
    # For simplicity, we'll send a static response
    response = {
        "fulfillmentText": "This is a response from your webhook!",
        # Add more fields as needed depending on the response structure you want
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
