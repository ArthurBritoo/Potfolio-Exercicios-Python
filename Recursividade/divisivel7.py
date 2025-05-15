#Crie uma função recursiva em python chamada “divisivel7” que recebe um parâmetro “numero”. Você deverá usar a recursão para verificar se "numero" é divisível por 7, isto é, se ocorre divisão exata com resto 0. Contudo, você deverá utilizar a seguinte regra recursiva que foi proposta recentemente pelo jovem nigeriano Chika Ofili, de 12 anos:
#Para verificar se um número é divisível por 7, basta pegar o último dígito e multiplicar por 5 e adicionar à parte restante (aos demais dígitos). Com isto você terá um novo número. Se este novo número é divisível por 7, o número original é divisível por 7.
#REGRA GERAL: Você deverá utilizar python 3. Você deve implementar uma função recursiva que receberá somente um número inteiro como parâmetro. Não é permitido usar loops (for, while) nem importar/usar blibliotecas extras, exceto para a leitura da entrada e exibição da saída. Não é permitido usar listas, dicionários ou outras estruturas de dados. Você não pode usar nenhuma função pronta para o cálculo, nem para calcular o resto por 7 ou por qualquer outro número, sendo permitida somente a divisão inteira por 10 e resto da divisão por 10.  
#Entrada: A entrada contém um número inteiro maior que zero.
#Saída: A saída deverá exibir "s" (se o número informado for divisível por 7) ou "n" (se o número informado não for divisível por 7).
def verifica_7(valor):
    if int(valor) < 10 and int(valor) != 7:
        return print("n")
    else:
        if int(valor) != 7 and int(valor) != 49:
            digito = int(valor[-1]) * 5
            novo_valor = str(int(valor[0:-1]) + digito)
            verifica_7(novo_valor)
        else:
            return print("s")

verifica_7(input())
