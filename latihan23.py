import json

produk = [
    {"nama": "Pena", "harga": 5000, "stok": 20},
    {"nama": "Buku", "harga": 15000, "stok": 5},
    {"nama": "Pensil", "harga": 3000, "stok": 0}
]

def hitung_inventaris(data):
    hasil = 0
    for i in data:
        hasil += i["harga"] * i["stok"]
    return hasil

def simpan_jadi_json(produk, nama_file):
    with open(nama_file, 'w') as f:
        json.dump(produk, f)

def baca_produk(nama_file):
    with open(nama_file, 'r') as f:
        return json.load(f)



simpan_jadi_json(produk, "produk.json")

data = baca_produk("produk.json")

print(data[0]['nama'])

print(hitung_inventaris(data))







