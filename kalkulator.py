def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

print("Kalkulator Sederhana")
print("====================")

while True:
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        hasil = tambah(angka1, angka2)
        print("Hasil penjumlahan:", hasil)
    elif pilihan == "2":
        hasil = kurang(angka1, angka2)
        print("Hasil pengurangan:", hasil)
    elif pilihan == "3":
        hasil = kali(angka1, angka2)
        print("Hasil perkalian:", hasil)
    elif pilihan == "4":
        hasil = bagi(angka1, angka2)
        print("Hasil pembagian:", hasil)
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
