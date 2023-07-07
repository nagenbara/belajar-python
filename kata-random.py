import random

kata_satu = ['Pagi', 'Siang', 'Malam', 'Senyum', 'Cinta', 'Bunga', 'Hujan']
kata_dua = ['indah', 'cerah', 'romantis', 'bahagia', 'damai', 'mengagumkan']
kata_tiga = ['di taman', 'di pantai', 'di dalam hati', 'di kota', 'di pegunungan']

kata_acak = random.choice(kata_satu) + ' ' + random.choice(kata_dua) + ' ' + random.choice(kata_tiga)

print("Kata Acak: " + kata_acak)
