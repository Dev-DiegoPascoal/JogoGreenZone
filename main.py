
import pygame
from random import randint

#Inicialize o mixer Pygame
pygame.mixer.init()

pygame.init()
relogio = pygame.time.Clock()

#Define o tamanho da Tela
tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("Green Zone")
dt = 0

#Carrega o áudio do jogo
musicaFundo = pygame.mixer.Sound("assets/Musicas/CidadeDeserta.mp3")

#Carrega a fonte a ser usada no jogo
fonteTempo = pygame.font.Font("assets/Fontes/BAD GRUNGE.ttf", 80)

#Carrega a fonte a ser na pontuação e na quantidade de obstáculos destruídos
fonteObstaculosPontos = pygame.font.Font("assets/Fontes/BAD GRUNGE.ttf", 40)

#Carrega a fonte a ser na pontuação e na quantidade de obstáculos destruídos
fonteGameOver = pygame.font.Font("assets/Fontes/GAME OVER.ttf", 150)

#Carrega a spritesheet para nosso projeto.
folhaSpritesAndandoDeCarro = pygame.image.load("assets/Golfista/AndandoDeCarro.png").convert_alpha()
folhaSpritesAtack = pygame.image.load("assets/Golfista/Atack.png").convert_alpha()
folhaSpritesCarroVazioParado = pygame.image.load("assets/Golfista/CarroVazioParado.png").convert_alpha()
folhaSpritesAndando = pygame.image.load("assets/Golfista/Andando.png").convert_alpha()
folhaSpritesDescendoVeiculo = pygame.image.load("assets/Golfista/DescendoVeiculo.png").convert_alpha()
folhaSpritesParado = pygame.image.load("assets/Golfista/Parado.png").convert_alpha()
folhaSpritesMorrendo = pygame.image.load("assets/Golfista/Morrendo.png").convert_alpha()
folhaSpritesMorrendoNoVeiculo = pygame.image.load("assets/Golfista/MorrendoNoVeiculo.png").convert_alpha()
folhaSpritesParadoNoCarro = pygame.image.load("assets/Golfista/ParadoNoCarro.png").convert_alpha()
folhaSpritesSofrendoDano = pygame.image.load("assets/Golfista/SofrendoDano.png").convert_alpha()
folhaSpritesSofrendoDanoCarro = pygame.image.load("assets/Golfista/SofrendoDanoCarro.png").convert_alpha()

#Folhas Sprites TANCK GUERRA
folhaSpritesTanckAndando = pygame.image.load("assets/TanckGuerraVerde/Andando.png").convert_alpha()
folhaSpritesTanckAndando2 = pygame.image.load("assets/TanckGuerraVerde/Andando2.png").convert_alpha()
folhaSpritesTanckAtackVoador = pygame.image.load("assets/TanckGuerraVerde/AtackVoador.png").convert_alpha()
folhaSpritesTanckAtacando = pygame.image.load("assets/TanckGuerraVerde/Atacando.png").convert_alpha()
folhaSpritesTanckBomba = pygame.image.load("assets/TanckGuerraVerde/Bomba.png").convert_alpha()
folhaSpritesTanckDano = pygame.image.load("assets/TanckGuerraVerde/Dano.png").convert_alpha()
folhaSpritesTanckMorte = pygame.image.load("assets/TanckGuerraVerde/Morte.png").convert_alpha()

#Define os frames
listFramesAndando = []
listFramesAndandoCarro = []
listFramesCarroVazioParado = []
listFramesDescendoVeiculo = []
listFramesAtack = []
listFramesMorrendo = []
listFramesMorrendoCarro = []
listFramesParado = []
listFramesParadoCarro = []
listFramesSofrendoDano = []
listFramesSofrendoDanoCarro = []

#Define os frames do Personagem Tanck
listFramesTanckAndando = []
listFramesTanckAndando2 = []
listFramesTanckAtackVoador = []
listFramesTanckAtacando = []
listFramesTanckBomba = []
listFramesTanckDano = []
listFramesTanckMorte = []

