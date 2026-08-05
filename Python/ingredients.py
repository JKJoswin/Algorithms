Tea = ("Milk","Tea Powder","Sugar","Water")
Coffee = ("Milk","Coffee Powder","Sugar")
HotChocolate = ("Milk","Chocolate","Sugar")

print(f"Ingredients for making a cup of tea: {Tea}")
print(f"Ingredients for making a cup of coffee: {Coffee}")
print(f"Ingredients for making a cup of hot chocolate: {HotChocolate}")

s1 = {"Milk","Tea Powder","Sugar","Water"}
s2 = {"Milk","Coffee Powder","Sugar"}

print(f"The ingredients required to make a cup of tea and a coffee:\n{s1.union(s2)}")
print(f"The ingredients in common to make a cup of tea and a coffee:\n{s1.intersection(s2)}")
print(f"The ingredients required to create the flavour of the tea:\n{s1.difference(s2)}")
print(f"The ingredients required to create the flavour of the tea and the coffee:\n{s1.symmetric_difference(s2)}")
