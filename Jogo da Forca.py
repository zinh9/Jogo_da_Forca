import random

def jogo_forca(palavra_vazia, palavra_escolhida):
    print('Bem vindos ao JOGO DA FORCA!\nVamos começar :)')
    letra_usu = []
    i = 0
    
    while i < len(palavra_escolhida) + 3:
        letra = input('Digite uma letra: ')
        letra_usu.append(letra)
        
        if letra in palavra_escolhida:
            for j in range(len(palavra_escolhida)):
                if palavra_escolhida[j] == letra:
                    palavra_vazia[j] = letra
            
        i += 1
        
        print(f'A palavra é: {" ".join(palavra_vazia)}')
        print(f'Letras já usadas: {" ".join(letra_usu)}')

def preencher_(palavra_escolhida):
    palavra_vazia = ['_' if letra != ' ' else ' ' for letra in palavra_escolhida]
    return palavra_vazia

palavras = [
    "star wars", "harry potter", "the lord of the rings", "matrix", "the avengers", "jurassic park",
    "the legend of zelda", "final fantasy", "super mario", "call of duty", "mass effect", "galaxy",
    "interstellar", "black hole", "dark matter", "astronaut", "gravity", "star trek", "alien",
    "eclipse", "nebula", "cosmos", "supernova", "hubble", "andromeda", "galactic", "cyberpunk", "orion",
    "spacex"
]

palavra_escolhida = random.choice(palavras)
palavra_vazia = preencher_(palavra_escolhida)
jogo_forca(palavra_vazia, palavra_escolhida)
