from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="krisha_geoai")

places = [
    "Rajkot, Gujarat",
    "Ahmedabad, Gujarat",
    "Dehradun, Uttarakhand",
    "Mumbai, Maharashtra"
]

for place in places:
    location = geolocator.geocode(place)

    print(place)
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)
    print("----------------")

    