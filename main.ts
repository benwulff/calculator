input.onButtonPressed(Button.A, function () {
    nr += 1
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(nr * nr_b)
    nr_b = 0
    nr = 0
})
input.onButtonPressed(Button.B, function () {
    nr_b += 1
})
let nr_b = 0
let nr = 0
nr = 0
nr_b = 0
basic.forever(function () {
	
})
