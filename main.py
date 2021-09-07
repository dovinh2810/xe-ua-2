def on_button_pressed_a():
    if player_car.get(LedSpriteProperty.X) < 4:
        player_car.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if player_car.get(LedSpriteProperty.X) < 4:
        player_car.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

car_4: game.LedSprite = None
car_3: game.LedSprite = None
car_2: game.LedSprite = None
car_1: game.LedSprite = None
car: game.LedSprite = None
game_On = False
score = 0
player_car: game.LedSprite = None
bluetooth.start_accelerometer_service()
bluetooth.start_button_service()
bluetooth.start_io_pin_service()
bluetooth.start_led_service()
bluetooth.start_temperature_service()
bluetooth.start_magnetometer_service()

def on_forever():
    global score, player_car, game_On
    score = 0
    player_car = game.create_sprite(2, 4)
    game_On = True
    while game_On == True:
        basic.pause(100)
    game.add_score(score)
    game.game_over()
    basic.pause(5000)
basic.forever(on_forever)

def on_forever2():
    global car, game_On, score
    basic.pause(100)
    if game_On == True:
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        car = game.create_sprite(0, 0)
        basic.pause(randint(0, 5000))
        while game_On == True:
            if car.get(LedSpriteProperty.Y) == 4:
                if player_car.is_touching(car):
                    game_On = False
                    music.stop_melody(MelodyStopOptions.ALL)
                    music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
                        MelodyOptions.ONCE)
                else:
                    score = score + 1
                    car.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
            else:
                car.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
basic.forever(on_forever2)

def on_forever3():
    global car_1, game_On, score
    basic.pause(100)
    if game_On == True:
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        car_1 = game.create_sprite(1, 0)
        basic.pause(randint(0, 5000))
        while game_On == True:
            if car_1.get(LedSpriteProperty.Y) == 4:
                if player_car.is_touching(car_1):
                    game_On = False
                    music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
                        MelodyOptions.ONCE)
                else:
                    score = score + 1
                    car_1.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
            else:
                car_1.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
basic.forever(on_forever3)

def on_forever4():
    global car_2, game_On, score
    basic.pause(100)
    if game_On == True:
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        car_2 = game.create_sprite(2, 0)
        basic.pause(randint(0, 5000))
        while game_On == True:
            if car_2.get(LedSpriteProperty.Y) == 4:
                if player_car.is_touching(car_2):
                    game_On = False
                    music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
                        MelodyOptions.ONCE)
                else:
                    score = score + 1
                    car_2.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
            else:
                car_2.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
basic.forever(on_forever4)

def on_forever5():
    global car_3, game_On, score
    basic.pause(100)
    if game_On == True:
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        car_3 = game.create_sprite(3, 0)
        basic.pause(randint(0, 5000))
        while game_On == True:
            if car_3.get(LedSpriteProperty.Y) == 4:
                if player_car.is_touching(car_3):
                    game_On = False
                    music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
                        MelodyOptions.ONCE)
                else:
                    score = score + 1
                    car_3.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
            else:
                car_3.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
basic.forever(on_forever5)

def on_forever6():
    global car_4, game_On, score
    basic.pause(100)
    if game_On == True:
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.FOREVER_IN_BACKGROUND)
        car_4 = game.create_sprite(5, 0)
        basic.pause(randint(0, 5000))
        while game_On == True:
            if car_4.get(LedSpriteProperty.Y) == 4:
                if player_car.is_touching(car_4):
                    game_On = False
                    music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
                        MelodyOptions.ONCE)
                else:
                    score = score + 1
                    car_4.set(LedSpriteProperty.Y, 0)
                    basic.pause(randint(0, 5000))
            else:
                car_4.change(LedSpriteProperty.Y, 1)
                basic.pause(500)
basic.forever(on_forever6)
