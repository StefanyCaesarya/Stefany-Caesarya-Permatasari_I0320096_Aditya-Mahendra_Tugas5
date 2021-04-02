Nama = str(input('Masukkan nama Anda: '))
Nilai = float(input('Ketik nilai anda dalam angka :'))

if Nilai <60:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah E")
elif Nilai >= 60 and Nilai <= 64:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah C")
elif Nilai >=65 and Nilai <=69:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah C+")
elif Nilai >=70 and Nilai <=74:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah B")
elif Nilai >=75 and Nilai <=79:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah B+")
elif Nilai >= 80 and Nilai <= 84:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah A-")
elif Nilai >= 85 and Nilai <= 100:
    print("Halo,", Nama + "! Nilai anda setelah dikonversi adalah A")
else:
    print("nilai yang selain disebutkan tidak valid")