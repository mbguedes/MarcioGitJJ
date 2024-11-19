dicionario2 = [
    {'nome': 'Breno Santana Lapa', 'idade': 19, 'cidade': 'ilhabela', 'coisaFavorita': 'Ouvir Musica'}, 
    {'nome': 'Kael', 'idade': 22, 'cidade': 'ilhabela', 'coisaFavorita': 'futebol'},
    {'nome': 'Marcio', 'idade': 33, 'cidade': 'IlhaBela', 'coisaFavorita': 'Cerveja'},
    {'nome': 'Alexandre Andrade', 'idade': 33, 'cidade': 'Ilhabela', 'coisaFavorita': 'Cerveja'},
    {'nome': 'adriano', 'idade': 17, 'cidade': 'ilhabela', 'coisaFavorita': 'jogar'},
    {'nome': 'Michael', 'idade': 27, 'cidade': 'Carangua', 'coisaFavorita': 'Cerveja'}
]
#Aqui utilizei pessoa como variável temporária de loop para percorrer o dicionário#
#assim 'pessoa' assume cada dicionario, cada abertura de "{ }"
for pessoa in dicionario2:
    for chave, valor in pessoa.items():
        print(f"chave: {chave} ------ Valor: {valor}")
    print()
