cuaca = input("Apakah cuaca hari ini cerah? (ya/tidak): ")
kelembaban = input("Masukkan tingkat kelembaban (%): ")

kelembapan = int(kelembaban)

if cuaca == "ya" and kelembapan > 80:
    print("lanjut panen")
else:
    print("tunda panen")