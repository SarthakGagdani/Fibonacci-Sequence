#WITHOUT RECURSION
def getfib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    first = 0
    second = 1
    next = first + second
    i = 2
    while i <position:
        first = second
        second = next
        next = first + second
        i+=1
  
    return next
            
        
def main():

    pos=input("Enter position-")
    print(getfib(int(pos)))
    
main()    
