# Informacoes

# Ler o arquivo com as notas
with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.split(":")
        # print(dados)

        nome_aluno = dados[0]
        nota = float(dados[1].strip())
        # print(f"Processando aluno {nome_aluno} com a nota {nota}")

        if (nota >= 9):
            classificacao = "APROVADO COM EXCELÊNCIA"
        elif (nota >= 7):
            classificacao = "APROVADO"
        elif (nota >= 5):
            classificacao = "EM RECUPERAÇÃO"
        else:
            classificacao = "REPROVADO"
        
        print(f"- A classificação do aluno {nome_aluno} com nota {nota} é {classificacao} ")