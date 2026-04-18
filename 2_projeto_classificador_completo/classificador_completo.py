import os

nome_arquivo_notas = "notas.txt"
nome_arquivo_classificacao = "notas_classificadas.txt"

# Caso o arquivo não exista, criar o arquivo
if not os.path.exists(nome_arquivo_notas):
    with open(nome_arquivo_classificacao, "w", encoding="utf-8") as arquivo:
        print("Arquivo criado")

# Abrir o arquivo de entrada e o arquivo de saida
with (
    open(nome_arquivo_notas, "r", encoding="utf-8") as arquivo_notas,
    open(nome_arquivo_classificacao, "w", encoding="utf-8") as arquivo_classificacao,
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


