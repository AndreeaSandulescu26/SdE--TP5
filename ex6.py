def on_button_pressed_ab():
    music.stop_all_sounds()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    music.start_melody(music.built_in_melody(Melodies.BLUES), MelodyOptions.ONCE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
