def bersihkan_nama(nama):
    bersih = nama.strip().upper().replace(" ", "_")
    return bersih

print(bersihkan_nama("  peternakan ayam jaya   "))