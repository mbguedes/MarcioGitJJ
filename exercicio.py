nome = "PAULA MARTINS"
mes = "Janeiro"
valor_compra = 500
desconto = 10
cupom = "PAULAÉ10"

tipo_valor = type(nome)


print(f"O valor original da compra é R${valor_compra}. Com um desconto de {desconto}%, o preço final é R${valor_compra * (1 - desconto / 100):.2f}.")


print(tipo_valor)
