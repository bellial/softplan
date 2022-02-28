from random import choice

jogada = ["pedra", "papel", "tesoura"]

#Matriz de possibilidades para comparação das jogadas
regras = (("empate", "derrota", "vitoria"), ("vitoria", "empate", "derrota"), ("derrota", "vitoria", "empate"))

resultado = {
    "empate": "    Empate!",
    "vitoria": "   Vitória!",
    "derrota": "   Derrota!",
}

# firulas
print('-=' * 13)

print('''Escolha dentre as opções: 

Pedra 
Papel 
Tesoura 

ou digite sair''')

print('-=' * 13)

# O jogo
while True:
    jogador, computador = input('Faça a sua jogada: ').lower(), choice(jogada)

    if jogador == "sair":  
        break

    if jogador in jogada:  
        print(f"  O computador jogou: {computador}")
        print(resultado[regras[jogada.index(jogador)][jogada.index(computador)]])
    else:
        print(f"  As opções válidas são:\n {jogada}")
