import keyboard
import sys
import os
import time
import configparser
from termcolor import colored
import helpers as h

if sys.platform == 'win32':
	os.system('color')

h.check_config_file()
config = configparser.ConfigParser()
config.read('config.ini')

keypress_time = time.time()
prev_key = 'none'

def jam_detector(event):
	if event.event_type == 'down':
		global keypress_time, prev_key
		key_input = str(event.name)
		new_keypress_time = time.time()
		delay_final = new_keypress_time - keypress_time
		keypress_time = new_keypress_time

		if key_input == prev_key and delay_final <= float(config['SETTINGS']['minimaldelay']):
			print('\n' + colored(f'-> KEY JAM DETECTED ON [ {key_input} ] <-', color='white',on_color='on_red') + '\n')
		else:
			print(f'[FINE] for [ {key_input} ]')
		prev_key = key_input

keyboard.hook(jam_detector)
keyboard.wait()