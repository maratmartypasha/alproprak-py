def main():
    print("Pilih nomor yang ingin Anda kerjakan!")
    print("1. Soal Nomor 1")
    print("2. Soal Nomor 2")
    print("3. Soal Nomor 3")
    print("4. Soal Nomor 4")

    no = input("Nomor: ")

    if no == "1":
        print("\nNo. 1")
        soal1()
    elif no == "2":
        print("\nNo. 2")
        soal2()
    elif no == "3":
        print("\nNo. 3")
        soal3()
    elif no == "4":
        print("\nNo. 4")
        soal4()
    else:
        print("Pilihan tidak valid.")


def soal1():
    # Mencari panjang garis singgung persekutuan luar dengan menginput (x1, y1), (x2, y2), r1, dan r2
    x1 = float(input("Masukkan x1: "))
    y1 = float(input("Masukkan y1: "))
    x2 = float(input("Masukkan x2: "))
    y2 = float(input("Masukkan y2: "))
    r1 = float(input("Masukkan r1: "))
    r2 = float(input("Masukkan r2: "))

    jarakPusat = x2 - x1
    jumlahR = r1 + r2

    if jarakPusat != jumlahR:
        if jarakPusat < jumlahR:
            print("Tidak memiliki garis singgung persekutuan luar")
        else:
            selisihR = r1 - r2
            garisSinggung = (jarakPusat ** 2 - selisihR ** 2) ** 0.5
            print("Panjang garis singgung persekutuan luar adalah =", garisSinggung)
    else:
        selisihR = r1 - r2
        garisSinggung = (jarakPusat ** 2 - (r1 - r2) ** 2) ** 0.5
        print("Panjang garis singgung persekutuan luar adalah =", garisSinggung)


def soal2():
    # Mencari tarif MyJeg dengan menginput jarak tempuh, waktu tempuh, dan cuaca.
    jarakTempuh = float(input("Masukkan jarak tempuh MyJeg (KM): "))
    waktuTempuh = float(input("Masukkan waktu tempuh MyJeg (Jam): "))
    cuaca = int(input("Pilih cuaca antara terang (input 1) atau hujan (input 2): "))

    tarifJarak = 10000
    tarifJarakTambahan = 2000 if jarakTempuh > 4 else 0
    tarifPerKm = max(jarakTempuh - 4, 0) * 50
    tarifJarakTotal = tarifJarak + tarifJarakTambahan + tarifPerKm

    waktuLebih = max(waktuTempuh - 2.5 * jarakTempuh, 0)
    tarifWaktu = tarifJarakTotal + waktuLebih * 1000

    tarifCuaca = tarifWaktu if cuaca == 1 else tarifWaktu * 1.15

    print("Tarif total tarif perjalanan MyJeg adalah = Rp", tarifCuaca)


def soal3():
    # Menghitung koordinat titik potong dari dua grafik (y1= ax^2 + bx + c) dan (y2= dx^2 + ex + f) dengan menginput a, b, c, d, e, dan f.
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))
    d = float(input("Masukkan nilai d: "))
    e = float(input("Masukkan nilai e: "))
    f = float(input("Masukkan nilai f: "))

    g = a - d
    h = b - e
    i = c - f
    diskriminan = h ** 2 - 4 * g * i

    if diskriminan <= 0:
        print("Kedua grafik saling lepas")
    else:
        x1 = (-h + diskriminan ** 0.5) / (2 * g)
        x2 = (-h - diskriminan ** 0.5) / (2 * g)
        y1 = a * x1 ** 2 + b * x1 + c
        y2 = a * x2 ** 2 + b * x2 + c

        if diskriminan < 0:
            print(f"Koordinat titik potong dari kedua grafik tersebut ada pada titik ({toFixed(x1, 2)}, {toFixed(y1, 2)}) sehingga kedua grafik tersebut berpotongan di satu titik.")
        else:
            print(f"Koordinat titik potong dari kedua grafik tersebut ada pada titik ({toFixed(x1, 2)}, {toFixed(y1, 2)}) dan pada titik ({toFixed(x2, 2)}, {toFixed(y2, 2)}) sehingga kedua grafik tersebut berpotongan di dua titik.")


def soal4():
    # Menghitung sudut terbesar (satuan radian) di antara jarum panjang dan pendek sebuah jam dengan menginput jam dan menit.
    jam = int(input("Masukkan nilai jam (0-12): "))
    menit = int(input("Masukkan nilai menit (0-59): "))

    jarumMenit = menit / 5
    jarumJam = jam + menit / 60
    sudutJam = jarumJam - jarumMenit
    sudut = sudutJam * 30

    sudutHasil = sudut if sudut > 180 else 360 + sudut
    sudutRadian = sudutHasil / 180

    print(f"Sudut terbesar sebesar {sudutHasil}° atau {sudutRadian}π radian")


def toFixed(value, digits):
    return f"{value:.{digits}f}"


if __name__ == "__main__":
    main()