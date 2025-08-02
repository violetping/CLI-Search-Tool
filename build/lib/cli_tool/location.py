
import requests
import sys
import time

HEADERS = {
    "User-Agent": "CLI Search Tool - Educational (quint@thiefness.com)"
}

def get_location_data(location_name):
    try:
        response = requests.get(
            f"https://nominatim.openstreetmap.org/search",
            params={"format": "json", "q": location_name},
            headers=HEADERS
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            print(f"No location data found for '{location_name}'.")
            return

        location = data[0]
        print(f"Location: {location.get('display_name', 'N/A')}")
        print(f"Latitude: {location.get('lat', 'N/A')}")
        print(f"Longitude: {location.get('lon', 'N/A')}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.RequestException as e:
        print(f"Error retrieving location data: {e}")

def run(location_name):
    get_location_data(location_name)