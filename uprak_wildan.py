print("1.balok")
p = int(input("masukan nilai pajang: "))
l = int(input("masukan nilai lebae: "))
t = int(input("masukan nilai tinggi: "))
volume_b = p * t 
print("volume balok adalah",volume_b)

print("2.linas")
la = int(input("masukan nlai luas alas: "))
t = int(input("masukan nilai tinggi: "))
volume_la = 1/3 * la * t 
print("volume limas adalah", volume_la)

print("3.tabung")
la = int(input("masukin nilai alas: "))
t = int(input("masukin nilai tinggi: "))
volume_t = la * t 
print("volume tabung adalah", volume_t)

kursDolar = 14000
rupiah = float(input("masukan uang rupiah= "))
rupToDol = rupiah/ kursDolar
    