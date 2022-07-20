price = 0
age = int(input("อายุของท่าน คือ>"))

if age >= 60:
	price = 50
elif age <=10:
	price = 30
else:
	price = 100

print("ค่าตั๋วของท่าน คือ", price)
