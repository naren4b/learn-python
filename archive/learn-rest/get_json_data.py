# Program Objective : Write a python program get data from a given url and print the repsonse in pretty json 
import requests;
import json;

def getData(url):
      response=requests.get(url)
      return response

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

if __name__ == "__main__":
    response=getData('https://restcountries.com/v3.1/name/india')
    jprint(response.json())


#someother websites
# https://dummy.restapiexample.com/api/v1/employees
# http://universities.hipolabs.com/search?country=India  
# https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/  