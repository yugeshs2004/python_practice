import screen_brightness_control as sbc
print(sbc.get_brightness(display=0))
sbc.set_brightness(display=0, value=50)