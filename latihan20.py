def baca_dari_file(nama_file):
    hasil = []
    with open(nama_file, 'r') as f:
        for p in f:
           p = p.strip()
           pecah = p.split("|")
           item = {
               "nama": pecah[0],
               "harga": int(pecah[1]),
               "stok": int(pecah[2])
           }
           hasil.append(item)
    return hasil

print(baca_dari_file("bebas"))
        