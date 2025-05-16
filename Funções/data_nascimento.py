def nome_mes(mes):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if 1 <= mes <= 12:
        return meses[mes - 1]
    else:
        return "Mês inválido"

if __name__ == "__main__":
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    novaData = data.split("/")
    nomeMes = nome_mes(int(novaData[1]))
    print(f"Você nasceu em {novaData[0]} de {nomeMes} de {novaData[2]}")
