import time
import keyboard


MAX_DELAY = 0.15
# ? Should probably make this constant configurable by user

keypress_time = time.time()
prev_key = 'none'


def keypress_event_check(event):
    if event.event_type == 'down':
        global keypress_time, prev_key
        key_input = str(event.name)
        new_keypress_time = time.time()
        delay_final = new_keypress_time - keypress_time
        keypress_time = new_keypress_time

        if key_input == prev_key and delay_final <= MAX_DELAY:
            pass
            # TODO: Jammed key detected on `key_input` -> Display on GUI
        else:
            pass
            # TODO: Fine for `key_input`, key is not jammed -> Display on GUI
        prev_key = key_input


def detect_jammed_key():
    keyboard.hook(keypress_event_check)
    keyboard.wait()
