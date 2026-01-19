import math  

def main():
    A = int(input("What is A?" ))
    B = int(input("What is B? "))
    result=pythag(A,B)
    print(result)

def pythag(a,b):
    c=a ** 2 + b ** 2
    return(math.sqrt(c))

main()
