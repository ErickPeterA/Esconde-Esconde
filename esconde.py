import random
import time

print("=== ESCONDE-ESCONDE ===")
print("Posições na grade:")
print("1  2  3")
print("4  5  6")
print("7  8  9")
print("=======================\n")

grade = ["🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦"]
pontosbot = 15
pontosjog = 15

#bot
print("O Bot 🤖 se escondeu! Você tem 3 chances para achar.")
bot_escondido = random.randint(0, 8) 
chances = 3

while chances > 0:
    print("\nGrade:")
    print(grade[0], grade[1], grade[2])
    print(grade[3], grade[4], grade[5])
    print(grade[6], grade[7], grade[8])
    time.sleep(1)
    
    escolha = int(input("\nOnde você vai procurar (1 a 9)? "))
    indice = escolha - 1 
    
    if indice == bot_escondido:
        grade[indice] = "🤖"
        print("========================")
        pontosjog= pontosjog + 5
        pontosbot= pontosbot - 5
        print("Parabéns, você achou o Bot 👏")
        break
    else:
        grade[indice] = "❌"
        chances = chances - 1
        pontosbot = pontosbot + 5
        pontosjog = pontosjog - 5
        print(f"\nCalma você ainda tem mais, {chances} chances.")

if chances == 0:
    grade[bot_escondido] = "🤖"
    print("\nO bot estava aqui...")

print(grade[0], grade[1], grade[2])
print(grade[3], grade[4], grade[5])
print(grade[6], grade[7], grade[8])

print("\n======================")
print(F"PLACAR ATUAL:\nJogador: {pontosjog}\nPontos bot: {pontosbot}")
print("======================")

print("\nAGORA É A SUA VEZ!")


grade = ["🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦", "🟦"]

esconderijo = int(input("Escolha onde você quer se esconder (1 a 9): "))
indice_jogador = esconderijo - 1

chances_bot = 3
opcoes_do_bot = [0, 1, 2, 3, 4, 5, 6, 7, 8] 

while chances_bot > 0:
    chute_do_bot = random.choice(opcoes_do_bot)
    time.sleep(2)
    
    print(f"\nO Bot procurou na posição, {chute_do_bot + 1}")
    
    if chute_do_bot == indice_jogador:
        grade[indice_jogador] = "😜"
        print("O bot te ACHOUUUU")
        pontosbot = pontosbot + 5
        pontosjog = pontosjog - 5
        break
    else:
        grade[chute_do_bot] = "❌"
        chances_bot = chances_bot - 1
        pontosbot = pontosbot - 5
        pontosjog = pontosjog + 5
        print(f"O Bot errou ele tem, {chances_bot},chances.")

if chances_bot == 0:
    grade[indice_jogador] = "😜"
    print("Parabenss o bot não te achou")

print("\nGrade Final:")
print(grade[0], grade[1], grade[2])
print(grade[3], grade[4], grade[5])
print(grade[6], grade[7], grade[8])

if pontosjog > pontosbot:
    print("Parabens jogador você ganhou do bot👏👌")
else:
    print("Que pena você perdeu para o Bot")
print(f"\nPLACAR FINAL:\nJogador: {pontosjog}\nPontos bot: {pontosbot}")