#Cria os frames do personagem na lista de listFramesParado
for i in range(1):
    #Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frame = folhaSpritesParado.subsurface(i * 72, 0, 72, 72)

    #Redimensiona o frame para 2 vezes o tamanho original
    frame = pygame.transform.scale2x(frame)

    #Adiciona o frame na lista de listFramesIdle
    listFramesParado.append(frame)

for i in range(3):
    frame = folhaSpritesAndando.subsurface(i * 70, 0, 70, 70)
    frame = pygame.transform.scale(frame, (141, 141))
    listFramesAndando.append(frame)

for i in range(4):
    frame = folhaSpritesAndandoDeCarro.subsurface(i * 70, 0, 70, 70)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesAndandoCarro.append(frame)

for i in range(6):
    frame = folhaSpritesAtack.subsurface(i * 70, 0, 70, 70)
    frame = pygame.transform.scale(frame, (141, 141))
    listFramesAtack.append(frame)

for i in range(4):
    frame = folhaSpritesCarroVazioParado.subsurface(i * 70, 0, 70, 70)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesCarroVazioParado.append(frame)

for i in range(6):
    frame = folhaSpritesDescendoVeiculo.subsurface(i * 70, 0, 70, 70)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesDescendoVeiculo.append(frame)

for i in range(4):
    frame = folhaSpritesMorrendo.subsurface(i * 70, 0, 70, 70)
    frame = pygame.transform.scale(frame, (135, 135))
    listFramesMorrendo.append(frame)

for i in range(6):
    frame = folhaSpritesMorrendoNoVeiculo.subsurface(i * 60, 0, 60, 60)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesMorrendoCarro.append(frame)

for i in range(2):
    frame = folhaSpritesSofrendoDano.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesSofrendoDano.append(frame)

for i in range(2):
    frame = folhaSpritesSofrendoDanoCarro.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesSofrendoDanoCarro.append(frame)

# Range do Tanque de Guerra
for i in range(4):
    frame = folhaSpritesTanckAndando.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (190, 190))
    listFramesTanckAndando.append(frame)

for i in range(6):
    frame = folhaSpritesTanckAndando2.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesTanckAndando2.append(frame)

for i in range(8):
    frame = folhaSpritesTanckAtacando.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesTanckAtacando.append(frame)

for i in range(6):
    frame = folhaSpritesTanckAtackVoador.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesTanckAtackVoador.append(frame)

for i in range(1):
    frame = folhaSpritesTanckBomba.subsurface(i * 5, 0, 5, 5)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesTanckBomba.append(frame)

for i in range(2):
    frame = folhaSpritesTanckDano.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesTanckDano.append(frame)

for i in range(6):
    frame = folhaSpritesTanckMorte.subsurface(i * 72, 0, 72, 72)
    frame = pygame.transform.scale(frame, (150, 150))
    listFramesTanckMorte.append(frame)

# Variaveis da animação do personagem parado
indexFrameParado = 0 # Controla qual imagem está sendo mostrada na tela
tempoAnimacaoParado = 0.0 # Controla quanto tempo se passou desde a última troca de frame
velocidadeAnimacaoParado = 5 # Controlar o tempo de animação em relação ao tempo real (1 / velocidadeAnimacaoIdle)

# Variaveis da animação do personagem andando
indexFrameAndando = 0
tempoAnimacaoAndando = 0.0
velocidadeAnimacaoAndando = 5

# Variaveis da animação do personagem andando de carro
indexFrameAndandoDeCarro = 0
tempoAnimacaoAndandoDeCarro = 0.0
velocidadeAnimacaoAndandoDeCarro = 5

# Variaveis da animação do personagem Atakando
indexFrameAtack = 0
tempoAnimacaoAtack = 0.0
velocidadeAnimacaoAtack = 5
# Variaveis da animação do carro parado
indexFrameCarroVazioParado = 0
tempoAnimacaoCarroVazioParado = 0.0
velocidadeAnimacaoCarroVazioParado = 3

# Variaveis da animação do personagem descendo do carro
indexFrameDescendoVeiculo = 0
tempoAnimacaoDescendoVeiculo = 0.0
velocidadeAnimacaoDescendoVeiculo = 3

