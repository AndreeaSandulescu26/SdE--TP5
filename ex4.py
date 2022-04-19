degrees = 0

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string("N")
        basic.clear_screen()
        basic.pause(1000)
        basic.show_number(input.sound_level())
    elif degrees < 135:
        basic.show_string("E")
        basic.clear_screen()
        basic.pause(1000)
        basic.show_number(input.temperature())
        basic.show_number(input.light_level())
    elif degrees < 225:
        basic.show_string("S")
        basic.clear_screen()
        basic.pause(1000)
        basic.show_number(input.sound_level())
    elif degrees < 315:
        basic.show_string("W")
        basic.clear_screen()
        basic.pause(1000)
        basic.show_number(input.temperature())
        basic.clear_screen()
        basic.pause(1000)
        basic.show_number(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)
