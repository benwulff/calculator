def on_button_pressed_a():
    global nr
    nr += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global nr_b, nr
    basic.show_number(nr * nr_b)
    nr_b = 0
    nr = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global nr_b
    nr_b += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

nr_b = 0
nr = 0
nr = 0
nr_b = 0

def on_forever():
    pass
basic.forever(on_forever)
