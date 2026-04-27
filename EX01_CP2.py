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

-----------------------------------------------------------------------------------------

#EXERCÍCIO 4

# FUNÇÕES

def calcular_horas_extras(salario_base, horas):
    """Calcula o valor total das horas extras (1.5% do salário base por hora)."""
    return salario_base * 0.015 * horas
 
 
def calcular_descontos_faltas(salario_base, faltas):
    """Calcula o total de desconto por faltas (2% do salário base por falta)."""
    return salario_base * 0.02 * faltas
 
 
def calcular_bonus(cargo, recebeu_bonus):
    """Retorna o valor do bônus por desempenho conforme o cargo."""
    if not recebeu_bonus:
        return 0.0
 
    bonus_por_cargo = {
        1: 1000.0,  # Gerente
        2: 500.0,   # Analista
        3: 300.0,   # Assistente
        4: 100.0    # Estagiário
    }
 
    return bonus_por_cargo.get(cargo, 0.0)
 
# DADOS

print("=" * 45)
print("       SISTEMA DE RH - CÁLCULO SALARIAL")
print("=" * 45)
 
nome = input("\nNome do funcionário: ")
 
print("\nCargos disponíveis:")
print("  1 - Gerente")
print("  2 - Analista")
print("  3 - Assistente")
print("  4 - Estagiário")
cargo = int(input("Cargo (1-4): "))
 
salario_base = float(input("Salário base (R$): "))
horas_extras = float(input("Total de horas extras trabalhadas: "))
faltas = float(input("Total de faltas no mês: "))
bonus_input = input("Recebeu bônus por desempenho? (s/n): ").strip().lower()
recebeu_bonus = bonus_input == "s"

# CAUCULOS

valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)
valor_desconto_faltas = calcular_descontos_faltas(salario_base, faltas)
 
total_acrescimos = valor_horas_extras + valor_bonus
total_descontos = valor_desconto_faltas
 
salario_bruto = salario_base
salario_final = salario_bruto + total_acrescimos - total_descontos

# SAÍDA

cargos = {1: "Gerente", 2: "Analista", 3: "Assistente", 4: "Estagiário"}
 
print("\n" + "=" * 45)
print("           RELATÓRIO SALARIAL")
print("=" * 45)
print(f"  Funcionário : {nome}")
print(f"  Cargo       : {cargos.get(cargo, 'Desconhecido')}")
print("-" * 45)
print(f"  Salário bruto          : R$ {salario_bruto:>10.2f}")
print(f"  Horas extras           : R$ {valor_horas_extras:>10.2f}")
print(f"  Bônus por desempenho   : R$ {valor_bonus:>10.2f}")
print(f"  Total de acréscimos    : R$ {total_acrescimos:>10.2f}")
print("-" * 45)
print(f"  Desconto por faltas    : R$ {valor_desconto_faltas:>10.2f}")
print(f"  Total de descontos     : R$ {total_descontos:>10.2f}")
print("=" * 45)
print(f"  SALÁRIO FINAL          : R$ {salario_final:>10.2f}")
print("=" * 45)
 

 


