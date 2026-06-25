from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="krisha_geoai")

location = geolocator.geocode("Rajkot, Gujarat")

print("Latitude:", location.latitude)
print("Longitude:", location.longitude)



