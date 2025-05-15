#✅ Criar um dicionário com dados pessoais (nome, idade, telefone, endereço).
#✅ Imprimir apenas o nome do dicionário criado.
dados = {'nome':'arthur',
          'idade': 19,
 'telefone': "98737585",
   'endereço':"Dois irmaos"}
print(dados['nome'])

#✅ Criar um dicionário com dados fornecidos pelo usuário.
#✅ Imprimir os itens do dicionário no formato chave: valor, ordenado pela chave.
n = input('Qual seu nome: ')
i = int(input('Qual sua idade: '))
t = input('Qual seu telefone: ')
e = input('Qual seu endereço: ')
dados = {'nome':n,
          'idade': i,
 'telefone': t,
   'endereço':e}
for chave in sorted(dados.keys()):  
    print(f"{chave}: {dados[chave]}")
