#MAX OF 3 NUMBERS:
def maximum(num1, num2, num3): 
  
    if (num1 >= num2) and (num1 >= num3): 
        max = num1 
  
    elif (num2 >= num1) and (num2 >= num3): 
        max = num2 
    else: 
        max = num3 
          
    return max 
  

n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
n3 = int(input("Enter the number:"))
print(maximum(n1,n2,n3))