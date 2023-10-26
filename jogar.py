from PPlay.sprite import *
import nave

def jogar(janela,tecla,click,bot,player,tiro):

    bot.set_position(janela.width/2 - bot.width/2,janela.height/ 2 - 230)
    player.set_position(janela.width / 2 - player.width / 2, janela.height - player.height - 10)


    if click.is_over_object(bot):
        bot = Sprite("z_jogar_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 - 230)
        bot.draw()
        if click.is_button_pressed(1):
            while True:
                janela.set_background_color([0,0,0])

                nave.nave(janela,tecla,player,tiro)

                if tecla.key_pressed("esc"):
                    break
            
                janela.update()
    else:
        bot.draw()