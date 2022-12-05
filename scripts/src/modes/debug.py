from rpi_ws281x import Color


def debug(strip):
    print(strip.numPixels())
    while True:
        index = 0
        try:
            index = int(input())
        except:
            break

        try:
            strip.setPixelColor(index, Color(255, 255, 255))
            strip.show()
        except:
            print()
            print("index :", index)
            print("transformed index :", strip._transform_index(index))
            pass
