# username: Azimbek 
# date : 09.04.2021 
# theme : lists. part 2

### TARTIBLASH 
cars=["bmw", "mersedez benz", "volvo", "general motors", "tesla", "audi"]
cars.sort()
print(cars)
# tartibga keltirganimizda katta harflar eng birinchiga o'tib oladi.
# shuning uchun harflar katta=kichikligiga e'tibor qaratishimiz kerak 
 
### KATTA VA KICHIK HARFLAR 
cars=["bmw", "Mersedez benz", "volvo", "general motors", "tesla", "audi"]
cars.sort()
print(cars)

# capitilise()
# title()
# upper()
# lower() kabi metodlardan foydalanib olinadi va bir xil harflarga aylantiriladi
# va keyin sort() metodidan foydalaniladi 
 
### TESKARI TARTIBLASH 

cars=["bmw", "mersedez benz", "volvo", "general motors", "tesla", "audi"]
cars.sort(reverse=True)
print(cars)
 

### vaqtinchalik tartiblash 

print(sorted(cars)) 

#### VAQTINCHALIK TESKARI TARTIBLASH 

print(sorted(cars, reverse=True)) 


#### TESKARI TARTIBNI SONLAR USTIDA QO'LLASH 

sonlar=[12, 45, 23, 56, 998, 1, -5, -7.2]
print(sorted(sonlar))

sonlar.sort()
print(sonlar)

sonlar.sort(reverse=True)
print(sonlar)


#### RO'YXATNI ORTIDAN QAYTARIB CHIQARISH 

cars=["bmw", "mersedez benz", "volvo", "general motors", "tesla", "audi"]
cars.reverse()
print(cars)


#### RO'YXAT UZUNLIGI 

print(len(cars))
print(len(sonlar))
uzunlik =len(sonlar + cars)
print(uzunlik)


### RANGE VA QADAM 
 

sonlar = list(range(0,10))
print(sonlar)
### range() metodidagi verguldan keyingi turgan raqamgacha bo'lgan sonlar 
# qatorini chiqarib beradi 
s=list(range(21,30))
print(s)

### qadam ### 

toq_sonlar=list(range(1,20, 2))
print("Toq sonlar : " , toq_sonlar) # 0 dan 20 gacha 2 qadamdan 

juft_sonlar=list(range(0,20,2)) # 0 dan 20 gacha 2 qadamdan
print("Juft sonlar : ", juft_sonlar)

sanash=list(range(0,101,10)) 
print(sanash)

### MIN(),MAX() , SUM ()  

narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narxlar)
print(arzon)
qimmat = max(narxlar)
print(qimmat)
jami = sum(narxlar)
print(jami) 
print("Eng arzon narx" , arzon , " . Eng qimmat narx ", qimmat, ".")           
print(" bugun bozorlikda jami ketgan summa " , jami, ".")

print("juft sonlar ichidagi eng kottasi ".capitalize(), max(juft_sonlar))
print("toq sonlar ichidagi eng kichigi ".capitalize(), min(toq_sonlar))

#### RO'YXATNI KESISH 

cars=["bmw", "mersedez benz", "volvo", "general motors", "tesla", "audi"]
my_cars = cars[0:3]  # 0-indeksdan boshlab 3 ta element ajratib oladi  
print("my first cars are ".capitalize(), my_cars) 
print("my father's are  ".capitalize() , (cars[2:5])) # 2-, 3-, 4- elementlarni ajratib olamiz
print("my mother's cars are ".upper(), cars[:4]) # ro'yxat boshidan 4-gacha kesadi 0,1,2,3
print("my brother's cars are  ".title(), (cars[2:])) # 2-elementdan boshlab ro'yxat oxirigacha kesadi

### RO'YXATDAN NUSXA OLISH 

numbers = [1, 2, 3, 4, 5] # raqamlar ro'yxatini yaratdik 
numbers2 = numbers # numbers ni numbers2 ga tenglashtirdik
numbers.append(6) # numbers2 ga 6 ni qo'shamiz 
numbers2.append(7) # numbers2 ga 7 ni qo'shamiz 
print("Bu sonlarning 1-ro'yxati " , numbers)
print("Bu sonlarning 2-ro'yxati " , numbers2)

numbers2 = numbers[:] # [:] ro'yxatni to'liq ko'chirib olinadi 
numbers2.append(8) # numbs2 ga 8 raqamini qo'shamiz 
numbers2.append(9) # numbs3 ga 9 raqamini qo'shamiz 
print("this is the first numbs are ".capitalize(), numbers, ".")
print("this is the second numbs are ".capitalize(), numbers2, ".")

### TUPLES  = O'ZGARMAS RO'YXAT 

tomonlar = (20, 30, 55.2 )
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

#toys[3] = "dragon"
#print(toys)

# o'zgarmas ro'yxatni o'zgartirish uchun uni list ga o'zgartirib olamiz
# toys.remove("bus")
# print(toys)
# o'zgarmas ro'yxatga o'zgartirish uchun [] qavs o'rniga () bu qavsni beramiz
# va u tuple ga o'zgardi, endi biz uni o'zgartira olmaymiz va yangi object ham qo'sha olmaymiz 

toys =list(toys)
print(toys)
print(type(toys))
 # tuple (o'zgarmas ro'yxatni o'zgartirish uchun uni list ga o'zgartiramiz)
# va undan istalgan objectni o'zgartira olamiz 
toys.remove("snake")
print(toys)
# va yana o'zgarmas ro'yxatga o'zgartirish uchun uni tuple metodiga aylantiramiz 
toys=tuple(toys)
print(type(toys))

