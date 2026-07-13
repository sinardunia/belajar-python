stok = [15, 8, 20, 3, 12]

for i in range(len(stok)):
    if stok[i] < 10:
        print(f"gudang ke-{i+1} stoknya rendah {stok[i]}")
    else:
        print(f"gudang ke-{i+1} stoknya aman {stok[i]}")