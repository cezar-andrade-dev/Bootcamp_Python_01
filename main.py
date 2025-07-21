# desafio 1 - Cálculo de KPI do bônus: 1000 + salário * bônus

#solicitando o nome do usuário
nome_usuario = input("Digite o seu nome: ")

#solicitando o valor do salário
sal_usuario = float(input("Digite o valor do seu salário: "))

#Solicitando o valor do Bônus
bonus_usuario = float(input("Digite o valor do Bônus recebido: "))

#cálculo do bônus final
CONST_BONUS = 1000
valor_do_bonus = CONST_BONUS + sal_usuario*bonus_usuario

#Imprimindo os valores

print(f"O usuário {nome_usuario} possui o bônus de {valor_do_bonus}.")

