stok_gudang = {
    "A": 15,
    "B": 8,
    "C": 20
}

print(stok_gudang["B"])

stok_gudang["D"] = 12

for key, value in stok_gudang.items():
    print(f"stok barang {key} adalah {value}")


total = 0
for value in stok_gudang.values():
    total += value

print(f"total stok gudang adalah {total}")

