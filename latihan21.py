import json

config = {
    "theme": "dark",
    "language": "id",
    "notifications": True,
    "max_items": 50
}

def simpan_config(config, nama_file):
    with open(nama_file, 'w') as f:
        json.dump(config, f)

simpan_config(config, "settings.json")