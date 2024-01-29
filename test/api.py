import http.client

conn = http.client.HTTPSConnection("aeona3.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "dedfbe9631msh93a3fd9874b2042p1a505djsn8a7db06c8e77",
    'X-RapidAPI-Host': "aeona3.p.rapidapi.com"
}
  
conn.request("GET", "/?text=hi&userId=12312312312", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))