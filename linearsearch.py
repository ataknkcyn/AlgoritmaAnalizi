
def linearSearch(n,array):
    for i in array:
        if i is n:
            return True
    return False

if '__main__' == __name__:
    array = [1,2,3,4,5,46,4,2,34,235,234,4,456]
    print(linearSearch(9,array))
    
