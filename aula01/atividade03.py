# Crie um algoritmo que desenvolva o controle de uma sessão de teatro, contendo os seguintes quesitos:
# O teatro deverá ter, no máximo, 40 linhas por 60 colunas (completando um total de 2400 cadeiras).
# O usuário, ao iniciar o sistema deverá escolher o tamanho da sala (informando linha e coluna, respectivamente e o valor de ingresso total.)
# Deverá ser desenhado um menu, com as seguintes opções:
# [1] - Iniciar o teatro: essa opção o usuário informa quantas linhas e colunas serão ocupadas, não podendo superar o total de linhas e colunas determinadas para o tamanho do teatro e, também não poderá ser feito se outro espetáculo estiver aberto.
# [2] - Reservar lugar, informando linha e coluna. Se este lugar estiver livre, poderá ser reservado e colocado uma informação que está reservado (para que futuramente não possa ser reservado novamente). Para reserva, deverá pagar 30% do valor total. Se estiver reservado, informar ao usuário e pedir novo conjunto de linha e coluna.
# [3] - Comprar lugar. Verificar se lugar está livre, se tiver, cobrar valor cheio, se estiver reservado, cobrar valor de 70% do valor cheio, já que para reservar, precisou pagar 30%.
# [4] - Liberar lugar. Caso lugar esteja reservado ou comprado, trocar status para Livre e subtrair do sistema o valor pago anteriormente (se reservado, subtrair 30% do valor cheio, se estiver vendido, subtrair 100% do valor cheio).
# [5] - Listar poltronas (assim o usuário poderá saber, quantos e quais locais estão livres, quais e quantos reservados e quais e quantos vendidos).
# [6] - Encerrar o espetáculo (essa opção só poderá ser utilizada se tivermos 60% + 1, da ocupação total do teatro - posições vendidas. Neste momento, reservas não contam). Quando o espetáculo for encerrado, deverá ser exibido o total de cadeiras vendidas (e o valor das vendas), o total de reserva (e o valor das reservas), o total de cadeiras livres (e o valor que não foi recebido). Deverá também exibir ao final, a totalização do espetáculo.
# Total Geral de Cadeiras: XXX
# Total de Cadeiras Vazias: XXX
# Total de Cadeiras Reservadas: XXX
# Total de Cadeiras Vendidas: XXX
# Total do Espetáculo em R$: 000.00
# Total não recebido em R$: 000.00
# Total em reservas R$: 000.00
# [7] - Reiniciar o espetáculo (todas as variáveis deverão ser reiniciadas e as cadeiras do espetáculo, liberadas).

total_linhas = 0
total_colunas = 0
valor_ingresso_total = 0
cadeiras_vendidas = 0
valor_vendas = 0
cadeiras_reservadas = 0
valor_reservas = 0
cadeiras_livres = 0
valor_nao_recebido = 0

teatro = []

def criar_teatro(linhas, colunas):
    global total_linhas, total_colunas, teatro, cadeiras_livres
    total_linhas = linhas
    total_colunas = colunas
    teatro = [['Livre'] * colunas for _ in range(linhas)]
    cadeiras_livres = linhas * colunas

def exibir_menu():
    print("[1] - Iniciar o teatro")
    print("[2] - Reservar lugar")
    print("[3] - Comprar lugar")
    print("[4] - Liberar lugar")
    print("[5] - Listar poltronas")
    print("[6] - Encerrar o espetáculo")
    print("[7] - Reiniciar o espetáculo")

def lugar_valido(linha, coluna):
    if linha >= 0 and linha < total_linhas and coluna >= 0 and coluna < total_colunas:
        return True
    return False

def reservar_lugar(linha, coluna):
    global cadeiras_reservadas, valor_reservas
    if teatro[linha][coluna] == 'Livre':
        teatro[linha][coluna] = 'Reservado'
        cadeiras_livres -= 1
        cadeiras_reservadas += 1
        valor_reservas += valor_ingresso_total * 0.3
        print("Lugar reservado com sucesso!")
    else:
        print("Este lugar já está reservado. Por favor, escolha outro.")

def comprar_lugar(linha, coluna):
    global cadeiras_vendidas, valor_vendas, valor_nao_recebido
    if teatro[linha][coluna] == 'Livre':
        teatro[linha][coluna] = 'Vendido'
        cadeiras_livres -= 1
        cadeiras_vendidas += 1
        valor_vendas += valor_ingresso_total
        print("Lugar comprado com sucesso!")
    elif teatro[linha][coluna] == 'Reservado':
        teatro[linha][coluna] = 'Vendido'
        cadeiras_reservadas -= 1
        cadeiras_vendidas += 1
        valor_vendas += valor_ingresso_total
        valor_reservas -= valor_ingresso_total * 0.3
        print("Lugar comprado com sucesso! (era uma reserva)")
    else:
        print("Este lugar já está vendido. Por favor, escolha outro.")

