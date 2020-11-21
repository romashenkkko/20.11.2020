a=int(input('Lungimea laturii a este '))
b=int(input('Lungimea laturii b este '))
c=int(input('Lungimea laturii c este '))
if ((a>b+c) and (b<a+c) and (c<a+b)):
    if (a==b and a==c and b==c):
        print('Laturilea formeaza un triunghi echilateral')
    elif (a==b or a==c or b==c):
        print('Laturile formeaza un triunghi isoscel')
    else:
        print('Laturile formeaza un triunghi scalen')
else :
    print('Laturile nu formeaza triunghi')