import json
import utils.utils

class Game():
    player_entities = []
    hero_entities = []
    map_entities = []

    def __init__(self,file_location:str):
        f = open(file_location)
        self.frames = json.load(f)



    def parse_frames(self,frames):
        frames = frames["frames"]
        entities = [x["Entities"] for x in frames]

        for framenum, frame in enumerate(entities):
            print(f"######FRAME NUMBER {framenum}##########")
            for ID, entity in frame.items():
                if entity["ENTITY_TYPE"] == "PlayerEntity":
                    dct = {k: [v] for k, v in entity.items()}
                    dct["Frame"] = framenum
                    utils.clean_dict(dct)
                    self.player_entities.append(dct)


                elif entity["ENTITY_TYPE"] == "HeroEntity":
                    dct = {k: [v] for k, v in entity.items()}
                    dct["Frame"] = framenum
                    utils.clean_dict(dct)
                    self.hero_entities.append(dct)

                elif entity["ENTITY_TYPE"] == "Dota2MapEntity":
                    dct = {k: [v] for k, v in entity.items()}
                    dct["Frame"] = framenum
                    utils.clean_dict(dct)
                    self.map_entities.append(dct)