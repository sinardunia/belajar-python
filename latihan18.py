produk = [
    {"nama": "Pena", "harga": 5000, "stok": 20},
    {"nama": "Buku", "harga": 15000, "stok": 5},
    {"nama": "Pensil", "harga": 3000, "stok": 0}
]

def filter_stok_rendah(daftar, batas=5):
    hasil = []
    for p in daftar:
        if p['stok'] < batas:
            hasil.append(p)
    return hasil

def total_nilai_inventaris(daftar):
    total = 0
    for p in daftar:
        total += p['harga'] * p['stok']
    return total

print(total_nilai_inventaris(produk))
print(filter_stok_rendah(produk))