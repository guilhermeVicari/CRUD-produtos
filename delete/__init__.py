from cadastro import *
from menu import *

def deletar():
    menu('DELETAR PRODUTO')

    codigo = int(input("Código do produto: "))
    for x in lista_produtos:
        if x['codigoProd'] == codigo:
            lista_produtos.remove(x)
            return "Produto deletado com sucesso!!"
