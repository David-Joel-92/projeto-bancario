
#Programa de cadastro de cliente e deposito bancariao para treinar as habilidades com os operadores condicionais

#Menu e variaveis para cadastrar ou fazer login do usuário

menu_cadastro= """
Digite uma opção:
[1] Login
[2] Criar cadastro 
[0] Sair

==> """

cadastro_usuario = ""
senha_cadastro = ""
tentativa_senha = 0

#Menu e vairaveis para operações bancarias 

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
opcao = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while  True:
    tentativa_senha = 0
    opcao_usuario = input (menu_cadastro)

#Inicio do código para a apção 1 do menu_cadastro
# onde permito o usuário a fazer o logim e as operações banccárias

    if opcao_usuario == "1":

     while opcao_usuario == "1" and tentativa_senha < 4 :
        
        login_usuario = input("\nDigite o nome do usuario: ")
        
        if login_usuario == cadastro_usuario:
            
            while tentativa_senha < 4  :
                
             if tentativa_senha <3 and opcao != "0" :
                  senha_login = input("\nDigite sua senha 11:")    
                     
                  if senha_login != senha_cadastro and tentativa_senha <3 :
                    tentativa_senha += 1  
                    print ("\nSenha invalida!")

                  elif senha_login == senha_cadastro:
                        

# Inicio do código para operações bancarias 

                     while opcao != "0":                     

                            opcao = input(menu)

                            if opcao == "1":
                                valor = float(input("Informe o valor do depósito: "))

                                if valor > 0:
                                    saldo += valor
                                    extrato += f"Depósito: R$ {valor:.2f}\n"

                                else:
                                    print("Operação falhou! O valor informado é inválido.")

                            elif opcao == "2":
                                valor = float(input("Informe o valor do saque: "))

                                excedeu_saldo = valor > saldo

                                excedeu_limite = valor > limite

                                excedeu_saques = numero_saques >= LIMITE_SAQUES

                                if excedeu_saldo:
                                    print("Operação falhou! Você não tem saldo suficiente.")

                                elif excedeu_limite:
                                    print("Operação falhou! O valor do saque excede o limite.")

                                elif excedeu_saques:
                                    print("Operação falhou! Número máximo de saques excedido.")

                                elif valor > 0:
                                    saldo -= valor
                                    extrato += f"Saque: R$ {valor:.2f}\n"
                                    numero_saques += 1

                                else:
                                    print("Operação falhou! O valor informado é inválido.")

                            elif opcao == "3":
                                print("\n================ EXTRATO ================")
                                print("Não foram realizadas movimentações." if not extrato else extrato)
                                print(f"\nSaldo: R$ {saldo:.2f}")
                                print("==========================================")

                            elif opcao == "0":
                               opcao_usuario == ""
                               print(" Fim de operação!") 
                               print(" Obrigador por usar nosso serviços!")  
                               break
                                 
                                 

                            else:
                                 print("Operação inválida, por favor selecione novamente a operação desejada.")

#Fim do bloco das operações bancarias

             elif tentativa_senha > 2:
                  print ("numero de tentativas exedidas!:"  )
                  tentativa_senha += 2

        elif login_usuario != cadastro_usuario:
          print("\nUsuario não cadastrado!")  
          break
#Fim do código da apção1 do menu_cadastro   ----------  Inicio docódigo da opção 2 do menu_cadastro opção cadastor  
   
    if opcao_usuario == "2":
   
       cadastro_usuario_novo = input("Digiti um nome de usuario: ")
       if cadastro_usuario_novo != cadastro_usuario:
          cadastro_usuario = cadastro_usuario_novo
          senha_cadastro = input ("Digite uma senha: ")
          print ( "\n**Usuario cadastrado com sucesso**")

       else:
        print ("\nUsuario invalido!") 
        print ("\nNome de usuário já cadastrado")

# Fim do códido da opção 2 e inicio da opção 0 
                            
    if opcao_usuario == "0":
      print ( "\nOperação finalizada com sucesso!")
      print ("Obrigador por usar nossos serviços!")  
      break


