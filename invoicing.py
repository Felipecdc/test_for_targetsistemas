import json

# Exemplo de faturamento mensal
faturamento_json = '{"faturamento_diario": [0, 500, 1500, 2000, 0, 3000, 0, 2500, 0]}'
faturamento = json.loads(faturamento_json)['faturamento_diario']

# Remover os dias sem faturamento (0)
faturamento_filtrado = [f for f in faturamento if f > 0]

# Calcular o menor e o maior valor
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

# Calcular a média
media_faturamento = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Contar dias com faturamento acima da média
dias_acima_media = sum(1 for f in faturamento_filtrado if f > media_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
