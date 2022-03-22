from atualizar import *
from cadastro import *
from delete import *
from menu import *


menu("SISTEMA DO VICAS: ")

while True:
    print("-="*20)
    print("""
    1 - Ver produtos cadastrados.
    2 - Cadastrar produto.
    3 - Alterar produto
    4 - Remover produto
    5 - Sair do sistema
    """)
    print("-="*20)

    try:
        escolha = int(input("Digite a opção desejada: "))
        print(" ")
        while str(escolha) not in "12345":
            print("Opção inválida")
            escolha = int(input("Digite a opção desejada: "))

        if escolha == 1:
            verLista()

        if escolha == 2:
            print(cadastroProduto())
        
        if escolha == 3:
            print(atualizacao())
        
        if escolha == 4:
            print(deletar())

        if escolha == 5:
            menu("ENCERRANDO SISTEMA...")
            break
    except (TypeError, ValueError):
        print("Digite apenas números!!")
        continue


