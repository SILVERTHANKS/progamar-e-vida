from time import sleep
energia = 5
passos = 0
while energia > 0:
    sleep(1)
    energia -= 1
    passos += 1
    print('energia',energia)
    print('passos',passos)
