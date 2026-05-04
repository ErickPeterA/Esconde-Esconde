import random
import time

print("=== ESCONDE-ESCONDE ===")
print("Posições na grade:")
print("1  2  3")
print("4  5  6")
print("7  8  9")
print("=======================\n")

nome_jogador = input("Digite seu nome: ").strip()
if not nome_jogador:
    nome_jogador = "Jogador"

grade = ["🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦"]
pontosbot = 15
pontosjog = 15


def entrada_valida(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if 1 <= valor <= 9:
                return valor
            else:
                print("Digite um número entre 1 e 9.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 9.")

print(f"\nO Bot se escondeu! Você tem 3 chances para achar, {nome_jogador}.")
bot_escondido = random.randint(0, 8)
chances = 3

while chances > 0:
    print("\nGrade:")
    print(grade[0], grade[1], grade[2])
    print(grade[3], grade[4], grade[5])
    print(grade[6], grade[7], grade[8])
    time.sleep(1)

    escolha = entrada_valida("\nOnde você vai procurar (1 a 9)? ")
    indice = escolha - 1

    if indice == bot_escondido:
        grade[indice] = "🤖"
        print("========================")
        pontosjog += 5
        pontosbot -= 5
        print(f"Parabéns {nome_jogador}, você achou o Bot")
        break
    else:
        grade[indice] = "❌"
        chances -= 1
        pontosbot += 5
        pontosjog -= 5
        print(f"\nErrou! Você ainda tem {chances} chance(s).")

if chances == 0:
    grade[bot_escondido] = "🤖"
    print("\nO bot estava aqui...")

print("\nGrade:")
print(grade[0], grade[1], grade[2])
print(grade[3], grade[4], grade[5])
print(grade[6], grade[7], grade[8])

print("\n======================")
print(f"PLACAR ATUAL:\n{nome_jogador}: {pontosjog}\nBot: {pontosbot}")
print("======================")

print("\nAGORA É A SUA VEZ DE SE ESCONDER!")

grade = ["🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦"]

esconderijo = entrada_valida("Escolha onde você quer se esconder (1 a 9): ")
indice_jogador = esconderijo - 1

chances_bot = 3
opcoes_do_bot = list(range(9))

while chances_bot > 0:
    chute_do_bot = random.choice(opcoes_do_bot)
    opcoes_do_bot.remove(chute_do_bot)
    time.sleep(2)

    print(f"\nO Bot procurou na posição {chute_do_bot + 1}.")

    if chute_do_bot == indice_jogador:
        grade[indice_jogador] = "😜"
        print("O bot te ACHOUUUU!")
        pontosbot += 5
        pontosjog -= 5
        break
    else:
        grade[chute_do_bot] = "❌"
        chances_bot -= 1
        pontosbot -= 5
        pontosjog += 5
        print(f"O Bot errou! Ele tem {chances_bot} chance(s).")

if chances_bot == 0:
    grade[indice_jogador] = "😜"
    print(f"Parabéns {nome_jogador}, o bot não te achou!")

print("\nGrade Final:")
print(grade[0], grade[1], grade[2])
print(grade[3], grade[4], grade[5])
print(grade[6], grade[7], grade[8])

print("\n======================")
if pontosjog > pontosbot:
    print(f"Parabéns {nome_jogador}, você ganhou do bot!")
elif pontosbot > pontosjog:
    print(f"Que pena {nome_jogador}, você perdeu para o Bot.")
else:
    print("Empate! Boa partida!")

print(f"\nPLACAR FINAL:\n{nome_jogador}: {pontosjog}\nBot: {pontosbot}")
print("======================")

resultado = "Vitória" if pontosjog > pontosbot else ("Derrota" if pontosbot > pontosjog else "Empate")

with open("pontuacoes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome_jogador} - Pontos: {pontosjog} | Bot: {pontosbot} | Resultado: {resultado}\n")

print(f"\nPontuação salva em 'pontuacoes.txt'!")
