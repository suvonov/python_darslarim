# username = Azimbek 
# time : 02.04.2021
# theme : 06-dars. Sonlar bilan ishlash 

a = 20 
b = 5.5
# a= (int) integer = butun son 
# b =(float)  floating point number = suzuvchi nuqatli sonlar 
temp = 36.6

print(type(a))
aholi_soni = 7_594_376_356
print("Aholi soni ", aholi_soni) 
x, y, z = 10, 5.5, -56

c= a*b
print(c)
d = 100/2
print(d)
m = 100//2
print(m)
radius = 20
Pi = 3.14159
diametr = 2*radius
print("Aylana uzunligi ", Pi * diametr)
# python dasturlsh tilida doimiy o'zgaruvchi yo'q ya'ni constanta
#dasturchilar Bosh harfli o'zgaruvchilarni ko'rishganda 
# bu o'zgarmas qiymat deb qabul qilishga kelishishgan 
ism = "Jobir"
yosh = 36 
yosh = str(yosh) 
xabar = ism + '   ' + yosh + " yoshda"
print(xabar)
# str - ma'lumotlarni ma'lum bir tipdan boshqa tipga o'zgartiradi 
# ya'ni bu berilgan qiymatdan bizga qator ya'ni tekst qaytaradi
# shundan boshlab yosh o'zgaruvchisi qator holatda ko'riladi raqam holatida emas
yosh = 36
ism = "Jobir "
xabar = ism + ''+ str(yosh)+ " yoshda" 
print(xabar)
# 
t_yil = int(input("Tug'ilgan yilingizni kiriting: ") )
yosh = 2021-t_yil
print("Siz " + str(yosh) + " da ekansiz")
# input() matni istalgan tipdagi ma'lumotlarni str ko'rinishida qabul qilib oladi 
# raqamga aylantirish uchun undan oldin int() funksiyasidan foydalaniladi

t_yil = int(input("Tug'ilgan yilingizni kiriting: ") )
yosh = 2021-t_yil
print("Siz ", yosh ," da ekansiz")

temp = 36.6
temp = str(temp) 
# int(temp)  bunda xatolik chiqadi, chunki 36.6 butun son emas
temp =  float(temp)

# int() sonlarni butun songa aylantiradi 
a=int("10")
b = float("10")
temp = str("36.6")
