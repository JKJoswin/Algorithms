shopName = "Mulberry"
price1 = 99.99
price2 = 59.99
amount = 199.99

balance = amount - price1
affordability = balance > 0
print("Shop Name:",shopName)
print("Affordability:",affordability)
print("Balance:",balance)
print("First letter:",shopName[0])
print("Price at the nearby shop:")
price1, price2 = price2, price1
print("Price of snack-1:",price1)
print("Price of snack-2:",price2)