print("Komen Kalkulator")

print("########################################")
print("Komen Untuk Kalkulator: ")
print("1.Untuk Tambah tulis = PLUS")
print("2.Untuk Kurang tulis = MINUS")
print("3.Untuk Perkalian tulis = MULTIPLE")
print("4.Untuk Pembagian tulis = DIVISION")
print("########################################")

print("")

Angka1 = int(input("Masukan Angka: "))
Angka2 = int(input("Masukan Angka kedua: "))

Komen = input("Masukan Komen: ")

if Komen == "PLUS":
    Perhitungan = Angka1 + Angka2
    print(Perhitungan)

elif Komen == "MINUS":
    Perhitungan2 = Angka1 - Angka2
    print(Perhitungan2)

elif Komen == "MULTIPLE":
    Perhitungan3 = Angka1 * Angka2
    print(Perhitungan3)

elif Komen == "DIVISION":
    Perhitungan4 = Angka1 / Angka2
    print(Perhitungan4)