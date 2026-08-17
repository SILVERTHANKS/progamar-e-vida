def verificar_media(n1, n2, n3):
    media =(n1+n2+n3)/3
    if media >= 7:
        return f'MEDIA :|{media:.2f} Aprovado'
    elif  media>= 5:
        return f'  MEDIA : {media:.2f} Recuperação'
    else:
        return f'MEDIA :| {media:.2f} Reprovado!'
resultado = verificar_media(1, 1, 7)   
print(f'Media calculada: {resultado}')
