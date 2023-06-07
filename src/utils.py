import os
import sys
import dill
import pickle
import pandas as pd
import numpy as np
from src.exception import CustomException


def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as obj_file:
            pickle.dump(obj, obj_file)

    except Exception as e:
        raise CustomException(e, sys)
