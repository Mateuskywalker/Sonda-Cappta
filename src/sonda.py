# Programa feito com Python 3.6

print("Bem-Vindo ao Move Sonda")
print("-------=========------- \n")

# funcoes de movimento da sonda

# move a sonda no eixo x
def executaComandoX(comando, direction, x):

    if comando == 'M' and direction == 'E':

        x += 1

    elif comando == 'M' and direction == 'W':

        x -= 1

    #print("X: {}".format(x))
    return x

# move a sonda no eixo y
def executaComandoY(comando, direction, y):

    if comando == 'M' and direction == 'N':

        y += 1

    elif comando == 'M' and direction == 'S':

        y -= 1

    #print("Y: {}".format(y))
    return y

# muda a direcao da sonda para 90 graus a direita
def mudaDirecaoR(comando, direction):

    if(comando == 'R' and direction == 'N'):

        direction = 'E'

    elif(comando == 'R' and direction == 'E'):

        direction = 'S'

    elif(comando == 'R' and direction == 'S'):

        direction = 'W'

    elif(comando == 'R' and direction == 'W'):

        direction = 'N'

    return direction

# muda a direcao da sonda para 90 graus a esquerda
def mudaDirecaoL(comando, direction):

    if(comando == 'L' and direction == 'N'):

        direction = 'W'

    elif(comando == 'L' and direction == 'W'):

        direction = 'S'

    elif(comando == 'L' and direction == 'S'):

        direction = 'E'

    elif(comando == 'L' and direction == 'E'):

        direction = 'N'

    return direction

# execucao das entradas de dados e das funcoes
x = int(input("Digite a posicao inicial no eixo x: "))
y = int(input("Digite a posicao inicial no eixo y: "))

direction = input("Digite a direcao da sonda: ")
direction = direction.upper()

j = 1
arrayComandos = []
while j != 0:

    comando = input("Digite os comandos para a sonda: ")
    comando = comando.upper()
    arrayComandos.append(comando) # adiciona todos os movimentos inseridos na lista 'arrayComandos'
    j = int(input("Digite 0 para sair da tela de comandos ou qualquer numero para continuar: "))

newX = x
newY = y
newDirection = direction

# verificacoes dos movimentos presentes na lista de movimentos da sonda
for movimento in arrayComandos:

    if movimento == 'M':

        resultX = executaComandoX(movimento, newDirection, newX)
        newX = resultX
        resultY = executaComandoY(movimento, newDirection, newY)
        newY = resultY

    if movimento == 'L':

        resultDirection = mudaDirecaoL(movimento, newDirection)
        newDirection = resultDirection

    if movimento == 'R':

        resultDirection = mudaDirecaoR(movimento, newDirection)
        newDirection = resultDirection

print("--X: {}, Y: {}, Direction: {} --".format(resultX, resultY, direction))
