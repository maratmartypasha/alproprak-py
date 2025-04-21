import random
def main():
    print("Pilih soal yang ingin anda kerjakan!")
    print("1. Soal Nomor 1")
    print("2. Soal Nomor 2")
    print("3. Soal Nomor 3")
    print("4. Soal Nomor 4")
    print("5. Soal Nomor 5")
    print("6. Soal Nomor 6")
    print("7. Soal Nomor 7")
    print("8. Soal Nomor 8")

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
    elif no == "6":
        print("\nNo. 6")
        soal6()
    elif no == "7":
        print("\nNo. 7")
        soal7()
    elif no == "8":
        print("\nNo. 8")
        soal8()  
    else:
        print("Input tidak valid")

def fill(arr, i, num):
    if i<num:
        arr[i] = int(random.random() * 10)
        i = i + 1
        fill(arr, i, num)

def out(arr, i, num):
    if i<num:
        print(str(arr[i]) + " ", end='', flush=True)
        i = i + 1
        out(arr, i, num)

def soal1():
    # Bualah function yang bersifat rekursif yang menampilkan data dari sebuah array dengan ukuran n. Urutan data yang ditampilkan dari depan ke belakang.
    print("Masukkan jumlah data yang diinginkan dalam array")
    num = int(input())
    arr = [0] * (num)

    i = 0
    fill(arr, i, num)
    print("Urutan data yang ditampilkan dari depan ke belakang: ")
    out(arr, i, num)

def reverse(arr, i):
    if i>=0:
        print(str(arr[i]) + " ", end='', flush=True)
        i = i - 1
        reverse(arr, i)

def soal2():
    # Bualah function yang bersifat rekursif yang menampilkan data dari sebuah array dengan ukuran n. Urutan data yang ditampilkan dari belakang ke depan.
    print("Masukkan jumlah data yang diinginkan dalam array")
    num = int(input())
    arr = [0] * (num)

    i = 0
    fill(arr, i, num)
    print("Urutan data yang ditampilkan dari depan ke belakang: ")
    out(arr, i, num)
    i = num - 1
    print("\nUrutan data yang ditampilkan dari belakang ke depan: ")
    reverse(arr, i)

def big(arr, i, j, num):
    if arr[i]<=arr[j]:
        max = arr[j]
        i = i + 1
    else:
        max = arr[i]
        j = j + 1
    if i<num:
        if j<num:
            big(arr, i, j, num)
        else:
            print(max)
    else: print(max)
    return max

def soal3():
    # Bualah function yang bersifat rekursif yang mengembalikan data terbesar dalam sebuah ARRAY dengan ukuran n.
    print("Masukkan jumlah data yang diinginkan dalam array")
    num = int(input())
    arr = [0] * (num)

    i = 0
    fill(arr, i, num)
    print("Array data: ")
    out(arr, i, num)
    i = 0
    j = 0
    print("\nVariabel terbesarnya adalah: ", end='', flush=True)
    big(arr, i, j, num)

def nbOfDigit(n):
    if n!=0:
        result = 1 + nbOfDigit(float(n) / 10)
    else:
        result = 0
    return result

def soal4():
    # Buatlah function rekursif nbOfDigit(n) yang mengembalikan banyaknya digit penyusun dari bilangan bulat n.
    print("Masukkan n")
    n = int(input())
    print(nbOfDigit(n))

def createArray(x, n):
    if n>=0:
        createArray(x, n-1)
        x[n] = int(random.random() * 10)

def disp(x, n):
    if n>=0:
        disp(x, n-1)
        print(str(x[n]) + " ", end='', flush=True)

def trueFalse(x, n, key, cek):
    if x[n]==key:
        cek = True
    else:
        if n>0:
            cek = trueFalse(x, n-1, key, cek)
    return cek

def soal5():
    # Bualah function yang bersifat rekursif  yang mengembalikan nilai TRUE bila key (parameter integer) terdapat dalam sebuah ARRAY dengan ukuran n. Function tersebut mengembalikan nilai FALSE jika tidak demikian.
    print("Masukkan jumlah data yang diinginkan dalam array")
    n = int(input())
    print("Masukkan key")
    key = int(input())
    x = [0] * (n)

    createArray(x, n-1)
    disp(x, n-1)
    cek = False
    print("")
    print(trueFalse(x, n-1, key, cek))


def angkaNol(y, i):
    if i>=0:
        y[i] = 0
        angkaNol(y, i-1)

def angkaKembar(x, n, cek, y):
    if n>=0:
        p = 0
        p = x[n]
        y[p] = y[p] + 1
        cek = angkaKembar(x, n-1, cek, y)
        if y[p]>1:
            cek = True
    return cek

def soal6():
    # Bualah function yang bersifat rekursif  yang mengembalikan nilai TRUE bila terdapat data yang kembar / double dalam sebuah ARRAY dengan ukuran n. Function tersebut mengembalikan nilai FALSE jika tidak demikian.
    print("Masukkan jumlah data yang diinginkan dalam array")
    n = int(input())
    x = [0] * (n)

    createArray(x, n-1)
    disp(x, n-1)
    cek = False
    y = [0] * (10)

    angkaNol(y, 9)
    print("")
    print(angkaKembar(x, n-1, cek, y))

def factor(n, i):
    i = i + 1
    if n<0:
        n = n * -1
    if n%i==0:
        print(str(i) + ", ", end='', flush=True)
        j = i * -1
        print(str(j) + ", ", end='', flush=True)
        factor(n, i)
    else:
        if i>n:
            pass
        else: factor(n, i)

def soal7():
    # Buatlah sebuah function rekursif yang menampilkan faktor-faktor dari bilangan bulat n.
    print("Masukkan nilai n")
    n = int(input())
    i = 0
    print("Faktor-faktor dari bilangan bulat " + str(n) + " adalah: ", end='', flush=True)
    factor(n, i)

def modulo(b, i, jumlah, a):
    b = b + 1
    if i%b==0:
        jumlah = jumlah + 1
        jumlah = modulo(b, i, jumlah, a)
    else:
        if b>i:
            pass
        else:
            jumlah = modulo(b, i, jumlah, a)
    return jumlah

def faktor(n, i, a, jumlah, b):
    i = i + 1
    if n%i==0:
        jumlah = 0
        jumlah = modulo(b, i, jumlah, a)
        if jumlah==2:
            a = a * i
        b = 0
        a = faktor(n, i, a, jumlah, b)
    else:
        if i>n:
            pass
        else:
            a = faktor(n, i, a, jumlah, b)
    return a

def soal8():
    # Buatlah sebuah function rekursif yang mengembalikan perkalian antara faktor-faktor positif PRIMA dari bilangan bulat n.
    print("Masukkan nilai n")
    n = int(input())
    i = 0
    a = 1
    jumlah = 0
    b = 0
    print("Hasil perkalian antara faktor-faktor positif prima dari bilangan bulat " + str(n) + " adalah: ", end='', flush=True)
    print(faktor(n, i, a, jumlah, b))

if __name__ == "__main__":
    main()