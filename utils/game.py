import json
import pandas as pd
from shapely.geometry import Point
from tqdm import tqdm
import swifter
from utils import utils
from utils.map_utils import lane_from_coords


class Game:
    player_entities = []
    hero_entities = []
    map_entities = []

    def __init__(self, file_location: str):
        f = open(file_location)
        self.frames = json.load(f)
        self.parse_frames(self.frames)

    def get_avg_player_gold(self):
        df = self.player_df.loc[self.player_df.index.min() + 900].groupby("ID").mean()["GOLD"]
        self.avg_player_gold = df
        return df

    def get_avg_player_exp(self):
        df = self.player_df.loc[self.player_df.index.min() + 900].groupby("ID").mean()["XP"]
        self.avg_player_exp = df
        return df

    def get_players(self):
        player_df = pd.DataFrame(self.player_entities)
        player_df.reset_index(inplace=True, drop=True)
        player_df = player_df.set_index("Frame").bfill()
        player_df["PLAYER"] = player_df["UID"]

        self.player_df = player_df
        return player_df

    def get_heros(self):
        hero_df = pd.DataFrame(self.hero_entities)
        hero_df.reset_index(inplace=True, drop=True)
        hero_df = hero_df.set_index("Frame").bfill()

        hero_df["map_position"] = hero_df.swifter.apply(
            lambda x: lane_from_coords(Point(float(x["XPOS"]), float(x["YPOS"]))), axis=1)
        self.hero_df = hero_df
        return hero_df

    def get_lane_percentage(self):
        f = lambda x: x.size / self.hero_df.groupby('ID', dropna=False).size()[x.iloc[0]] * 100

        df = (self.hero_df.groupby(['ID', 'map_position'], dropna=False)
              .agg(counts=('map_position', 'size'),
                   prcntg=('ID', f))
              ).unstack(fill_value=0).stack()
        self.lane_percentage = df
        return df

    def parse_frames(self, frames):
        frames = frames["frames"]
        entities = [x["Entities"] for x in frames]

        for frame_num, frame in enumerate(entities):
            for ID, entity in frame.items():
                if entity["ENTITY_TYPE"] == "PlayerEntity":
                    dct = {k: v for k, v in entity.items()}
                    dct["Frame"] = frame_num
                    self.player_entities.append(dct)


                elif entity["ENTITY_TYPE"] == "HeroEntity":
                    dct = {k: v for k, v in entity.items()}
                    dct["Frame"] = frame_num
                    self.hero_entities.append(dct)
