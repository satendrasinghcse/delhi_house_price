import pandas as pd
from src.utils.helpers import load_config
from sklearn.model_selection import train_test_split



def data_lodder():
    config = load_config() # It return a dictionary
    df = pd.read_csv("notebook/newdata.csv")
    df.to_csv(config["data"]["raw_data_path"],index=False)
        
    train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

    train_set.to_csv(config["data"]["train_path"],index=False)

    test_set.to_csv(config["data"]["test_path"],index=False)
    