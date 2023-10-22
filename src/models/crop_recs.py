

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

if __name__=="__main__":
    # testing
    crop_recs = Crop_Recs("rice", [Pest("aphids", "high"), Pest("daniels", "low")], "drought")
    print(crop_recs.serialize())
    print()
    print(crop_recs.serialize()['pests'][1].serialize()['name']) # daniels