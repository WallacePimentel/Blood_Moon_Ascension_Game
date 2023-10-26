from PPlay.sprite import *

def sair(janela,click,bot):

    bot.set_position(janela.width/2 - bot.width/2,janela.height / 2 + 190)

    if click.is_over_object(bot):
        bot = Sprite("z_sair_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 + 190)
        bot.draw()
        if click.is_button_pressed(1):
            janela.close()
    else:
        bot.draw()