count = 0
while True:
    if input.logo_is_pressed() and count == 0:
        count += 1
        basic.show_icon(IconNames.SQUARE)
    if input.logo_is_pressed() and count != 0:
        count = 0
        basic.show_icon(IconNames.SMALL_SQUARE)