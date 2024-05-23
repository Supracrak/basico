#slicing= criar uma substring apartir da reparticao de outra string

#INDEXING
#[start:stop:step]

name= "pedro silva"

first_name = name[0:5] #o stop sempre e exclusivo e o start sempre inclusivo
#comeca no 0 vai ate o 5 (ja que se pusesse ate o 4 nao daria, pois seria exclusivo)
#tambem pode se usar [:5] (ate o 5 index)
last_name = name[6:11] 
#comeca no 6 vai ate o 11
#tambem pode se usar [6:] (do sexto para frente)
sosegundasletras = name[0:11:2]
#fara com que seja imprimido apenas as segundas letras da palavra
#tambem pode se usar [::2] o computador entendera que comeca no primeiro index e termina no ultimo
nomereverso= name[::-1] 
#nesse caso especifico nomereverso= name[0:11:-1] nao funcionaria

print(first_name)
print(last_name)
print(sosegundasletras)
print(nomereverso)

#SLICING
#slice = slice(x,-y)
#diferente do indexing, o slice servira para multiplas variaveis

cortar = slice(4,-4)

website = "www.google.com"
website2= "www.wikipedia.com"

print(website[cortar])
print(website2[cortar])

