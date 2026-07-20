import requests

post_baru = {"title": "Belajar HTTP", "body": "Ini isi", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_baru)
print(response.status_code)  # 201 (created)
print(response.json())        # post_baru yang baru dibuat