hujan = input("Apakah hujan hari ini? (ya/tidak): ")
angin_kencang = input("Apakah angin kencang hari ini? (ya/tidak): ")

if  hujan == "ya" or  angin_kencang == "ya":
    print("tunda panen")
else:
    print("lanjut panen")