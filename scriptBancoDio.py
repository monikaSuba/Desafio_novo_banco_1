
saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
extrato = ""

menu = '''
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
'''

while True:
  print("Bem vindo ao nosso novo sistema bancário!")
  print("Digite o número da ação que deseja realizar:")
  acao = int(input(menu))
  if acao == 1:
    print("Digite o valor que deseja depositar:")
    valor = float(input())
    if valor>0:
      saldo += valor
      extrato+=(f"Sua conta recebeu um depósito de R$ {valor:.2f}\n")
      recado = f'''
              Sua conta recebeu um depósito de R$ {valor}.00
              Seu saldo é de R$ {saldo:.2f}
              '''
      print(recado)

  elif acao == 2:
    if numero_saques >= limite_saques:
       print("Limite de 3 saques diários atingido. Não é possível realizar a operação.")
    else:
      print("Informe o valor que deseja sacar:")
      saque = float(input())

      if saque > 500:
        print("Não é possível realizar a operação! O limite máximo para saque é R$ 500.00")
      else:
        if saque > saldo:
          print("Saldo insuficiente! Não é possível realizar o saque.")
        else : 
          saldo -= saque
          numero_saques +=1
          extrato+=(f"Foi realizado um saque de R${saque:.2f}\n")
          print(f"Saque de R${saque:.2} realizado com sucesso")


  elif acao == 3:
    print("\n ============== extrato =================")
    print("Não foi realizado qualquer ação na conta." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("===========================================")
   


  elif acao == 4:
    print("Obrigado por usar o nosso sistema!")
    break

  else:
    print("Operação inválida! Por favor selecione novamente a operação que deseja.")
