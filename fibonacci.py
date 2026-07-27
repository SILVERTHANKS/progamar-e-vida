#contagem de numeros fibonacci
print('Contagem de numeros fibonacci'.center(50, '-'))
n = int(input('Digite seu numéro :'))# Digite um numéro com int -input de entrada do ususario!
t1=0 #começa com 0!
t2=1# acresenta 1!
print(f'→ {t1} → {t2}',end = ' ')#print
while n > 0: #uso do laço while ate a condicão se atendida !
    n -= 1
    t3 = t1 +t2
    print(f'→ {t3} →',end=' ')
    t1 = t2 #O segundo número passa a ser o primeiro.
    t2 = t3 #O número recém-calculado passa  a ser o segundo.
print('fim')    
