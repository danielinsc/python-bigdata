'''1) Faça função que calcule a área do trapézio, dados:a) Base maior
b) Base menor
c) Altura
Lembrando que a área pode ser calculada por:
O programa principal deve pedir os valores e usar a função para calcular a área.'''

B = float(input('Qual o valor da base maior? '))  # solicita informacao
b = float(input('Qual o valor da base menor? ')) # solicita informacao
h = float(input('Qual o valor da altura? ')) # solicita informacao
a = 2

formula = ((B + b) * h) / a # realizacao do calculo

print("A área do trapézio é: ", formula) # printa na tela o calculo
