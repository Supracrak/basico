#int e o tipo de variavel relacionado a numeros inteiros, diferente da string, nao e usado aspas, pois se fosse usado, viraria uma string
#exemplo:

age = 15
print(age)

#para adicionar um numero a uma variavel int usa-se:

age+=1 #ira somar 1 a idade ja definida
print(age)

#variaveis de classe diferente nao iram se juntar
#exemplo:

#print("minha idade e" + age)

#o resultado sera:
#TypeError: can only concatenate str (not "int") to str

#o que significa que voce nao pode juntar uma string com inteiro

#nesse caso devemos converter o int para str

print("minha idade e " + str(age))