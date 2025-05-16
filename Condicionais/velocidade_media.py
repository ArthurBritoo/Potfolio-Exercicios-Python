# 3. Entrar com uma distância (km) e tempo de viagem (horas) de um automóvel,
# e dizer se a velocidade média foi superior ao limite (110 km/h) ou não
distancia = float(input("Digite a distância percorrida (km): "))
tempo = float(input("Digite o tempo da viagem (horas): "))
velocidade = distancia / tempo

if velocidade > 110:
    print(f"Velocidade média {velocidade:.2f} km/h - Acima do limite")
else:
    print(f"Velocidade média {velocidade:.2f} km/h - Dentro do limite")
