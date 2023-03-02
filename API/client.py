import requests

BASE = "http://127.0.0.1:5000/"

# call the put request
requests.put(BASE + "student/1235", {'name':'John Doe','age':30})

# pause before the get request
input()

# call the get request
response = requests.get(BASE + 'student/123324')

# print out the response
print(response.json())