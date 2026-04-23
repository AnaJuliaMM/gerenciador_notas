with open("cardapio.txt", "r", encoding="utf-8") as arquivo:
    
    # Analisar linha a linha
    for linha in arquivo:
        
        # Separar a linha em duas partes
        dados = linha.split(">")

        # Criar variáveis dedicadas
        alimento = dados[0]
        preco = dados[1] # ' 8.7\n'

        # Extrair a nota 
        preco = preco.strip()
        preco = float(preco)

        # Classificar as notas
        if (preco >= 30):
            classificacao = "PREÇO ALTO"
        elif (preco >= 10):
            classificacao = "PREÇO MÉDIO"
        else:
            classificacao = "PREÇO BAIXO"

        print(f"- A classificação do alimento {alimento} com preço {preco} é {classificacao}")