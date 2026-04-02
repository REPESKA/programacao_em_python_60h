import random
import pygame
import sys


pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")


trex1 = pygame.image.load("assets/trex1.png")
trex = pygame.image.load("assets/trex.png")
trex = pygame.image.load("assets/trex.png")
cacto1 = pygame.image.load("assets/cacto1.png")
poste1 = pygame.image.load("assets/poste1.png")


chao = pygame.image.load("assets/chao.png")


trex_x = 100
trex_y = 300

vel_y = 0
gravidade = 1
pulando = False

cacto1_x = 800
cacto1_y = 300

poste1_x = 800
poste1_y = 300

frame = 0
score = 0
font = pygame.font.SysFont("Arial", 30) 
trex = pygame.transform.scale(trex, (50, 50))
game_over = False


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

if event.type == pygame.KEYDOWN and game_over:
    if event.key == pygame.K_SPACE and not pulando:
        game_over = False
        score = 0
        cacto1_x = 800
        poste1_x = 800
        trex_y = 300
        vel_y = 0
        pulando = False
 