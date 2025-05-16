# Programa que converte uma sequência de DNA em RNA mensageiro (RNA-m)
# Segue a tabela de conversão:
# | DNA | RNA-m |
# |-----|-------|
# | A   | U     |
# | G   | C     |
# | C   | G     |
# | T   | A     |

# Recebe a sequência de DNA do usuário
sequencia_dna = input("Digite a sequência de DNA: ").lower()

# Processo de conversão usando substituições temporárias
sequencia_dna = sequencia_dna.replace("a", "x")  # Substitui A por um marcador temporário
sequencia_dna = sequencia_dna.replace("g", "y")  # Substitui G por um marcador temporário
sequencia_dna = sequencia_dna.replace("c", "g")  # Converte C para G
sequencia_dna = sequencia_dna.replace("t", "a")  # Converte T para A
sequencia_dna = sequencia_dna.replace("y", "c")  # Converte o marcador Y (original G) para C
sequencia_dna = sequencia_dna.replace("x", "u")  # Converte o marcador X (original A) para U

# Converte para maiúsculas para exibição
sequencia_rna = sequencia_dna.upper()

print(f"A sequência em RNA é: {sequencia_rna}")
