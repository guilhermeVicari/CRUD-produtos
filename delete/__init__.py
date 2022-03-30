from cadastro import *
from menu import *

def deletar():
    menu('DELETAR PRODUTO')

    if len(lista_produtos) == 0:
        return 'Não existe nenhum produto cadastrado!!'
    else:
        codigo = int(input("Código do produto: "))
        for x in lista_produtos:
            if x['codigoProd'] == codigo:
                lista_produtos.remove(x)
                return "Produto deletado com sucesso!!"
