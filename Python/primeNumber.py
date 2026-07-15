num = int(input("Enter a number:"))
is_prime = True
if num < 2:
    is_prime=False
for i in range(2,num):
    if num%i==0:
        is_prime=False
if is_prime:
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")