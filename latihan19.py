produk = [
    {"nama": "Pena", "harga": 5000, "stok": 20},
    {"nama": "Buku", "harga": 15000, "stok": 5},
    {"nama": "Pensil", "harga": 3000, "stok": 0}
]

def simpan_ke_file(daftar, nama_file):
    with open(nama_file, 'w') as f:
        for i in daftar:
            f.write(f"{i['nama']}|{i['harga']}|{i['stok']}\n")

simpan_ke_file(produk, "bebas")