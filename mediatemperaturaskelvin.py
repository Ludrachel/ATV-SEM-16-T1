meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Lendo a temperatura média de cada mês
temperaturas = []
temperaturas_kelvin = []
for i in range(len(meses)):
    temperatura = float(input())
    unidade = input().upper()
    if unidade == 'C':
        temperatura_kelvin = temperatura + 273.15
    elif unidade == 'F':
        temperatura_kelvin = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_kelvin = temperatura
    temperaturas_kelvin.append(temperatura_kelvin)
    temperaturas.append(temperatura)

# Calculando a média anual das temperaturas em Kelvin
print("TEMPERATURA MÉDIA ANUAL")
media_anual_kelvin = sum(temperaturas_kelvin) / len(temperaturas)
print(f'{media_anual_kelvin:.2f}K')

# Mostrando as temperaturas acima da média anual em Kelvin e seus respectivos meses
print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
for i in range(len(temperaturas)):
    if temperaturas_kelvin[i] > media_anual_kelvin:
        print(f"{meses[i+1]}: {temperaturas_kelvin[i]:.2f}K")
