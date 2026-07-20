import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/3")
print(response.status_code) 
coba = response.json()

print(coba['title'])
print(coba['body'])