maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}° pessoa: kg'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso da lista é {maior}kg\nO menor peso da lista é {menor}kg')
