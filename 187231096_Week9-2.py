def soal1():
    # Mencari jumlah seluruh harta warisan yang ditinggalkan oleh seorang suami dari ibu beranak tiga dengan diketahui bahwa ibu menerima warisan sebesar 1/6 bagian dari harta warisan dan tiga orang putranya menerima warisan masing-masing sebesar 1/3 dari sisanya.
    ibu = 1 / 6
    putra = 1 / 3 * 5 / 6

    # Diketahui bahwa ibu dan seorang putra menerima total warisan sebesar 6 milyar.
    ibu_dan_putra = ibu + putra

    # Jumlah warisan ibu dan seorang putra adalah 0.444444 atau bisa disebut 4/9 dari total seluruh harta warisan.
    print("Jumlah warisan ibu dan seorang putra adalah =", ibu_dan_putra)
    ibu_dan_putra = int(input())
    variabel = 9 / 9 / (4 / 9)

    # Hasil perhitungan variabel adalah 2.25
    harta_suami = ibu_dan_putra * variabel
    print("Jumlah seluruh harta warisan yang ditinggalkan oleh suami ibu adalah =", harta_suami)

def soal2():
    # Mencari bilangan k dari 4 bilangan 6, 9, 11, dan k dengan menginput rata-rata (n) dari 4 bilangan tersebut.
    bil6 = 6
    bil9 = 9
    bil11 = 11
    n = int(input("Masukkan rata-rata (n): "))
    if n > 6:
        k = 4 * n - (bil6 + bil9 + bil11)
        print("Hasil dari k adalah =", k)
    else:
        print("Nilai n harus lebih dari 6")



def soal3():
    # Mencari persentase kenaikan harga jual minyak goreng dibandingkan harga belinya dengan menginput harga beli, persentase ongkos kirim, dan keuntungan dari minyak goreng.
    harga_beli = int(input("Masukkan harga beli: "))
    p = float(input("Masukkan persentase ongkos kirim (p): "))
    untung = int(input("Masukkan keuntungan: "))
    harga_jual = harga_beli + (harga_beli * p) / 100 + untung
    persentase_naik = ((harga_jual - harga_beli) / harga_beli) * 100
    print("Persentase kenaikan harga jual dibandingkan harga belinya adalah", persentase_naik, "%")

def soal4():
    # Mencari waktu kedatangan sebuah bus di lokasi tujuan dengan menginput waktu keberangkatan, jarak tempuh, dan kecepatan rata-rata bus.
    jam_berangkat = int(input("Masukkan jam keberangkatan bus: "))
    menit_berangkat = int(input("Masukkan menit keberangkatan bus: "))
    s = float(input("Masukkan jarak tempuh bus (s): "))
    v = float(input("Masukkan kecepatan rata-rata bus (v): "))
    istirahat = 45
    jam_dalam_menit = jam_berangkat * 60
    t1 = jam_dalam_menit + menit_berangkat
    t = s / v
    tambahan_menit = int(t * 60)

    # Perhitungan akan dimulai pada pukul 00.00, oleh sebab itu waktu keberangkatan juga dipakai dalam perhitungan.
    t2 = t1 + istirahat + tambahan_menit
    if t2 > 1440:
        t2 = t2 % 1440
    jam_tiba = t2 // 60
    menit_tiba = t2 % 60
    print("Waktu kedatangan bus di lokasi tujuan adalah pada pukul", jam_tiba, "lebih", menit_tiba, "menit")

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
        print("Input tidak valid.")

if __name__ == "__main__":
    main()
