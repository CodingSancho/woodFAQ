# Wood Price Estimator
# Author: Viktor Lantos

import os
from wit import Wit
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Wit(os.getenv('WIT_ACCESS_TOKEN'))

# Sample wood pricing database
WOOD_PRICES = {
    'pine': {'price_per_foot': 2.50, 'unit': 'square foot'},
    'oak': {'price_per_foot': 5.75, 'unit': 'square foot'},
    'maple': {'price_per_foot': 4.50, 'unit': 'square foot'},
    'cedar': {'price_per_foot': 3.75, 'unit': 'square foot'},
    'walnut': {'price_per_foot': 8.00, 'unit': 'square foot'}
}

def process_wood_query(wit_response):
    try:
        entities = wit_response['entities']
        wood_type = next((entity['value'] for entity in entities.get('wood_type:wood_type', [])), None)
        quantity = next((entity['value'] for entity in entities.get('quantity:quantity', [])), 1)
        
        if wood_type and wood_type.lower() in WOOD_PRICES:
            price_info = WOOD_PRICES[wood_type.lower()]
            total_price = price_info['price_per_foot'] * float(quantity)
            return {
                'wood_type': wood_type,
                'quantity': quantity,
                'price_per_unit': price_info['price_per_foot'],
                'unit': price_info['unit'],
                'total_price': round(total_price, 2)
            }
        return {'error': f'Wood type {wood_type} not found in database'}
    except Exception as e:
        return {'error': str(e)}

@app.route('/estimate', methods=['POST'])
def get_estimate():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        wit_response = client.message(user_message)
        result = process_wood_query(wit_response)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)