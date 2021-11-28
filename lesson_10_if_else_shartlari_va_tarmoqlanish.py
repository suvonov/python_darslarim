# username : Azimbek 
# Time : 11.04.2021
# Theme : if-else shartlanish va tarmoqlanish 

### RO'YXAT ICHIDAGI HAR BIR SO'ZNI BOSH HARFGA AYLANTIRDI 

avtolar = ['audi', 'bmw', 'volva', 'kia', 'hyundai' ]
for avto in avtolar:  # avtolar ichidagi har bir avtolar uchun 
    print(avto.title())
    # bu yerda bmw so'zining barcha harfi bosh bo'lib yozilishi kerak
### AGAR RO'YXAT ICHIDA QISQARGAN SO'ZLAR BO'LIB QOLSACHI     

    
avtolar = ['audi', 'bmw', 'volva', 'kia', 'hyundai' ]
for avto in avtolar:  # avtolar ichidagi har bir avtolar uchun 
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa...
    # = teng ma'nosini beradi 
    # == tengmi 
        print(avto.upper()) # avto nomining har bir harfini bosh harfga aylantirgin
    else:   # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini bosh harf qilgin

### TRUE / FALSE EKANLIGINI TEKSHIRISH UCHUN 
   
print(avto)   # AVTO BU YERDA RO'YXATNING ENG OXIRGI ELEMENTINI QABUL QILIB OLADI  
print(avto == 'bmw')   # dastur FALSE berdi. chunki u hyundaiga teng emas 
print(avto =="hyundai") # dastur TRUE beradi, chunki u hyundaiga teng 

# agar argument TRUE bo'lsa If qismi bajariladi 
# agar argument FALSE bo'lsa else qismi bajariladi 


### BERILGAN QIYMATNI TRUE/FALSE GA TEKSHIRISH 


a = "Ali" # qiymat "Ali" 
print(a=="ali") # a tengmi "ali" ga : False 
print(a== "Ali")  # a tengmi "Ali" ga : True 
# matnlarni solishtirishda katta yoki kichik harf ekanligiga e'tibor berishimiz kerak 

# saytlardan ro'yxatdan o'tayotganimizda u katta yoki kichik harf ekanligini tizimdagi 
# akkauntga solishtirib chiqadi. bir xil chiqmasa, xato berovuradi 
# biz matnlarni bir xil ko'rinishga keltirib olishimiz kerak 

ism = "Ali"

# ism.lower() =="ali" deb so'raganimizda u true qiymat qaytaradi 

print(ism.lower()== "ali")
  
# = TENG 
# == TENGMI DEB SO'RAYAPMIZ 
# != TENG EMASMI deb so'rayapmiz 
a= 5 
print(a==5) # True (a teng 5 ga) 
print(a==10) # Falsa (a 10 ga teng emas)
print(a!=10) # True (a teng emas 10 ga, shundaya : true (teng emas) )
print(a!=5) # False (a teng emas 5 ga, shundaya : False (u 5 ga teng))

### SAYTDA RO'YXAT TO'LDIRISH

###ism = "zaynura"
ism=input("Ismingiz nima, xonim? \n >>> ")# foydalanuvchining ismini so'radik 
if ism.lower() != "zaynura":# agar ism "zaynura" ga teng bo'lmasa ... 
    print(f" Uzur, {ism.title()} , siz uchun kaminaning qalbi berk, uning o'z egasi bor" )
else:
    print("Salom, qalbimning malikasi.\n")
    print("I LOVE YOU, MY LIFE!!!")    
    
### != (TENG EMAS) BELGISINI SONLAR USTIDA ISHLATIB KO'RISH 

javob = float(input("12 x 6 = ? (Nechaga teng?)\n>>> "))
### float funksiyasi butun sonlar uchun ishlatiladi    
if javob != 72: ## agar javob 72 ga teng bo'lmasa 
    print(" Siz xato javob berdingiz")
else: 
    print("siz to\'g\'ri topdingiz".title())
    
#### SAYTLARDAGI YOSHNI TEKSHIRIB KO'RISH 

yosh = int(input("Sizning yoshingiz nechada?\n>>>")) 
if yosh >= 18: ### 18 dan katta yoki teng bo'lsa
    print("siz bu saytga kira olasiz\n".capitalize())
else: # aks holda
    print("\n Siz uchun bu saytga kirish ta'qiqlangan".upper())
    
# > kotta  
# <kichik 
# <= kichik yoki teng 
# >= katta yoki teng     

### LOGINLAR BILAN ISHLASH 

# len() funksiyasi matnning uzunligini tekshiardi 

login = input("Yangi login kiriting:")
if len(login) <= 5: # login uzunligini tekshiramiz 
    print("Parol 5 ta harfdan ko'proq bo'lishi shart")
    
### foydalanuvchining tug'ilgan yiliga qarab tekshirish

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2021-yil<18: # foydalanuvchining yoshini so'raymiz 
    print(f"Yoshingiz {2021 - yil} da ekan")
    print("Kirish mumkin emas!")
else: 
    print("Xush kelibsiz !")
    
yosh_2 = int(input("Yoshingiz nechada?"))
if yosh_2 >65: print("Siz COVID 19 RISK GURUHIDA EKANSIZ")   
# agar kodimiz qisqa bo'lsa, bu holatda ham yozish mumkin

x, y = 25, 50 # x=25, y + 5 
print("x>y") if  x>y else print("x<y") 
# ifning badani if dan oldin kelgan, else niki esa o'zidan keyin kelgan 

