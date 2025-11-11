#capitalize()	gapni bowidagi sozni bow harfini katta qiladi
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "salom meing ismim sarvar."
x = txt.capitalize()
print (x)

txt = "men it parkda o'qiyman."
x = txt.capitalize()
print (x)



# casefold()	hamma harflarni kichkina qiladi
txt = "men it parda backend kursida o'qiyman"
x = txt.casefold()
print(x)

txt = "men tinofka ham qilaman"
x = txt.casefold()
print(x)

txt = "hozir home work iwlayapman"
x = txt.casefold()
print(x)


# center()	sozni ortaga qoyadi
txt = "nautbuk"
x = txt.center(20)
print(x)


txt = "telefon"
x = txt.center(20)
print(x)

txt = "kampyuter"
x = txt.center(20)
print(x)



# count()	bir gapda nechta bir hil soz qatnashganinin topadi
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


txt = "salom meing ismim python, salom men bn dostlash!"
x = txt.count("salom")
print(x)


txt = "men juda hursandman,cunki men pythonni organyapman!"
x = txt.count("hursandman")
print(x)



# encode()	Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "MEN JUDA BANDMAN"
x = txt.encode()
print(x)

txt = "juda jahlm ciqyapti"
x = txt.encode()
print(x)



# endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)


txt = "soat 5da ketwim kerak"
x = txt.endswith(".")
print(x)

txt = "juda wowilyapman,iwmi judaham kop"
x = txt.endswith(".")
print(x)



# expandtabs()	\t sozni orasini ocib beradi
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)


txt = "S\ta\tl\to\tm"
x =  txt.expandtabs(2)
print(x)


txt = "H\ta\ty\tr"
x =  txt.expandtabs(2)
print(x)



# find()	sozda necta harf borligini sanab beradi
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


txt = "Hello sarvar ."
x = txt.find("sarvar")
print(x)


txt = "Assalomu Alekum qalaysiz."
x = txt.find("Alekum")
print(x)



# format()	Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "olma narxi {price:.2f} dollars!"
print(txt.format(price = 12))


txt = "oyinchoq narxi {price:.2f} dollars!"
print(txt.format(price = 500))



# format_map()	Formats specified values in a string





# index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


txt = "sallom juda bandman."
x = txt.index("juda")
print(x)


txt = "juda kec qoldim iwoning"
x = txt.index("kec")
print(x)



# isalnum()	Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)


txt = "sarvar65"
x = txt.isalnum()
print(x)


txt = "Color"
x = txt.isalnum()
print(x)



# isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)


txt = "Comat"
x = txt.isalpha()
print(x)


txt = "CompanY13"
x = txt.isalpha()
print(x)



# isascii()	Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x)


txt = "Company"
x = txt.isascii()
print(x)


txt = "SARVAR"
x = txt.isascii()
print(x)



# isdecimal()	Returns True if all characters in the string are decimals
txt = "1234"
x = txt.isdecimal()
print(x)


txt = "ALOOOO"
x = txt.isdecimal()
print(x)


txt = "123SARVAR"
x = txt.isdecimal()
print(x)



# isdigit()	Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)


txt = "sardor"
x = txt.isdigit()
print(x)


txt = "urgach 90"
x = txt.isdigit()
print(x)



# isidentifier()	Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x)


txt = "Demo14"
x = txt.isidentifier()
print(x)


txt = "alex"
x = txt.isidentifier()
print(x)



# islower()	Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)


txt = "salom hammaga!"
x = txt.islower()
print(x)


txt = "12!"
x = txt.islower()
print(x)




# isnumeric()	Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)


txt = "sarvar16"
x = txt.isnumeric()
print(x)


txt = "sardor12"
x = txt.isnumeric()
print(x)




# isprintable()	Returns True if all characters in the string are printable
txt = "kechiring iltimos"
x = txt.isprintable()
print(x)


txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)


txt = "sarvar #1?"
x = txt.isprintable()
print(x)




# isspace()	Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)


txt =''
x = txt.isspace()
print(x)


txt ="ali"
x = txt.isspace()
print(x)



# istitle()	Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)


txt = "Hello world"
x = txt.istitle()
print(x)


txt = "sarvar16"
x = txt.istitle()
print(x)




# isupper()	Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


txt = "it park"
x = txt.isupper()
print(x)



txt = "sarvar prime!"
x = txt.isupper()
print(x)



# join()	Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)



myTuple = ("sarvar", "jony", "sardor")
x = "#".join(myTuple)
print(x)


myTuple = ("ali", "prime", "jeki")
x = "#".join(myTuple)
print(x)



# ljust()	Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")


txt = "olma"
x = txt.ljust(20)
print(x, "bu meva hisoblanadi.")


txt = "mashina"
x = txt.ljust(20)
print(x, "turlari juda kop")



# lower()	hamma sozlarni kichik qiladi
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)


txt = "MEN KETDIM"
x = txt.lower()
print(x)


txt = "Salom Dunyo"
x = txt.lower()
print(x)





































