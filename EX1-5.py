def rangeofage(x):
    '''
    (int)==>str
    determines range of age as infant,child,teenager and adult.
    example:
    rangeofage(10)
    Child
    '''
    if(x<=1 and x>0):
        print('infant')
    elif(x<13 and x>1):
        print('child')
    elif(x>=13 and x<20):
        print('teenager')
    elif(x>=20):
        print('adult')
    elif(x<=0):
        print('Baby not found :)')
