import json

def baca_config(nama_file):
    with open(nama_file, 'r') as f:
        return json.load(f)

def simpan_config(config, nama_file):
    with open(nama_file, 'w') as f:
        json.dump(config, f)

data = baca_config("settings.json")
print(f"before: {data}")

data['theme'] = "light"

simpan_config(data, "settings.json")

data_baru = baca_config("settings.json")
print(f"after: {data_baru}")