# Variaveis da animação do personagem morrendo
indexFrameMorrendo = 0
tempoAnimacaoMorrendo = 0.0
velocidadeAnimacaoMorrendo = 3

# Variaveis da animação do personagem morrendo no veículo
indexFrameMorrendoNoVeiculo = 0
tempoAnimacaoMorrendoNoVeiculo = 0.0
velocidadeAnimacaoMorrendoNoVeiculo = 3

# Variaveis da animação do personagem morrendo no veículo
indexFrameSofrendoDano = 0
tempoAnimacaoSofrendoDano = 0.0
velocidadeAnimacaoSofrendoDano = 3

# Variaveis da animação do personagem morrendo no veículo
indexFrameSofrendoDanoCarro = 0
tempoAnimacaoSofrendoDanoCarro = 0.0
velocidadeAnimacaoSofrendoDanoCarro = 3

## Variáveis da animação dos Personagem TANK DE GUERRA
# Variaveis da animação do Tanck Andando
indexFrameSTanckAndando = 0
tempoAnimacaoTanckAndando = 0.0
velocidadeAnimacaoTanckAndando= 3

# Variaveis da animação do Tanck Andando2
indexFrameSTanckAndando2 = 0
tempoAnimacaoTanckAndando2 = 0.0
velocidadeAnimacaoTanckAndando2= 3

# Variaveis da animação do Tanck Andando2
indexFrameSTanckAndando2 = 0
tempoAnimacaoTanckAndando2 = 0.0
velocidadeAnimacaoTanckAndando2= 3

# Variaveis da animação do Tanck Atacando
indexFrameSTanckAtacando = 0
tempoAnimacaoTanckAtacando = 0.0
velocidadeAnimacaoTanckAtacando= 3

# Variaveis da animação do Tanck Voando
indexFrameSTanckAtackVoador = 0
tempoAnimacaoTanckAtackVoador = 0.0
velocidadeAnimacaoTanckAtackVoador= 3

# Variaveis da animação da Bomba
indexFrameSTanckBomba = 0
tempoAnimacaoTanckBomba = 0.0
velocidadeAnimacaoTanckBomba= 3

# Variaveis da animação do Tanck Sofrendo Dano
indexFrameSTanckDano = 0
tempoAnimacaoTanckDano = 0.0
velocidadeAnimacaoTanckDano = 3

# Variaveis da animação do Tanck Morrendo
indexFrameSTanckMorte = 0
tempoAnimacaoTanckMorte = 0.0
velocidadeAnimacaoTanckMorte= 3

#Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagemRect = listFramesParado[0].get_rect(midbottom=(250, 480))
personagemColisaoRect = pygame.Rect(personagemRect.x, personagemRect.y, 80, 120)

gravidade = 1 # Gravidade do jogo, valor que aumenta a cada frame
direcaoPersonagem = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)
estaAndando = False # Define se o personagem está andando ou não

#ASSETS PARA OS OBSTÁCULOS
listaImagensObstaculos = [
    pygame.image.load(f"assets/Obstaculos/Icon28_{i:02d}.png").convert_alpha() for i in range(1, 16)
]

listaImagensTanckGuerraAndando = [
    pygame.image.load(f"assets/TanckGuerraVerde/{nome}.png").convert_alpha()
    for nome in [
        "Andando", "Andando2"
    ]
]

for i in range(len(listaImagensTanckGuerraAndando)):
    listaImagensTanckGuerraAndando[i] = pygame.transform.flip(listaImagensTanckGuerraAndando[i], True, False)
    # listaImagensTanckGuerraAndando[i] = pygame.transform.scale(listaImagensTanckGuerraAndando[i], (144, 144))

# Loop que redimensiona as imagens dos obstáculos
for i in range(len(listaImagensObstaculos)):
    # Redimensiona a imagem para 50x50 pixels
    listaImagensObstaculos[i] = pygame.transform.scale(listaImagensObstaculos[i], (50, 50))
    # Inverte a imagem no eixo X
    listaImagensObstaculos[i] = pygame.transform.flip(listaImagensObstaculos[i], True, False)
    # Rotaciona a imagem em 35 graus
    listaImagensObstaculos[i] = pygame.transform.rotate(listaImagensObstaculos[i], 35)

