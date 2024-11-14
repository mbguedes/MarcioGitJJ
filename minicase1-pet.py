def calcularIdadePet ():
    nomePet = str(input("Primeiramente me fale o nome do seu Pet: "))
    idadePet = int(input("Me fale agora, por favor utilize apenas números, a idade do seu cachorro (ex.: 5): "))
    portePet = int(input("Agora me fale o tamanho dele caso seja grande porte digite 1, caso seja médio porte digite 2, e pequeno porte digite 3: "))
    qtdBanho = int(input("E quantas vezes nos últimos 12 meses ele tomou banho conosco? Responda apenas o número de vezes por favor: ")) 
    
    if portePet == 1: print(input(f"Olá, a idade humana do {nomePet} é {idadePet * 7} e nos últimos 12 meses o lucro com este animal foi de R${qtdBanho*55} conosco"))
    elif portePet == 2: print(input(f"Olá, a idade humana do {nomePet} é {idadePet * 7} e nos últimos 12 meses o lucro com este animal foi de R${qtdBanho*45} conosco"))
    elif portePet == 3: print(input(f"Olá, a idade humana do {nomePet} é {idadePet * 7} e nos últimos 12 meses o lucro com este animal foi de R${qtdBanho*45} conosco"))

calcularIdadePet()
