import matplotlib.pyplot
meses = ['Janeiro','Fevereiro','Março','Abril','Maio']
números = [5,8,4,7,2]
matplotlib.pyplot.title('Notas individuais de Lucas nos primeiros cinco meses')
matplotlib.pyplot.ylabel('Notas individuais de Lucas')
matplotlib.pyplot.xlabel('Meses (janeiro até maio)')
matplotlib.pyplot.plot(meses,números)
matplotlib.pyplot.show()
