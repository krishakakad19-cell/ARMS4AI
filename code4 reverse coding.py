from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="krisha_geoai")

location = geolocator.reverse((22.3053263, 70.8028377))

print("Address:", location.address)
