import requests

BASE = "http://127.0.0.1:5000/"

# call the get request
response = requests.get(BASE + "helloworld")

# print out the response
print(response.json())