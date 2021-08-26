import json

def load():
    with open('cred.json') as json_file:
        data = json.load(json_file)
        return data

        
