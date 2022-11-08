from rpi_ws281x import Color

from .utils.reset_strip import reset_strip


def debug(strip):
    while True:
        index = 0
        try:
            index = int(input())
        except:
            break

        reset_strip(strip)
        try:
            strip.setPixelColor(index, Color(255, 255, 255))
            strip.show()
        except:
            print()
            print("index :", index)
            print("transformed index :", strip._transform_index(index))
            pass
