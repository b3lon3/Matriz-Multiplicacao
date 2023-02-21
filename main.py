#feito para botoes e camisas, mas input ta aberto, funf com qqr couisa

X = int(input("Numero de linhas da matriz botoes: "))
Y = int(input("Numero de colunas da matriz camisas:"))
Z = int(input("Numero de coluns da matriz botoes / Numero de linhas da matriz camisas:"))

print("Elementos em botoes:")
botoes = [[int(input()) for i in range(Y)] for j in range(X)]
print("Botoes:")
for i in range(X):
    for j in range(Y):
        print(format(botoes[i][j], "<3"), end = "")
    print()

print("Elementos em camisas:")
camisas = [[int(input()) for i in range(Y)] for j in range(X)]
print("Camisas:")
for i in range(X):
    for j in range(Y):
        print(format(camisas[i][j], "<3"), end = "")
    print()
total = [[0 for i in range(Y)] for j in range(X)]

for i in range(X):
    for j in range(Y):
        for k in range(Z):
            total[i][j] = botoes[i][j] + camisas[i][j]

print("Total de botoes:")
for i in range(X):
    print()
    for j in range(Y):
        print(format(total[i][j], "<3"), end = "")
    print()
