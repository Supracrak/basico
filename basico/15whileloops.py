#while loop executa um bloco de código enquanto uma condição for verdadeira, e para de executá-lo quando a condição se tornar falsa.

#exemplo:
contador = 0

while contador < 5:
    print("O contador é:", contador)
    contador = contador + 1 #nesse caso o contador sempre se somara 1 a ponto que em determinada hora, o contador sera maior sera 
#maior que 5 quebrando o loop

print("Fim do laço while!")

#-----------------------------------------------------------------------------------------------------
number =4

#while number <5:
    #print("im stuck!helppp!!!!")

#-----------------------------------------------------------------------------------------------------
name= ""
while len(name) == 0:
    name=input("what is your name")    

    print("hello "+name)

#outra forma de escrever seria

#name= none
#while not name:
   #name=input("what is your name")    