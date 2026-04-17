# ETAPA 1 - ENTENDENDO O FLUXO: ---------------------------------------------------

# Estrutura do comando open():
# variavel_conexao = open("nome_arquivo.extensao", modo)
# modos:
# - "r": ler o conteudo
# - "w": escrever
# - "a": manter o que existe e adicionar novas linhas
conexao = open("notas.txt", "r")

# A variavel não guarda o conteudo do arquivo, mas 
# é uma conexão entre seu código e o arquivo
print("CONEXÃO:")
print(conexao)

# Para exibir o conteúdo do arquivo no terminal, você 
# precisa usar o comando read()
print("\nCONTEÚDO:")
conteudo = conexao.read()
print(conteudo)

# É necessário fechar a conexão, pois há risco de 
# corrupção do arquivo
conexao.close()



# ETAPA 2 - MELHORANDO O FLUXO: ---------------------------------------------------
# Ao invés de precisar lembrar de fechar o arquivo, você 
# pode usar os blocos with()

with open("notas.txt", "r") as file:
    print("\nCONTEÚDO:")
    conteudo = file.read()
    print(conteudo)
    
