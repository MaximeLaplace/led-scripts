LED_COUNT = 149  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

BREAKPOINTS = [0, 13, 50, 72, 75, 78, 115, 136, 149]
KANOPEE_BREAKPOINTS = [0, 13, 15, 16, 19, 20, 25, 29, 30, 32, 38, 40, 46, 51, 56, 60, 66, 68, 74]

CADRE_BREAKPOINTS = [0, 15, 38, 52]
TAILLE_BUFFER_KANOPEE = 8