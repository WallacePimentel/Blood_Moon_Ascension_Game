def jogador (janela,player,tecla,click):

    if tecla.key_pressed("left"):
        velocidade = -200
        player.x = player.x + velocidade * janela.delta_time()

    if tecla.key_pressed("right"):

        velocidade = 200
        player.x = player.x + velocidade * janela.delta_time()


    player.draw()