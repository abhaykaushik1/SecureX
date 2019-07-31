import geocoder
from geopy.geocoders import Nominatim


def get_location():
    g = geocoder.ip('me')
    coordinates = g.latlng
    geolocator = Nominatim(user_agent="byteMe")
    location = geolocator.reverse(str(coordinates[0]) + ", " + str(coordinates[1]))
    address = location.address
    address = address.split(',')[0]
    return address


# print(get_location())
