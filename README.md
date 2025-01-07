# Wood Price Estimator - intent classification and entity extraction

A smart wood price estimation service that uses Natural Language Processing to understand and process wood pricing queries. Quick and free intent classification and entity extraction.

Example input:
```
curl -X POST http://localhost:5000/estimate \
  -H "Content-Type: application/json" \
  -d '{"message": "How much would 50 square feet of oak wood cost?"}'
```
Example output:
```
{
    "price_per_unit": 5.75,
    "quantity": 1,
    "total_price": 5.75,
    "unit": "square foot",
    "wood_type": "oak"
}
```

## Features

- Natural language processing for wood price queries
- Support for multiple wood types
- Quantity and price calculations
- RESTful API endpoint
- Easy to extend and customize

## Setup

1. Clone the repository
```
git clone https://github.com/CodingSancho/woodFAQ.git
cd wood-price-estimator
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Set up Wit.ai
- Create a new Wit.ai app at https://wit.ai
- Add intents for wood price estimation
- Create entities for wood_type and quantity
- Train your model with sample utterances

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your Wit.ai access token
```

5. Run the application
```bash
python woodPrice.py
```

## Usage

Send a POST request to `/estimate` with a JSON body:

```bash
curl -X POST http://localhost:5000/estimate \
  -H "Content-Type: application/json" \
  -d '{"message": "How much would 50 square feet of oak wood cost?"}'
```

Sample response:
```json
{
  "wood_type": "oak",
  "quantity": 50,
  "price_per_unit": 5.75,
  "unit": "square foot",
  "total_price": 287.50
}
```

## Wit.ai Setup Guide

1. Create intents:
   - get_wood_price
   - get_wood_types
   - get_quantity

2. Create entities:
   - wood_type (keyword)
   - quantity (number)

3. Sample training utterances:
   - "How much does oak wood cost?"
   - "What's the price of 20 square feet of maple?"
   - "I need a price estimate for cedar wood"
   - "Can you tell me the cost of walnut?"
