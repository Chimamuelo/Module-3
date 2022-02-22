import requests
from pprint import pprint

##API KEYS IN txt file
with open(r'C:\Users\alber\Desktop\Coding Nomads\python-301-main\03_inheritance\Loggin.txt') as f:
    lines=[]
    for line in f.read().splitlines():
        lines.append(line)
    

API_ID=lines[0]
API_KEY=lines[1]
query={"type": "public","q": "chicken"+" onion", "app_id": API_ID, "app_key": API_KEY}


response=requests.get("https://api.edamam.com/api/recipes/v2",params=query)
print(response)
data=response.json()
data=data["hits"]
for recipe in data:
    print(type(recipe))
    print(recipe['recipe']['label'])


