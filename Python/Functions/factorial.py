
# implementation of function fact 
# in this fucntion fact passing n as a argument  
def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
# declare the value of n is 5
# we can value of n from user also --- n = int("Enter the value of n")
num = 5  
print("Factorial of",num,"is",)  
# call the fucntion fact
fact(num))  
