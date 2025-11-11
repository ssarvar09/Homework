###### 1
# # add() elemenlarni qo'shadi
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)
#
# d = {'ali', 'sardor', 'samir'}
# d.add('shermat')
# print(d)
#


# ####2
# clear() setni bo'shatib beradi
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)
#
#
#
# s = {'pear','apple','banana'}
# s.clear()
# print(s)



####3

# copy() nushalab setdai kabi chqarib beradi

# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)
#
#
# h = {'sher', 'yo\'lbars', 'baliq'}
# k = h.copy()
# print(h)


#### 4

##difference()	-	2da matinda bir hil soz bolsa wularni olib tawlaydi
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)
#
#
# x = {"on ix", "damas", "spark"}
# y = {"malibu", "gentra", "on ix"}
# z = x.difference(y)
# print(z)


###### 5

###difference_update()	-=	Removes the items in this set that are also included in another, specified set
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y)
# print(x)
#
#
#
# x = {"telefon", "ayiq", "baliq"}
# y = {"televizor", "noutbook", "telefon"}
# x.difference_update(y)
# print(x)



#### 6 discard()	 	sozlarni belgilab print qilsangiz olib tawlaydi
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)
#
#
# kiyimlar = {"qurtka", "shim", "paypoq"}
# kiyimlar.discard("shim")
# print(kiyimlar)


### 7 intersection()	& alohida bolgan listlarda bir hil so'ni topib ajratib oladi
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)
#
#
#
# y = {"google", "microsoft", "ali"}
# x = {"ali", "akmal", "kamron"}
# z = x.intersection(y)
# print(z)


### 8 intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)
#
#
#
# x = {"sobir", "vali", "sardor"}
# y = {"zohid", "suxrob", "sobir"}
# x.intersection_update(y)
# print(x)


### 9 isdisjoint()	 	Returns whether two sets have a intersection or not

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z)
#
#
# x = {"apple", "banana", "cherry"}
# y = {"apple", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z)
#

### 10 issubset()	<=	Returns True if all items of this set is present in another set

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)
#
#
# x = {"b", "a", "l"}
# y = {"f", "e", "d", "w", "k", "s"}
# z = x.issubset(y)
# print(z)

### 11 issuperset()	>=	Returns True if all items of another set is present in this set
#
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)
#
#
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"s", "h", "l"}
# z = x.issuperset(y)
# print(z)


### 12 pop()	 	Removes an element from the set
# fruits = {"apple", "banana", "cherry"}
# fruits.pop()
# print(fruits)
#
#
# fruits = {"sarvar", "ali", "sobir"}
# fruits.pop()
# print(fruits)



### 13 remove()	 	belgilanganlarni olib tawlaydi

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
#
#
# car = {"supra", "bmw", "mers"}
# car.remove("mars")
# print(fruits)


### 14 symmetric_difference()	^	Returns a set with the symmetric differences of two sets

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
#
#
# x = {"sobir", "sardor", "salim"}
# y = {"abu", "shermat", "ali'"}
# z = x.symmetric_difference(y)
# print(z)


### 15 symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)
#
#
# x = {"volga", "tiko", "matiz"}
# y = {"mers", "bugatti", "bmw"}
# x.symmetric_difference_update(y)
# print(x)



### 16 union()	|	Return a set containing the union of sets

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z)
#
#
# x = {"sardor", "jony", "tohir"}
# y = {"shermat", "ali", "charos"}
# z = x.union(y)
# print(z)


### 17 update()	|=	Update the set with the union of this set and others

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.update(y)
# print(x)
#
#
# x = {"spark", "damas", "cobalt"}
# y = {"gentra", "lasetti", "nexia"}
# x.update(y)
# print(x)
#
