import time
# Exercicio de medir valor gasto no mês de um aparelho!

while True:
    app = str(input("\033[34mDigite Qual é o Nome do Aparelho: \033[m")) # Nome do aplicativo

    app_hr = float(input("\033[34mQuantas horas o Seu aparelho fica ligado durante o dia ?\033[m ")) # Tempo que o aparelho fica ligado!

    app_dia = int(input("\033[34mQuantos dias no mês seu aparelho fica ligado ? \033[m ")) # Total de dia no mês que o aparelho fica ligado!

    app_pot = float(input("\033[34mQual é a pontencia do Aparelho ?\033[m ")) # Pede a potencia do aparelho

    app_soma = app_pot * app_hr * app_dia / 1000


    print(f"Seu Aparelho \033[34m{app}\033[m esta com gasto de \033[31m {app_soma:.2f} \033[m Por Mês!")
    print("Aguarde...")

    time.sleep(2)
    app_tot = app_soma + app_soma
    continuar = str(input("Voce deseja continuar ? [S/N]: ")).strip().upper()[0]



    if continuar == "S":
        continue

    elif continuar == "N":
        print(f"O valor total de gastos foi \033[31m R${app_tot}\033[m")
        print("Ate a proxima")
        break

    else:
        print("\033[31mResposta invalida, por favor Verifique os dados e tente novamente!")
        break

print("oi")
