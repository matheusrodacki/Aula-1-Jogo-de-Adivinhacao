import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

numero_secreto = random.randrange(1,101)

chute_str = "0"

while (chute_str != "x"):
  chute_str = input("Digite um número entre 1 e 100, ou digite x para sair: ")
  print("Você digitou {}".format(chute_str))

  if (chute_str != "x"):
    chute = int(chute_str)
    if (chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
      print("\nParabéns, você acertou!!!!!!11")
      break
    else:
      if (maior):
        print("\nVocê errou! O seu chute foi maior que o número secreto.")
      elif (menor):
        print("\nVocê errou! O seu chute foi menor que o número secreto.")

  else:
    print("Você saiu do jogo!\n")


print("Obrigado por jogar!")
