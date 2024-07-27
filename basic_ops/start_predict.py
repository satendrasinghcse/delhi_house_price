import pandas as pd
from src.model.predict import predicted_data


if __name__=="__main__":

    new_data = {
    "area":1500,
    "bedrooms":4,
    "bathrooms":3,
    "balcony":2,
    "status":"Ready to Move",
    "neworold":"New Property",
    "parking":2,
    "furnished_status":"Furnished",
    "lift":2,
    "type_of_building":"Flat",
    "price_sqft":4500,
    "city":"New Delhi",}
    new_data_df = pd.DataFrame([new_data])
    h_price  = predicted_data(new_data_df)
    print(h_price[0])