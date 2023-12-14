from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.animation import *

#Janela do Jogo:
janela = Window(1080,720)
start = 0
onda = 1

#Teclado
tecla = janela.get_keyboard()

#Mouse
click = janela.get_mouse()

#Fundo
background = GameImage("Game Assets/Background/background2.png")
background_game_over = GameImage("Game Assets/Background/game_over.png")
background_vitoria = GameImage("Game Assets/Background/vitoria.png")

#Player
player = Sprite("Game Assets/Characters/Iddle Right/player1.png")
player_hitbox = Sprite("Game Assets/Characters/player_hitbox.png")
index_animacao = 0
player_direction = 1
player_running = False
player_attacking = False
atacou = False
cronometro_ataque = 0
cronometro_dash = 2
player_dash = False
player_invuneravel = False
player_invuneravel_cronometro = 0
pulou = False
gravity = 800
gravity_bkup = 800

#Frames de Animação do Player:

#Frames Iddle:
framesp1 = [pygame.image.load("Game Assets/Characters/Iddle Right/player1.png").convert_alpha(), pygame.image.load("Game Assets/Characters/Iddle Right/player2.png"), pygame.image.load("Game Assets/Characters/Iddle Right/player3.png"),pygame.image.load("Game Assets/Characters/Iddle Right/player4.png"),pygame.image.load("Game Assets/Characters/Iddle Right/player5.png"),pygame.image.load("Game Assets/Characters/Iddle Right/player6.png"),pygame.image.load("Game Assets/Characters/Iddle Right/player7.png")]
framesp2 = [pygame.image.load("Game Assets/Characters/Iddle Left/player1.png").convert_alpha(), pygame.image.load("Game Assets/Characters/Iddle Left/player2.png"), pygame.image.load("Game Assets/Characters/Iddle Left/player3.png"),pygame.image.load("Game Assets/Characters/Iddle Left/player4.png"),pygame.image.load("Game Assets/Characters/Iddle Left/player5.png"),pygame.image.load("Game Assets/Characters/Iddle Left/player6.png"),pygame.image.load("Game Assets/Characters/Iddle Left/player7.png")]

#Frames Correndo:
framespr1 = [pygame.image.load("Game Assets/Characters/Run Right/player1.png").convert_alpha(),pygame.image.load("Game Assets/Characters/Run Right/player2.png"),pygame.image.load("Game Assets/Characters/Run Right/player3.png"),pygame.image.load("Game Assets/Characters/Run Right/player4.png"),pygame.image.load("Game Assets/Characters/Run Right/player5.png"),pygame.image.load("Game Assets/Characters/Run Right/player6.png"),pygame.image.load("Game Assets/Characters/Run Right/player7.png"),pygame.image.load("Game Assets/Characters/Run Right/player8.png")]
framespr2 = [pygame.image.load("Game Assets/Characters/Run Left/player1.png").convert_alpha(),pygame.image.load("Game Assets/Characters/Run Left/player2.png"),pygame.image.load("Game Assets/Characters/Run Left/player3.png"),pygame.image.load("Game Assets/Characters/Run Left/player4.png"),pygame.image.load("Game Assets/Characters/Run Left/player5.png"),pygame.image.load("Game Assets/Characters/Run Left/player6.png"),pygame.image.load("Game Assets/Characters/Run Left/player7.png"),pygame.image.load("Game Assets/Characters/Run Left/player8.png")]

#Frames Atacando Padrão 1:
framespa1_1 = [pygame.image.load("Game Assets/Characters/Attack 1 Right/player1.png").convert_alpha(), pygame.image.load("Game Assets/Characters/Attack 1 Right/player2.png"), pygame.image.load("Game Assets/Characters/Attack 1 Right/player3.png"), pygame.image.load("Game Assets/Characters/Attack 1 Right/player4.png"), pygame.image.load("Game Assets/Characters/Attack 1 Right/player5.png"), pygame.image.load("Game Assets/Characters/Attack 1 Right/player6.png"),pygame.image.load("Game Assets/Characters/Attack 1 Right/player7.png")]
framespa1_2 = [pygame.image.load("Game Assets/Characters/Attack 1 Left/player1.png").convert_alpha(), pygame.image.load("Game Assets/Characters/Attack 1 Left/player2.png"), pygame.image.load("Game Assets/Characters/Attack 1 Left/player3.png"), pygame.image.load("Game Assets/Characters/Attack 1 Left/player4.png"), pygame.image.load("Game Assets/Characters/Attack 1 Left/player5.png"), pygame.image.load("Game Assets/Characters/Attack 1 Left/player6.png"),pygame.image.load("Game Assets/Characters/Attack 1 Left/player7.png")]

#Frames Atacando Padrão 2:
framespa2_1 = [pygame.image.load("Game Assets/Characters/Attack 2 Right/player1.png").convert_alpha(), pygame.image.load("Game Assets/Characters/Attack 2 Right/player2.png"), pygame.image.load("Game Assets/Characters/Attack 2 Right/player3.png"), pygame.image.load("Game Assets/Characters/Attack 2 Right/player4.png"), pygame.image.load("Game Assets/Characters/Attack 2 Right/player5.png"), pygame.image.load("Game Assets/Characters/Attack 2 Right/player6.png"),pygame.image.load("Game Assets/Characters/Attack 2 Right/player7.png")]
framespa2_2 = [pygame.image.load("Game Assets/Characters/Attack 2 Left/player1.png").convert_alpha(), pygame.image.load("Game Assets/Characters/Attack 2 Left/player2.png"), pygame.image.load("Game Assets/Characters/Attack 2 Left/player3.png"), pygame.image.load("Game Assets/Characters/Attack 2 Left/player4.png"), pygame.image.load("Game Assets/Characters/Attack 2 Left/player5.png"), pygame.image.load("Game Assets/Characters/Attack 2 Left/player6.png"),pygame.image.load("Game Assets/Characters/Attack 2 Left/player7.png")]

#Status Player:
healthbar = Sprite("Game Assets/Icones/health40.png")
vida_player = 40
dano_player = 15