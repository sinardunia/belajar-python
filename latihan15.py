catatan = {}

def simpan_entri(buku, judul, isi):
    buku[judul] = isi
    return buku

catatan = simpan_entri(catatan, "daftar_belanja", "telur, susu, roti")
catatan = simpan_entri(catatan, "ide_project", "aplikasi pencatat")
catatan = simpan_entri(catatan, "daftar_belanja", "telur, susu, roti, kopi")



def tampilkan_semua(buku):
    if not buku:
        print("buku kosong")
        return 
    for k, v in buku.items():
        print(f"[{k}]")
        print(f"    {v}")

tampilkan_semua(catatan)