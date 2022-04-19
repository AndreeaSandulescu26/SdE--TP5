def on_sound_loud():
    for index in range(5):
        led.plot(index, 2)
input.on_sound(DetectedSound.LOUD, on_sound_loud)