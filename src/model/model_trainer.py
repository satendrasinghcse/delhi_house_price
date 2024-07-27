import pickle
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from src.utils.helpers import load_config

def model_trainer(x_train,y_train,x_test,y_test):
    report = {}
    models = {"Linear Regression":LinearRegression(),
          "Decision Tree":DecisionTreeRegressor(),
          "XG boost":XGBRegressor(),
          "Ada boost":AdaBoostRegressor(),
          "Gradient boost":GradientBoostingRegressor(),
          "Random Forest":RandomForestRegressor()
          }
    for i in range(len(list(models))):
        model = list(models.values())[i]
        model_name = list(models.keys())[i]
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        r2 = r2_score(y_test,y_pred)
        report[model_name]=r2
        print("r2 scor for ",model_name,"=",r2)
    #print(max(report.values()))
    key = None
    for i in report:
        if report[i]==max(report.values()):
            key=i
            break
    print(report[key])
    best_model = models[key]
    best_model.fit(x_train,y_train)
    config = load_config()
    with open(config["artifacts"]["best_model_path"],"wb") as f:
        pickle.dump(best_model,f)