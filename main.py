def on_button_pressed_a():
    Nave.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Lluvia():
    global a, x, MeteoroD, MeteoroI, GameOn, Vivo
    a = 0
    x = randint(1, 4)
    MeteoroD = game.create_sprite(x, 0)
    MeteoroI = game.create_sprite(x - 1, 0)
    for index in range(4):
        basic.pause(1000)
        a += 1
        MeteoroD.change(LedSpriteProperty.Y, 1)
        MeteoroI.change(LedSpriteProperty.Y, 1)
        if MeteoroD.is_touching(Nave) or MeteoroI.is_touching(Nave):
            basic.show_icon(IconNames.SAD)
            music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
            basic.pause(5000)
            GameOn = False
            Vivo = False
        elif MeteoroD.is_touching_edge() and MeteoroI.is_touching_edge():
            basic.pause(1000)
            MeteoroD.delete()
            MeteoroI.delete()
            game.add_score(1)
            music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
            Lluvia()
    if GameOn == False:
        MeteoroD.delete()
        MeteoroI.delete()
        Nave.delete()
        basic.show_string("Score")
        basic.show_string("" + str((game.score())))
        basic.pause(2000)

def on_button_pressed_ab():
    global GameOn, Nave
    for index2 in range(1):
        game.set_score(-1)
        GameOn = True
        Nave = game.create_sprite(2, 4)
        Lluvia()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Nave.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Vivo = False
MeteoroI: game.LedSprite = None
MeteoroD: game.LedSprite = None
x = 0
a = 0
Nave: game.LedSprite = None
GameOn = False
GameOn = False

def on_forever():
    pass
basic.forever(on_forever)
