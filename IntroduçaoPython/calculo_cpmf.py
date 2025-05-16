# 6. Calcular o valor do imposto CPMF (0.3%) sobre um cheque
valor_cheque = float(input("Digite o valor do cheque: R$ "))
imposto = valor_cheque * 0.003
valor_liquido = valor_cheque - imposto
print(f"Valor do imposto CPMF (0.3%): R$ {imposto:.2f}")
print(f"Valor líquido após o imposto: R$ {valor_liquido:.2f}")
