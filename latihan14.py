def filter_stok_rendah(list, batas = 10):
    rendah = []
    for i in list:
        if i < batas:
            rendah.append(i)
    return rendah

stok = [15, 8, 12, 3, 12]

print(filter_stok_rendah(stok, 10))