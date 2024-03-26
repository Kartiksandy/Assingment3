from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200556572"})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming request
    req = request.get_json(silent=True, force=True)
    
    # Check if the intent is the one we're interested in
    if req.get("queryResult", {}).get("intent", {}).get("displayName") == "Phonebrand":
        # Define a list of phone brands
        phone_brands = ["Apple", "Samsung", "LG", "Motorola", "Blackberry"]
        
        # Create a response text listing the phone brands
        response_text = "List of phone brands available in the market are:\n" + "\n".join([f"{i+1}. {brand}" for i, brand in enumerate(phone_brands)])
        
        # Construct the response in the format Dialogflow expects
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [response_text]
                    }
                }
            ]
        }
        return jsonify(response)
    else:
        # Default response if the intent is not recognized
        response = {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": ["Sorry, I didn't understand that."]
                    }
                }
            ]
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
