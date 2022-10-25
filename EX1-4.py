def daynumber(x):
    '''
(int)=>str
return number of day.
example:
daynumber(Friday)
7
be careful your day start whit capital.
'''
    if(x==1):
        print('Monday')
    elif(x==2):
        print('Tuesday')
    elif(x==3):
        print('Wednesday')
    elif(x==4):
        print('Thursday')
    elif(x==5):
        print('Friday')
    elif(x==6):
        print('Saturday')
    elif(x==7):
        print('Sunday')
    else:
        print('error')
