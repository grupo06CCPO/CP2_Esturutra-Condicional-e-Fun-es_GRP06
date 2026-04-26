#EX 01
#entrada
estado_de_origem = int(input("Digite o estado de origem (1 a 5): "))
peso_toneladas = float(input("Digite o peso de carga do caminhão, em toneladas: "))
codigo_carga = int(input("Qual é o código da carga? "))

#conversao do peso
#peso da carga do caminhao de t em kg
peso_em_kg = peso_toneladas * 1000

#preco da carga do caminhao
if codigo_carga >= 10 and  codigo_carga <=20:
    preco_por_kg = 100.00
elif codigo_carga >= 21 and  codigo_carga <=30:
    preco_por_kg = 250.00
elif codigo_carga >= 31 and  codigo_carga <=40:
    preco_por_kg = 340.00
else:
    preco_por_kg = 0.00

#Calcular preco (total da carga)
preco = peso_em_kg * preco_por_kg

#Definir Percentual de impostos eh cobrado com base no preco da carga e estado de origem
if estado_de_origem == 1:
    percentual = 0.35
elif estado_de_origem == 2:
    percentual = 0.25
elif estado_de_origem == 3:
    percentual = 0.15
elif estado_de_origem == 4:
    percentual = 0.05
else:
    percentual = 0.0

#Imposto
imposto = preco * percentual   #valor do imposto
total = preco + imposto      #valor total (imposto + carga)

#resultados calculados para o usuario
print (f'O peso da carga do caminhão em KG é:  {peso_em_kg} KG')
print(f'O preço da carga do caminhão é:  {preco:,.2f} R$')
print(f'O valor do imposto cobrado sobre o peso da carga e estado de origem é:  {imposto:,.2f} R$')
print(f'O valor total transportado pelo caminhão é: {total:,.2f} R$ ')
