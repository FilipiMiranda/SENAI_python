# nome = "Filipi"
# idade = 17
# altura = 1.75
# casado = False

# print("Nome:"+ nome)
# print("minha idade é:"+ str(idade))
# print("tenho " + str(altura) + "de altura")
# print("com status: " + str(casado))

# print("ola {}" .format(nome))
# print("ola", nome)
# print("ola %s" %(nome))
# print(f"ola {nome}")

for i in range(3):
    email = input("Digite seu Email: ")
    senha = input("Digite sua Senha: ")

    if (email == "Filipi" and senha == "123456"):

        print("Acesso permitido")
        opcao = input("1-Saque  2-Deposito  3-Pix")
        match opcao:
            case "1":
                print("Você escolheu o Saque")
                saque = input ("Informe o valor do Saque: ")
            case "2":
                dep = input ("Informe o valor do Deposito: ")
            case "3":
                pix = input ("Informe o valor do Pix: ")
    else:
        print("Acesso negado")
        




