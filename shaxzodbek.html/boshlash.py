# misol = 6+5
# print(misol)
# ism = 'shammi'
# print(ism)
# import turtle
# import colorsys
# t = turtle. Turtle()
# s = turtle. Screen(). bgcolor ('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range (360):
#     c =colorsys.hsv_to_rgb(h, 1, 0.8)
#     h+= 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range(2):
#         t.left(2)
#         t.circle(100)
# ism = 'shamshod' 
# yosh = 18
# xabar = ism + ''
# mevalar = ['olma', 'anor', 'uzum' , 'shammi']
# print("Birinchi meva:", mevalar [0])
# narhlar=[12000, 1000, 3000, 12000]
# # print(narhlar[3] + narhlar[0])
# print("narxlar", "\n", mevalar[0],' = ',  narhlar[0], "\n", mevalar[1], " =" , narhlar[1], "\n", mevalar[2], " =" , narhlar[2]), "\n",
# mevalar= ["olma", "anor", "nok", "uzum", "anjir"]
# sonlar = [10, 20, 30, 40, 50]
# for son in sonlar:
#     print(son)
# Ismlar ro'yxatini yaratish
# ism= "Durvadik"
# print ("mening ismim "  +  ism)

# ism = "James"
# familiya = 'Bond'
# print(f"salom, mening ismim {ism}. {ism} {familiya} ")

"""
# sort() bilan ishlash
cars=["Bmw", 'Aers toshbaqa', "supra"  ]
cars.sort()
print(cars)


# sort () da teskari yozish
cars=["Bmw", 'Aers toshbaqa', "supra"  ]
cars.sort(reverse=True)
print(cars)




# sorted() bilan ishlash
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)



# text nechda ekanlikini aniqlash
text= ['olma', 'anor', 'anjir', 'nok', 'banan']
print('text soni' , len(text))



#sonlar ketma-ketligini yaratish mumkin list(range(0,10))
text=list(range(0,10))
print(text)



# min()  max()   sum() bilan ishlash
narhlar=[1000,1200,300,5040,4512,2215]
arzon=min(narhlar)
qimmat=max(narhlar)
jami=sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
 


# ro'yxatni kesib olish 
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars=cars[0:2]
print(my_cars)





#amaliy mashg'ulot
countrs=["O'zbekiston", "Rossiya", "Qozog'iston", "Tojikiston", "Turkmaniston"]
text=sorted(countrs, reverse=True )
print(text)


#revers
fruits=["olma", "nok", "anor"]
fruits.reverse()
print(fruits)


#sort()
fruits=["olma", "nok", "anor"]
fruits.sort()
print(fruits)

#sort() teskari
fruits=["olma", "nok", "anor"]
fruits.sort(reverse=True)




#sonlar
numbers=list(range(120,1200,2))
jami=sum(numbers)
print(numbers,jami)


numbers=[120,1200,2]
numbers_1 = min(numbers)
numbers_2 = max(numbers)
javob = int(numbers_2-numbers_1)
print(javob)


#elementlar soni 
fruits=["olma", "nok", "anor"]
print(len(fruits))


cars=["bmw","mers", "audi", "bugatti"]
for car in cars :
    print(f"Hurmatli {car}, sizni ertaga bo'ladigan poygaga taklif qilamiz")
    print("hurmat bilan boshqaruvchi")

# sonlar=[12,135,155,1546,454,123,125]
sonlar1=list(range(520))
print(sonlar1[-20:])
# son= sonlar[4:]
# print(sonlar[-4])
# print[500:]


#taomlar
foods=["osh", "kabob", "manti", "sho'rva"]
nonushta=foods[:]  
nonushta.append("egg")
nonushta.append("choy")
nonushtaa=nonushta[0]=  "qaymoq va non"
print(foods)
print(nonushta)





#09 mavzu
ismlar=["olim","zohit", "shamshod", "abror"]
for dostlar in ismlar:
    print(f"Hurmatli {dostlar}" ,)
print(len(ismlar), "marta takrorlandi")


#sonlar
sonlar=list(range(11,100,2))
for son in sonlar:
    print(son**3)



#kino
kinolar=[]
print("sevimli filmlaringizni kiriting")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-kino nomini kiriting: "  ))
print(kinolar)


#sorov
ism=[]
print("suhbatlashgan odamizni kim edi")
for ismlar in range(5):
    ism.append(input(f"{ismlar+1} uning ismi nima edi: "))
print(ism)
"""



