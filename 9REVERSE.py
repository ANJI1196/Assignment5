#function to reverse the given string
def my_reverse(name):
    str1 = ''
    for i in str:
        str1 = i + str1
    return str1
str=input("Enter the name to be reversed:")
print("The original string is: ",str)  
reverse_name=my_reverse(str)
print("The reverse string is:",reverse_name)