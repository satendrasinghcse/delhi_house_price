import pickle
from src.utils.helpers import load_config


def predicted_data(dict):
    config = load_config()
    with open(config["artifacts"]["transformer_path"],"rb") as f:
        trans = pickle.load(f)
    
    with open(config["artifacts"]["best_model_path"],"rb") as f:
        loaded_model = pickle.load(f)

    scaled_data = trans.transform(dict)
    y_pred = loaded_model.predict(scaled_data)
    return y_pred