import random

def menang(pilihan_pengguna, pilihan_komputer):
    return ((pilihan_pengguna == 'batu' and pilihan_komputer == 'gunting') or
            (pilihan_pengguna == 'gunting' and pilihan_komputer == 'kertas') or
            (pilihan_pengguna == 'kertas' and pilihan_komputer == 'batu'))

while True:
    pilihan_pengguna = input("Pilih Batu, Gunting, atau Kertas: ").lower()
    if pilihan_pengguna == 'exit':
        break
    pilihan_komputer = random.choice(['batu', 'gunting', 'kertas'])

    print("Pilihan Komputer:", pilihan_komputer)

    if pilihan_pengguna in ['batu', 'gunting', 'kertas']:
        if pilihan_pengguna == pilihan_komputer:
            print("Hasil: Seri!")
        elif menang(pilihan_pengguna, pilihan_komputer):
            print("Hasil: Anda Menang!")
        else:
            print("Hasil: Komputer Menang!")
    else:
        print("Pilihan tidak valid. Silakan pilih antara Batu, Gunting, atau Kertas.")

