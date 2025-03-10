print("masukkan bilangan bulat 4 digit (n)")
n = int(input())
bil1 = n % 10
n = float(n) / 10
bil2 = n % 10
n = float(n) / 10
bil3 = n % 10
n = float(n) / 10
bil4 = n % 10

bil1 = int(bil1)
bil2 = int(bil2)
bil3 = int(bil3)
bil4 = int(bil4)

hasil = bil1 + bil2 + bil3 + bil4
print("hasil jumlah 4 digit")
print(hasil)
