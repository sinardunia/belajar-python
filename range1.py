biaya_pakan = 50000
total = 0


for i in range(1, 31):
    total += biaya_pakan
    print(f"hari ke-{i} total biaya pakan ayam adalah Rp{total}")

print(f"total biaya pakan ayam selama 30 hari adalah Rp{total}")