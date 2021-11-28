""" 
Time: 28.11.2021 
programmer: Azimbek 
Theme : Eng ko'p uchraydigan xatolar 
"""
# Pythonda 3 xil xato uchraydi 

# NUMBER_1: Sytax error 

#print ("Hello world"
# Missing parentheses in call to 'print'. Did you mean print("Hello world")?

#print("hello world"
# File "C:\python\python_by_sariq_dev\lesson_12_eng_ko'p_uchraydigan_xatolar.py", line 17
#     ^
# SyntaxError: unexpected EOF while parsing
# EOF - end of function ; parse - grammatik tahlil qilmoq 
# EOF XATOLIKDA ANIQ JOY KO'RSATILMAYDI, BIZ UNI SINCHIKLAB QAYTA KO'RIB CHIQISHIMIZGA TO'G'RI KELADI 

# print("Hello world
# print("Hello world
#                       ^
# SyntaxError: EOL while scanning string literal
# EOL - end of line 

#NUMBER_2: IndentationError

#     print("Hello world")
#  print("Hello world")
#     ^
# IndentationError: unexpected indent - ya'ni kutilmagan bo'sh joy

# print("o'ngacha sanaymiz")
# for n in range(10):
# print(n+1)    

# print(n+1)
#         ^
# IndentationError: expected an indented block = to'p-to'p surish kutilgan edi 
# 1 ta joy tashlasak ham, 10 ta joy tashlasak ham dastur ishlayveradi, lekin keyingi 
#shu funksiyaning ichida biror amalda oldingidek joy tashlanmasa dasturimiz ishlamaydi
# tab orqali 4 ta surish yoki space(probel) tugmasini 4 marta bosish tavsiya etiladi 

# Number_3: Run time Error - dastur bajarilib bo'lingandan keyin chiqadigan xatolar 

# TypeError - 
 
# son = input("Istalgan son kiriting \n>>>") 
# son = int(son)
# print(f" {son} ning kvafdati {son**2} ga teng")
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

#NameError - biror funksiyaning nomi xato yozilishi 

# prit("Hello world!")
# NameError: name 'prit' is not defined - bunaqa narsaning o\'zi yo\'q
# print("Hello world!")

# mevalar = ['olma', 'uzum', 'anjir', 'shaftoli', 'olcha']
# for meva in mvalar:
#     print(meva)
# NameError: name 'mvalar' is not defined
    
# ValueError - qiymatda xatolik 

# son = int(input("Istalgan son kiriting \n>>>"))
# if son > 0: 
#     print(f"{son} soni musbat son" )
# elif son <= 0:
#         print(f"{son} soni manfiy son" )
# ValueError: invalid literal for int() with base 10: '23.5'

# # IndexError 
# mevalar = ['olma', 'anor', 'uzum']
# print(mevalar[3])
# IndexError: list index out of range

#ZeroDivisionError - nol(0) ga bo'lishda xatolik 
# x, y = 50, 50 
# z = 250/(x-y)
# ZeroDivisionError: division by zero

# Mantiqiy xatolar - bu xatolarni python xato deb hisoblamaydi, natija ham chiqadi, 
#faqat natija xato chiqovuradi 

# radius = 5
# pi = 4.14
# aylana_yuzi = pi * radius**2
# print(aylana_yuzi) 

#pi = 3.14 bo'lishi kerak edi lekin biz nimadir sabab bo'lib uni boshqa qiymatga 
# almashtirib qo'ydik, Dasturning yangi abnavleniyasi chiqqanda shu narsalar to'g'irlanib ketiladi 

# son = float(input("Istalgan son kiriting \n>>>"))
# ildiz = son**1/2 # son avval 1 ga ko'paytirilib so'ng 2 ga bo'linayapti 
# # aslida esa son**(1/2) yoki son**0.5 bo'lishi kerak 
# print(f"{son} ning ildizi {ildiz} ga teng") 

# mevalar = ['olma', 'uzum', 'anjir', 'shaftoli', 'olcha']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")

# bu yerda dastur tugadi degan yozuv ko'p marta takrorlanayapti, 
# chunki u for sikli badani ichida qolib ketgan