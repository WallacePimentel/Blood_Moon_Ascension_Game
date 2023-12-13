from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from variaveis import *
from demon import *
from main import inic_jogo
from math import fabs
from ghost import *

janela.set_title("Blood Moon Ascension")
healthbar.set_position(janela.width - 230, 30)
player.set_position(janela.width / 2, janela.height - player.height - 24)
demon.set_position(janela.width + 100, janela.height - demon.height - 24)
ghost_spawn_left()
ghost_spawn_right()

while True:

    # ------DRAW-FUNDOS-E-ICONES------#
    background.draw()
    healthbar.draw()

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////#


    # ------MOVIMENTAÇÃO-PLAYER------#
    if ((tecla.key_pressed("left")) and not player_dash):
        player_running = True
        player_direction = -1
        start = 1
        v_player = 100 * player_direction
        player.x = player.x + v_player * janela.delta_time()
    elif ((tecla.key_pressed("right")) and not player_dash):
        player_running = True
        player_direction = 1
        start = 1
        v_player = 100 * player_direction
        player.x = player.x + v_player * janela.delta_time()
    else:
        player_running = False

    # ------ATAQUE-DO-PLAYER------#
    if (tecla.key_pressed("x") and cronometro_ataque == 0):
        if (player_direction == 1):
            player.x += 1000 * janela.delta_time()
        if (player_direction == -1):
            player.x -= 2500 * janela.delta_time()
        index_animacao = 0
        player_attacking = True
        atacou = True

    if (atacou):
        cronometro_ataque += janela.delta_time()
        if (cronometro_ataque > 0.7):
            if (player_direction == -1):
                player.x += 4.5
            player_attacking = False
            atacou = False
            cronometro_ataque = 0

    # ------PLAYER-DASH------#
    cronometro_dash += janela.delta_time()
    if (tecla.key_pressed("space") and (cronometro_dash >= 2) and player_running == True):
        cronometro_dash = 0
        player_dash = True

    if (player_dash and cronometro_dash < 0.2):
        if (player_direction == 1):
            player.x += 500 * janela.delta_time()
        if (player_direction == -1):
            player.x -= 500 * janela.delta_time()
    else:
        player_dash = False

    #------INVUNERABILIDADE-PÓS-DANO-DO-PLAYER------#
    if (player_invuneravel):
        player_invuneravel_cronometro += janela.delta_time()
        if (player_invuneravel_cronometro >= 2):
            player_invuneravel_cronometro = 0
            player_invuneravel = False


    # ------STATUS-ANIMAÇÃO-PLAYER------#

    if (player_direction == 1):
        if (player_running):
            frames_atual = framespr1
        elif (player_attacking):
            frames_atual = framespa2_1
        else:
            frames_atual = framesp1
    if (player_direction == -1):
        if (player_running):
            frames_atual = framespr2
        elif (player_attacking):
            frames_atual = framespa2_2
        else:
            frames_atual = framesp2

    # ------ANIMAÇÃO-PLAYER------#
    if (player_attacking):
        index_animacao += 0.019
    else:
        index_animacao += 0.01
    if index_animacao >= len(frames_atual):
        index_animacao = 0
    player.image = frames_atual[int(index_animacao)]
    player.draw()

    # ------ESTADO-VIDA-DO-PLAYER------#
    if (vida_player == 30):
        healthbar = Sprite("Game Assets/Icones/health30.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()
    if (vida_player == 20):
        healthbar = Sprite("Game Assets/Icones/health20.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()
    if (vida_player == 10):
        healthbar = Sprite("Game Assets/Icones/health10.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()
    if (vida_player == 0):
        healthbar = Sprite("Game Assets/Icones/health0.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #------ATAQUE-DEMONIO------#
    if (demon_direction == 1):
        if ((demon.x - player.x) <= 5) and (demon_cronometro == 0):
            demon_attacking = True
            demon_atacou = True

    if (demon_direction == -1):
        if (player.x - demon.x <= 5) and (demon_cronometro == 0):
            demon_attacking = True
            demon_atacou = True

    #------DURAÇÃO-DO-ATAQUE-DEMONIO------#
    if (demon_atacou):
        demon_cronometro += janela.delta_time()
        if (demon_cronometro > 0.7):
            demon_cronometro = 0
            demon_atacou = False
            demon_attacking = False

    #------STATUS-DEMONIO------#
    if (demon.x + demon.width / 2 >= player.x + player.width / 2):
        demon_direction = 1
        if (demon_attacking):
            frames_atual_d = demon_at1
        else:
            frames_atual_d = demon_w1
    if (demon.x + demon.width / 2 < player.x + player.width / 2):
        demon_direction = 1
        if (demon_attacking):
            frames_atual_d = demon_at2
        else:
            frames_atual_d = demon_w2

    # ------ANIMAÇÃO-DEMONIO------#
    if (demon_attacking):
        index_animacao_d += 0.019
    else:
        index_animacao_d += 0.01
    if index_animacao_d >= len(frames_atual_d):
        index_animacao_d = 0
    demon.image = frames_atual_d[int(index_animacao_d)]
    demon.draw()

    # ------MOVIMENTAÇÃO-DEMONIO------#
    if (start == 1):
        if (onda == 2):
            if (demon_attacking == False):
                if (demon.x + demon.width / 2 < player.x + player.width / 2):
                    demon.x = demon.x + v_demon * janela.delta_time()
                else:
                    demon.x = demon.x - v_demon * janela.delta_time()

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #------MOVIMENTAÇÃO-E-DESENHO-DOS-FANTASMAS------#
    ghost_draw()
    ghost_move_left()
    ghost_move_right()

    if (verificador_ghosts_mortos()):
        onda += 1
        lista_ghost_left = []
        lista_ghost_right = []
        vidas_ghost_left = []
        vidas_ghost_right = []
        lista_booleano_ghost_left = []
        lista_booleano_ghost_right = []
        lista_crono_ghost_left = []
        lista_ghost_right = []

    #------COLISÃO-GHOST-E-PLAYER------#
    for i in range(n):
        if (lista_ghost_left[i].x == player.x) and (not player_dash):
            if (player_attacking):
                vidas_ghost_left[i] -= dano_player
                lista_booleano_ghost_left[i] = True
            else:
                vida_player -= ghost_dano
                player_invuneravel = True
        if (lista_ghost_right[i].x == player.x) and (not player_dash):
            if (player_attacking):
                vidas_ghost_right[i] -= dano_player
                lista_booleano_ghost_right[i] = True
            else:
                if (not player_invuneravel):
                    vida_player -= ghost_dano
                    player_invuneravel = True

    #------TEMPO-DE-HIT-DO-FANTASMA------#
    for i in range(n):
        if lista_booleano_ghost_left[i] == True:
            lista_crono_ghost_left[i] += janela.delta_time()
            if lista_crono_ghost_left[i] > 1:
                lista_crono_ghost_left[i] = 0
        if lista_booleano_ghost_right[i] == True:
            lista_crono_ghost_right[i] += janela.delta_time()
            if lista_crono_ghost_right[i] > 1:
                lista_crono_ghost_right[i] = 0

    janela.update()
