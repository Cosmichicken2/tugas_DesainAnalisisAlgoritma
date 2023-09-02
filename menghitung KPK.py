def cari_kpk(a, b):
    # Menemukan bilangan terbesar antara a dan b
    maks = max(a, b)

    while True:
        if maks % a == 0 and maks % b == 0:
            kpk = maks
            break
        maks += 1

    return kpk

# Menentukan bilangan yang akan dicari KPK-nya
bilangan1 = 3
bilangan2 = 4

# Memanggil fungsi untuk mencari KPK
kpk = cari_kpk(bilangan1, bilangan2)

print(f"KPK dari {bilangan1} dan {bilangan2} adalah {kpk}")