""" 
username: Azimbek 
date: 05.04.2021
theme :7-dars list bilan ishlash 
"""
# list bu ro'yxat hisoblanadi 
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] #mevalar ro'yxati {list} text ko'rinishida
narxlar = [20000, 30000, 50000, 15000, -63, 52.35] # narxlar ro'yxati (son)
sonlar = ["bir", 'ikki', 3, 4, 5 ] # sonlar va so'zlar aralash
ismlar = [] # bo'sh ro'yxat 
# dasturlash tilida ro'yxat ichidagi har bir qiymat elementlar deb yuritiladi va ular 0,1,2,3 deb sanaladi
# indeks = tartib raqami
print(mevalar[0])
# agar listdagi oxirgi so'zni chiqarmoqchi bo'lsak indeks ichiga [-1] 
# oxiridan ikkinchi elementni chiqarmoqchi bo'lsak indeksga [-2]
print(mevalar[0].upper()) # barcha harflar katta
print(mevalar[-2].title()) # faqat birinchi so'zni katta
print(narxlar[0] + narxlar[2]) 
# ro'yxat ichidagi qiymatlar ustida ham bemalol amallar bajarsak bo'ladi
print(narxlar[0] + 58000 - 900000 + 35.0005)
# ro'yxatga o'zgartirish kiritishning 1-usuli: indeksning o'rnidan foydalanamiz
mevalar[0] = 'anor'
print(mevalar)
mevalar[-1] = 'uzum'
print(mevalar)

# .append() metodi ro'yxatga yangi elementni oxiridan qo'shadi 
mevalar.append('tarvuz')
print(mevalar)
mevalar.append("o'rik")
print(mevalar)
# .insert() metodi - ro'yxatning istalgan joyiga ma'lumot qo'shishga yordam beradi 
mevalar.insert(0, "banana") # avval indeks. keyin object qo'shiladi
print(mevalar)
mevalar.insert(3, "ananas")
print(mevalar) 

cars = []
# ro'yxat yaratoyotganimizda ko'plik shaklida turish tavsiya etiladi 
cars.append("Lacetti")  
cars.append("Nexia")
cars.append("Malibu")
cars.append("Tracker")
print(cars)
del cars[0] # o'chirilish kerak bo'lgan indeks ko'rsatiladi
# del() operatori orqali listdagi biror qiymatni o'chiramiz
print(cars)
cars.insert(0, "Nexia 3")
print(cars) 
del cars[1] 
print(cars)

# remove("cskjcjsvh")
# ro'yxat ichidagi biror qiymatni o'chirishimiz kerak, lekin uning indeksini 
# bilmaymiz, shunda biz removdan foydalanamiz 
cars.remove("Malibu")
print(cars)

hayvonlar = ["It", "mushuk", "sigir", "qo'y", "quyon", 'mushuk']
hayvonlar.remove("mushuk")
print(hayvonlar)
# remove metodi ro'yxat ichidagi bir xil nomlarning faqatgina ro'yxatning 
# eng boshidagisini o'chiradi qolgan nomlarni o'chirish uchun 
# bu metodni qayta-qayta takrorlashga to'g'ri keladi  

# pop() metodi
# ro'yxat ichidan biror elementni sug'urib olishimiz kerak
#

bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
mahsulot = bozorlik.pop(1)
print(mahsulot) 
print(bozorlik)

bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
mahsulot = bozorlik.pop(3) # ro'yxatdan bananni sug'urib olamiz 
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar " , bozorlik)

# Agar pop() metodidan keyin hech qanaqangi indeks ko'rsatmasak, 
# bizga ro'yxat oxiridagi eng oxirgi elementni sug'urib beradi 

mahsulot2 = bozorlik.pop()
print(mahsulot2)

print(narxlar)
narxlar.remove(-63)
narxlar.remove(52.35)

print(narxlar)

narxlar[0] = narxlar[0]+2000
print(narxlar)
