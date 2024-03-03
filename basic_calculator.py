print("Enter a number")
a=int(input())
print("Enter second number")
b=int(input())
print("Enter arithmetic operation of your choice")
op=input()
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
elif op=='%':
    print(a%b)
else:
    print(a**b)

