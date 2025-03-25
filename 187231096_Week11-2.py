def main():
    print("Pilih soal yang ingin anda kerjakan!")
    print("1. Soal Nomor 1")
    print("2. Soal Nomor 2")
    print("3. Soal Nomor 3")
    print("4. Soal Nomor 4")

    no = input("Nomor: ")

    if no == "1":
        print("\nNo 1")
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
        print("Input tidak valid")

def soal1():
    berat = []
    ratarata = float(input("Masukkan Rata-Rata Berat Bebek (Kg): "))
    total7 = 0
    for i in range(7):
        bebek = i + 1
        berat_bebek = float(input(f"Masukkan Berat Bebek Ke {bebek} (Kg): "))
        berat.append(berat_bebek)
        total7 += berat_bebek
    print(f"Berat total 7 bebek adalah {total7} Kg")
    total3 = ratarata * 10 - total7
    print(f"Berat total 3 bebek yang hilang adalah {total3} Kg")
    berat.append(total3 * 1 / 3.75)
    berat.append(total3 * 1.25 / 3.75)
    berat.append(total3 * 1.5 / 3.75)
    print(f"Berat 3 bebek yang hilang adalah {berat[7]} Kg, {berat[8]} Kg, {berat[9]} Kg")
    p = 0
    for i in range(10):
        p += (berat[i] - ratarata) ** 2
    standardeviasi = (p / 10) ** 0.5
    print(f"Standar Deviasinya adalah {standardeviasi}")

def soal2():
    nilai = []
    kategori = {"A": 0, "AB": 0, "B": 0, "BC": 0, "C": 0, "D": 0, "E": 0}
    for i in range(15):
        nilai_ke = i + 1
        nilai_mahasiswa = float(input(f"Masukkan nilai ke-{nilai_ke}: "))
        nilai.append(nilai_mahasiswa)
        if nilai_mahasiswa >= 86:
            kategori["A"] += 1
        elif nilai_mahasiswa >= 78:
            kategori["AB"] += 1
        elif nilai_mahasiswa >= 70:
            kategori["B"] += 1
        elif nilai_mahasiswa >= 62:
            kategori["BC"] += 1
        elif nilai_mahasiswa >= 54:
            kategori["C"] += 1
        elif nilai_mahasiswa >= 40:
            kategori["D"] += 1
        else:
            kategori["E"] += 1
    for kategori_nilai, jumlah in kategori.items():
        print(f"Jumlah mahasiswa yang masuk kategori nilai {kategori_nilai} ada {jumlah} orang")

def soal3():
    angka = []
    for i in range(20):
        bilangan_ke = i + 1
        bilangan = int(input(f"Masukkan bilangan ke-{bilangan_ke}: "))
        angka.append(bilangan)
    panjang_pertama = 1
    panjang_terakhir = 1
    index_pertama = 0
    index_terakhir = 0
    for i in range(1, 20):
        if angka[i - 1] > angka[i]:
            panjang_pertama += 1
        else:
            if panjang_pertama > panjang_terakhir:
                panjang_terakhir = panjang_pertama
                index_pertama = i - panjang_pertama
                index_terakhir = i - 1
            panjang_pertama = 1
    if panjang_pertama > panjang_terakhir:
        panjang_terakhir = panjang_pertama
        index_pertama = 20 - panjang_pertama
        index_terakhir = 19
    print("Bilangan yang menurun dari besar ke kecil secara berurutan (decrease) terpanjang adalah", end=" ")
    for i in range(index_pertama, index_terakhir + 1):
        print(angka[i], end="")
    print(f" ({panjang_terakhir})")

def soal4():
    tanggal = int(input("Masukkan tanggal: "))
    bulan = input("Masukkan bulan: ").lower()
    tahun = int(input("Masukkan tahun: "))
    bulan_angka = {
        "januari": 1, "februari": 2, "maret": 3, "april": 4,
        "mei": 5, "juni": 6, "juli": 7, "agustus": 8,
        "september": 9, "oktober": 10, "november": 11, "desember": 12
    }
    x = bulan_angka.get(bulan, 0)
    if x == 0:
        print("Bulan tidak valid")
        return
    tanggal_bulan = tanggal * 100 + x
    polindrome = int(str(tahun)[::-1])
    gabungan_tanggal = f"{tanggal}-{x}-{tahun}"
    print(tanggal_bulan)
    print(polindrome)
    if tanggal_bulan == polindrome:
        print(f"Tanggal {gabungan_tanggal} merupakan angka POLINDROME")
    else:
        print(f"Tanggal {gabungan_tanggal} BUKAN angka POLINDROME")

if __name__ == "__main__":
    main()