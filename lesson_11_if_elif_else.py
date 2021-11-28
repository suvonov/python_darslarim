""" 
theme : if-elif-else operatorlari 
programmer : Azimbek 
time : 25.11.2021 
""" 

# son = 50
# if son > 0:
#     print("Son musbatga teng ")
# else: 
#     print("Son manfiyga teng ")

# son = -45
# if son > 0:
#     print("Son musbatga teng ")
# else: 
#     print("Son manfiyga teng ")
    
# yosh = int(input("Yoshingizni kiriting? "))
# if yosh <= 7:
#     print("Sizga kirish bepul")
# elif yosh <= 12 :
#     print('Sizga bilet puli 50% , ya\'ni 5000')
# elif yosh <=18:
#     print('Sizga kirish bilet puli 8000 so\'m')
# elif yosh <=65:
#     print('sizga kirish bilet puli 8000 so\'m')
# elif yosh > 90:
#     print("Siz murdasiz yoki arvohsiz")
# else : 
#     print("Sizga kirish puli 10000")

# yosh = int(input("Yoshingingizni kiriting \n >>> "))

# if yosh <=7:
#     narx = 4000
# elif yosh <=18:
#     narx = 8000
# elif yosh <= 55:
#     narx = 10000
# else :
#     narx = 0
# print(f'sizga kirish narxi {narx} so\'m')

# or operatorlari

# kun = input("Bugun haftaning qaysi kuni ? \n >>>")
# if kun.lower() == "shanba" or "Yakshanba":
#     print("Bugun dam olish kuni ")
# elif kun.lower() == "dushanba" or "seshanba" or "chorshanba" or "payshanba" or "juma":
#     print("Bugun ish kuni ")

# kun = input('Bugun qanday kun ? \n >>>')
# harorat = float(input("Havo harorati qanday ? \n >>>"))

# if kun.lower() == "yakshanba" and harorat >=30:
#     print('Cho\'milgani ketdik')
# elif kun.lower() == 'yakshanba' and harorat <30:
#     print("Uyda dam olamiz")

# kun = input('Bugun qanday kun ? \n >>>')
# harorat = float(input("Havo harorati qanday ? \n >>>"))

# if (kun.lower() == "yakshanba" or kun.lower() == 'shanba') and harorat >=30:
#     print('Cho\'milgani ketdik')
# elif (kun.lower() == "yakshanba" or kun.lower() == 'shanba') and harorat <30:
#     print("Uyda dam olamiz")
# # agar joy tashlanib ketilsa dastur ishlamayapti

# narh = 15000 # mijoz 15 000 ga ovqat oldi 
# salat = False # mijoz salat olmadi 
# choy = True # mijoz choy oldi 

# if choy and salat:# agar mijoz ham choy ham salat olgan bo\'lsa
#     narh = narh + 10000
# elif choy or salat: # agar choy yoki salat olinsa 
#     narh = narh + 5000
# print (f'Jami {narh} so\'m') 

# narh = 15_000 # mijoz 15 000 ga ovqat oldi 
# choy = True # biz True qiymat o'rniga 1 sonini qo'yib ketsak ham bo'ladi
# salat = False # False qiymat o'rniga 0 raqamini qo'ysak ham dastur ishlaydi
# non = True
# kompot = True 
# assorti = False 

# # Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas 
# if choy :
#     print("Mijoz choy oldi ")
#     narh = narh + 3_000
# if salat: 
#     print("Mijoz salat oldi ")
#     narh = narh + 5_000
# if non: 
#     print("Mijoz non oldi ")
#     narh = narh + 3_000
# if kompot: 
#     print("Mijoz kompot oldi ")
#     narh = narh + 5_000
# if assorti: 
#     print("Mijoz assorti oldi ")
#     narh = narh + 15_000 
# print(f"Jami {narh} so\'m") 

# in funksiyasi ro'yxat ichida biror obyekt bormi yo'qligini tekshiradi 

# menu = ['osh', 'qozonkabob', 'somsa', 'norin', 'somsa']
# print('manti' in menu) # manti menyuda bormi ?  
# print('somsa' in menu) # somsa menyuda bormi ?
# ovqat = input("Siz nima ovqat yeysiz? \n>>>")
# if ovqat in menu: 
#     print("Buyurtmangiz qabul qilindi !")
# else: 
#     print("Afsuski menyumizda bunday ovqat yo'q! ")

# not in yordamida ro'yxatda biror obyekt yo'qligini tekshiradi 

# print('osh' not in menu )
# print('lavash' not in menu )

# ovqat = input("Siz nima ovqat yeysiz?")
# if ovqat not in menu: 
#     print("Afsuski menyumizda bunday ovqat yo'q! ")
# else: 
#     print("Buyurtmangiz qabul qilindi !")

#buyurtmalar =('osh', 'somsa', 'manti', 'shashlik')
# for taom in buyurtmalar: 
#     if taom in menu:
#         print(f"Menyuda {taom} bor")
#     else: 
#         print(f"Kechirasiz, Menyuda {taom} yo'q")

# ba'zan foydalanuvchi aynan biron narsa buyurtmasligi ham mumkin
# buning uchun biz ro'yxatning menyuning ichini tekshirib ko'rishimiz kerak bo'ladi 

# buyurtmalar = ()
# if buyurtmalar: 
#     print(f"menyuda {len(buyurtmalar)} ta taom bor ")
# else:
#     print("ro'yxat bo'sh")
    
menu = ['osh', 'qozonkabob', 'somsa', 'norin', 'somsa']
buyurtmalar =('osh', 'somsa', 'manti', 'shashlik')

if buyurtmalar: 
    for taom in buyurtmalar:
        if taom in menu:
            print(f'Menyuda {taom} bor ')
        else: 
            print(f'Kechirasiz, menyuda {taom} yo\'q')
else: # agar savatcha bo'sh bo'ladigan bo'lsa 
    print("Sizning savatchangiz bo'sh")