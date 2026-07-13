def hitung_diskon(total_belanja):
    if total_belanja > 500000:
        return total_belanja * 0.1
    else:
        return 0
    
diskon = hitung_diskon(600000)

print(f"Diskon yang didapatkan adalah Rp{diskon}")

