'''
3) Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
a) A entrada é dada em dois inteiros. 
b) Deve haver pelo menos duas funções: uma para a conversão e uma para a saída. 
c) Registre a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para 
registrar se é A.M. ou P.M. 
d) Inclua um loop que permita que o usuário repita esse cálculo para novos valores 
de entrada todas as vezes que desejar, digitando um valor negativo para a hora 
quando quiser encerrar '''


def hora_convertida(horas,minutos):
  novaHora = hora if hora <=12 else hora-12
  am_pm = "AM" if hora <12 else "PM" # se o valor for menos que 12 é AM, caso nao, pm
  return str(novaHora)+":"+str(minutos)+am_pm #conversor
  
while True: #loop ate a pessoa sair digitando -1
   hora = int(input("Insira a hora ou digite um valor negativo para sair")) #solicita que insira as horas
   if hora <=0: # se o valor digitado for negativo, sai do loop
    break #quebra o loop
   minutos = int(input("Insira os minutos")) # solicitado os minutos
   print(hora_convertida(hora,minutos)) #printa na tela os valores convertidos
