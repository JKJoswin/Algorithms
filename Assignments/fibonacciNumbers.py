f_n=[1,1]
def fibonacci(count,n):
    if n<=1:
        return 1
    f_n.append(f_n[count-(n-1)]+f_n[count-n])
    return fibonacci(count,n-1)

number = int(input("Enter a number: "))
conj=number
if number<1:
    print("Invalid Number. Try using numbers greater than 1.")
else:
    fibonacci(number,conj)
    print(f"First {number} fibonacci numbers are:\n{f_n}")