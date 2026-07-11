pendapatan = int(input("Masukkan pendapatan Anda: "))
pengeluaran = int(input("Masukkan pengeluaran Anda: "))

riwayat_kredit = input("Apakah Anda memiliki riwayat kredit yang baik? (baik/buruk): ")

if pendapatan > pengeluaran and riwayat_kredit == "baik":
    print("kredit disetujui")
else:
    print("kredit ditolak")