# ICONES de vida
iconeVida = pygame.image.load("assets/Icons/Icon29.png").convert_alpha()
iconeVida = pygame.transform.scale2x(iconeVida)

# ASSETS PARA O PLANO DE FUNDO
# Importa as imagens do plano de fundo
listBgImages = [
    pygame.image.load("assets/Cenario/9.png").convert_alpha(),
    pygame.image.load("assets/Cenario/8.png").convert_alpha(),
    pygame.image.load("assets/Cenario/7.png").convert_alpha(),
    pygame.image.load("assets/Cenario/6.png").convert_alpha(),
    pygame.image.load("assets/Cenario/5.png").convert_alpha(),
    pygame.image.load("assets/Cenario/4.png").convert_alpha(),
    pygame.image.load("assets/Cenario/3.png").convert_alpha(),  
    pygame.image.load("assets/Cenario/2.png").convert_alpha(),
    pygame.image.load("assets/Cenario/1.png").convert_alpha(),
]

listaBgVelocidades = [1, 3, 7, 9, 10, 15, 20, 23, 26] # Velocidades de cada imagem do plano de fundo

listaBgPosicoes = [0 for _ in range(len(listBgImages))] # Posições de cada imagem do plano de fundo

# Loop que redimensiona as imagens do plano de fundo
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanhoTela)

ALTURA_CHAO = 535
velocidadePersonagem = 30
vidas = 3
GameOver = False
tempoJogo = 0
pontuacaoJogo = 0
obstaculoDestruido = 0
tempo_acumulado = 0 
intervalo_tempo = 5  
DURACAO_FRAME_ATAQUE = 0.1
apareceuChefao = False

listaObstaculos = [] # Lista de obstáculos que aparecerão na tela

AUMENTA_DIFICULDADE = pygame.USEREVENT + 1 # Evento para aumentar a dificuldade do jogo
pygame.time.set_timer(AUMENTA_DIFICULDADE, 10000) # Aumenta a dificuldade a cada 10 segundos

tempoMaximoEntreObstaculos = 3000
ADICIONA_OBSTACULO = pygame.USEREVENT + 2 # Evento para adicionar um obstáculo na tela
pygame.time.set_timer(ADICIONA_OBSTACULO, randint(500, tempoMaximoEntreObstaculos)) # Adiciona um obstáculo a cada 1 segundo

listaChefao = []

ADICIONA_CHEFAO = pygame.USEREVENT + 1 
pygame.time.set_timer(ADICIONA_CHEFAO, 10000)  

# Função para adicionar o chefão
def adiciona_chefao():
    global apareceuChefao
    if not apareceuChefao:
        # Posição inicial do chefão
        chefaoRect = listaImagensTanckGuerraAndando[0].get_rect(midbottom=(1280, 500))  # Posição inicial

        chefao = {
            "rect": chefaoRect,
            "imagens": listaImagensTanckGuerraAndando,  # Lista de imagens para animação
            "vida": 100,  
            "estado": 0,  # Indice para controlar o estado da animação (ex: "Andando", "Atacando", etc.)
            "tempo_animacao": 0  # Tempo acumulado para controlar a animação
        }

        listaChefao.append(chefao)  # Adiciona o chefão à lista
        apareceuChefao = True
        print("Chefão apareceu!")

    # No loop principal, vamos desenhar o chefão com animação
tempo_por_frame = 300 # O tempo entre cada troca de frame (em milissegundos)

#Toca o som do jogo
pygame.mixer.music.load("assets/Musicas/CidadeDeserta.mp3") 
pygame.mixer.music.play(-1) 

