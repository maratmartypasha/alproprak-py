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

def prime(n):
    result = True
    i = 0
    j = 2
    if n>=2:
        while i<n-2:
            if n%j==0:
                result = False
            i = i + 1
            j = j + 1
    else:
        result = False
    return result

def soal1():
    # Function prime (integer n) yang mengembalikan nilai true bila n adalah bilangan prima atau false bila tidak demikian
    print("Masukkan nilai n yang ingin dites")
    n = int(input())
    result = prime(n)
    print(result)

def dispPrime(n):
    i = 0
    print("Semua bilangan prima yang lebih kecil atau sama dengan " + str(n) + " adalah ", end='', flush=True)
    while i<=n:
        result = prime(i)
        if result == True:
            print(str(i) + " ", end='', flush=True)
        i = i + 1

def soal2():
    # Function dispPrime(integer n) yang menampilkan semua bilangan prima yang lebih kecil atau sama dengan n
    print("Masukkan nilai n yang ingin dites")
    n = int(input())
    result = prime(n)
    dispPrime(n)

def dispFirstPrime(n):
    i = 0
    j = 0
    print("Sejumlah " + str(n) + " bilangan prima pertama adalah ", end='', flush=True)
    while i<n:
        result = prime(j)
        if result==True:
            print(str(j) + " ", end='', flush=True)
            i = i + 1
        j = j + 1

def soal3():
    # Function dispFirstPrime(integer n) yang menampilkan sejumlah n bilangan prima yang pertama
    print("Masukkan nilai n yang ingin dites")
    n = int(input())
    result = prime(n)
    dispFirstPrime(n)

def primeFactor(n):
    i = 1
    print("Semua faktor dari " + str(n) + " yang prima adalah ", end='', flush=True)
    while i<=n:
        if n%i==0:
            result = prime(i)
            if result==True:
                print(str(i) + " ", end='', flush=True)
        i = i + 1

def soal4():
    # Function primeFactor(integer n) yang menampilkan semua faktor dari n yang prima
    print("Masukkan nilai n yang ingin dites")
    n = int(input())
    result = prime(n)
    primeFactor(n)

def sameFactor(n, k):
    if n>k:
        size = n
    else:
        size = k
    print("Semua faktor dari " + str(n) + " dan " + str(k) + " yang sama adalah ", end='', flush=True)
    for i in range(2, size+1, 1):
        if n==i or k==i:
            pass
        else:
            if n%i==0:
                if k%i==0:
                    print(str(i) + " ", end='', flush=True)

def soal5():
    # Function sameFactor(int n, int k) yang mengembalikan nilai faktor persekutuan terkecil dari n dan k
    print("Masukkan nilai n")
    n = int(input())
    print("Masukkan nilai k")
    k = int(input())
    sameFactor(n, k)

def smallestComFactor(n, k):
    i = 2
    j = 0
    print("Nilai faktor persekutuan terkecil dari " + str(n) + " dan " + str(k) + " adalah ", end='', flush=True)
    while j==0:
        if n==i or k==i:
            pass
        else:
            if n%i==0:
                if k%i==0:
                    print(str(i) + " ", end='', flush=True)
                    j = j + 1
        i = i + 1

def soal6():
    # Function smallestComFactor(int n, int k) yang mengembalikan nilai faktor persekutuan terkecil dari n dan k
    print("Masukkan nilai n")
    n = int(input())
    print("Masukkan nilai k")
    k = int(input())
    smallestComFactor(n, k)

def numOfDigit(n):
    n = abs(n)
    i = 0
    while n!=0:
        n = float(n) // 10
        i = i + 1
    print("Banyaknya digit pada bilangan n yang telah diinput adalah " + str(i))

def soal7():
    # Function numOfDigit(int n) yang mengembalikan banyaknya digit pada bilangan positif n
    print("Masukkan nilai n yang ingin dites")
    n = int(input())
    numOfDigit(n)

def numOfUniqDigit(n):
    n = abs(n)
    arr = [0] * (10)

    j = 0
    for i in range(0, 9+1, 1):
        arr[i] = 0
    while n!=0:
        hasilModulo = n % 10
        for i in range (0, 9+1, 1):
            if hasilModulo==i:
                arr[i] = arr[i] + 1
        n = float(n) // 10
    for i in range(0, 9+1, 1):
        if arr[i]>0:
            j = j + 1
    print("Banyaknya angka unik adalah " + str(j))

def soal8():
    # Function numOfUniqDigit(int n) yang mengembalikan banyaknya digit pada bilangan positif n dengan aturan digit yang sama atau kembar dihitung 1
    print("Masukkan nilai n yang ingin dites")
    n = int(input())
    numOfUniqDigit(n)

if __name__ == "__main__":
    main()