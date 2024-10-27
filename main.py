
import pygame

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

#Cria os frames do personagem na lista de listFramesParado
for i in range(4):
    #Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frame = folhaSpritesParado.subsurface(i * 128, 0, 128, 128)

    #Redimensiona o frame para 2 vezes o tamanho original
    frame = pygame.transform.scale2x(frame)

    #Adiciona o frame na lista de listFramesIdle
    listFramesParado.append(frame)

for i in range(4):
    frame = folhaSpritesAndando.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesAndando.append(frame)

for i in range(4):
    frame = folhaSpritesAndandoDeCarro.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesAndandoCarro.append(frame)

for i in range(6):
    frame = folhaSpritesAtack.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesAtack.append(frame)

for i in range(4):
    frame = folhaSpritesCarroVazioParado.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesParadoCarro.append(frame)

for i in range(6):
    frame = folhaSpritesDescendoVeiculo.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesDescendoVeiculo.append(frame)

for i in range(4):
    frame = folhaSpritesMorrendo.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesMorrendo.append(frame)

for i in range(6):
    frame = folhaSpritesMorrendoNoVeiculo.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesMorrendoCarro.append(frame)

for i in range(2):
    frame = folhaSpritesSofrendoDano.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesSofrendoDano.append(frame)

for i in range(2):
    frame = folhaSpritesSofrendoDanoCarro.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesSofrendoDanoCarro.append(frame)

# Variaveis da animação do personagem parado
indexFrameParado = 0 # Controla qual imagem está sendo mostrada na tela
tempoAnimacaoParado = 0.0 # Controla quanto tempo se passou desde a última troca de frame
velocidadeAnimacaoParado = 5 # Controlar o tempo de animação em relação ao tempo real (1 / velocidadeAnimacaoIdle)

# Variaveis da animação do personagem andando
indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

# Variaveis da animação do personagem pulando
indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJump = 5

# Variaveis da animação do personagem correndo
indexFrameRunn = 0
tempoAnimacaoRunn = 0.0
velocidadeAnimacaoRunn = 10

# Variaveis da animação do personagem morto
indexFrameDead = 0
tempoAnimacaoDead = 0.0
velocidadeAnimacaoDead = 3
