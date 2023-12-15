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
demon_hitbox.set_position(demon.x + 100,demon.y + 200)
boss_esquerda.set_position(janela.width + 200, janela.height - boss_esquerda.height - 24)
nightmare_esquerda.set_position(-1200,janela.height - nightmare_esquerda.height - 24)
nightmare_direita.set_position(janela.width + 2000, janela.height - nightmare_direita.height - 24)
ghost_spawn_left()
ghost_spawn_right()
skull_spawn_left()
skull_spawn_right()
skull_spawn_up()
fim = False
passou = 0
fim_de_jogo = False
restart_enable = False
sound1.set_volume(100)
sound1.play()

while True:

    # ------DRAW-FUNDOS-E-ICONES------#
    background.draw()
    healthbar.draw()

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    # ------HITBOX-PLAYER------#
    player_hitbox.x = player.x
    player_hitbox.y = player.y

    if (vida_player > 30):
        tempx = healthbar.x
        tempy = healthbar.y
        healthbar = Sprite("Game Assets/Icones/health40.png")
        healthbar.set_position(tempx,tempy)

    # ------MOVIMENTAÇÃO-PLAYER------#
    if ((tecla.key_pressed("left")) and not player_dash and not atacou and (player_hitbox.x > 0)):
        player_running = True
        player_direction = -1
        start = 1
        v_player = 200 * player_direction
        player.x = player.x + v_player * janela.delta_time()
    elif ((tecla.key_pressed("right")) and not player_dash and not atacou and (player_hitbox.x + 22 <= janela.width)):
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

    # ------INVUNERABILIDADE-PÓS-DANO-DO-PLAYER------#
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
    if (30 >= vida_player > 20):
        healthbar = Sprite("Game Assets/Icones/health30.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()
    if (20 >= vida_player > 10):
        healthbar = Sprite("Game Assets/Icones/health20.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()
    if (10 >= vida_player > 0):
        healthbar = Sprite("Game Assets/Icones/health10.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()
    if (vida_player <= 0):
        healthbar = Sprite("Game Assets/Icones/health0.png")
        healthbar.set_position(janela.width - 230, 30)
        healthbar.draw()

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #------DEMON-HITBOX------#
    demon_hitbox.x = demon.x + 107
    demon_hitbox.y = demon.y + 72
    demon_hitbox_atacando_direita.x = demon.x + 107
    demon_hitbox_atacando_direita.y = demon.y + 72
    demon_hitbox_atacando_esquerda.x = demon.x + 45
    demon_hitbox_atacando_esquerda.y = demon.y + 72

    # ------ATAQUE-DEMONIO------#
    if vida_demon > 0:
        if (demon_direction == 1):
            if ((demon.x - player.x) <= -25) and (demon_delay_attack > 3):
                demon_attacking = True
                demon_atacou = True

        if (demon_direction == -1):
            if (player.x < demon.x + demon.width - 45) and (demon_delay_attack > 3):
                demon_attacking = True
                demon_atacou = True
        demon_delay_attack += janela.delta_time()

        # ------COLISAO-DEMONIO-PLAYER------#
        if not player_dash and demon_hitbox_atacando_direita.collided(player_hitbox) and demon_cronometro > 0.39 and not player_levou_dano and demon_direction == -1:
            player_levou_dano = True
            player_invuneravel = True
            vida_player -= 15
        if not player_dash and demon_hitbox_atacando_esquerda.collided(player_hitbox) and demon_cronometro > 0.39 and not player_levou_dano and demon_direction == 1:
            player_levou_dano = True
            player_invuneravel = True
            vida_player -= 15

        if demon_hitbox.collided(player) and player_attacking and cronometro_dano_sofrido_demon == 0:
            vida_demon -= dano_player
            cronometro_dano_sofrido_demon += janela.delta_time()
        if cronometro_dano_sofrido_demon != 0:
            cronometro_dano_sofrido_demon += janela.delta_time()
            if cronometro_dano_sofrido_demon > 0.4:
                cronometro_dano_sofrido_demon = 0

        # --------DRAWN-DEMONIO--------#
        if cronometro_dano_sofrido_demon == 0:
            demon.draw()
        else:
            if 0 < cronometro_dano_sofrido_demon <= 0.1:
                pass
            if 0.1 < cronometro_dano_sofrido_demon <= 0.2:
                demon.draw()
            if 0.2 < cronometro_dano_sofrido_demon <= 0.3:
                pass
            if 0.3 < cronometro_dano_sofrido_demon <= 0.4:
                demon.draw()

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
            index_animacao_d += 0.035
        else:
            index_animacao_d += 0.02
        if index_animacao_d >= len(frames_atual_d):
            index_animacao_d = 0
        demon.image = frames_atual_d[int(index_animacao_d)]


        # ------MOVIMENTAÇÃO-DEMONIO------#
        if (start == 1):
            if (onda == 3):
                if (demon_attacking == False):
                    if (demon_direction == 1):
                        if ((demon.x - player.x) >= -25):
                            demon.x = demon.x - v_demon * janela.delta_time()
                    if (demon_direction == -1):
                        if (player.x > demon.x + demon.width - 45):
                            demon.x = demon.x + v_demon * janela.delta_time()

    #------THE-EVIL-DEAD------#
    if (vida_demon <= 0):
        demon_morrendo.set_position(demon.x,demon.y)
        index_animacao_death_demonio += 0.025
        cronometro_excluir += 0.025
        if index_animacao_death_demonio >= len(demon_dy):
            index_animacao_death_demonio = 0
        if cronometro_excluir >= 22:
            demon_morrendo.set_position(1000000,1000000)
        demon_morrendo.image = demon_dy[int(index_animacao_death_demonio)]
        demon_morrendo.draw()
        if (not fim_de_jogo):
            passou += 1

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    # ------MOVIMENTAÇÃO-E-DESENHO-DOS-FANTASMAS------#
    if start == 1:
        ghost_draw()
        ghost_move_left()
        ghost_move_right()

    if (verificador_ghosts_mortos(fim)):
        fim = True
        onda = 2

    # ------COLISÃO-GHOST-E-PLAYER------#
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

    # ------TEMPO-DE-HIT-DO-FANTASMA------#
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

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    # ------FUNÇÕES-CAVEIRA-FLAMEJANTE------#
    if (start == 1):
        if (onda == 2):
            fim_skull()
            skull_move_right()
            skull_move_left()
            skull_move_up()
            skull_draw()
            skull_hitbox_accuracy()

    if (onda == 2):
        for i in range(numero):
            if (lista_hitbox_skull_left[i].collided(player_hitbox) and not player_invuneravel and not player_dash):
                vida_player -= skull_dano
                player_invuneravel = True
            if (lista_hitbox_skull_right[i].collided(player_hitbox) and not player_invuneravel and not player_dash):
                vida_player -= skull_dano
                player_invuneravel = True
            if (lista_hitbox_skull_up[i].collided(player_hitbox) and not player_invuneravel and not player_dash):
                vida_player -= skull_dano
                player_invuneravel = True


    if (contador_passadas[0] >= 50):
        onda = 3 + passou

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    if (start == 1):
        if (onda >= 4):
            boss_hitbox_accuracy()
            boss_move(boss_atacando)
            boss_direction_now()
            boss_sincronismo()
            nightmare_move()
            boss_draw(boss_atacando,boss_timer)

    #------ATAQUE-BOSS------#
    if (onda >= 4):
        boss_intervalo_ataque_cronometro += janela.delta_time()
        if (boss_intervalo_ataque_cronometro > 5):
            boss_atacando = True

        if (boss_atacando):
            boss_atacando_cronometro += janela.delta_time()
            if (boss_atacando_cronometro > 2):
                boss_atacando_cronometro = 0
                boss_intervalo_ataque_cronometro = 0
                boss_atacando = False

            if (boss_direction[0] == -1):
                if (boss_hitbox_ataque_esquerda.collided(player_hitbox) and not player_invuneravel and not player_dash):
                    vida_player -= boss_dano_fogo
                    player_invuneravel = True
            if (boss_direction[0] == 1):
                if (boss_hitbox_ataque_direita.collided(player_hitbox) and not player_invuneravel and not player_dash):
                    vida_player -= boss_dano_fogo
                    player_invuneravel = True

        if (not boss_atacando) and (boss_hitbox.collided(player)) and player_attacking and boss_timer == 0:
            boss_tomou_dano = True
            boss_vida -= dano_player

        if boss_tomou_dano:
            boss_timer += janela.delta_time()
        if boss_timer > 0.4:
            boss_tomou_dano = False
            boss_timer = 0

        #------COLISÃO-CAVALO------#
        if (nightmare_hitbox_esquerda.collided(player_hitbox) and not player_invuneravel and not player_dash):
            vida_player -= nightmare_damage
            player_invuneravel = True
        if (nightmare_hitbox_direita.collided(player_hitbox) and not player_invuneravel and not player_dash):
            vida_player -= nightmare_damage
            player_invuneravel = True

    if (boss_vida <= 0):
        fim_de_jogo = True
        background_vitoria.draw()

    if (vida_player <= 0):
        fim_de_jogo = True
        background_game_over.draw()

    if (fim_de_jogo):
        start = 0
        if (tecla.key_pressed("space")):
            for i in range(n):
                vidas_ghost_left[i] = 10
                vidas_ghost_right[i] = 10
                lista_booleano_ghost_left[i] = False
                lista_booleano_ghost_right[i] = False
                lista_ghost_left[i].set_position(-1200 * random.randint(2, 4) +
                                                 ghost_distance_appart * i, janela.height - lista_ghost_left[i].height - 24)
                lista_ghost_right[i].set_position(janela.width + 1200 * random.randint(2, 4) -
                                               ghost_distance_appart * i, janela.height - lista_ghost_right[i].height - 24)
            for i in range(numero):
                lista_skull_left[i].set_position(-1200 + skull_plus * i,
                                                 janela.height - lista_skull_left[i].height - 20 - (200 * i * 0.5))
                lista_skull_right[i].set_position(janela.width + 2400 - skull_plus * i,
                                                  janela.height - lista_skull_right[i].height - 20 - (200 * i * 0.5))
                lista_skull_up[i].set_position(30 + (skull_plus * (random.randint(0, 7))) + (skull_plus * i), -1200)
            player.set_position(janela.width / 2, janela.height - player.height - 24)
            demon.set_position(janela.width + 100, janela.height - demon.height - 24)
            demon_hitbox.set_position(demon.x + 100, demon.y + 200)
            boss_esquerda.set_position(janela.width + 200, janela.height - boss_esquerda.height - 24)
            nightmare_esquerda.set_position(-1200, janela.height - nightmare_esquerda.height - 24)
            nightmare_direita.set_position(janela.width + 2000, janela.height - nightmare_direita.height - 24)
            vida_player = 60
            boss_vida = 150
            vida_demon = 200
            onda = 1
            fim = False
            contador_passadas[0] = 0
            passou = 0
            fim_de_jogo = False


    janela.update()