#string methods, metodos usados juntos ao string

name = "ALfred"
print(name)

#----------------------------------------------------------------------------------------------------
#lEN()
#usado para saber a quantidade de caracteres de uma string
print(len(name))
#terminal entrega: 6 

#----------------------------------------------------------------------------------------------------
#.find()
#usado para achar qual o index relacionado ao caracter (INDEX NA PROGRAMACAO COMECA NO 0, ou seja o A e 0, o l e 1, o f e 2 e assim por diante)
print(name.find("f"))
#terminal entrega: 2 (f esta no index 2)

#----------------------------------------------------------------------------------------------------
#.capitalize()
#usado para deixar a primeira letra de uma palavra maiuscula

print(name.capitalize())

#----------------------------------------------------------------------------------------------------
#.upper() e lower()
#usado para deixar tudo maiusculo e tudo minusculo

print(name.upper())
print(name.lower())

#-----------------------------------------------------------------------------------------------------
#.isdigit()
#usado para saber se a variavel e um digito

print(name.isdigit())

#------------------------------------------------------------------------------------------------------
#.isalpha()
#usado para saber se a variavel e alfabetica

print(name.isalpha())
#----------------------------------------------------------------------------------------------------
#.count()
#usado para contar quantos caracteres em especifico tem na variavel

print(name.count("e"))

#----------------------------------------------------------------------------------------------------
#.replace()
#usado para substituir algum caracter por outro

print(name.replace("e","o"))

#----------------------------------------------------------------------------------------------------
#*x
#multiplicar a variavel por uma quantidade de vezes

print(name*3)

