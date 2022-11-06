from datetime import datetime


def init_time(time_delta: int):
    """Renvoie la fonction time_left qui donne le temps restant en millisecondes

    Args:
        time_delta (int): temps total désiré en secondes

    Returns:
        time_left (Callable): fonction qui retourne le temps restant
    """
    start_time = datetime.now().timestamp()

    def time_left():
        return time_delta * 1000 - (datetime.now().timestamp() - start_time)

    return time_left
