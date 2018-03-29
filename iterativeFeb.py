from time import time
start_time = time( ) 
def F_iter(n):
      if (n == 0):
              return 0
      elif (n == 1):
              return 1
      elif (n >1 ):
              fn = 0
              fn1 = 1
              fn2 = 2
              for i in range(3, n):
                      fn = fn1+fn2
                      fn1 = fn2
                      fn2 = fn
              return fn
      else:
              return -1
            
#nterms = 10

# uncomment to take input from the user
nterms = int(input("How many terms? "))

# check if the number of terms is valid


print(F_iter(nterms))
end_time = time( )                    # record the ending time
elapsed = end_time - start_time       # compute the elapsed time

print(elapsed)