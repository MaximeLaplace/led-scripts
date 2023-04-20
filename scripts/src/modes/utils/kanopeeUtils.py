KANOPEE_LETTERS_SIZES = [5, 6, 6, 6, 4, 6, 6]

def map_letters(colors):
    if len(colors) < 7:
        new_colors = [colors[i%len(colors)] for i in range(7)]
    else:
        new_colors = colors[:7]

    final_array = []
    for i in range(7):
        final_array.extend([new_colors[i]]*KANOPEE_LETTERS_SIZES[i])
    
    return final_array
    
