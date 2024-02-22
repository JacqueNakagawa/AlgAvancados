# SABE-SE QUE O NÚMERO 6 É UM NÚMERO PERFEITO, EXIBA OS OUTROS PERFEITOS QUE EXISTEM ENTRE 1 E O NÚMERO INFORMADO PELO USUÁRIO.
# Número perfeito: seus divisores naturais exceto ele somados são iguais ao seu valor. 6 é divisível por 1, 2, 3 que somados resultam em 6.

limite = int(input("Digite um número para encontrar os números perfeitos até esse valor: "))

numeros_perfeitos = []
for num in range(1, limite + 1):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        numeros_perfeitos.append(num)

print("Números perfeitos até", limite, ":")
for numero in numeros_perfeitos:
    print(numero)