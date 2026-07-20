import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()


def filter(link):
    hasil = []
    for i in link:
        if i["userId"] == 1:
            hasil.append(i)
            print(i["title"])
    return len(hasil)

print(filter(data))
