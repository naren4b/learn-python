import requests


try:
    response = requests.get("https://swapi.dev/api/planets/1/")
    response.raise_for_status()
    planet_data = response.json()
    print("Planet Data:")
    print(planet_data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
