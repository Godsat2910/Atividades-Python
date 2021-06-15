print("{:=^50}".format("Loja do Igor"))

soma = 0

while True:
    produto = str(input("\nQual o produto que você deseja cadastrar?"))
    preço = float(input("Qual o valor deste produto? R$"))

    desconto = (preço) * 95/100
    soma = soma + desconto

    #.upper = deixar a letra maiúscula / .strip = caracter que o programa vai ler eliminando outros espaços
    escolha = str(input("\ndeseja continuar com outros cadastros? [S] ou [N]")).upper().strip()[0]

    if escolha == "N":
        break
print("\na soma total dos valores com o percentual de desconto é: R${:.2f}".format(soma))
print("\nfim de programa!")

