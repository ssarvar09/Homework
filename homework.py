# ###1
def toliq_ism(ism, tugilgan_kun, joriy_yil=2025):
    """Foydalanuvchi ism va yilini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi yili: {joriy_yil-tugilgan_kun}\n")
toliq_ism('sarvar',16)


# ###2
def kvadrat_va_kub():
    s = float(input("hohlagan sonizni kiriting:"))
    k = s **2
    k2 = s **3
    print(f"{s}ning kvadrati:{k}✅")
    print(f"{s}ning kubi:{k2}✅")
kvadrat_va_kub()
#
#
# ### 3
def juft_va_toq():
    s1 = float(input("bironta son kiriting:"))
    if s1 % 2==0:
        print("juft son")
    else:
        print("toq son")
juft_va_toq()


### 4
def katta_va_kichik(a,b):
    if a>b:
        print(f"Kattasi: {a}")
    elif a<b:
        print(f"Kattasi: {b}")
    else:
        print("teng sonlar")
katta_va_kichik(24,43)













