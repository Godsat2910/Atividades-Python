from time import *
#se colocar apenas input ele também classifica como str
nome = str(input("digite o que pensas:"))
print("aguarde um momento...")
sleep(2)
print("o tipo primitivo é:{}", type(nome))
print("este nome tem espaços?", nome.isspace())
print("é um número?", nome.isnumeric())
print("Como fica todo maiúsculo:", nome.upper())
print("como fica tudo minúsculo:", nome.lower())
print("é alfabético?", nome.isalpha())
