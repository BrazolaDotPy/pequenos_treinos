from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input("Informe o nível de dificuldade desejado (1 - Muito fácil, 2 - Fácil, 3 - Médio, 4 - Difícil): "))
    calc = Calcular(dificuldade)
    print("Informe o resultado para a seguinte operação: ")
    calc.mostrar_operacao()
    resultado: int = int(input())
    if calc.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} pontos")
    continuar: int = int(input("Deseja continuar no jogo? (1 - Sim, 0 - Não): "))
    if continuar:
        jogar(pontos)
    else:
        print(f"Você finalizou o jogo com {pontos} pontos\n"
              f"Até a próxima!")

if __name__ == '__main__':
    main()
