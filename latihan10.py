def cari_kosong(gudang):
    for k, v in gudang.items():
        if v == 0:
            print(f"gudang ke-{k} kosong")
            return k

def hitung_isi(gudang):
    total = 0
    for k, v in gudang.items():
        if v > 0:
            total += v
    return total

print(cari_kosong({"A":5, "B":0, "C":0, "D":3}))
print(hitung_isi({"A":5, "B":0, "C":0, "D":3}))