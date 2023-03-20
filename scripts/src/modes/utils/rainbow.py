from rpi_ws281x import Color


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

    return [Color(*(red(x), green(x), blue(x))) for x in range(length)]


def create_rgb_rainbow_array(strip):
    length = strip.numPixels()
    m13 = length / 3
    m23 = 2 * length / 3

    def red(x):
        return int(max(255 - 255 / m13 * abs(x - m13), 0))

    def green(x):
        return int(max(255 * (abs(x - length / 2) / m13 - 0.5), 0))

    def blue(x):
        return int(max(255 - 255 / m13 * abs(x - m23), 0))

    return [(red(x), green(x), blue(x)) for x in range(length)]


def shift(rainbow):
    rainbow.append(rainbow.pop(0))
