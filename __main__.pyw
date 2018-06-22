from pynput.keyboard import Key, Listener
import on_press


def __main__():
    with Listener(on_press=on_press.on_press) as listener:
        key = listener.join()
    on_press.on_press(key)
__main__()

