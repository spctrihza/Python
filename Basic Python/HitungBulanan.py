"""Tahap 1 Menghitung Harian """

pendapatan = {}
pengeluaran = {}

while True:
    Opsi = raw_input("1. Tekan \"N\" untuk ke Menu Pendapatan\n"
                 "2. Tekan \"Y\" untuk ke Menu Pengeluaran\n"
                 "   Silahkan Pilih : ")
    if Opsi == "N":
        while True:
            a = raw_input("Masukkan Pendapatan : ")
            b = input("Masukan Jumlah Pendapatan : ")
            pendapatan[a] = b
            Nilai = raw_input("Lanjut ? (Y)es / (N)o : ")
            if Nilai == "N":
                break
    elif Opsi == "Y":
        while True:
            a = raw_input("Masukkan Pengeluaran : ")
            b = input("Masukan Pendapatan : ")
            pengeluaran[a] = b
            Nilai = raw_input("Lanjut ? (Y)es / (N)o : ")
            if Nilai == "N":
                break
    Opsi1 = raw_input("1. Tekan \"N\" untuk kembali ke menu Awal\n"
                      "2. Tekan \"Y\" untuk keluar menu\n"
                      "\tSilahakan Pilih : ")

    if Opsi1 == "Y":
        break


jumpen = pendapatan.values()
jumpeng = pengeluaran.values()

harian = sum(jumpen) - sum(jumpeng)

print harian

mingguan = []

mingguan.append(harian)

print mingguan
