import requests;
import json;


def printMyPlanets(all_planets):
        index=0
        print("SlNo.Name:Population")
        for planet in all_planets:
            index=index+1
            name=planet['name']
            population=planet['population']    
            print(f"{index}.{name}: {population}")


page=1
url="https://swapi.dev/api/planets/?page="
all_planets=[]
while(True):
        response=requests.get(f"{url}{page}")
        if (response.status_code !=200):
                break
        data=response.json()
        planets=data['results']
        all_planets.extend(planets)
        page=page+1

printMyPlanets(all_planets)
