#2 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13,
# 21, 34...), escreva um programa na linguagem que desejar onde, informado um
# número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando
# se o número informado pertence ou não a sequência.

#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência
# ou pode ser previamente definido no código;


def existeFibonacci(entrada):
    x, y = 0, 1

    while y < entrada:
        x, y = y, x + y

    if y == entrada:
        return True
    else:
        return False

entrada = int(input("Digite um número inteiro para checar se ele existe na sequencia de Fibonacci: "))
if(existeFibonacci(entrada)):
    print(f"O número {entrada} existe na sequência de Fibonacci!")
else:
    print(f"O número {entrada} não existe na sequência de Fibonacci!")


