import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_training import ModelTrainerConfig
from src.components.model_training import ModelTrainer

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# with the use of dataclass, one can directly define variables and their data types in a class
@dataclass
class DataSplitsPaths():
    # Create a variable that holds the three paths for the data(original, train, test)
    # Provides the inputs to this data_ingestion component
    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str  = os.path.join("artifacts", "train.csv")
    test_data_path:str  = os.path.join("artifacts", "test.csv")



class DataIngestion():
    # A class to split and store the data
    def __init__(self):
        self.splits_paths = DataSplitsPaths()

    def split_and_store(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/stud.csv") #Read the data from somewhere
            logging.info("Dataset was read into a dataframe")

            # Create the "artifacts" folder
            # here, raw_data_path can be replaced by either train_data_path or test_data_path
            # كده كده هيبني اسم المجلد مش ملف csv
            os.makedirs(os.path.dirname(self.splits_paths.raw_data_path), exist_ok=True)

            #Store the data:
            df.to_csv(self.splits_paths.raw_data_path, index=False, header=True)

            train, test = train_test_split(df, test_size= 0.2, random_state=42)
            train.to_csv(self.splits_paths.train_data_path, index=False, header=True)
            test.to_csv(self.splits_paths.test_data_path, index=False, header=True)

            logging.info("Data was splitted and stored")

            return ( # return the paths to use them in the transformation step
                self.splits_paths.train_data_path,
                self.splits_paths.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()
    train_data_path, test_data_path = data_ingestion_obj.split_and_store()

    data_transformation = DataTransformation()
    train_arr, test_arr, _= data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
