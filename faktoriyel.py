def faktoriyel(n):
    if n<=1 : 
        return 1
    else:
        return faktoriyel(n-1)*n

if __name__ == '__main__':
    print( faktoriyel(5) )


    
