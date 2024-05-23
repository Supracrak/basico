#for loops=for loop e semelhante ao while loop, porem enquanto o while loop pode se repetir por uma quantidade ilimitada de vezes
#o for loop sera limitado

for x in range(10): #x
    print(x+1) #o ultimo numero sempre sera exclusivo, sendo necessario adicionar +1

for y in range(50,100+1,2): #o ultimo numero sempre sera exclusivo, sendo necessario adicionar +1
    print(y)                #"",2" fara com que conte de 2 em 2

for z in "jonas silva": #fara com que cada letra seja imprimida,uma por uma
    print(z)

import time

for seconds in range(10,0-1,-1): #como e decrescente se faz necessario adicionar o ,-1
    print(seconds)
    time.sleep(1)
print("acorde")


