from rpi_ws281x import Color


def color_array(strip, color):
    length = strip.numPixels()
    return [color] * length


def half(rainbow):
    for i in range(len(rainbow)):
        if i % 2:
            rainbow[i] = Color(0, 0, 0)


def shrink(rainbow):
    rainbow.pop(0)
    rainbow.append(Color(0, 0, 0))
    return len([i for i in rainbow if i != Color(0, 0, 0)])


def overlay(layers):
    overlay = layers[0]
    array_length = len(overlay)
    for layer in layers[1:]:
        for i in range(array_length):
            if overlay[i] == Color(0, 0, 0):
                overlay[i] = layer[i]
    return overlay


def mix(layers, ratios):
    if len(layers) != len(ratios):
        return
    num_leds = len(layers[0])
    done_until = 0
    mix = [Color(0, 0, 0)] * num_leds
    for i in range(len(layers)):
        until = int(num_leds * ratios[i] / 100)
        for j in range(done_until, until):
            mix[j] = layers[i][j]
        done_until = until
    return mix
