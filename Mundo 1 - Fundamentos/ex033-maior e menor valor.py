numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valo: '))
maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
print('O número maior digitado foi {}'.format(maior))
print('O número menor digitado foi {}'.format(menor))