#amaliy mashg'ulot
# a=1
# b=2
# c=3
# d=4
# i=5
# print(a*b*c*d*i)



# 2chi amaliy mashg'ulot
# a=1
# for sonlar in range(1,151):
#     a = a * sonlar

# print(a)



# if va else

# sonlar=[12,25,1454,45,45641,1515,1450]
# for son in sonlar :
#     if son == 25:
#         print(son)
#     else :
#         print("teng emas ")



#amaliyot

# cars=["mers", "audi", "bugatti", "bmw"]
# for car in cars :
#     if car =="bmw":
#         print(car.upper())
#     else:
#         print(car.lower())


# cars=["bmw", "bugatti", "mers", "tayotta"]
# for car in cars:
#     if car !="bmw":
#         print(car.title())
#     else:
#         print(car.upper())


#keyingi amaliyot
# ism=input("ismingiz ")
# foydalanuvchi=["admin"]
# for men in foydalanuvchi:
#     if men.lower() =="admin":
#         print(men.title(), "Hush kelibsiz foydalanuvchilar ro'yxatini ko'rsataymi")
#     else:
#         print(men.upper(), "Hush kelibsiz")




#amalyot
# son = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting:"))
# if son==son2: print(f"Sonlar teng: {son}={son2}")



#amaliyot
# son = float(input("Istalgan son kiriting:"))
# print("Son manfiy") if son<0 else print("Son musbat")




#amaliyot
# son=int(input("son kiriting"))
# print(son**2 ) if son<0 else print("manfiy son kiriting")






#11- dars

# x=int(input("Juft son kiriting"))
# if x % 2 :
#     print("bu toq son")
# else:
#     print("rahmat")


#amaliy
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<=4 or yosh>=60:
#     price=0
# elif yosh<=18:
#     price=10000
# elif yosh>18:
#     price=20000
# print(f"Sizga kirish {price} so'm")


#amaliy
# son=float(input("birinchi sonni kiriting "))
# son2=float(input("ikkinchi sonni kiriting "))
# if son < son2:
#     print(son2, " > ", son )
# elif son > son2:
#     print(son," >", son2)
# elif son == son2:
#     print( son, "=", son2)



#amaliy
# mahsulotlar=["cola", "fanta", "redbull", "sprite", "olma", "anor", "uzum",]
# savat=[]
# print("nima kerak")
# for buyurtma in range(5):
#     savat.append(input(f"{buyurtma+1}-maxsulot nomini kiriting "))
# for x in savat:
#     if x in mahsulotlar:
#         print(f"bizda {x} bor")
#     else:
#         print(f"kechirasiz, bizda {x} yo'q")



#amaliyot

# ichimliklar=["cola", "sprite","kofe", "fanta", "pepsi","redbull", "adrinalin", "moxito"]
# kerak=[]
# borlar=[]
# yoqlar=[]
# print("nima kerak")
# for buyum in range(5):
#     kerak.append(input(f"{buyum+1}-maxsulot nomini kiriting "))
# for y in kerak:
#     if yoqlar ==[]:
#          print("hamma maxsulotlar bor")
#     if y not in ichimliklar:
#         yoqlar.append(y)    
# print("bizda bular yoq ", yoqlar) 





# #amaliy
# foydalanuvchilar=["zoxid", "shamshod", "elmurod", "nurali" , "behruz"]
# text=input("login ")
# if text in foydalanuvchilar:
#      print(f"iltimos boshqa login tanlang")
# else:
#         print(f"hush kelibsiz")


# son=int(input("son "))
# for i in range(2,11):
#     if son % i == 0:
#         print(f"{son} soni {i} ga qoldiqsiz bo'linadi")


# sonlar=[2,5,6,7,4,3,449,6545,265]
# for x in sonlar:
#     if x <10:
#         print(x)


#amaliy
# sonlar=range(1,51)
# for x in sonlar:
#     if x % 3 == 0 and x % 5 == 0:
#         print(x , "fizbuz")
#     elif x % 5 == 0 :
#         print(x, "buz")
#     elif x % 3 == 0 :
#         print(x," feez")


# #amaliyot 
# numbers=[1,5,2,54,1,5,3,4,6,2,3,5,3,78,6,78]
# numbers.remove(2)
# numbers.remove(5)
# numbers.remove(3)
# print(numbers)



# #amaliyot2
# numbers=[1,5,2,54,1,5,3,4,6,2,3]
# number=[]
# for x in numbers:
#     if x not in number:
#         number.append(x)
# print(number)


#git
a=(5)
b=(6)
print(a+b)