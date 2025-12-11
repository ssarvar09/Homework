# # ### 1  Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
import datetime as dt
bugunn = dt.date.today()
for h in range(10):
    hisobla = bugunn + dt.timedelta(days=14*h)
    print(hisobla)
#
# # ### 2  Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
import datetime as dt
bugun = dt.date.today()
ramazon_kuni = dt.date(2026,2,19)
qurbon_hayiti = dt.date(2026,5,28)
farq = ramazon_kuni - bugun
farq2 = qurbon_hayiti - bugun
print(f"Ramazon oyiga {farq.days} kun qoldi😊 \nQurbon hayitiga {farq2.days} kun qoldi😊")
#
#
# ### 3  Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
from  datetime import date
def yil_hisobla(yil,oy,kun):
    tugildim=date(yil,oy,kun)

    hozir=date.today()

    hisobla = (hozir - tugildim).days

    yil = hisobla //365
    oy = hisobla %365 //30
    kun = hisobla %365 %30
    return yil,oy,kun
yil,oy,kun= yil_hisobla(2009,5,7)
print(f'sizning tug\'ilgan kuningizga {yil}yil,{oy}oy,{kun}kun bo\'libdi😊')
#
#
# # ### 4 Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
import re
# matn = """assalomu alaykum  +919367788755 IT park sarvar@gmail.com menijiriman +998990679412"""
kirit = input("Telefon raqamingizni kiriting:")
andoza ='[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
if re.fullmatch(andoza,kirit):
    print('nomer to\'g\'ri✅')
else:
    print('bu nomer to\'g\'ri emas❌')


### 5 Biror mantdan (biror mant ichida url qatnashtiring ) veb sahifa manzilini ajratib olyuvchi funksiya yozing.
import re
matn = 'https://sarvar.com, www.gogle.com, https://ali.com'
def url_u(matn):
    andoza = r'https?://[^\s]+'
    url = re.findall(andoza, matn)
    return url
print(url_u(matn))

