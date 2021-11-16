input.onButtonPressed(Button.A, function () {
    Nave.change(LedSpriteProperty.X, -1)
})
function Lluvia () {
    x = randint(1, 4)
    MeteoroD = game.createSprite(x, 0)
    MeteoroI = game.createSprite(x - 1, 0)
    for (let index = 0; index < 4; index++) {
        basic.pause(300)
        MeteoroD.change(LedSpriteProperty.Y, 1)
        MeteoroI.change(LedSpriteProperty.Y, 1)
        if (MeteoroD.isTouching(Nave) || MeteoroI.isTouching(Nave)) {
            basic.showIcon(IconNames.Sad)
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
            basic.pause(5000)
            GameOn = false
            Vivo = false
        } else if (MeteoroD.isTouchingEdge() && MeteoroI.isTouchingEdge()) {
            basic.pause(200)
            MeteoroD.delete()
            MeteoroI.delete()
            game.addScore(1)
            music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
            Lluvia()
        }
    }
    if (GameOn == false) {
        MeteoroD.delete()
        MeteoroI.delete()
        Nave.delete()
        basic.showString("Score:" + game.score())
        basic.showString("Press A+B to start")
        basic.pause(2000)
    }
}
input.onButtonPressed(Button.AB, function () {
    game.setScore(0)
    GameOn = true
    Nave = game.createSprite(2, 4)
    Lluvia()
})
input.onButtonPressed(Button.B, function () {
    Nave.change(LedSpriteProperty.X, 1)
})
let Vivo = false
let MeteoroI: game.LedSprite = null
let MeteoroD: game.LedSprite = null
let x = 0
let Nave: game.LedSprite = null
let GameOn = false
GameOn = false
basic.forever(function () {
	
})
