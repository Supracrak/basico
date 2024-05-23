#if statment= ira executar apenas "se" uma condicao for verdadeira
#elif= else if

age= int(input("how old are you"))

if age == 100: #esse tem que vir primeiro que >=18, pois se o >=18 viesse primeiro, e voce pusesse 100 como idade,
               #retornaria que voce e maior que 18, logo a condicao de voce ter 100 anos seria anulada
    print("you are really old")
elif age<0: #condicao intermediaria, usar elif quando quiser outros if antes do else
    print("you havent born yet")
elif age >= 18:
    print("you are a adult")    
else: #se nao
    print("you are a child")

