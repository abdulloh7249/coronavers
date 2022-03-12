# V12:
# Notebook nomli class e'lon qiling va
# - firmasi
# - model
# - CPU
# - DDR
# - price
# nomli property lari bo'lsin.
# - info_notebook()
# nomli method e'lon qiling, va bu method shu notebook haqida hamma ma'lumotlarni text shaklida ekranga chiqarsin

# class Noutbook:
#     def __init__(self):
#         pass
#     def info_noutbook(self):
#         self.firmasi = "Lenovo"
#         self.model = "legion"
#         self.spu = 8
#         self.DDR = 1000
#         self.price = "tushunmadim"
# mana = Noutbook
# print(f"firma {mana.info_noutbook}")

# V21:
# Animal nomli class oching, va u:
# - name
# - age
# nomli property larga ega bo'lsin, hamda
# - eat()
# nomli method ga ega bo'lsin, ichiga "eat" ni print qiling
# So'ngra, Birds nomli class oching, bu class Animals class idan voris olsin. Birds ni ichida shunchaki pass bo'lsin.
# Shu class dan
# - owl
# nomli object oching, va owl uchun eat method ini ishalting
# V21:
# class Animal:
#     def __init__(self):
#         self.name = None
#         self.age = None
#
#     def eat(self):
#         print("eat")
#
#
# class Birds(Animal):
#     pass
#
# owl = Animal()
# owl.eat()



# Odam va kuchuk classlarini e'lon qiling. Odamda
# - ism               »»»» property
# - baqirish()     »»»» method
# lari bo'lsin. Kuchukda
# - laqab            »»»» property
# - tishlash()      »»»» metod
# lari bo'lsin. Shulardan foydalanib 1 ta odam va kuchik obyekti e'lon
# qilng va kuchukning tishlash methodi chaqirilganda odamning baqirish metodi ham ishlasin.
# V20

# class Odam:
#     def baqirish(self):
#         self.ism="baqay"
#         print("baqirdi")
# class Kuchuk:
#        def tishlash(self):
#            self.laqab = "bobik"
#            print("tishladi")
# odam = Odam()
# kuchuk = Kuchuk()
# kuchuk.tishlash()
# odam.baqirish()


# Aylana nomli Class e'lon qiling, u 1 ta parameter qabul qilsin:
# - radius
# va shu Class ning:
# - aylana_uzunligi       »»»»   aylana uzunligini qaytaruvchi function
# - aylana_yuzi              »»»»   aylananing yuzini qaytaruvchi function
# nomli methodlari bo'lsin. Ushbu Class dan 2 object oling, va shu '
# objectlarning aylana uzunligi hamda aylana yuzalarini hisoblang
# V19:
# class Aylana:
#     def __init__(self, keldi):
#         self.radus = keldi
#
#     def aylana_uzunligi(self):
#         return round(2*3.14*self.radus)
#
#     def aylana_yuzi(self):
#         return round(3.14 * self.radus**2)
#
#
# aylana = Aylana(5)
# print(aylana.aylana_yuzi())
# print(aylana.aylana_uzunligi())

# V28:
# Player() classi e'lon qiling. Property lari:
# - jon
# - qurol
# Methodlari:
# - otish()
# - reduce_life()                »»»»» ya'ni player o'q yegan vaqtda jonni
# kamytirib qo'yuvchi method
# Shu classdan 2 ta object hosil qiling.
# 1-obyekt 2-sini otganda 2-sini joni qanchagadir kamaysin.
# Yoki
# 2-obyekt 1-sini otganda 1-sini joni qanchagadir kamaysin.
class Player():
    def __init__(self):
        pass
    def jon(self):
        pass
    def qurol(self):
        pass
    

