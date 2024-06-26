from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200556572"})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON request
    req = request.get_json(force=True)
    
    # Extract the intent name from the request
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    # Initialize a response dictionary
    response = {"fulfillmentMessages": []}
    
    # Handle the Phonebrand intent
    if intent_name == "Phonebrand":
        # List of phone brands
        phone_brands = ["Apple", "Samsung", "LG", "Motorola", "Blackberry"]
        # Building the response text
        response_text = "List of phone brands available in the market are: \n" + "\n".join([f"{i+1} - {item}" for i, item in enumerate(phone_brands)])
        
        # Set the response in the fulfillmentMessages format
        response["fulfillmentMessages"].append({
            "text": {"text": [response_text]}
        })
    
    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
