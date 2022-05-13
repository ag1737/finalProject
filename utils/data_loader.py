import os

import pandas as pd
import numpy as np
import json
import pprint
import glob
import pathlib

from tqdm import tqdm

from utils.game import Game


class DataLoader:

    def __init__(self, folder_location: str):
        filenames = f"{folder_location}/*"
        self.files = glob.glob(filenames)
        self.__index = 0

    def __next__(self):
        yield self.files[self.__index]
        self.__index += 1

    def load_files(self):
        self.game_dict = {}
        for game_file in tqdm(self.files):
            self.game_dict[os.path.basename(game_file).split(".")[0]] = Game(game_file)
