import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "How to Joe", "views": 100000},
		{"likes": 10, "name": "How to make REST API", "views": 198745},
		{"likes": 10000, "name": "lotr", "views": 133},
		{"likes": 1999, "name": "How to be a jerk", "views": 99999999999}]


for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())



#json because I do not want response object
