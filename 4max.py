#MAX OF 2 NUMBERS:
def max(num1, num2): 
      
    if num1 >= num2: 
        return num1 
    else: 
        return num2 
      
 
n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
print(max(n1,n2))