'''
Faça um programa em Python com uma função chamada soma_imposto. A função 
possui dois parâmetros formais:
a) taxa_imposto, que é a quantia de imposto sobre vendas expressa em 
porcentagem; e 
b) custo, que é o custo de um item antes do imposto. A função "altera" o valor de 
custo para incluir o imposto sobre vendas.
O programa principal deve pedir os dados e usar a função para calcular preço do produto.
'''

def soma_imposto(taxa_imposto, Custo): #funcao 
    return (1 + taxa_imposto/100)*Custo # realiza o calculo dos parametros
taxa = float(input('Digite a taxa de imposto: ')) #solicita o usuario inserir os dados
custo = float(input('Digite o custo do produto: ')) #solicita o usuario inserir os dados
print('Valor do produto com imposto:', soma_imposto(taxa,custo)) #printa o valor do produto com a taxa de imposto
