from pynput.keyboard import Key, Listener
import on_press


def __main__():
    with Listener(on_press=on_press.on_press) as listener:
            listener.join()
__main__()