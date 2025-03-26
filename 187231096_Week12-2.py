import os
os.system("cls")

def main():
    print("Pilih soal yang ingin anda kerjakan!")
    print("1. Soal Nomor 1")
    print("2. Soal Nomor 2")
    print("3. Soal Nomor 3")
    print("4. Soal Nomor 4")
    print("5. Soal Nomor 5")

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
    elif no == "5":
        print("\nNo. 5")
        soal5()
    else:
        print("Input tidak valid")

def soal1():
    # Membuat gabungan data x (6 data) dan y (5 data) yang diinput user ke dalam array baru berukuran 11 data dengan ketentuan nilai-nilai array kedua disisipkan ke array pertama
    x = [0] * (6)
    y = [0] * (5)
    xy = [0] * (11)

    i = 0
    j = 0
    k = 0
    while i<6:
        print("Masukkan nilai x ke-" + str(i + 1))
        x[i] = int (input())
        i = i + 1
    i = 0
    while i<5:
        print("Masukkan nilai y ke-" + str(i + 1))
        y[i] = int (input())
        i = i + 1
    i = 0
    while i<11:
        if i%2 == 0:
            xy[i] = x[j]
            j = j + 1
        else:
            xy[i] = y[k]
            k = k + 1
        i = i + 1
    i = 0
    print("Hasil gabungan array adalah ", end='', flush=True)
    while i<11:
        print(str(xy[i]) + " ", end='', flush=True)
        i = i + 1


def soal2():
    # Membuat algoritma untuk menyisipkan data ke-4 di posisi pertama dan data ke-5 di posisi tengah dengan ketentuan data ke-1, ke-2 dan ke-3 tetap terurut dan data diinput user
    x = [0] * (5)
    y = [0] * (5)

    i = 0
    while i<5:
        print("Masukkan nilai x ke-" + str(i + 1))
        x[i] = int(input())
        i = i + 1
    i = 0
    j = 0
    k = 1
    while i<5:
        if i<3:
            y[k] = x[i]
            k = k + (2-i)
        else:
            y[j] = x[i]
            j = j + 2
        i = i + 1
    i = 0
    while i<5:
        print(str(y[i]) + " ", end='', flush=True)
        i = i + 1

def soal3():
    # Menemukan data ascending dengan jumlah digit terbesar
    bilangan = [0] * (20)

    i = 0
    while i<20:
        print("Masukkan bilangan ke-" + str(i + 1))
        bilangan[i] = int(input())
        i = i + 1
    i = 0
    sum = 0
    maximal = 0
    var_while = 0
    a = 0
    b = 0
    while i<18:
        if bilangan[i + 1] >= bilangan[i]:
            sum = sum + bilangan[i]
            if sum>maximal:
                a = var_while
                maximal = sum
                b = i + 1
        else:
            sum = 0
            var_while = i + 1
        i = i + 1
    i = a
    sum = 0
    print("[", end='', flush=True)
    while a<=i and i<=b:
        sum = sum + bilangan[i]
        if bilangan[i] == bilangan[b]:
            print(bilangan[i], end='', flush=True)
        else:
            print(str(bilangan[i]) + " ", end='', flush=True)
        i = i + 1
    print("] karena ", end='', flush=True)
    i = a
    while a<=i and i<=b:
        if bilangan[i] == bilangan[b]:
            print(bilangan[i], end='', flush=True)
        else:
            print(str(bilangan[i]) + "+", end='', flush=True)
        i = i + 1
    print(" = " + str(sum) + " adalah jumlah angka berurutan terbesar")

def soal4():
    # Menampilkan barisan bilangan Fibonacci dengan menggunakan while sampai 10 bilangan
    print("Masukkan nilai pertama dari  barisan bilangan Fibonacci")
    a = int(input())
    print("Masukkan nilai kedua dari  barisan bilangan Fibonacci")
    b = int(input())
    i = 0
    c = 0
    print(str(a) + "  " + str (b))
    while i<=3:
        c = a + b
        a = b
        b = c
        d = a + b
        a = b
        b = d
        i = i + 1
        print("  " * i + str(c) + "  " + str(d))

def soal5():
    # Menentukan apakah sebuah bilangan positip itu merupakan angka segitiga atau bukan dan menampilkan p angka segitiga pertama
    print("Masukkan bilangan positif yang ingin Anda cek")
    bilangan = int(input())
    print("Masukkan jumlah bilangan segitiga yang ingin Anda dapatkan")
    p = int(input())
    array = [0] * (p)

    i = 0
    jumlah = 0
    print(str(p) + " angka segitiga pertama adalah ", end='')
    while i<p:
        jumlah = jumlah + i + 1
        print(str(jumlah) + " ", end='', flush=True)
        array[i] = jumlah
        i = i + 1
    print("")
    i = 0
    x = 0
    while i<p:
        if bilangan == array[i]:
            x = 1
        i = i + 1
    if x == 1:
        print(str(bilangan) + " merupakan angka segitiga")
    else:
        print(str(bilangan) + " bukan angka segitiga")

if __name__ == "__main__":
    main()