from src.data_process.data_transformation import data_transformer
from src.model.model_trainer import model_trainer


if __name__=="__main__":
    x_train,y_train,x_test,y_test = data_transformer()
    model_trainer(x_train,y_train,x_test,y_test)