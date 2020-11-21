n=int(input('Numarul de zile a lunii '))
if (n>=28) and (n<=31):
    if n==28:
        print('Februarie in an simplu')
    if n==29:
        print('Februarie in an bisect')
    if n==30:
        print('Aprilie, iunie, septembrie, noiembrie')
    if n==31:
        print('Ianuarie, martie, mai, iulie, august, octombrie, decembrie ')
else :
    print('Eroare')
    