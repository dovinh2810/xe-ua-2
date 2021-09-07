input.onButtonPressed(Button.A, function () {
    if (player_car.get(LedSpriteProperty.X) < 4) {
        player_car.change(LedSpriteProperty.X, -1)
    }
})
input.onButtonPressed(Button.B, function () {
    if (player_car.get(LedSpriteProperty.X) < 4) {
        player_car.change(LedSpriteProperty.X, 1)
    }
})
let car_4: game.LedSprite = null
let car_3: game.LedSprite = null
let car_2: game.LedSprite = null
let car_1: game.LedSprite = null
let car: game.LedSprite = null
let game_On = false
let score = 0
let player_car: game.LedSprite = null
bluetooth.startAccelerometerService()
bluetooth.startButtonService()
bluetooth.startIOPinService()
bluetooth.startLEDService()
bluetooth.startTemperatureService()
bluetooth.startMagnetometerService()
basic.forever(function () {
    score = 0
    player_car = game.createSprite(2, 4)
    game_On = true
    while (game_On == true) {
        basic.pause(100)
    }
    game.addScore(score)
    game.gameOver()
    basic.pause(5000)
})
basic.forever(function () {
    basic.pause(100)
    if (game_On == true) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        car = game.createSprite(0, 0)
        basic.pause(randint(0, 5000))
        while (game_On == true) {
            if (car.get(LedSpriteProperty.Y) == 4) {
                if (player_car.isTouching(car)) {
                    game_On = false
                    music.stopMelody(MelodyStopOptions.All)
                    music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
                } else {
                    score = score + 1
                    car.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
                }
            } else {
                car.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (game_On == true) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        car_1 = game.createSprite(1, 0)
        basic.pause(randint(0, 5000))
        while (game_On == true) {
            if (car_1.get(LedSpriteProperty.Y) == 4) {
                if (player_car.isTouching(car_1)) {
                    game_On = false
                    music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
                } else {
                    score = score + 1
                    car_1.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
                }
            } else {
                car_1.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (game_On == true) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        car_2 = game.createSprite(2, 0)
        basic.pause(randint(0, 5000))
        while (game_On == true) {
            if (car_2.get(LedSpriteProperty.Y) == 4) {
                if (player_car.isTouching(car_2)) {
                    game_On = false
                    music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
                } else {
                    score = score + 1
                    car_2.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
                }
            } else {
                car_2.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (game_On == true) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        car_3 = game.createSprite(3, 0)
        basic.pause(randint(0, 5000))
        while (game_On == true) {
            if (car_3.get(LedSpriteProperty.Y) == 4) {
                if (player_car.isTouching(car_3)) {
                    game_On = false
                    music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
                } else {
                    score = score + 1
                    car_3.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
                }
            } else {
                car_3.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
basic.forever(function () {
    basic.pause(100)
    if (game_On == true) {
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        car_4 = game.createSprite(5, 0)
        basic.pause(randint(0, 5000))
        while (game_On == true) {
            if (car_4.get(LedSpriteProperty.Y) == 4) {
                if (player_car.isTouching(car_4)) {
                    game_On = false
                    music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
                } else {
                    score = score + 1
                    car_4.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
                }
            } else {
                car_4.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
            }
        }
    }
})
