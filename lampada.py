#iniciar c/valor para demostra lampada apagada!
lampada = False
def desligada():
    global lampada
    print('Desligada!')

def ligada():
    global lampada
    lampada = True
    print('ligada!')   

def estado_da_lampada():
    if lampada:     
        print('estado ligado')
    else:
        print('Estado desligado')   
estado_da_lampada()         
desligada()
estado_da_lampada()
ligada()
estado_da_lampada()