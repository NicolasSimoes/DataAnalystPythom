from geopy.geocoders import Nominatim 
geolocator = Nominatim(user_agent="geoapiExcercises")
place = input ("Enter the Place Name: ")
location=geolocator.geocode(place)
data=location.raw
loc_Data=data['display_name'].split()
print(loc_Data)
print("Zip code : ",loc_Data[-2])