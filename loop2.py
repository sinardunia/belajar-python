stok = [15, 8, 20, 3, 12] 
nomor = 1

for i in stok:
    if i < 10:
        print(f"gudang ke-{nomor} stoknya rendah {i}")
    else:
        print(f"gudang ke-{nomor} stoknya aman {i}")
    nomor += 1
