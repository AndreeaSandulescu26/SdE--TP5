while True:
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature())
    if input.logo_is_pressed():
        basic.show_number(input.light_level())
    basic.clear_screen()