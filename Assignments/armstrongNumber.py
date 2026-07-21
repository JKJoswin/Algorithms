num = input("Enter a number: ")
number = int(num)
if number<0:
    print("Invalid number. Use whole numbers.")
else:
    sum=0
    exp=len(num)
    for i in range(1,exp+1):
        sum=sum + (number%10)**exp
        number = (number - number%(10))/10
    if sum==int(num):
        print(f"{num} is an Armstrong Number.")
    else:
        print(f"{num} is not an Armstrong Number.")