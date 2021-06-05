import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
FILE_PATH = os.path.join(BASE_DIR, 'ElectricCarData_Clean.csv')


def get_data():
    return pd.read_csv(FILE_PATH)
