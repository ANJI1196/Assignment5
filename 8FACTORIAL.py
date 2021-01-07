#FACTORIAL:
def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
x=int(input("Enter the number:"))
res=fact(x)
print(res)