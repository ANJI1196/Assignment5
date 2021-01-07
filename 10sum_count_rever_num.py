# function to find sum, count, and reverse of the given number:
def sum_num(n):  
     
    a = 0
    for digit in str(n):   
      a += int(digit)        
    return a
    
#
def count_number(number2):
    count = 0
    while(number2 > 0):
        number2 = number2 // 10
        count = count + 1
    return count


def reverse_integer(number1):
    reverse = 0
    while(number1 > 0):
        reminder = number1 %10
        reverse = (reverse *10) + reminder
        number1 = number1 //10
    return reverse




num = int(input("Please Enter any Number: "))
sum=sum_num(num)
count=count_number(num)
reverse = reverse_integer(num)
print("sum of entered number is:",sum)
print("count of entered number is:",count)
print("Reverse of entered number is:",reverse)

