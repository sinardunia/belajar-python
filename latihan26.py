import json

def file(nama_file):
    try:
        with open(nama_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("file-nya eror bang")
        return []

data = file("apadeh.txt")

print(data)
