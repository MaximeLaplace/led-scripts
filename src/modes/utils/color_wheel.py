from rpi_ws281x import Color


def color_wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def create_rainbow_array(strip):
    length = strip.numPixels()
    m13 = length / 3
    m23 = 2 * length / 3

    def red(x):
        return int(max(255 - 255 / m13 * abs(x - m13), 0))

    def green(x):
        return int(max(255 * (abs(x - length / 2) / m13 - 0.5), 0))

    def blue(x):
        return int(max(255 - 255 / m13 * abs(x - m23), 0))

    return [Color(red(x), green(x), blue(x)) for x in range(length)]
