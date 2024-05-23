#nestedloops= o loop interno ira realizar suas interacoes antes de finalizar as interacoes do loop exterior

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


rows= int(input("how many rows"))
columns= int(input("how many columns"))
symbol= input("enter a symbol")

for x in range(rows):
  for y in range(columns):
    print(symbol, end="")
  print()
