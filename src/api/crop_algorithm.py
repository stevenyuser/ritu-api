'''
        "lat": coordinates.latitude,
        "long": coordinates.longitude,
        "time": datetime.now() # datetime object
'''
import requests
from datetime import datetime

# models 
# work around - not good code, should import from src.models.crop_recs_model
class Crop_Recs:
    def __init__(self, name, pests: [], extreme_weather_conditions):
        self.name = name # string
        self.pests = pests # array of Pest objects
        self.extreme_weather_conditions = extreme_weather_conditions # string

    def serialize(self):
        return {
            'name': self.name, # e.g. "rice"
            'pests': self.pests, # array of Pest objects
            'extreme_weather_conditions': self.extreme_weather_conditions # e.g. "drought"
        }

class Pest:
    def __init__(self, name, risk_level):
        self.name = name # string
        self.risk_level = risk_level # string

    def serialize(self):
        return {
            'name': self.name, # e.g. "aphids"
            'risk_level': self.risk_level # high, medium, or low
        }

# crop algorithm

def crop_algorithm(llt: dict):

    # lat = 0
    # long = 0
    # time = datetime.datetime.now().strftime('%Y-%m-%dT%H') + ":00"

    # if 'lat' in llt.keys():
    #     lat = llt['lat']
    
    # if 'long' in llt.keys():
    #     long = llt['long']

    # if 'time' in llt.keys():
    #     time = llt['time'].strftime('%Y-%m-%dT%H') + ":00"

    # req_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,windspeed_10m,relativehumidity_2m,precipitation_probability,soil_temperature_0cm"
    # req_json = requests.request(url=req_url, method='GET').json()
    
    # try:
    #     time_index = req_json['hourly']['time'].index(time)
    # except:
    #     time_index = 0
    
    # pests = []

    # if req_json['hourly']['soil_temperature_0cm'][time_index] > 10 and req_json['hourly']['windspeed_10m'][time_index] < 3:
    #     pests.append(Pest("aphids", "high"))

    # extreme_weather_conditions = None

    # if req_json['hourly']['temperature_2m'][time_index] > 20 and req_json['hourly']['precipitation_probability'][time_index] < 0.1:
    #     extreme_weather_conditions = 'Drought'

    pests = [Pest("Stem borer", "Low"), Pest("Leaf roller", "Low"), Pest("Gall midge", "Low")]

    extreme_weather_conditions = "None"

    return Crop_Recs("Rice", pests=pests, extreme_weather_conditions=extreme_weather_conditions)

if __name__ == '__main__':
    crop_algorithm(
        {
            'lat': 42.4534,
            'long': 76.4735,
            'time': datetime.now()
        }
    )