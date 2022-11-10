from config import BREAKPOINTS, LED_COUNT


def int_to_2chars_hex(n: int):
    h = hex(n)[2:]
    h += "0" * (2 - len(h))
    return h.upper()


def rbg_to_hex(r, b, g):
    return f"#{int_to_2chars_hex(r)}{int_to_2chars_hex(b)}{int_to_2chars_hex(g)}"


def get_color_string(r, g, b):
    return f"\33[38;2;{r};{b};{g}m█"


def Color(a, b, c):
    return a, b, c


class PixelStrip:
    def __init__(
        self,
        num,
        pin,
        freq_hz=800000,
        dma=10,
        invert=False,
        brightness=255,
        channel=0,
        strip_type=None,
        gamma=None,
    ):
        self.num = num
        self.pin = pin
        self.freq_hz = freq_hz
        self.dma = dma
        self.invert = invert
        self.brightness = brightness
        self.channel = channel
        self.strip_type = strip_type
        self.gamma = gamma

        self._led_data = [(0, 0, 0) for _ in range(num)]

        self.begun = False

    def numPixels(self):
        return self.num

    def setPixelColor(self, index, color: tuple[int, int, int]):
        if index < LED_COUNT:
            self._led_data[index] = color or Color(0, 0, 0)

    def begin(self):
        self.begun = True

    def getPixelColor(self, index):
        return self._led_data[index]

    def show(self):
        strip_repr = ""
        for i in range(LED_COUNT):
            if i in BREAKPOINTS and i != 0:
                strip_repr += "\033[38;2;255;255;255m|"
            strip_repr += get_color_string(*self.getPixelColor(i))

        print(strip_repr, end="\r")
