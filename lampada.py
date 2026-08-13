#estado da lampada
lampada = False
def ligar():
    global lampada
    lampada = True
def desligar():
    global lampada
    lampada = False

def condicao():
    if lampada :
        print('Lampada Ligada!')   

    else:
        print('Estado desligada!')     
condicao()
ligar()
condicao()
desligar()
condicao()
