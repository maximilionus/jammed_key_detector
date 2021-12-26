import time
import keyboard


MAX_DELAY = 0.15
# ? Should probably make this constant configurable by user

keypress_time = time.time()
prev_key = 'none'


def iskeyjammed_event_check(event) -> bool:
    if event.event_type == 'down':
        global keypress_time, prev_key

        key_input = str(event.name)
        delay_final = event.time - keypress_time
        keypress_time = event.time

        result = key_input == prev_key and delay_final <= MAX_DELAY
        prev_key = key_input

        return result


def detect_jammed_key():
    keyboard.hook(iskeyjammed_event_check)
    keyboard.wait()
