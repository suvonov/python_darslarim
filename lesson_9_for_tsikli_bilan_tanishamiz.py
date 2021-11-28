### USERNAME : AZIMBEK 
### DATE : 10.04.2021 

### PROGRAMMING COURSE ON PYTHON 


### FOR TSIKLI BILAN ISHLASH 

# sikl aylantirish - ma'lum bir kodni qayta-qayta takrorlamaslik uchun ishlatiladi 

mehmonlar =['Ali' , 'Vali' , 'Hasan' ,'Husayn' , 'Olim' ]
for mehmon in mehmonlar: 
    print("Assalomu aleykum" , mehmon) 
    print(" Hayrli kun, ey qadrli mehmonimiz !" , mehmon) 
#### siklning body qismi 4 ta probel bilan yozilishi kerak bo'ladi, 
# agar kam/ko'p bo'lib qolsa u xato ishlaydi 

mehmonlar =['Ali' , 'Vali' , 'Hasan' ,'Husayn' , 'Olim' ]
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 28-dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi\n")
    
#sonlar = list(range(1,11))
#for son in sonlar:
 #   print(f"{son} ning kvadrati {son**2} ga teng") 
  
    
sonlar = list(range(11)) ###11gacha sonlar ro'yxatini yozamiz
sonlar_kvadrati= [] ### bo'sh ro'yxat yaratamiz 
for son in sonlar: # sonlar ichidagi har bir son uchun 
    sonlar_kvadrati.append(son**2) # uni darajaga ko'tarib yangi sonlar_kvadrati degan o'zgaruvchiga yukla

print(sonlar)
print(sonlar_kvadrati) 
 

dostlar = [] # bo'sh ro'yxat yaratdik 
print("5 ta eng yaqin do'stingizning kim? ") # n bu yerda 0 dan 4 gacha qiymatlar oladi 
for n in range(5): # range(5) bu 0 dan 4 gacha sonlar qatori 
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting :  " ))
print(dostlar)
                         

