# API example

# response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
# print(response.status_code)

# API example with json

# response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)
# jprint(response.json())



import requests

response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5e8c4862")
print(response.status_code)