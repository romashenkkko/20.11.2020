import math
m=int(input('Numarul m este  '))
n=int(input('Numarul n este '))
if m<n:
    if math.sqrt(n)==m:
        print('n este o putere a lui m')
    else :
        print('Eroare')
