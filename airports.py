import json

def get_airport(icao):
    with open("backend/data/airports.json") as f:
        data = json.load(f)
    return data.get(icao.upper())