def liberar_lugar(linha, coluna):
    global cadeiras_vendidas, valor_vendas, cadeiras_reservadas, valor_reservas, cadeiras_livres, valor_nao_recebido
    if teatro[linha][coluna] == 'Vendido':
        teatro[linha][coluna] = 'Livre'
        cadeiras_vendidas -= 1
        cadeiras_livres += 1
        valor_vendas -= valor_ingresso_total
        print("Lugar liberado com sucesso!")
    elif teatro[linha][coluna] == 'Reservado':
        teatro[linha][coluna] = 'Livre'
        cadeiras_reservadas -= 1
        cadeiras_livres += 1
        valor_reservas -= valor_ingresso_total * 0.3
        print("Lugar liberado com sucesso! (era uma reserva)")
    else:
        print("Este lugar já está livre.")

def listar_poltronas():
    print("Estado das poltronas:")
    for linha in range(total_linhas):
        for coluna in range(total_colunas):
            print(f'Linha {linha+1}, Coluna {coluna+1}: {teatro[linha][coluna]}')

def encerrar_espetaculo():
    global cadeiras_vendidas, valor_vendas, cadeiras_reservadas, valor_reservas, cadeiras_livres, valor_nao_recebido
    ocupacao_total = cadeiras_vendidas + cadeiras_reservadas + cadeiras_livres
    if cadeiras_vendidas >= ocupacao_total * 0.6 + 1:
        print("Espetáculo encerrado!")
        print("Total de cadeiras vendidas:", cadeiras_vendidas)
        print("Total de vendas: R$", valor_vendas)
        print("Total de cadeiras reservadas:", cadeiras_reservadas)
        print("Total de reservas: R$", valor_reservas)
        print("Total de cadeiras livres:", cadeiras_livres)
        print("Total não recebido: R$", valor_nao_recebido)
        print("Total do Espetáculo em R$:", valor_vendas + valor_reservas)
        reiniciar_espetaculo()
    else:
        print("Não é possível encerrar o espetáculo. A ocupação mínima não foi atingida.")

def reiniciar_espetaculo():
    global total_linhas, total_colunas, valor_ingresso_total, cadeiras_vendidas, valor_vendas, cadeiras_reservadas, valor_reservas, cadeiras_livres, valor_nao_recebido, teatro
    total_linhas = 0
    total_colunas = 0
    valor_ingresso_total = 0
    cadeiras_vendidas = 0
    valor_vendas = 0
    cadeiras_reservadas = 0
    valor_reservas = 0
    cadeiras_livres = 0
    valor_nao_recebido = 0
    teatro = []

def executar_programa():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            if total_linhas == 0 and total_colunas == 0:
                linhas = int(input("Digite o número de linhas do teatro: "))
                colunas = int(input("Digite o número de colunas do teatro: "))
                valor_ingresso_total = float(input("Digite o valor total do ingresso: "))
                criar_teatro(linhas, colunas)
                print("Teatro criado com sucesso!")
            else:
                print("Já existe um espetáculo em andamento.")
        
        elif opcao == '2':
            if total_linhas == 0 or total_colunas == 0:
                print("Não há um teatro em funcionamento.")
            else:
                linha = int(input("Digite a linha desejada: ")) - 1
                coluna = int(input("Digite a coluna desejada: ")) - 1
                if lugar_valido(linha, coluna):
                    reservar_lugar(linha, coluna)
                else:
                    print("Lugar inválido.")
        
        elif opcao == '3':
            if total_linhas == 0 or total_colunas == 0:
                print("Não há um teatro em funcionamento.")
            else:
                linha = int(input("Digite a linha desejada: ")) - 1
                coluna = int(input("Digite a coluna desejada: ")) - 1
                if lugar_valido(linha, coluna):
                    comprar_lugar(linha, coluna)
                else:
                    print("Lugar inválido.")
        
        elif opcao == '4':
            if total_linhas == 0 or total_colunas == 0:
                print("Não há um teatro em funcionamento.")
            else:
                linha = int(input("Digite a linha desejada: ")) - 1
                coluna = int(input("Digite a coluna desejada: ")) - 1
                if lugar_valido(linha, coluna):
                    liberar_lugar(linha, coluna)
                else:
                    print("Lugar inválido.")
        
        elif opcao == '5':
            if total_linhas == 0 or total_colunas == 0:
                print("Não há um teatro em funcionamento.")
            else:
                listar_poltronas()
        
        elif opcao == '6':
            encerrar_espetaculo()
        
        elif opcao == '7':
            reiniciar_espetaculo()
        
        else:
            print("Opção inválida. Por favor, digite novamente.")