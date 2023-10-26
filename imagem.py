
def imagem(janela,tecla,click):

    if tecla.key_pressed("left"):
        return "player_a.png"

    if tecla.key_pressed("right"):
        return "player_d.png"

    return "player.png"