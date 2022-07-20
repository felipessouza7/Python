    #calculadora braba

#nomear o que vai ser usado
operacao = input("quer fazer o que mané? (somar, subtrair, multiplicar, dividir): ")
numero1 = input("me fala entao o primeiro numero: ")
numero2 = input(" E o segundo mané? nao tenho o dia todo: ")

#atribuir funções a string nomeada
if operacao == "somar":
    resultado = int(numero1) + int(numero2)
elif operacao == "subtrair":
    resultado = int(numero1) - int(numero2)
elif operacao == "multiplicar":
    resultado = int(numero1) * int(numero2)
elif operacao == "dividir":
    resultado = int(numero1) / int(numero2)

#caso isso nao for essas operações aparecer
else:
    resultado = ("ta de sacanagem?")

#imprimir resultado
print("a merda do resultado é: " + str(resultado))
