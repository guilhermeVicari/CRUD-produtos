from menu import *

lista_produtos = list()
produto = dict()

def cadastroProduto():
    menu('CADASTRO PRODUTOS')

    while True:
        try:
            codProd = int(input("Código produto: "))
            nomeprod = str(input("Nome produto: "))
            qtdProd = int(input("Quantidade produto: "))

            produto["codigoProd"] = codProd
            produto["nomeProduto"] = nomeprod
            produto["qtdProduto"] = qtdProd

            lista_produtos.append(produto.copy())
            produto.clear()
            
            print("Cadastro Realizado com sucesso!!")
        except (TypeError, ValueError):
            return "Você digitou errado algum valor, digite novamente!! "
            
        resposta = str(input('Deseja cadastrar outro produto ? [S/N]: ')).upper()[0]

        while resposta not in 'SsNn':
            print("Digite uma resposta válida, apenas S ou N")
            resposta = str(input('Deseja cadastrar outro produto ? [S/N]: ').upper()[0])

        if resposta == 'N':
            break
        if resposta == 'S':
            continue


def verLista():
    menu("INFORMAÇÕES PRODUTOS")
    for elemento in lista_produtos:
        for chave, valor in elemento.items():
            print(f'{chave}:\t{valor}')
        print("-"*10)
