a=100000
b=int(input())
c=9005
if a>b:
    print('continue transaction')
    print('enter password')
    d=int(input())
    if d==c:
        e=a-b
        print('transaction success')
        print('credit amount',b)
        print('balance',e)
    else:
        print('invalid password')
else:
    print('unsufficent amount')
