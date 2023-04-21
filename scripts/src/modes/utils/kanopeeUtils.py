from rpi_ws281x import Color

KANOPEE_LETTERS_SIZES = [5, 6, 6, 6, 5, 6, 6]
CADRE_SIZE = 52

def map_letters(colors):
    if len(colors) < 7:
        new_colors = [colors[i%len(colors)] for i in range(7)]
    else:
        new_colors = colors[:7]

    final_array = []
    for i in range(7):
        final_array.extend([new_colors[i]]*KANOPEE_LETTERS_SIZES[i])
    final_array.append(new_colors[4])
    
    return final_array

def invert(array, colorA, colorB):
    for i in range(len(array)):
        if array[i] == colorA:
            array[i] = colorB
        elif array[i] == colorB:
            array[i] = colorA
    return array

def padForKanopeeCadre(list):
    new_list = ([Color(0, 0, 0)]*CADRE_SIZE)
    new_list.extend(list)
    return new_list