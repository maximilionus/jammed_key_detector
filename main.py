import msvcrt
import time

keypress_time = time.time()
prev_key = 'none'
while True:
	if msvcrt.kbhit():
		key_stroke = msvcrt.getch()
		new_keypress_time = time.time()
		delay_final = new_keypress_time - keypress_time
		keypress_time = new_keypress_time
		if key_stroke == prev_key and delay_final <= 0.15:
			print(f'\n=====\n-> Clip on key {key_stroke}\n=====\n')
		else:
			prev_key = key_stroke
			print(f'[FINE] for {key_stroke}')