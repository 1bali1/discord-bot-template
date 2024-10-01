# Import modules
import json

configPath = "config.json"


# Get config.json data
def getConfig():
    with open(configPath, "r") as f:
        data = json.load(f) 
    return data   
