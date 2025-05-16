# 6. Jogo da forca onde o jogador pode errar até 6 vezes
contagem_erros = 0
palavra_secreta = "FOCA"  # Poderia ser lida de um arquivo
palavra_oculta = ["_"] * len(palavra_secreta)

while contagem_erros < 6:
    print(f"\nA palavra secreta tem {len(palavra_secreta)} caracteres.")
    print(f"Palavra atual: {' '.join(palavra_oculta)}")
    
    chute = input("Você só pode errar 6 vezes. Chute uma letra: ").upper()
    
    if len(chute) != 1:
        print("Por favor, chute apenas uma letra!")
        continue
        
    if chute in palavra_oculta:
        print(f"Você já adivinhou a letra '{chute}'. Tente outra.")
        continue
        
    if chute in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == chute:
                palavra_oculta[i] = chute
        print(f"Boa! Você acertou a letra '{chute}'.")
    else:
        contagem_erros += 1
        print(f"Você errou pela {contagem_erros}a vez. Tente de novo!")
    
    if "_" not in palavra_oculta:
        print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
        break

if contagem_erros == 6:
    print("\nVocê atingiu o número máximo de tentativas. O jogo acabou.")
    print(f"A palavra secreta era: {palavra_secreta}")
