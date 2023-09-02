def tukar_posisi(x, y):
    temp = x
    x = y
    y = temp
    return x, y

# Kasus dengan manggis dan pisang
piring_1 = "manggis"
piring_2 = "pisang"
piring_3 = "kosong"

print("Sebelum pertukaran:")
print("Piring 1:", piring_1)
print("Piring 2:", piring_2)
print("Piring 3:", piring_3)

piring_1, piring_2 = tukar_posisi(piring_1, piring_2)

print("\nSetelah pertukaran:")
print("Piring 1:", piring_1)
print("Piring 2:", piring_2)
print("Piring 3:", piring_3)