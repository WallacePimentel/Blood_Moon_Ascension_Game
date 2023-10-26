from PPlay.sprite import *
from player import jogador

def jogar(janela,tecla,click,bot,ground,background,vila):

    bot.set_position(janela.width/2 - bot.width/2,janela.height/ 2 - 230)
    ground.set_position(0,janela.height - ground.height)
    vila.set_position(0,janela.height - ground.height - vila.height)
    player = Sprite("player.png")
    player.set_position(janela.width / 2 - player.width / 2, janela.height - player.height - 67)


    if click.is_over_object(bot):
        bot = Sprite("z_jogar_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 - 230)
        bot.draw()
        if click.is_button_pressed(1):
            while True:
                janela.set_background_color([0,0,0])
                background.draw()
                vila.draw()
                ground.draw()
                jogador(janela, player, tecla, click)

                if tecla.key_pressed("esc"):
                    break
            
                janela.update()
    else:
        bot.draw()