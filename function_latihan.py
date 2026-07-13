def hitung_total_panen(panen):
    total = 0
    for  i in panen:
        total += i
    return total

print(f"Total panen: {hitung_total_panen([100, 200, 300, 400, 500])} kg")