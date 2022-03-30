from cadastro import *
from menu import *

def atualizacao():
    menu('ATUALIZAR PRODUTO')

    if len(lista_produtos) == 0:
        return 'Não existe nenhum produto cadastrado!!'
    else:
        codigo = int(input("Código do produto: "))
        for elemento in lista_produtos:
            if elemento['codigoProd'] == codigo:
                try:
                    nomeprod = str(input("Nome produto: "))
                    qtdProd = int(input("Quantidade produto: "))

                    elemento['nomeProduto'] = nomeprod
                    elemento['qtdProduto'] = qtdProd
                
                    return "Atualização realizada com sucesso!!"
                except (TypeError, ValueError):
                    return "Você digitou errado algum valor, digite novamente!! "