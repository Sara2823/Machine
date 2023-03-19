import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataSplitsPaths():
    # Create a variable that holds the three paths for the data(original, train, test)
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
        
# if __name__ == "__main__":
#     data_ingestion_obj = DataIngestion()
#     data_ingestion_obj.split_and_store()
