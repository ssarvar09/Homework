# 1
class Product:
    def __init__(self, id, nomi, narxi, soni, omborda, rating):
        self.id = id
        self.nomi = nomi
        self.narxi = float(narxi)   # narxni SON qilib oldik!
        self.soni = soni
        self.omborda = omborda
        self.rating = rating

    def info(self):
        print(f"Id: {self.id} , Nomi: {self.nomi}, Narxi: {self.narxi} so'm, "
              f"Omborda: {self.soni} dona, Rating: {self.rating}")

    def update_price(self, yangi_narx):
        self.narxi = float(yangi_narx)
        print(f"{self.nomi} narxi yangilandi: {yangi_narx}$Dollar")

product = Product(2009,'Asus Vivobook',500,'10','100','4')
p = product.info()



# 2
class Cart:
    def __init__(self):
        self.mahsulot = []
        self.ummumiy_narx = 0

    def add_product(self, product):
        self.mahsulot.append(product)
        self.calculate_total()
        print(f"{product.nomi} savatga qo'shildi.")

    def remove_product(self, product_id):
        for p in self.mahsulot:
            if p.id == product_id:
                self.mahsulot.remove(p)
                self.calculate_total()   # (oldin xato edi: calculate_totol)
                print(f"{p.nomi} savatdan olib tashlandi.")
                return
        print("Mahsulot topilmadi")

    def clear(self):
        self.mahsulot.clear()
        self.ummumiy_narx = 0
        print("Savat tozalandi.")

    def calculate_total(self):
        self.ummumiy_narx = sum(p.narxi for p in self.mahsulot)
        return self.ummumiy_narx

    def is_empty(self):
        return len(self.mahsulot) == 0

cart = Cart()
mahsulot = Product(1, 'iphone 13pro', 1000, 3, 4, 4.7)  # Narx: 1000 SON!
cart.add_product(mahsulot)
print("Umumiy narx:", cart.ummumiy_narx)











































































































































































































































































































