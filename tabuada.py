from time import *
print ("="* 50)
print("{:=^50}".format("Tabuada"))

valor = float(input("informe o número que deseja multiplicar:"))

print("estamos calculando..\n")
sleep(2)

for c in range (1,101):
    print("{} x {} = {}".format(valor, c, valor * c))

