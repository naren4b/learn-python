import requests
import pprint as pprint

response = requests.get("https://swapi.dev/api/planets/1/")
# Access different parts of the response
print("Status Code: {response.status_code}\n")  # 200 (success)
print(f"The URL requested:  {response.url}\n")  # The URL requested
print(
    f"Response headers (metaresponse): {response.headers}\n"
)  # Response headers (metaresponse)
# print(f"Text :{response.text}\n")  # Response as text string
# print(f"Json :{response.json()}\n")  # Response as JSON/dict (MOST USEFUL)

if response.status_code == 200:
    print("Planet response from SWAPI:")
    pprint.pprint(response.json(), indent=4)
else:
    print("Error in API request")
    print(f"Error Code: {response.status_code}")
