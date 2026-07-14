def cek_stok_rendah(stok, batas = 10):
    total_rendah = 0
    for key, value in stok.items():
        if value < batas:
            print(f"stok barang {key} rendah, hanya {value} tersisa")
            total_rendah += 1
    return total_rendah

cek_stok_rendah({"A": 15, "B": 8, "C": 20, "D": 3, "E": 12})

jumlah_rendah = cek_stok_rendah({"A": 15, "B": 8, "C": 20, "D": 3, "E": 12})
print(f"total stok rendah adalah {jumlah_rendah}")