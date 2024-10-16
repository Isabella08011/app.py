import random

# Função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Há muitos e muitos anos atrás,", "Agora irei contar como minha história começou,", "Em um dia não muito ensolarado,"]
    return random.choice(introducoes)

# Função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["um poderoso feiticeiro", "o vilão mais temido por tudo e todos",
                        "uma poderosa feiticeira escarlate", "uma futura rainha"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    finais = ["enfrentando outros grandes feiticeiros.", "derrotando um terrível vilão que vivera por muitos e muitos anos.",
               "salvando o reino da escuridão.",
              " a caminho de encontrar um amor verdadeiro."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia())