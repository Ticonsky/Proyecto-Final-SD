import requests

from Property import Property

def get_coordinates(address):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response_data = response.json()
    
    if response_data:
        lat = response_data[0]['lat']
        lon = response_data[0]['lon']
        return lat, lon
    else:
        raise Exception("Error fetching coordinates")

def generate_osm_url(lat, lon):
    return f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}&zoom=16"

def main():
    address = input("Introduce la dirección: ")
    try:
        lat, lon = get_coordinates(address)
        osm_url = generate_osm_url(lat, lon)
        print(f"La URL de OpenStreetMap es: {osm_url}")
    except Exception as e:
        print(f"Error: {e}")


