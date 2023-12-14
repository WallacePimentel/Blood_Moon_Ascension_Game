import boss
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from variaveis import *
from demon import *
from main import inic_jogo
from math import fabs
from ghost import *
from fire_skull import *
from boss import *

janela.set_title("Blood Moon Ascension")
healthbar.set_position(janela.width - 230, 30)
player.set_position(janela.width / 2, janela.height - player.height - 24)
demon.set_position(janela.width + 100, janela.height - demon.height - 24)
boss_esquerda.set_position(janela.width + 200, janela.height - boss_esquerda.height - 24)
ghost_spawn_left()
ghost_spawn_right()
skull_spawn_left()
skull_spawn_right()
skull_spawn_up()

while True:

    # ------DRAW-FUNDOS-E-ICONES------#
    background.draw()
    healthbar.draw()

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #------HITBOX-PLAYER------#
    player_hitbox.x = player.x
    player_hitbox.y = player.y

    # ------MOVIMENTAÇÃO-PLAYER------#
    if ((tecla.key_pressed("left")) and not player_dash and not atacou):
        player_running = True
        player_direction = -1
        start = 1
        v_player = 200 * player_direction
        player.x = player.x + v_player * janela.delta_time()
    elif ((tecla.key_pressed("right")) and not player_dash and not atacou):
        player_running = True
        player_direction = 1
        start = 1
        v_player = 200 * player_direction
        player.x = player.x + v_player * janela.delta_time()
    else:
        player_running = False

    if tecla.key_pressed("up") and not player_dash and not pulou:
        pulou = True
    if pulou and not player_dash:
        if player.y <= janela.height - player.height - 24:
            player.y -= gravity * janela.delta_time()
            gravity -= 3000 * janela.delta_time()
        else:
            gravity = gravity_bkup
            pulou = False
            player.y = janela.height - player.height - 24

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
        if (cronometro_ataque > 0.4):
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
        gravity = 0

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
    if not player_invuneravel:
        player.draw()
    else:
        if player_invuneravel_cronometro > 0 and player_invuneravel_cronometro < 0.2:
            pass
        elif player_invuneravel_cronometro > 0.2 and player_invuneravel_cronometro < 0.4:
            player.draw()
        elif player_invuneravel_cronometro > 0.4 and player_invuneravel_cronometro < 0.6:
            pass
        elif player_invuneravel_cronometro > 0.6 and player_invuneravel_cronometro < 0.8:
            player.draw()
        elif player_invuneravel_cronometro > 0.8 and player_invuneravel_cronometro < 0.9:
            pass
        elif player_invuneravel_cronometro > 0.9 and player_invuneravel_cronometro < 1.2:
            player.draw()
        else:
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
        if ((demon.x - player.x) <= -55) and (demon_delay_attack > 3):
            demon_attacking = True
            demon_atacou = True

    if (demon_direction == -1):
        if (player.x < demon.x + demon.width - 95) and (demon_delay_attack > 3):
            demon_attacking = True
            demon_atacou = True
    demon_delay_attack += janela.delta_time()

    # ------COLISAO-DEMONIO-PLAYER------#
    if demon.collided(player_hitbox) and demon_cronometro > 0.35 and not player_levou_dano:
        player_levou_dano = True
        player_invuneravel = True
        vida_player -= 15

    # ------DURAÇÃO-DO-ATAQUE-DEMONIO------#
    if (demon_atacou):
        demon_cronometro += janela.delta_time()
        if (demon_cronometro > 0.7):
            demon_cronometro = 0
            demon_atacou = False
            demon_attacking = False
            player_levou_dano = False
            demon_delay_attack = 0

    # ------STATUS-DEMONIO------#
    if (demon.x + demon.width / 2 >= player.x + player.width / 2):
        demon_direction = 1
        if (demon_attacking):
            frames_atual_d = demon_at1
        else:
            frames_atual_d = demon_w1
    if (demon.x + demon.width / 2 < player.x + player.width / 2):
        demon_direction = -1
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
                if (demon_direction == 1):
                    if ((demon.x - player.x) >= -55):
                        demon.x = demon.x - v_demon * janela.delta_time()
                if (demon_direction == -1):
                    if (player.x > demon.x + demon.width - 95):
                        demon.x = demon.x + v_demon * janela.delta_time()

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #------MOVIMENTAÇÃO-E-DESENHO-DOS-FANTASMAS------#
    if start == 1:
        ghost_draw()
        ghost_move_left()
        ghost_move_right()

    if (verificador_ghosts_mortos()):
        onda = 2


    #------COLISÃO-GHOST-E-PLAYER------#
    for i in range(n):
        if (lista_ghost_left[i].collided(player) and vidas_ghost_left[i] > 0):
            if (player_attacking and not lista_booleano_ghost_left[i] and player_direction == -1):
                vidas_ghost_left[i] -= dano_player
                lista_booleano_ghost_left[i] = True
            elif (not player_invuneravel and not player_dash) and (lista_ghost_left[i].collided(player_hitbox)):
                vida_player -= ghost_dano
                player_invuneravel = True
        if (lista_ghost_right[i].collided(player) and vidas_ghost_right[i] > 0):
            if (player_attacking and not lista_booleano_ghost_right[i] and player_direction == 1):
                vidas_ghost_right[i] -= dano_player
                lista_booleano_ghost_right[i] = True
            elif (not player_invuneravel and not player_dash and (lista_ghost_right[i].collided(player_hitbox))):
                vida_player -= ghost_dano
                player_invuneravel = True

    #------TEMPO-DE-HIT-DO-FANTASMA------#
    for i in range(n):
        if lista_booleano_ghost_left[i] == True:
            lista_crono_ghost_left[i] += janela.delta_time()
            if lista_crono_ghost_left[i] > 1:
                lista_booleano_ghost_left[i] = False
                lista_crono_ghost_left[i] = 0
        if lista_booleano_ghost_right[i] == True:
            lista_crono_ghost_right[i] += janela.delta_time()
            if lista_crono_ghost_right[i] > 1:
                lista_crono_ghost_right[i] = 0
                lista_booleano_ghost_right[i] = False

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    #------FUNÇÕES-CAVEIRA-FLAMEJANTE------#
    if (start == 1):
        if (onda == 2):
            skull_move_right()
            skull_move_left()
            skull_move_up()
            #skull_draw()

    if (contador_passadas[0] >= 50):
        fim_skull()
        onda = 3

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    onda = 4
    if (start == 1):
        if (onda == 4):
            boss_hitbox_accuracy()
            boss_move()
            boss_draw()

    if (boss_direction[0] == 1):
        boss = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle2.png")

    if (boss_atacando):
        if (boss_hitbox_ataque.collided(player_hitbox)):
            vida_player -= boss_dano_fogo
            player_invuneravel = True



    janela.update()