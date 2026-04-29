# pcp_1sem_cp2_ex03.py

# Entrada de dados
cp1 = float(input("Digite a nota do Checkpoint 1: "))
cp2 = float(input("Digite a nota do Checkpoint 2: "))
cp3 = float(input("Digite a nota do Checkpoint 3: "))

sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))

gs = float(input("Digite a nota da Global Solution: "))

# Encontrando a menor nota dos checkpoints sem usar min()
menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

# Soma das duas maiores notas dos checkpoints
soma_checkpoints = cp1 + cp2 + cp3 - menor

# Média base (2 checkpoints + 2 sprints)
media_base = (soma_checkpoints + sp1 + sp2) / 4

# Média do semestre
media_semestre = (media_base * 0.4) + (gs * 0.6)

# Média com peso
media_peso = media_semestre * 0.4

# Saída
print("\n--- RESULTADO ---")
print(f"Média do semestre: {media_semestre:.1f}")
print(f"Média do semestre com peso: {media_peso:.1f}")