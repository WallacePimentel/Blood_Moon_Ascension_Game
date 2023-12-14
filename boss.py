from variaveis import *

boss_vida = 150
boss_velocidade = 165

#------BOSS-FRAMES------#
boss_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle.png", 6)
boss_direita = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle2.png",6)
boss_esquerda.set_total_duration(750)
boss_hitbox = Sprite("Game Assets/Mobs/Final Boss/boss_idle/boss_hitbox.png")
boss_hitbox_ataque = Sprite("Game Assets/Mobs/Final Boss/boss_attack/boss_attack_hitbox.png")
boss_direction = [-1]

#------ATAQUE-BOSS------#
boss_ataque_cronometro = 0
boss_atacando = False
boss_dano_fogo = 20

def boss_hitbox_accuracy():
    boss_hitbox.x = boss_esquerda.x
    boss_hitbox.y = boss_esquerda.y
    boss_hitbox_ataque.x = (boss_esquerda.x - 50)
    boss_hitbox_ataque.y = boss_esquerda.y

def boss_move ():
    if (not boss_atacando):
        if (boss_hitbox.x) > (player.x):
            boss_direction[0] = -1
            boss_esquerda.x -= boss_velocidade * janela.delta_time()
        if (boss_hitbox.x + boss_hitbox.width) < player.x:
            boss_direction[0] = 1
            boss_esquerda.x += boss_velocidade * janela.delta_time()

def boss_draw():
    boss_esquerda.draw()
    boss_esquerda.update()