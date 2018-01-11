print("Bem-Vindo ao Move Sonda")
print("-------=========------- \n")

# funcoes de movimento da sonda
def executaComandoX(comando, direction, x):

    if comando == 'M' and direction == 'E':

        x += 1

    elif comando == 'M' and direction == 'W':

        x -= 1

    #print("X: {}".format(x))
    return x

def executaComandoY(comando, direction, y):

    if comando == 'M' and direction == 'N':

        y += 1

    elif comando == 'M' and direction == 'S':

        y -= 1

    #print("Y: {}".format(y))
    return y

x = int(input("Digite a posicao inicial no eixo x: "))
y = int(input("Digite a posicao inicial no eixo y: "))
direction = input("Digite a direcao da sonda: ")
direction = direction.upper()

newX = x
newY = y

i = 1
while(i != 0):



    comando = input("Digite um comando para nave: ")
    comando = comando.upper()

    if comando == 'M':

        resultX = executaComandoX(comando, direction, newX)
        newX = resultX
        resultY = executaComandoY(comando, direction, newY)
        newY = resultY

    print("--X: {}, Y: {}--".format(resultX, resultY))

    i = int(input("Digite 0 para sair da tela de comandos ou qualquer tecla para continuar: "))
