from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(student_number="200556572")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Here you'd process the request from Dialogflow and return a response
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    # Depending on the intent, you can customize your response
    if intent_name == 'Contact US':
        # Call an external API to get weather info perhaps?
        response_text = "THi, For more information and question kindly contact travel@companion .com"
    elif intent_name == 'Accommodation':
        # Similarly, for crypto rates, call the relevant API and construct your response
        response_text = "What are the best hotel in the area"
    else:
        response_text = "Sorry, I didn't understand that."

    return jsonify(fulfillmentText=response_text)

if __name__ == '__main__':
    app.run(debug=True)
