import pickle
import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.utils.helpers import load_config,save_object


def data_transformer():
    config = load_config()
    train_set=pd.read_csv(config["data"]["train_path"])
    test_set=pd.read_csv(config["data"]["test_path"])
    train_features = train_set.drop(columns=["price"])
    train_target = train_set["price"]
    test_features = test_set.drop(columns=["price"])
    test_target = test_set["price"]

    num_cols = ['area','bedrooms','bathrooms','balcony','parking','lift','price_sqft']
    cat_cols = ['status','neworold','furnished_status','type_of_building','city']

    num_pipeline = Pipeline([("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())])#here it take list of tuples
    cat_pipeline = Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("ohe",OneHotEncoder()),("scaler",StandardScaler(with_mean=False))])
    
    preprocessor = ColumnTransformer([("num_pipeline",num_pipeline,num_cols),("cat_pipeline",cat_pipeline,cat_cols)])

    transformed_train_feature = preprocessor.fit_transform(train_features)

    transformed_test_feature = preprocessor.transform(test_features)

    with open(config["artifacts"]["transformer_path"],"wb") as f:
        pickle.dump(preprocessor,f)

    return transformed_train_feature,np.array(train_target),transformed_test_feature,np.array(test_target)