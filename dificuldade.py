from PPlay.sprite import *

def dif (janela,tecla,click,bot):
    bot.set_position(janela.width/2 - bot.width/2,janela.height / 2 - 90)
    botao_facil = Sprite("z_facil.png")
    botao_medio = Sprite("z_medio.png")
    botao_dificil = Sprite("z_dificil.png")

    if click.is_over_object(bot):
        bot = Sprite("z_dificuldade_p.png")
        bot.set_position(janela.width / 2 - bot.width / 2, janela.height / 2 - 90)
        bot.draw()
        if click.is_button_pressed(1):
            while True:
                botao_facil.set_position(janela.width/2 - botao_facil.width/2,janela.height/2 - 150)
                botao_medio.set_position(janela.width/2 - botao_medio.width/2,janela.height/2)
                botao_dificil.set_position(janela.width / 2 - botao_dificil.width / 2, janela.height / 2 + 150)

                janela.set_background_color([0,0,0])

                if click.is_over_object(botao_facil):
                    botao_facil = Sprite("z_facil_p.png")
                    botao_facil.set_position(janela.width / 2 - botao_facil.width / 2, janela.height / 2 - 150)
                    botao_facil.draw()
                else:
                    botao_facil.draw()

                if click.is_over_object(botao_medio):
                    botao_medio = Sprite("z_medio_p.png")
                    botao_medio.set_position(janela.width / 2 - botao_medio.width / 2, janela.height / 2)
                    botao_medio.draw()
                else:
                    botao_medio.draw()

                if click.is_over_object(botao_dificil):
                    botao_dificil = Sprite("z_dificil_p.png")
                    botao_dificil.set_position(janela.width / 2 - botao_dificil.width / 2, janela.height / 2 + 150)
                    botao_dificil.draw()
                else:
                    botao_dificil.draw()

                if tecla.key_pressed("esc"):
                    break

                janela.update()
    else:
        bot.draw()