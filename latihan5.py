total_belanja = int(input("Masukkan total belanja Anda: "))
member = input("Apakah Anda member? (ya/tidak): ")
jumlah_ayam = int(input("Masukkan jumlah ayam yang dibeli: "))

if total_belanja > 500000 or member == "ya" and jumlah_ayam > 100:
    print("Anda mendapatkan diskon 10%")
else:
    print("TIDAK ADA DISKON")