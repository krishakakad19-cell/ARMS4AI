from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="krisha_geoai")

location = geolocator.geocode("UPES, Dehradun")

print("Full Address:", location.address)
print("Latitude:", location.latitude)
print("Longitude:", location.longitude)