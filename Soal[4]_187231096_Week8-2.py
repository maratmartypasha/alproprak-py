import math
tinggiAwal = 10
print("masukkan radius alas (x)")
radiusAlas = float(input())
print("masukkan tinggi yang akan dipotong (y<10)")
tinggiTerpotong = float(input())
isiAwal = float(1) / 3 * math.pi * radiusAlas * radiusAlas * tinggiAwal
radiusTutup = radiusAlas * tinggiTerpotong / tinggiAwal
isiTerpotong = float(1) / 3 * math.pi * radiusTutup * radiusTutup * tinggiTerpotong
isiAkhir = isiAwal - isiTerpotong
garisPelukisAwal = math.sqrt(tinggiAwal * tinggiAwal + radiusAlas * radiusAlas)
luasAwal = math.pi * radiusAlas * (radiusAlas + garisPelukisAwal)
garisPelukisTerpotong = math.sqrt(tinggiTerpotong * tinggiTerpotong + radiusTutup * radiusTutup)
luasTerpotong = math.pi * radiusTutup * (radiusTutup + garisPelukisTerpotong)
luasAkhir = luasAwal - luasTerpotong
print("isi kerucut yang telah dipotong puncaknya")
print(isiAkhir)
print("luas permukaan kerucut yang telah dipotong puncaknya")
print(luasAkhir)
