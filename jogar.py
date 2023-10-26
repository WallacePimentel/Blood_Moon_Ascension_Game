from PPlay.sprite import *
from player import jogador
from imagem import imagem

def jogar(janela,tecla,click,bot,ground,background):

    bot.set_position(janela.width/2 - bot.width/2,janela.height/ 2 - 230)
    ground.set_position(0,janela.height - ground.height)
    background.set_position(0,janela.height - ground.height - background.height)
    img = "player.png"
    player = Sprite(img)
    player.set_position(janela.width / 2 - player.width / 2, janela.height - player.height - 67)


    if click.is_over_object(bot):
        bot = Sprite("z_jogar_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 - 230)
        bot.draw()
        if click.is_button_pressed(1):
            while True:
                janela.set_background_color([0,0,0])
                img = imagem(janela, tecla, click)
                background.draw()
                ground.draw()
                jogador(janela, player, tecla, click)

                if tecla.key_pressed("esc"):
                    break
            
                janela.update()
    else:
        bot.draw()