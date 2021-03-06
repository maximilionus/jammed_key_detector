import configparser
import os
import sys
from termcolor import colored

def check_config_file():
	if not 'config.ini' in os.listdir():
		config = configparser.ConfigParser()
		config.add_section('SETTINGS')
		config.set('SETTINGS', 'minimaldelay', '0.15')
		with open('config.ini', 'w') as config_file:
			config.write(config_file)
			print(colored("Can't find config.ini, generated new one.", color='green', attrs=['reverse']) + '\n')
