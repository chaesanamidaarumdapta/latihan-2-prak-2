import math
input("masukkan nama kota A =" )
x1 = float(input("masukkan lattitude kota A = "))
y1 = float(input("masukkan longittude kota A = "))

print("==================================================")

input("masukkan nama kota B = ")
x2 = float(input("masukkan lattitude kota B = "))
y2 = float(input("masukkan longittude kota B = "))

xlat = x2-x1
ylon = y2-y1

a = math.sin(math.radians(xlat/2)) **2 + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.sin(math.radians(ylon/2) **2)

# versi arc sinus
b = 2* math.asin(math.sqrt(a))

#versi tangen 2
r = 6371.071

print("===================================================") 

print("jarak antara dua kota adalah" , b*r , "kilometer")
 