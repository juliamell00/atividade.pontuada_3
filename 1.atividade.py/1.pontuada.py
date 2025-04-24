import os
os.system ("cls || clear")

dependente = 1
salario_irrf : float
desconto_irrf = 0

# Solicite a matrícula e senha do funcionário para ter acesso aos seus dados.

matricula = int(input("Digite sua matrícula: "))
senha = (input("Digite sua senha: "))
print("==Acesso permitido==")

# Solicite o salário base do funcionário.
salario_base = float(input("Digite seu salário base: "))

def salariando(salario):
    if salario <= 1320.00:
        desconto_inss = salario * 0.075
    elif 1320.01 <= salario <= 2571.29:
        desconto_inss = salario * 0.09
    elif 2571.30 <= salario <= 3856.94:
        desconto_inss = salario * 0.12
    elif 3856.95 <= salario <= 7507.49:
        desconto_inss = salario * 0.14
    
    return min(desconto_inss, 1051.05) 
       
desconto_inss = salariando(salario_base)
print(f"Desconto INSS: {desconto_inss:.2f}")

def impostando(salario, dependente):
    deducao_dependente = 189.59 * dependente
    salario_irrf = salario - deducao_dependente
   
    if 2112.01 >= salario_irrf <= 2826.65:
        desconto_irrf = salario_irrf * 0.075
    elif 2826.66 <= salario_irrf <= 3544.00:
        desconto_irrf = salario_irrf * 0.15
    elif 3544.01 <= salario_irrf < 4256.00:
        desconto_irrf = salario_irrf * 0.225
    elif salario_irrf >= 4256.00:
        desconto_irrf = salario_irrf * 0.275
    return desconto_irrf

desconto_irrf = impostando(salario_base, dependente)  



vale = input("Voce deseja receber vale transpote? 's' ou 'n':").lower() 
if vale == 's':
    transporte = salario_base * 0.06
        
    
valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa: R$"))
vale_refeicao = valor_vale_refeicao * 0.20


plano_de_saude = dependente * 150.00
    
descontos_valor_total = desconto_inss + desconto_irrf + vale_refeicao + transporte + plano_de_saude
salario_liquido = salario_base - descontos_valor_total


print(f"\n=== FOLHA DE PAGAMENTO ===")
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Desconto do INSS: R$ {desconto_inss:.2f}")
print(f"Desconto do IRRF: R$ {desconto_irrf:.2f}")
print
print(f"Desconto Vale Transporte: R$ {transporte:.2f}")
print(f"Vale Refeição: R$ {vale_refeicao:.2f}")
print(f"Desconto Plano de Saúde: R${plano_de_saude:.2f}")
print(f"Salário liquido: R${salario_liquido:.2f}")


