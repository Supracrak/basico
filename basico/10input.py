#INPUT
#Usado para dar uma entrada ao usuario, o qual podera interagir com a mesma.

name= input("What is your name")

print("hello " + name)

age= int(input("what is your age")) #int para que o numero seja inteiro

print(", your age is "+ str(age) + " years old")

height= float(input("How tall are you")) #mesma coisa aqui

print("you are "+ str(height) + " cm tall") 

print ("your name is "+ name+" ,you have " + str(age)+ " years old and "+ str(height) + "cm tall")