a=[]
n=int(input("enter range of the number"))
for i in range(1,n+1):
    if i%15==0:
        a.append("FizzBuzz")
    elif i%5==0:
        a.append("Buzz")
    elif i%3==0:
        a.append("Fizz")
    else:
        a.append(f'{i}')
print(a)