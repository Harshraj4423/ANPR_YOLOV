from geopy.geocoders import Nominatim
from datetime import datetime


def return_values(text):
    # geoLoc = Nominatim(user_agent="GetLoc")
    # locname = geoLoc.reverse("18.728307, 73.664627")
    locname = "Talegaon Dabhade, Mawal, Maharashtra, 410506, India"


    dict = {
        "CZ17 KOD" : "Vikas Pawar",
        "MEGANE RS": "HariPreetam reddy",
        "CYNICAL"  :  "Apurv Jha",
        "RN 6138"  : "Beluga"
        }
    
    Owner = dict.get(text)
    if(Owner == None):
        Owner = "Not Found"

    current_time = datetime.today()

    return current_time, locname , Owner
