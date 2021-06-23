from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("===" * 10)
    print("======== Bem Vindo(a) ========")
    print("============ SHOP ============")
    print("===" * 10)
    print('\n')
    print('Selecione a opção:\n'
          '1 - Cadastrar produto;\n'
          '2 - Listar produtos;\n'
          '3 - Comprar produto;\n'
          '4 - Visualizar carrinho;\n'
          '5 - Fechar pedido;\n'
          '6 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        sair()
    else:
        print("Opção inválida")



def cadastrar_produto() -> None:
    print("Cadastro de Produto\n"
          "===================")
    nome: str = str(input("Informe o nome do produto: "))
    preco: float = float(input("Informe o preço do produto: "))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f"O produto {produto.nome} com o valor de {formata_float_str_moeda(produto.preco)} foi cadastrado com sucesso")
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print("Lista de Produtos")
        print("=================")
        sleep(2)
        for i in produtos:
            print(i)
            print("=================")
            sleep(1)
    else:
        print("Ainda não há produtos cadastrados")
        sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print("Produtos disponíveis\n"
              "=================")
        for i in produtos:
            print(i)
            print("=================")
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for i in carrinho:
                    qtd: int = i.get(produto)
                    if qtd:
                        i[produto] = qtd + 1
                        print(f"O produto {produto.nome} agora possui {qtd + 1} unidades no carrinho")
                        tem_no_carrinho = True
                        sleep(2)
                if not tem_no_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} de valor {formata_float_str_moeda(produto.preco)} foi adicionado ao carrinho")
                    sleep(2)
            else:
                item: dict = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} de valor {formata_float_str_moeda(produto.preco)} foi adicionado ao carrinho")
                sleep(2)
        else:
            print(f"O produto de código {codigo} não foi encontrado")
            sleep(2)
        menu()

    else:
        print("Ainda não há produtos cadastrados")
        sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("Produtos no carrinho")
        for item in carrinho:
            for dado in item.items():
                print(dado[0])
                print(f"Quantidade: {dado[1]} unidade(s)")
                print("=================")
                sleep(1)
    else:
        print("Ainda não há produtos no carrinho")
        sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print("Produtos no Carrinho")
        for item in carrinho:
            for dado in item.items():
                print(dado[0])
                print(f"Quantidade: {dado[1]} unidade(s)")
                valor_total += dado[0].preco * dado[1]
                print("=================")
                sleep(1)
        print(f"Sua fatura é de {formata_float_str_moeda(valor_total)}")
        carrinho.clear()
        sair()
        sleep(3)
    else:
        print("Ainda não há produtos no carrinho")
        sleep(2)
    menu()


def sair():
    print("Adeus, volte sempre!")
    exit(0)


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()