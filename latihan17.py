daftar_produk = []

produk = [
    {"nama": "Pena", "harga": 5000, "stok": 20},
    {"nama": "Buku", "harga": 15000, "stok": 5},
    {"nama": "Pensil", "harga": 3000, "stok": 0}
]

def tampilkan_produk(daftar):
    if not daftar:
        print("tidak ada produk")
        return
    for i, p in enumerate(daftar, start=1):
        print(f"{i} {p['nama']} -Rp{p['harga']} stok: {p['stok']}")


tampilkan_produk(produk)
