from variaveis import *
import random

#------VARIAVEIS-DE-SPAWN-E-MOVIMENTAÇAO------#
n = 5
lista_ghost_right = []
lista_ghost_left = []
vidas_ghost_right = []
vidas_ghost_left = []
velocidade_ghost = 285
ghost_distance_appart = 150

#------VARIAVEIS-DE-INTERAÇÃO------#
lista_booleano_ghost_left = []
lista_booleano_ghost_right = []
lista_crono_ghost_left = []
lista_crono_ghost_right = []
ghost_dano = 10

def ghost_spawn_left ():
    for i in range(n):
        new_ghost = Sprite("Game Assets/Mobs/Ghost/ghost_iddle_right/ghost-idle.png",7)
        new_ghost.set_total_duration(1000)
        vida_atual = 10
        vidas_ghost_left.append(vida_atual)
        lista_booleano_ghost_left.append(False)
        lista_crono_ghost_left.append(0)
        new_ghost.set_position(-1200 * random.randint(2,4)  +
                               ghost_distance_appart * i,janela.height - new_ghost.height - 24)
        lista_ghost_left.append(new_ghost)

def ghost_spawn_right ():
    for i in range(n):
        new_ghost = Sprite("Game Assets/Mobs/Ghost/ghost_iddle/ghost-idle.png",7)
        new_ghost.set_total_duration(1000)
        vida_atual = 10
        vidas_ghost_right.append(vida_atual)
        lista_booleano_ghost_right.append(False)
        lista_crono_ghost_right.append(0)
        new_ghost.set_position(janela.width + 1200 * random.randint(2,4) -
                               ghost_distance_appart * i,janela.height - new_ghost.height - 24)
        lista_ghost_right.append(new_ghost)
def ghost_draw():
    for i in range(n):
        if (vidas_ghost_left[i] > 0):
            lista_ghost_left[i].draw()
            lista_ghost_left[i].update()
        if (vidas_ghost_right[i] > 0):
            lista_ghost_right[i].draw()
            lista_ghost_right[i].update()
def ghost_move_left ():
    for i in range(n):
        if lista_crono_ghost_left[i] == 0:
            lista_ghost_left[i].x += velocidade_ghost * janela.delta_time()
            if (lista_ghost_left[i].x >= janela.width) and (vidas_ghost_left[i] > 0):
                lista_ghost_left[i].set_position(-1200,janela.height - lista_ghost_left[i].height - 24)

def ghost_move_right():
    for i in range(n):
        if lista_crono_ghost_right[i] == 0:
            lista_ghost_right[i].x += velocidade_ghost * -1 * janela.delta_time()
            if lista_ghost_right[i].x <= 0:
                lista_ghost_right[i].set_position(janela.width + 1200,janela.height - lista_ghost_right[i].height - 24)

def verificador_ghosts_mortos (fim):
    if fim:
        return False
    for i in range(n):
        if (vidas_ghost_left[i] > 0) or (vidas_ghost_right[i] > 0):
            return False
    return True