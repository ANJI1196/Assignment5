#PRINT ODD NUMBER UP TO GIVEN NUMBER
def odd_number(start,end):
    
    for i in range(start,end+1):
        if i%2!=0:
            print(i, end = " ")
n1=int(input("enter the start number:"))
n2=int(input("enter the end number"))
result=odd_number(n1,n2)
