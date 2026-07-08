nama_barang = input("Masukkan nama barang:")
harga_barang = input("Masukkan harga per barang: ")
jumlah_perkg = input("Masukkan jumlah per kg: ")

total_harga = float(harga_barang) * float(jumlah_perkg)

print(f"Total harga {nama_barang} adalah Rp{total_harga}")