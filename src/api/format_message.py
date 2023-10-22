import datetime

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


# text message
def format_message(crop_recs: Crop_Recs, name: str):
    return f'''
    [RITU NOTIFICATION]
    {name}'s Weekly Crop Projection for {datetime.datetime.now().strftime("%m/%d/%Y")} - {(datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%m/%d/%Y")}
    ---
    'Name': {crop_recs.name.capitalize()},
    'Pests': {", ".join([" - ".join((pest.name.capitalize(), pest.risk_level.capitalize())) for pest in crop_recs.pests])},
    'Extreme Weather Conditions': {crop_recs.extreme_weather_conditions.capitalize()}.
    ---
    See Ritu app for more detailed information.
    '''

if __name__=="__main__":
    # testing
    crop_recs = Crop_Recs("rice", [Pest("aphids", "high"), Pest("daniels", "low")], "drought")
    print(format_message(crop_recs=crop_recs,name="Jane Doe"))