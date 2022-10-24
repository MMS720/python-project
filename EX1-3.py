def max3lenght(A,B):
    '''
    (int,int)=>int
    The maximum value of the third side.
    example:
    max3lenght(3,5):
    7
    '''
    C=A+B-1
    if (A>0 and B>0):
        return(C)
    else:
        print("triangle is not true")
        
