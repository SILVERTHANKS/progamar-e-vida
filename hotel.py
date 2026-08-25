def hospedagem(diaria, dias):
    custo = diaria*dias
    valor_final = custo
    if custo >= 600:
        desconto = custo * 0.10
        valor_final = custo- desconto
        
        resposta ='Hospedagem cara'
    elif custo >=300:
        resposta ='Hospedagem media' 
    else:
        resposta ='Hospedagem barata'
    return custo, resposta,valor_final   
dados_clientes=[{
    'nome': 'carlos',
    'diaria': 150,
    'dias': 3
},
{   'nome': 'duda',
    'diaria': 80,
    'dias': 5

},
{   'nome': 'alicia',
    'diaria': 130,
    'dias': 2

},
{   'nome': 'Joao',
    'diaria': 200,
    'dias': 4

}]   
total = 0
for i in dados_clientes:
    contagem,resposta,valor_final= hospedagem(i['diaria'], i['dias'])
    total+= contagem
    print(f"Nome do Cliente: {i['nome']}")
    print(f"Valor da hospedagem: R$ {contagem:.2f}")
    print(resposta)

    if contagem >= 600:
        print(f"Desconto de 10% aplicado")
        print(f"Valor final: R$ {valor_final:.2f}")
    else:
        print(f"Valor final: R$ {valor_final:.2f}")
    
    
    
    
    
        