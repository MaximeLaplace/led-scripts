import time


def blackout(strip):
    while True:
        strip.reset()
        strip.show()
        time.sleep(24 * 3600)
