# Abrir o arquivo de entrada e o arquivo de saida
with (
    open("notas.txt", "r", encoding="utf-8") as arquivo_notas,
    open("notas_classificadas.txt", "w", encoding="utf-8") as arquivo_classificacao,
):
    for linha in arquivo_notas:
        dados = linha.split(":")
        nome_aluno = dados[0]
        nota = float(dados[1].strip())

        # Classificar as notas
        if (nota >= 9):
            classificacao = "APROVADO COM EXCELÊNCIA"
        elif (nota >= 7):
            classificacao = "APROVADO"
        elif (nota >= 5):
            classificacao = "EM RECUPERAÇÃO"
        else:
            classificacao = "REPROVADO"

        # Gravar no novo arquivo
        arquivo_classificacao.write(f"- {nome_aluno} ({nota}) -> {classificacao}\n")
    
    print("Arquivo gerado com sucesso")


