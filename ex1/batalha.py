"""
batalha.py - Exercício 1: batalha por turnos.

Conteúdos: laços (while e for), estruturas de decisão (if/elif/else),
funções e parâmetros (inclusive parâmetros com valor padrão).

Cada lutador é um dicionário, por exemplo:
    {"nome": "Gork", "vida": 100, "vida_max": 100, "ataque": 18, "defesa": 5}

TAREFA: complete as funções marcadas com TODO. Apague a linha
"raise NotImplementedError" de cada função que você completar.
Para conferir, rode o arquivo testes_ex1.py.
"""

import random


def calcular_dano(ataque, defesa, critico=False):

    dano = ataque - defesa
    if critico == True:
        dano = dano*2


def aplicar_dano(vida, dano):

    vida-=dano

    if vida <= 0:
        vida = 0


def curar(vida, vida_max, cura=30):

    vida += cura

    if vida >= vida_max:
        vida = vida_max

def barra_de_vida(vida, vida_max, tamanho=10):

    barra = ''
    for i in range(tamanho):
        if i < vida * tamanho // vida_max:
            barra += '#'
        else:
            barra += '-'

    print(f"[{barra}] {vida}/{vida_max}")

def classificar_resultado(vida, vida_max):

    if vida == 0:
        print("DERROTA")
    elif vida == vida_max:
        print("Perfct Victory")
    elif vida > vida_max//2:
        print("Vitória")
    elif vida <= vida_max//2 and vida > 0:
        print("Vitória Apertada")


def ler_acao():
    """Mostra as ações e repete a pergunta ATÉ a pessoa digitar 1, 2 ou 3.
    Devolve o texto digitado ("1", "2" ou "3").
        1 - Atacar   2 - Tomar poção   3 - Fugir
    Se digitar outra coisa, mostre "Ação inválida!" e pergunte de novo."""
    while True:
        print("===== Ações =====")
        print("1 - Attack")
        print("2 - Drink Potion")
        print("3 - To escape")
        option = input("Select one only option: ")
        if option == "1":
            return 1
        elif option == "2":
            return 2
        elif option == "3":
            return 3
        else:
            print("Action invalide. Retry")

def batalha(heroi, inimigo, pocoes=3):
    """Executa a batalha e devolve um dicionário com o resultado:
       {"resultado": "vitoria" | "derrota" | "fuga", "turnos": ...,
        "vida_restante": ..., "pocoes": quantas poções sobraram}
    """
    turno = 0
    while heroi["vida"] > 0 and inimigo["vida"] > 0:
        turno = turno + 1
        print(f"\n--- Turno {turno} ---")
        print(f"{heroi['nome']:<12} {barra_de_vida(heroi['vida'], heroi['vida_max'])}")
        print(f"{inimigo['nome']:<12} {barra_de_vida(inimigo['vida'], inimigo['vida_max'])}")

        acao = ler_acao()
        if acao == "1":
            # TODO: 1) sorteie o crítico:  critico = random.randint(1, 10) == 10
            #       2) calcule o dano com calcular_dano(ataque do herói, defesa do inimigo, critico)
            #       3) atualize a vida do inimigo com aplicar_dano
            #       4) mostre quanto de dano foi causado (avise se foi crítico)
            pass
        elif acao == "2":
            # TODO: se ainda houver poções: diminua 1, cure o herói com curar() e avise
            #       quantas restam. Se não houver: mostre "Você não tem mais poções!"
            pass
        else:
            # TODO: mostre que o herói fugiu e devolva (return) o dicionário com
            #       "resultado": "fuga" (veja o formato no início desta função)
            pass

        # TODO: se o inimigo ainda estiver vivo, ele ataca o herói
        #       (dano = calcular_dano(ataque do inimigo, defesa do herói), sem crítico)

    if heroi["vida"] > 0:
        resultado = "vitoria"
    else:
        resultado = "derrota"
    print("\n" + classificar_resultado(heroi["vida"], heroi["vida_max"]) + "!")
    return {"resultado": resultado, "turnos": turno,
            "vida_restante": heroi["vida"], "pocoes": pocoes}


# Este bloco só roda quando executamos ESTE arquivo (python batalha.py).
# Quando outro arquivo faz "import batalha", ele NÃO roda.
if __name__ == "__main__":
    heroi = {"nome": "Gork", "vida": 100, "vida_max": 100, "ataque": 18, "defesa": 5}
    inimigo = {"nome": "Goblin", "vida": 60, "vida_max": 60, "ataque": 12, "defesa": 3}
    final = batalha(heroi, inimigo)
    print(final)
