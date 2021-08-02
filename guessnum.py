lstNum=[2,4,7,9,10,21,34,56,8,5,6,11,12]

while True:
    n = input('Give me an integer or type \'q\' to quit: ')

    if n == 'q':
        break
    else:
        
        if int(n) in lstNum:
            print('You are correct! ' + n +' is in the list')
        else:
            print('Sorry, tha number ' + n +  ' is not in the list!')
    continue

    

print('Thank you and goodbye')