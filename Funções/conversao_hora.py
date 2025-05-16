def hora_em_12h(h, m):
    if h > 12:
        h_convertida = h - 12
        return h_convertida, m, "P.M."
    elif h == 12:
        return h, m, "P.M."
    elif h == 0:
        return 12, m, "A.M."
    else:
        return h, m, "A.M."

if __name__ == "__main__":
    while True:
        hora24 = input("Digite a hora em 24 horas (00-23): ")
        minuto = input("Digite os minutos (00-59): ")
        if hora24.isdigit() and minuto.isdigit():
            hora24 = int(hora24)
            minuto = int(minuto)
            if (0 <= hora24 < 24) and (0 <= minuto < 60):
                hora12, minuto_convertido, periodo = hora_em_12h(hora24, minuto)
                print(f"A hora convertida para 12h é: {hora12}:{minuto_convertido:02d} {periodo}")
            else:
                print("Hora ou minuto fora dos limites!")
        else:
            print("Por favor, insira apenas números válidos.")
        
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break
