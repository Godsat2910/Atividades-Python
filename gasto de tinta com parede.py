largura = float(input("primeiro informe a largura da parede: "))
altura = float(input("agora informe a altura da mesma: "))

área = largura * altura
litro = área/2

print("\nsua largura {} com sua altura {} "
      "\ncuminam num gasto total de {} litros de tinta".format(largura, altura, litro))
