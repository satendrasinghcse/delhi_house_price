from flask import Flask, request, jsonify, render_template
import pandas as pd
from src.model.predict import predicted_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    
    # For demonstration purposes, let's assume a simple prediction algorithm
    # In a real application, you would use a machine learning model here
    area = float(data['area'])
    bedrooms = int(data['bedrooms'])
    bathrooms = int(data['bathrooms'])
    balcony = float(data['balcony'])
    parking = int(data['parking'])
    lift = float(data['lift'])
    price_sqft = float(data['price_sqft'])
    status = str(data['status'])
    neworold = str(data['neworold'])
    furnished_status = str(data['furnished_status'])
    type_of_building = str(data['type_of_building'])
    city = str(data['city'])


    new_data = {
    "area":area,
    "bedrooms":bedrooms,
    "bathrooms":bathrooms,
    "balcony":balcony,
    "status":status,
    "neworold":neworold,
    "parking":parking,
    "furnished_status":furnished_status,
    "lift":lift,
    "type_of_building":type_of_building,
    "price_sqft":price_sqft,
    "city":city}

    df = pd.DataFrame([new_data])
    predicted_price = predicted_data(df)

    



    # Simplified prediction logic (for demonstration purposes)
    #predicted_price = area * price_sqft + bedrooms * 100000 + bathrooms * 50000 + balcony * 20000 + parking * 30000 + lift * 50000 + status * 200000 + neworold * 150000 + furnished_status * 100000 + type_of_building * 100000

    return jsonify(predicted_price=predicted_price[0])

if __name__ == '__main__':
    app.run(debug=True)
