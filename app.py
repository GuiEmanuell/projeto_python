#dicionario que armazena os produtos, contendo codigo, nome, preco e quantidade
produtos = {
    "cod1": {
        "nome": "Turbocompressor HKS",
        "preco": 800.90,
        "quantidade": 15
    },
    "cod2": {
        "nome": "Filtro de Ar Esportivo",
        "preco": 300.00,
        "quantidade": 20
    }
}

#funcao para adicionar um novo produto
def adicionar():
    cod = input("digite o codigo do produto: ")
    nome = input ("digite o nome do produto: ")
    preco = float(input("digite o preco do produto: "))
    quantidade = int(input("digite a quantidade do produto: "))
    produtos[cod] = {}  #cria um novo dicionario para o produto

    produtos[cod]["nome"] = nome
    produtos[cod]["preco"] = preco
    produtos[cod]["quantidade"] = quantidade

#funcao para listar os produtos
def listar():
    for prod in produtos:
        print(produtos[prod])

#funcao para buscar um produto pelo codigo
def buscar():
    cod = input("digite o codigo: ")
    print(produtos[cod])

#funcao para atualizar um atributo de um produto (nome, preco ou quantidade)
def atualizar():
    cod = input("digite o codigo do produto: ")
    atributos = input("digite nome da area que voce quer mudar(ex: preco, quantidade, ou nome): ")    
    atualiza_prod = input("digite o novo nome, preco ou quantidade: ")

    produtos[cod][atributos] = atualiza_prod  #atualiza o valor do atributo

#funcao para remover um produto pelo codigo
def remover():
    cod = input("digite o codigo do produto: ")
    del produtos[cod]
    
#funcao para calcular o valor total em estoque de um produto (preço x quantidade)
def calcular():
    cod = input("digite o codigo do produto: ")
    resultado = produtos[cod]["preco"]*produtos[cod]["quantidade"]

    print(resultado)

#parte principal do programa, exibe o menu e executa as funcoes conforme a escolha do usuario
while True:
    print("1 para atualizar os produtos")
    print("2 para adicionar os produtos")
    print("3 para remover os produtos")
    print("4 para calcular os produtos")
    print("5 para buscar os produtos")
    print("6 para listar os produtos")

    opcao = int(input("escolha uma opcao(1 a 6): "))

    if opcao == 1:
        atualizar()

    elif opcao == 2:
        adicionar()

    elif opcao == 3:
        remover()

    elif opcao == 4:
        calcular()

    elif opcao == 5:
        buscar()

    elif opcao == 6:
        listar()

    else:
        print("opcao nao correspondente")
   
    resposta = input("quer continuar? s/n?")

    if resposta.lower() == 'n':
        break