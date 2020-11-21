n=int(input('Numarul este '))
print('Dizivorii numaruui sunt')
for i in range(1,n+1):
    if(n%i==0):
        print(i)
