import math



#Exercice 1 :
##### a #####
# asking the user to enter a value 

x = float(input("enter a number to get the Polynome :")) 
# Create the Function 
def Polynome(x):
    result = math.pow(x, 3) - 1.5 * math.pow(x, 2) - 6* x +5
    print(result)
#Call the Function 
Polynome(x)

###### b #####
n = int(input("enter a number to get the Factorial: "))

def  factorielle(n):
    fact = 1
    if (n==0):
        return 1
    else:
        for i in range(1,n+1):
            fact = fact * i
        print ("The factorial of",n, " is: ", fact)
factorielle(n)

##### C ####
Term = int(input("enter a number to get the Fibbonaci : "))
def fibonacci(Term):
    Term1 = 0
    Term2 = 1
    c = 0
    if Term <= 0:
        print("Incorrect input")
    elif Term == 1:
        print(Term1)
    else:
        print("The fibonacci of ", Term,  " is:")
        while c < Term:
            print(Term1)
            K = Term1 + Term2
            Term1 = Term2
            Term2 = K
            c += 1 

fibonacci(Term)
