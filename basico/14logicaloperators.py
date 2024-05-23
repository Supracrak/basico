#logical operators= (and, or,not) usado para saber se duas ou mais condicoes sao verdadeiras

temperature = int(input("what is the temperature today"))
if temperature >=0 and temperature <= 30: #AND nesse caso esta indicando que a temperatura tem que estar dentro desse intervalor de 0 a 30
    print("the temperature is good today")
    print("go outside!")
elif temperature <0 or temperature>30: #OR nesse caso esta indicando que a temperatura tem que ser menor que 0 ou maior que 30, nao existe um intervalo entre eles
    print("the temperature is bad today")
    print("stay inside")


#not sera usado para fazer  o inverso, ao inves de if, ficara if not, elif not

temperature2= int(input("what is the temperature today"))


if not (temperature2 >=0 and temperature2<= 30): #nesse caso esta indicando que SE a temperatura NAO estiver dentro desse intervalor de 0 a 30, sera ruim
      print("the temperature is bad today")
      print("stay inside")
elif not (temperature2 <0 or temperature2>30): #nesse caso esta indicando que SE a temperatura NAO for menor que 0 ou maior que 30, sera boa
     print("the temperature is good today")
     print("go outside!")

