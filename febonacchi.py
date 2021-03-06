from time import time
start_time = time( )  
def recur_fibo(n):
    """Recursive function to
    print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# uncomment to take input from the user
nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):

        print(recur_fibo(nterms))


end_time = time( )                    # record the ending time
elapsed = end_time - start_time       # compute the elapsed time

print(elapsed)