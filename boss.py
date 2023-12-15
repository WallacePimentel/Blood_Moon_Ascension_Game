from variaveis import *

boss_vida = 150
boss_velocidade = 110
nightmare_velocidade = 300
nightmare_damage = 5

#------BOSS-FRAMES------#
boss_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle.png", 6)
boss_direita = Sprite("Game Assets/Mobs/Final Boss/boss_idle/demon-idle2.png",6)
boss_atacando_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_attack/demon-attack.png",11)
boss_atacando_direita = Sprite("Game Assets/Mobs/Final Boss/boss_attack/demon-attack2.png",11)
boss_direita.set_total_duration(750)
boss_esquerda.set_total_duration(750)
boss_atacando_direita.set_total_duration(1175)
boss_atacando_esquerda.set_total_duration(1175)
boss_hitbox = Sprite("Game Assets/Mobs/Final Boss/boss_idle/boss_hitbox.png")
boss_hitbox_ataque_esquerda = Sprite("Game Assets/Mobs/Final Boss/boss_attack/boss_attack_hitbox.png")
boss_hitbox_ataque_direita = Sprite("Game Assets/Mobs/Final Boss/boss_attack/boss_attack_hitbox2.png")
boss_direction = [-1]
boss_horse = False
nightmare_esquerda = Sprite("Game Assets/Mobs/Nightmare/nightmare-galloping_direita.png",4)
nightmare_direita = Sprite("Game Assets/Mobs/Nightmare/nightmare-galloping.png",4)
nightmare_esquerda.set_total_duration(400)
nightmare_direita.set_total_duration(400)
nightmare_hitbox_esquerda = Sprite("Game Assets/Mobs/Nightmare/nightmare-hitbox2.png")
nightmare_hitbox_direita = Sprite("Game Assets/Mobs/Nightmare/nightmare-hitbox.png")

#------ATAQUE-BOSS------#
boss_intervalo_ataque_cronometro = 0
boss_atacando_cronometro = 0
boss_atacando = False
boss_dano_fogo = 10
boss_timer = 0
boss_tomou_dano = False

def boss_hitbox_accuracy():
    boss_hitbox.x = boss_esquerda.x
    boss_hitbox.y = boss_esquerda.y
    boss_hitbox_ataque_esquerda.x = (boss_esquerda.x - 50)
    boss_hitbox_ataque_esquerda.y = boss_esquerda.y
    boss_hitbox_ataque_direita.x = boss_esquerda.x + 25
    boss_hitbox_ataque_direita.y = boss_esquerda.y - 10
    nightmare_hitbox_esquerda.x = nightmare_esquerda.x + 53
    nightmare_hitbox_esquerda.y = nightmare_esquerda.y + 25
    nightmare_hitbox_direita.x = nightmare_direita.x + 10
    nightmare_hitbox_direita.y = nightmare_direita.y + 25

def boss_direction_now ():
    if (boss_hitbox.x) > (player.x):
        boss_direction[0] = -1
    if (boss_hitbox.x + boss_hitbox.width) < player.x:
        boss_direction[0] = 1

def boss_move (boss_atacando):
    if (not boss_atacando):
        if (boss_hitbox.x) > (player.x):
            boss_direction[0] = -1
            boss_esquerda.x -= boss_velocidade * janela.delta_time()
        if (boss_hitbox.x + boss_hitbox.width) < player.x:
            boss_direction[0] = 1
            boss_esquerda.x += boss_velocidade * janela.delta_time()

def boss_draw(boss_atacando,boss_timer):
    if (boss_direction[0] == -1):
        if (not boss_atacando):
            if boss_timer == 0:
                boss_esquerda.draw()
            else:
                if 0 < boss_timer <= 0.1:
                    pass
                if 0.1 < boss_timer <= 0.2:
                    boss_esquerda.draw()
                if 0.2 < boss_timer <= 0.3:
                    pass
                if 0.3 < boss_timer <= 0.4:
                    boss_esquerda.draw()
            boss_esquerda.update()
        else:
            if boss_timer == 0:
                boss_atacando_esquerda.draw()
            else:
                if 0 < boss_timer <= 0.1:
                    pass
                if 0.1 < boss_timer <= 0.2:
                    boss_atacando_esquerda.draw()
                if 0.2 < boss_timer <= 0.3:
                    pass
                if 0.3 < boss_timer <= 0.4:
                    boss_atacando_esquerda.draw()
            boss_atacando_esquerda.update()
    if (boss_direction[0] == 1):
        if (not boss_atacando):
            if boss_timer == 0:
                boss_direita.draw()
            else:
                if 0 < boss_timer <= 0.1:
                    pass
                if 0.1 < boss_timer <= 0.2:
                    boss_direita.draw()
                if 0.2 < boss_timer <= 0.3:
                    pass
                if 0.3 < boss_timer <= 0.4:
                    boss_direita.draw()
            boss_direita.update()
        else:
            if boss_timer == 0:
                boss_atacando_direita.draw()
            else:
                if 0 < boss_timer <= 0.1:
                    pass
                if 0.1 < boss_timer <= 0.2:
                    boss_atacando_direita.draw()
                if 0.2 < boss_timer <= 0.3:
                    pass
                if 0.3 < boss_timer <= 0.4:
                    boss_atacando_direita.draw()
            boss_atacando_direita.update()
    nightmare_esquerda.draw()
    nightmare_esquerda.update()
    nightmare_direita.draw()
    nightmare_direita.update()

def boss_sincronismo ():
    boss_direita.x = boss_esquerda.x
    boss_direita.y = boss_esquerda.y
    boss_atacando_esquerda.x = boss_esquerda.x - 50
    boss_atacando_esquerda.y = boss_esquerda.y - 40
    boss_atacando_direita.x = boss_esquerda.x - 30
    boss_atacando_direita.y = boss_esquerda.y - 40

def nightmare_move ():
    nightmare_direita.x -= nightmare_velocidade * janela.delta_time()
    nightmare_esquerda.x += nightmare_velocidade * janela.delta_time()
    if (nightmare_esquerda.x >= janela.width):
        nightmare_esquerda.set_position(-1200, janela.height - nightmare_esquerda.height - 24)
    if (nightmare_direita.x <= 0):
        nightmare_direita.set_position(janela.width + 2000, janela.height - nightmare_direita.height - 24)