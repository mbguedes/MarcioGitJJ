minhaTupla = (33, "Marcio", 3.14, True, "Cerveja")

print(minhaTupla)
print(type(minhaTupla))

minhaLista = list(minhaTupla)

print(minhaLista)
print(type(minhaLista))

minhaLista.append("Mais Cerveja")
print(minhaLista)

minhaLista.pop(0)
minhaLista.pop()
print(minhaLista)

print(minhaLista[0])

if len(minhaLista) > 1:
    print(f"A quantidade de dados são {len(minhaLista)} e os dados são: {minhaLista}")
else:
    print(f"A quantidade de dado é {len(minhaLista)} e o dado é: {minhaLista}")

dicionario1 = {
    'nome': 'Marcio',
    'idade': 33,
    'profissao': 'Triste'
}

for valor in dicionario1.values():
    print(valor)

