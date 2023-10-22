from firebase_admin.firestore import FieldFilter
from datetime import datetime

def get_user_by_number(db, number) -> dict:
    users = db.collection(u'users').where(filter=FieldFilter("phone_number", "==", number)).get()

    if len(users) == 0:
        print(f"No user accounts with {number}!")
        return None
    
    user_dict = users[0].to_dict()

    coordinates = user_dict["position"]

    result = {
        "lat": coordinates.latitude,
        "long": coordinates.longitude,
        "time": datetime.now() # datetime object
    }

    return result