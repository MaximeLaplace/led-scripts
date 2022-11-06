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


def hsl_rainbow(start: int, end: int, position: int):
    min_hue = 360
    max_hue = 0
    cur_percent = (position - start) / (end - start)
    hue = cur_percent * (max_hue - min_hue) + min_hue
    return hue, 1, 0.5


def hsl_to_rgb(h, s, l):
    if h == 360:
        h = 0
    c = s * (1 - abs(2 * l - 1))
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    rp, gp, bp = 0, 0, 0

    if h < 60:
        rp, gp, bp = c, x, 0
    elif h < 120:
        rp, gp, bp = x, c, 0
    elif h < 180:
        rp, gp, bp = 0, c, x
    elif h < 240:
        rp, gp, bp = 0, x, c
    elif h < 300:
        rp, gp, bp = x, 0, c
    elif h < 360:
        rp, gp, bp = c, 0, x

    return (rp + m) * 255, (gp + m) * 255, (bp + m) * 255


def invert_green_blue(t: tuple[int, int, int]):
    r, g, b = t
    return r, b, g


def int_tuple(t: tuple[int, int, int]):
    a, b, c = t
    return int(a), int(b), int(c)


def multiply_tuple_by(factor: int):
    def inner(t: tuple[int, int, int]):
        a, b, c = t
        return a * factor, b * factor, c * factor

    return inner
