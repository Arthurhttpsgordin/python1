import datetime

produtos = []
historico = []

def cadastro():
    print("== Cadastro de produtos ==")
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    promo = input("Está em promoção? (s/n): ").upper() == "S"

    if nome == "":
        print("Nome do produto não informado")
        return
    if valor <= 0:
        print("Valor do produto inválido")
        return
    if estoque <= 0:
        print("Estoque não informado")
        return
    if promo:
        valor -= valor * 0.15

    produto = {
        "nome": nome,
        "valor": valor,
        "estoque": estoque,
        "promo": promo
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def pesquisa():
    print("== Pesquisar produto ==")
    pes = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"].lower() == pes.lower():
            print("Nome:", produto["nome"])
            print("Valor:", produto["valor"])
            print("Estoque:", produto["estoque"])
            print("Promoção:", produto["promo"])
            return
    print("Produto não encontrado.")

def alterar_produto():
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            nomenovo = input(f"Digite o novo nome para {nome}: ")
            if nomenovo != "":
                produto["nome"] = nomenovo
            estoquenovo = int(input("Digite o novo estoque: "))
            if estoquenovo >= 0:
                produto["estoque"] = estoquenovo
            valornovo = float(input("Digite o novo valor: "))
            produto["valor"] = valornovo
            promonovo = input("O produto está em promoção? (s/n): ").upper()
            if promonovo == "S":
                produto["promo"] = True
                valornovo -= valornovo * 0.15
                produto["valor"] = valornovo
            else:
                produto["promo"] = False
            print("Alteração bem sucedida")

def remover():
    nome = input("Digite o nome do produto: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            print("Produto removido")
            return

def venda():
    print("== Realizar venda ==")
    respnome = input("Digite o nome do produto desejado: ")
    for produto in produtos:
        if produto["nome"].lower() == respnome.lower():
            quantnome = int(input("Digite a quantidade: "))
            if quantnome > produto["estoque"]:
                print("Quantidade informada não disponível")
                print("Estoque: ", produto["estoque"])
                return
            valortotal = quantnome * produto["valor"]
            print("Valor total a ser pago:", valortotal)
            dinheiror = float(input("Digite o valor do cliente: "))
            if dinheiror < valortotal:
                print("Valor insuficiente para a compra.")
                return
            troco = dinheiror - valortotal
            produto["estoque"] -= quantnome
            data_venda = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            venda = {
                "produto": produto["nome"],
                "quantidade": quantnome,
                "valor_total": valortotal,
                "troco": troco,
                "data": data_venda
            }
            historico.append(venda)
            print("Troco:", troco)
            print("Venda realizada com sucesso!")
            return
    print("Produto não encontrado.")

def historicovenda():
    print("== Histórico de vendas ==")
    for venda in historico:
        print("Produto:", venda["produto"])
        print("Quantidade:", venda["quantidade"])
        print("Valor total:", venda["valor_total"])
        print("Troco:", venda["troco"])
        print("Data:", venda["data"])

while True:
    print('''1 - Cadastrar
2 - Pesquisar
3 - Alterar produto
4 - Remover produto
5 - Realizar venda
6 - Listar vendas
7 - Sair''')
    resp = input("Digite sua ação: ")

    if resp == "7":
        print("Obrigado por utilizar o sistema. Até logo!")
        break
    elif resp == "1":
        cadastro()
    elif resp == "2":
        pesquisa()
    elif resp == "3":
        alterar_produto()
    elif resp == "4":
        remover()
    elif resp == "5":
        venda()
    elif resp == "6":
        historicovenda()
    else:
        print("Opção inválida. Tente novamente.")