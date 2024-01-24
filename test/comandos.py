



import requests

url = "https://waifu.p.rapidapi.com/path"

querystring = {"user_id":"waifu","message":"Hi","from_name":"Boy","to_name":"Girl","situation":"Girl loves Boy.","translate_from":"auto","translate_to":"auto"}

payload = {}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "dedfbe9631msh93a3fd9874b2042p1a505djsn8a7db06c8e77",
	"X-RapidAPI-Host": "waifu.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())