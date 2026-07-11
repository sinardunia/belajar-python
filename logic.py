stok = input("Masukan stok barang: ")
permintaan = input("Masukan permintaan barang: ")

stok = int(stok)
permintaan = int(permintaan)

if stok < 15 and permintaan > 50:
    print("Harga naik")
else:
    print("Harga normal")
