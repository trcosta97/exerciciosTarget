#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


import json

with open('dadosDistribuidora.json') as r:
    json_string = r.read()

lista_dicionarios = json.loads(json_string)


soma_valores = 0
for dicionario in lista_dicionarios:
    soma_valores += dicionario["valor"]
media_valores = soma_valores / len(lista_dicionarios)

dias_acima_da_media = []
for dicionario in lista_dicionarios:
    if dicionario["valor"] > media_valores:
        dias_acima_da_media.append(dicionario["dia"])



menor_valor = min([dia['valor'] for dia in lista_dicionarios])
maior_valor = max([dia['valor'] for dia in lista_dicionarios])




dia_menor_valor = min(lista_dicionarios, key=lambda x: x['valor'])['dia']
dia_maior_valor = max(lista_dicionarios, key=lambda x: x['valor'])['dia']

print(f"o dia de menor valor foi o dia {dia_menor_valor}")
print(f"o dia de maior valor foi o dia {dia_maior_valor}")
print(f"os com o faturamento acima da média foram: {dias_acima_da_media}")
