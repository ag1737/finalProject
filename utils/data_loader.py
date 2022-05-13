import pandas as pd
import numpy as np
import json
import pprint
import os


class DataLoader():

    def __int__(self, folder_location: str):
        file = open(folder)

    def folder_parser(self, folder: str):
        directory = os.fsencode(folder)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            print(filename)
