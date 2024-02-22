# CRIE UM PROGRAMA EM PYTHON QUE RESOLVA A SÉRIE DE FIBONNACCI - Serie de Fibonnacci: 0, 1, 1, 2, 3, 5, 8 ...

n = int(input("Digite o número de termos da série de Fibonacci que você deseja calcular: "))

sequencia = [0, 1]
while len(sequencia) <= n:
    prox = sequencia[-1] + sequencia[-2]
    sequencia.append(prox)

resultado = sequencia[:n + 1]

print("A série de Fibonacci até o", n, "º termo é:")
print(resultado)