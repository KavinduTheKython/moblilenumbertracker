import phonenumbers

##Get phone number from testpnumber file
from testpnumber import number

##Get location to trackedmap file
import folium

from phonenumbers import geocoder

##Get Api key from opencage
Key = '1c58d5bb5afa4fd9bb94bee545b95ec6'

##Get country name
kythonNumbers = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(kythonNumbers, "en")
print(yourLocation)


## get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

Query = str(yourLocation)

results = geocoder.geocode(Query)
##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))

## save html map

myMap.save("trackedmap.html")
