import hashlib
from getpass import getpass

SENHA_CORRETA = 'carlos0'
MAX_TENTATIVAS = 3


def autenticar():
    """Pede a senha até MAX_TENTATIVAS vezes. Retorna True se autenticou."""
    hash_senha = hashlib.md5(SENHA_CORRETA.encode()).hexdigest()

    for tentativa in range(MAX_TENTATIVAS):
        digitada = getpass('Digite sua senha aqui: ').strip().lower()
        hash_digitado = hashlib.md5(digitada.encode()).hexdigest()

        if hash_digitado == hash_senha:
            print('Senha liberada!')
            return True

        tentativas_restantes = MAX_TENTATIVAS - tentativa - 1
        if tentativas_restantes > 0:
            print(f'Senha incorreta. Você tem mais {tentativas_restantes} tentativa(s).')
        else:
            print('Você excedeu as 3 tentativas. Senha bloqueada.')

    return False


def ver_saldo(saldo):
    print(f'Seu saldo é de $ {saldo:.2f}')


def depositar(saldo):
    try:
        valor = float(input('Digite o valor para seu depósito $: '))
    except ValueError:
        print('Valor inválido.')
        return saldo

    if valor <= 0:
        print('O valor do depósito deve ser positivo.')
        return saldo

    saldo += valor
    print(f'Seu novo saldo é $ {saldo:.2f}')
    return saldo


def sacar(saldo):
    try:
        valor = float(input('Digite o valor a ser retirado $: '))
    except ValueError:
        print('Valor inválido.')
        return saldo

    if valor <= 0:
        print('O valor do saque deve ser positivo.')
    elif valor > saldo:
        print('Saldo insuficiente!')
    else:
        saldo -= valor
        print(f'Seu saldo é de $ {saldo:.2f}')

    return saldo


def menu(saldo):
    opcoes = {
        '1': 'Ver saldo',
        '2': 'Depósito',
        '3': 'Sacar dinheiro',
        '4': 'Sair',
    }

    while True:
        print('\nOpções (1 - 4)')
        for chave, texto in opcoes.items():
            print(f'opção {chave} - {texto}')

        escolha = input('Digite sua opção aqui: ').strip()

        if escolha == '1':
            ver_saldo(saldo)
        elif escolha == '2':
            saldo = depositar(saldo)
        elif escolha == '3':
            saldo = sacar(saldo)
        elif escolha == '4':
            print('Obrigado por usar o programa -> fim')
            break
        else:
            print('Opção inválida, escolha de 1 a 4.')


def caixa_eletronico():
    print('Bem vindo ao caixa eletrônico'.center(32, '-'))
    saldo_inicial = 1000.0

    if autenticar():
        menu(saldo_inicial)
    else:
        print('Acesso negado.')


if __name__ == '__main__':
    caixa_eletronico()