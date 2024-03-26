from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Corrected to return a JSON response properly
    return jsonify({"student_number": "200556572"})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Corrected list of phone brands with proper string quoting
    Phonebrand = ["Apple", "Samsung", "LG", "Motorola", "Blackberry"]

    # Corrected the building of the response text
    responseText = "List of phone brands available in the market are: \n" + "\n".join([f"{i+1} - {item}" for i, item in enumerate(Phonebrand)])

    # Corrected dictionary structure for fulfillmentMessages
    res = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [responseText]
                }
            }
        ]
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
