def format_produk(nama):
    nama_bersih = nama["nama"].strip().upper()
    harga = nama["harga"]
    return f"Nama Produk: {nama_bersih}, Harga: Rp{harga}"

print(format_produk({"nama": "  telur ayam ", "harga": 30000}))