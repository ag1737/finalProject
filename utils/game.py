import json
import pandas as pd

from utils import utils


class Game:
    player_entities = []
    hero_entities = []
    map_entities = []

    def __init__(self, file_location: str):
        f = open(file_location)
        self.frames = json.load(f)
        self.parse_frames(self.frames)

    def get_players(self):
        player_df = pd.DataFrame(self.player_entities)
        player_df.reset_index(inplace=True, drop=True)
        player_df = player_df.set_index("Frame").bfill()
        player_df["PLAYER"] = player_df["UID"]

        return player_df

    def get_heros(self):
        hero_df = pd.DataFrame(self.hero_entities)
        hero_df.reset_index(inplace=True, drop=True)
        hero_df = hero_df.set_index("Frame").bfill()

        return hero_df

    def parse_frames(self, frames):
        frames = frames["frames"]
        entities = [x["Entities"] for x in frames]

        for frame_num, frame in enumerate(entities):
            print(f"######FRAME NUMBER {frame_num}##########")
            for ID, entity in frame.items():
                if entity["ENTITY_TYPE"] == "PlayerEntity":
                    dct = {k: [v] for k, v in entity.items()}
                    dct["Frame"] = frame_num
                    utils.clean_dict(dct)
                    self.player_entities.append(dct)


                elif entity["ENTITY_TYPE"] == "HeroEntity":
                    dct = {k: [v] for k, v in entity.items()}
                    dct["Frame"] = frame_num
                    utils.clean_dict(dct)
                    self.hero_entities.append(dct)

                elif entity["ENTITY_TYPE"] == "Dota2MapEntity":
                    dct = {k: [v] for k, v in entity.items()}
                    dct["Frame"] = frame_num
                    utils.clean_dict(dct)
                    self.map_entities.append(dct)