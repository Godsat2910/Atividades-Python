from time import *
nota1 = float(input("informe sua primeira nota:"))
nota2 = float(input("informe sua segunda nota:"))

média = (nota1 + nota2)/ 2

print("Estamos calculando sua média...")
sleep(3)

#{} é onde o computador vai responder e .format substitui as {}
print("\nsua média é: {}".format(média))

if média >= 7:
    print("você passou")

else:
    print("você está reprovado")