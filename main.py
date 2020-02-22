import msvcrt
import sys
import os
import time
import configparser
from termcolor import colored

if sys.platform == 'win32':
	os.system('color')

config = configparser.ConfigParser()
config.read('config.ini')

keypress_time = time.time()
prev_key = 'none'
while True:
	if msvcrt.kbhit():
		key_input = msvcrt.getch()
		new_keypress_time = time.time()
		delay_final = new_keypress_time - keypress_time
		keypress_time = new_keypress_time
		if key_input == prev_key and delay_final <= float(config['SETTINGS']['MinimalDelay']):
			print('\n' + colored(f'-> KEY JAM DETECTED ON {key_input} <-', color='white',on_color='on_red') + '\n')
		else:
			prev_key = key_input
			print(f'[FINE] for {key_input}')