# The Input 

n = input("enter a number to get the Factorial: ")


# Complexe Number Functuion
def is_cplx(n):
  if (type(n) == complex) :
        n= n.real 
        return n 

# Negative Number Functuion
def neg(n):
  if (n < 0):
    a = abs(a)
    return (n)

# Huge Number Functuion
def limit_digit(n):
  if (len(str(n)) > 8) :
    while((len(str(n)) > 8)): 
      print("The entered number have {} digit, Please enter asmaller number".format(8)) 
      n = int(input()) 
  else:
    pass



# Factorial Functuion
def factorielle(n):
    fact = 1

    ## 1. STR Exception 

    try:
        n = int(n)
    except NameError :
        print( 'Please enter an integer.')
    
    ## 2. Complexe Exception
  
    if (type(n) == complex):
        is_cplx(n)

    ### 3. Negative Exception 
    elif(n < 0):
        neg(n)

    ### 4. Huge Number 
    elif (len(str(n)) > 8):
        limit_digit(n)


    ### the fact     
    elif (n==0):
        return 1
    else:
        for i in range(1,n+1):
            fact = fact * i
        print ("The factorial of",n, " is: ", fact)
factorielle(n)