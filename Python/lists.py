fruits = ["Apple","Banana","Mango","Watermelon","Orange"]

print(f"The first value is {fruits[0]} and the last value is {fruits[-1]}.")
print(f"Three fruits are {fruits[1:4]}.")

fruits.remove("Banana")
print(fruits)
fruits.pop()
print(fruits)
fruits[-1] = "Kiwi"
print(fruits)

fruits.append("Strawberry")
fruits.insert(3,"Blueberry")
print(fruits)
print(f"Length of the list is {len(fruits)}")

fruits.sort()
print(f"The fruits in dictionary order are {fruits}.")
fruits.reverse()
print(f"The fruits in reverse order {fruits}")

for i in fruits:
    print(i,end=", ")