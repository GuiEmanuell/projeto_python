#dicionario que guarda os produtos, codigo, nome, preco e quantidade
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

#definicao de uma funcao para adicionar um novo produto
def add_prod():
    cod = input("digite o codigo do produto: ")
    nome = input ("digite o nome do produto: ")
    preco = float(input("digite o preco do produto: "))
    quantidade = int(input("digite a quantidade do produto: "))
    produtos[cod] = {}  #cria um novo dicionario para o produto

    produtos[cod]["nome"] = nome
    produtos[cod]["preco"] = preco
    produtos[cod]["quantidade"] = quantidade

#definicao de uma funcao para listar os produtos
def listar_prod():
    for prod in produtos:
        print(produtos[prod])

#definicao de uma funcao para buscar um produto pelo codigo(mas eficiente)
def buscar_prod():
    cod = input("digite o codigo do produto que queira buscar: ")
    print(produtos[cod])

#definicao de uma funcao para atualizar um atributo de um produto (nome, preco ou quantidade)
def atualizar_prod():
    cod = input("digite o codigo do produto que queria mudar: ")
    atributos = input("digite nome da area que voce quer mudar(ex: preco, quantidade, ou nome): ")    
    atualiza_prod = input("digite o novo nome, preco ou quantidade: ")

    produtos[cod][atributos] = atualiza_prod  #atualiza o valor do atributo

#definicao de uma funcao para deletar um produto pelo codigo
def deletar_prod():
    cod = input("digite o codigo do produto que queira deletar: ")
    del produtos[cod]
    
#definicao de uma funcao para calcular o valor total em estoque de um produto (preço * quantidade)
def calcular():
    cod = input("digite o codigo do produto para que seu estoque seja calcular: ")
    resultado = produtos[cod]["preco"]*produtos[cod]["quantidade"]

    print(resultado)

#parte que sera exibida quando iniciar o codigo, um menu que executa as funcoes conforme a escolha do usuario
while True:
    print("1 para atualizar os produtos")
    print("2 para adicionar os produtos")
    print("3 para remover os produtos")
    print("4 para calcular os produtos")
    print("5 para buscar os produtos")
    print("6 para listar os produtos")

    opcao = int(input("escolha uma opcao(1 a 6): ")) #le a opcao do usuario

    if opcao == 1:
        atualizar_prod() 

    elif opcao == 2:
        add_prod()

    elif opcao == 3:
        deletar_prod()

    elif opcao == 4:
        calcular()

    elif opcao == 5:
        buscar_prod()

    elif opcao == 6:
        listar_prod()

    else:
        print("opcao nao correspondente")
   
    resposta = input("quer continuar? s/n?")

    if resposta.lower() == 'n': #se a resposta for nao, o loop se encerra
        break