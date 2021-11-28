# username: Azimbek 
# date : 02.04.2021 
# theme : 05-dars/ Strings (matnlar)
ism ="Azimbek" 
shahar = "Termez"
viloyat = "Surxondaryo"
matn = "Men yangi 📱 sotib oldim"
smayl = "🥰"
print(matn)
# string ustida amallar 
print("Mening ismim " + ism)
ism="Azimbek "
familiya="Suvonov"
print(ism+familiya)
print(familiya+" "+ism)
ism='Azimbek'
familiya ='Suvonov'
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
print(f"Mening ismim {ism}")
ism='James'
familiya='Bond'
print(f"Salom, mening ismim {ism}. {ism} {familiya}!")

# maxsus belgilar 
print('Hello, world!')
print('hello,\t world')
# backflesh \t beldgi o'zidan keyin 4 ta probel qoldiradi 
print('Hello \n world')
# backflash \n belgisi o'zidan keyingi so'zni yangi qatorga ko'chiradi 

# MATN METODLARI 
# matn.metod() nomi bilan murojaat qilinadi
ism='james'
familiya='bond'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())
ism_sharif=ism_sharif.upper()
# .upper() metodi matn ichidagi hamma harflarni katta qilish uchun ishlatiladi
print(ism_sharif.lower())
# .lower() metodi esa matn ichidagi hamma harflarni kichkina qiladi  
print(ism_sharif.title())
# .title() metodi esa matn ichidagi har bir so'zni bosh harfga aylantiradi
print(ism_sharif.capitalize())
# capitalize() metodi gap ichidagi kabi bosh harfga aylantiradi 

meva = "     olmani    "
print("Men " + meva.lstrip() + "yaxshi ko'raman")
# .lstrip() metodi chap tarafdagi bo'shliqni olib tashlaydi
print("Men " + meva.rstrip() + " yaxshi ko'raman!")
# .rstrip() metodi o'ng tarafdagi bo'shliqni olib tashlaydi
print("Men " + meva.strip() + " yaxshi ko'raman!")
# .strip() metodi so'zning har ikki tomonidagi bo'shliqlarni olib tashlaydi

# INPUT METODI 
# input metodi foydalanuvchidan qandaydir ma'lumotlarni olish uchun ishlatiladi
# ya'ni foydalanuvchi ma'lumotlarni o'zi kirgizadi 

ism=input("Ismingiz nima?\n>>>")
print("Assalomu aleykum " + ism.title() + " Siz bilan tanishganimdan xursandman!")
name=input("What is your name, sir?\n>>>")
age= input("How old are you?")
place = input("where are you from?")
print("Your name is " + name.title() + " Madam")
print("Your age is  " + age + "years old")
print("You are from " + place.upper()+ "I'm glad to see you!!!")