while True:
    # Loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop() 
            pygame.quit()
            exit()

        # Aumenta a dificuldade
        if event.type == AUMENTA_DIFICULDADE:
            velocidadePersonagem += 4
            if tempoMaximoEntreObstaculos > 1100:
                tempoMaximoEntreObstaculos -= 300
            pygame.time.set_timer(ADICIONA_OBSTACULO, randint(800, tempoMaximoEntreObstaculos))

        # Adiciona obstáculos
        if event.type == ADICIONA_OBSTACULO:
            obstaculoImage = listaImagensObstaculos[randint(0, len(listaImagensObstaculos) - 1)]
            posicaoX = randint(1280, 1500)
            obstaculoRect = obstaculoImage.get_rect(midbottom=(posicaoX, 620))
            obstaculo = {
                "rect": obstaculoRect,
                "image": obstaculoImage
            }
            listaObstaculos.append(obstaculo)

        # Adiciona o chefão
        if event.type == ADICIONA_CHEFAO:
            if apareceuChefao == False:
                # Adiciona o chefão (apenas uma vez por evento)
                adiciona_chefao()  # Chama a função para adicionar o chefão

        # Atualizar obstáculos na tela
        for obstaculo in listaObstaculos[:]:  # Usando uma cópia da lista para evitar problemas ao remover itens
            # Movimento dos obstáculos
            obstaculo["rect"].x -= 5  # Ajuste a velocidade de movimento dos obstáculos

            # Verifica colisão ou outros comportamentos, como remoção de obstáculos fora da tela
            if obstaculo["rect"].x < 0:
                listaObstaculos.remove(obstaculo)

            # Desenha os obstáculos
            tela.blit(obstaculo["image"], obstaculo["rect"])

            # Verifica o ataque
            listTeclas = pygame.key.get_pressed()
            if listTeclas[pygame.K_a] and not atacando:
                atacando = True
                indexFrameAtack = 0
                tempoAnimacaoAtack = 0.0

                # Atualiza a animação de ataque
                if atacando:
                    tempoAnimacaoAtack += dt
                    if tempoAnimacaoAtack >= DURACAO_FRAME_ATAQUE:
                        indexFrameAtack += 1
                        tempoAnimacaoAtack = 0.0
                        if indexFrameAtack >= len(listFramesAtack):
                            indexFrameAtack = 0
                            atacando = False

        # Definir a área de alcance do ataque
        alcanceAtaque = pygame.Rect(personagemRect.centerx, personagemRect.centery - 20, 100, 50)  # Ajuste o alcance conforme necessário

        # Verifica a colisão entre o ataque e os obstáculos
        for obstaculo in listaObstaculos[:]:  # Usa uma cópia da lista para evitar problemas ao remover itens
            if alcanceAtaque.colliderect(obstaculo["rect"]):  # Verifica a colisão
                listaObstaculos.remove(obstaculo)  # Remove o obstáculo se colidir
                pontuacaoJogo += 50
                obstaculoDestruido += 1  

    tela.fill((255, 255, 255))  # Preenche a tela com a cor branca

    # Verifica se o jogador perdeu todas as vidas
    if vidas <= 0:
        GameOver = True

    # Percorre todas as imagens do plano de fundo para movimentar
    for i in range(len(listBgImages)):
        if estaAndando:
            listaBgPosicoes[i] -= listaBgVelocidades[i] * velocidadePersonagem * dt * direcaoPersonagem # Move a imagem para a esquerda

        # Verifica se a imagem saiu da tela para a esquerda
        if listaBgPosicoes[i] <= -tamanhoTela[0]:
            listaBgPosicoes[i] = 0 # Retorna a imagem para a posição inicial

        # Verifica se a imagem saiu da tela para a direita
        if listaBgPosicoes[i] >= tamanhoTela[0]:
            listaBgPosicoes[i] = 0

    # Desenha o plano de fundo
    for i in range(len(listBgImages)):
        # Desenha a imagem do plano de fundo que está na tela
        tela.blit(listBgImages[i], (listaBgPosicoes[i], 0))

        # Desenha a imagem do plano de fundo que está fora da tela na direita
        tela.blit(listBgImages[i], (listaBgPosicoes[i] + tamanhoTela[0], 0))

        # Desenha a imagem do plano de fundo que está fora da tela na esquerda
        tela.blit(listBgImages[i], (listaBgPosicoes[i] + -tamanhoTela[0], 0))
    
    if not GameOver:
        tempoJogo += dt
        tempo_acumulado += dt  # Acumula o tempo decorrido

    # Atualiza a pontuação se o intervalo for alcançado
    if tempo_acumulado >= intervalo_tempo:
        pontuacaoJogo += 20  # Adiciona 20 pontos, por exemplo
        tempo_acumulado = 0  # Reinicia o acumulador para o próximo intervalo

    # Cria o texto para o tempo de jogo
    textoTempo = fonteTempo.render(str(int(tempoJogo)), False, (255, 255, 255))

    # Cria o texto para a Pontuação com uma mensagem
    textoPontuacao = fonteObstaculosPontos.render(f"Pontos: {int(pontuacaoJogo)}", False, (255, 255, 255))

    # Cria o texto para a Pontuação com uma mensagem
    textoObstaculoDestruido = fonteObstaculosPontos.render(f"Obstaculos: {int(obstaculoDestruido)}", False, (255, 255, 255))

    # Desenha o tempo de jogo na tela
    tela.blit(textoTempo, (tamanhoTela[0] / 2, 30))

     # Desenha o tempo de jogo na tela
    tela.blit(textoPontuacao, (tamanhoTela[0] / 38, 85))

     # Desenha o tempo de jogo na tela
    tela.blit(textoObstaculoDestruido, (tamanhoTela[0] / 38, 120))

     # Cria o texto para as vidas do jogador
    for i in range(vidas):
        tela.blit(iconeVida, (20 + i * iconeVida.get_width(), 20))

    # DESENHA O MENU DE REINICIAR O JOGO
    if GameOver:
        # Cria o texto para o menu de reiniciar o jogo
        textoGameOver = fonteGameOver.render("GAME OVER", False, (255, 255, 255))
        textoReiniciar = fonteGameOver.render("Tecle ENTER para recomeçar", False, (255, 255, 255))
       
        # Desenha o menu de reiniciar o jogo na tela
        tela.blit(textoGameOver, (484, 260))
        tela.blit(textoReiniciar, (270, 360))

     # DESENHA OS OBSTÁCULOS NA TELA
    for obstaculo in listaObstaculos:
        obstaculo["rect"].x -= 30 * velocidadePersonagem * dt

        # Verifica se o obstáculo saiu da tela
        if obstaculo["rect"].right < 0:
            listaObstaculos.remove(obstaculo)

        tela.blit(obstaculo["image"], obstaculo["rect"])

        # Verifica se houve colisão entre o personagem e o obstáculo
        if personagemColisaoRect.colliderect(obstaculo["rect"]):
            listaObstaculos.remove(obstaculo)
            vidas -= 1

    # Soma o tempo que se passou desde o último frame
    tempoAnimacaoParado += dt

     # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoParado >= 1 / velocidadeAnimacaoParado:
        # Atualiza o frame do personagem parado de acordo com a lista de frames
        indexFrameParado = (indexFrameParado + 1) % len(listFramesParado)
        tempoAnimacaoParado = 0.0 # Reseta o tempo entre os frames

    # Atualiza a animação do personagem andando
    tempoAnimacaoAndando += dt

    # Verifica se o tempo de animação do personagem andando é maior ou igual ao tempo de animação
    if tempoAnimacaoAndando >= 1 / velocidadeAnimacaoAndando:
        # Atualiza o frame do personagem andando
        indexFrameAndando = (indexFrameAndando + 1) % len(listFramesAndando)
        tempoAnimacaoAndando = 0.0

    # Verifica se o tempo de animação do personagem andando é maior ou igual ao tempo de animação
    if tempoAnimacaoAtack >= 1 / velocidadeAnimacaoAtack:
        # Atualiza o frame do personagem andando
        indexFrameAtack = (indexFrameAtack +1) % len(listFramesAtack)
        tempoAnimacaoAtack = 0.0
        # Atualiza a animação do personagem andando
    tempoAnimacaoAtack += dt

    # Atualiza a animação do personagem morto
    if GameOver and indexFrameMorrendo != len(listFramesMorrendo) - 1:
        tempoAnimacaoMorrendo += dt
        
    # Verifica se o tempo de animação do personagem morto é maior ou igual ao tempo de animação
    if tempoAnimacaoMorrendo >= 1 / velocidadeAnimacaoMorrendo:
        # Atualiza o frame do personagem morto
        indexFrameMorrendo = (indexFrameMorrendo + 1) % len(listFramesMorrendo)
        tempoAnimacaoMorrendo = 0.0

    # Verifica se o personagem está andando ou atacando
    estaAndando = False
    atacando = False

    # Atualizar animação do chefão
    for chefao in listaChefao:
        # Atualiza o tempo de animação do chefão
        chefao["tempo_animacao"] += relogio.get_time()

        # Verifica se é hora de trocar de frame
        if chefao["tempo_animacao"] > tempo_por_frame:
            chefao["tempo_animacao"] = 0  # Reseta o tempo de animação
            chefao["estado"] += 1  # Vai para o próximo estado da animação

            # Se o índice do estado exceder o número de frames disponíveis, reinicia
            if chefao["estado"] >= len(chefao["imagens"]):
                chefao["estado"] = 0  # Reinicia a animação (volta para o primeiro frame)

        # Obtém a imagem atual com base no estado da animação
        imagem_atual = chefao["imagens"][chefao["estado"]]

        # Desenha o chefão na tela
        tela.blit(imagem_atual, chefao["rect"])

    # Função para realizar o ataque
    def atacar():
        global atacando
        atacando = True

    # Pega as teclas que foram pressionadas
    listTeclas = pygame.key.get_pressed()

    if not GameOver:
        if listTeclas[pygame.K_LEFT]: # Verifica se a tecla esquerda foi pressionada
            direcaoPersonagem = -1 # Define a direção do personagem para a esquerda
            estaAndando = True # Define que o personagem está andando

        if listTeclas[pygame.K_RIGHT]:
            direcaoPersonagem = 1
            estaAndando = True

         # Verifica se a tecla de ataque foi pressionada
        if listTeclas[pygame.K_a]:
            atacar()

        if listTeclas[pygame.K_SPACE]: # Verifica se a tecla espaço foi pressionada
            if personagemRect.centery == ALTURA_CHAO: # Verifica se o personagem está no chão
                gravidade = -30 # Define como negativo para o personagem subir
                indexFrameJump = 0 # Reseta o frame do pulo
    else:
        # Reinicia o jogo
        if listTeclas[pygame.K_RETURN]:
            vidas = 3
            GameOver = False
            tempoJogo = 0
            pontuacaoJogo = 0
            velocidadePersonagem = 30
            tempoMaximoEntreObstaculos = 3000
            listaObstaculos = []
            indexFrameDead = 0
            obstaculoDestruido = 0

    # Gravidade Aumenta
    gravidade += 2

    # Atualiza a posição Y do personagem de acordo com a gravidade
    personagemRect.y += gravidade

    # Verifica se o personagem está no chão
    if personagemRect.centery >= ALTURA_CHAO:
        personagemRect.centery = ALTURA_CHAO

    personagemColisaoRect.midbottom = personagemRect.midbottom
    
   # Desenha o personagem
    if not GameOver:
        if atacando:  # Verifica se o personagem está atacando
            frame = listFramesAtack[indexFrameAtack]
            velocidadeAnimacaoAndando = 1

        elif estaAndando:  # Verifica se o personagem está andando
            frame = listFramesAndando[indexFrameAndando]
            velocidadeAnimacaoAndando = 4
        else:  # O personagem está parado
            frame = listFramesParado[indexFrameParado]
    else:
        frame = listFramesMorrendo[indexFrameMorrendo]

    if direcaoPersonagem == -1: # Verifica se o personagem está olhando para a esquerda e inverte a imagem
        frame = pygame.transform.flip(frame, True, False) # Inverte a imagem

    tela.blit(frame, personagemRect) # Desenha o personagem na tela

    pygame.display.update() # Atualiza a tela

    dt = relogio.tick(60) / 1000 # Define o tempo de cada frame em segundos



