import requests
import json
url = "https://bing-image-search1.p.rapidapi.com/images/search"

querystring = {"q":"Apple"}

headers = {
	"X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e",
	"X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.text
data = json.loads(data)
value = []
value = data["value"]
for key in value:
    print(key["contentUrl"])

