import json
import os

def load_config(filename):
    with open(filename, "r") as config_file:
        obj = json.loads(config_file.read())
        if obj["cache"]["dir"] == "DEFAULT":
            obj["cache"]["dir"] = f"{os.getcwd()}/newsletter_cache"
        return obj

