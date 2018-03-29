def fib_iter2(n):
 a, b = 1, 0
 for i in range(n):
     a,b = a + b, a
 
 return b



def main():
    
    print(fib_iter2(7))
    
main()