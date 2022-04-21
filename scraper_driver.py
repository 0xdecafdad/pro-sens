# Author(s):	Shaun Derstine
# Date Created:	4/21/2022
# Description:	Driver for scraper.py

from scraper import *

def main():
	# Input validation loop
	# Users must select either VALORANT, Apex Legends, or CS:GO from list
	while True:
		print('Select game:')
		print('(1) VALORANT')
		print('(2) Apex Legends')
		print('(3) Counter Strike: Global Offensive')
		game = input('\n> ')
		
		# If valid selection, get edpis for appropriate game and break loop
		# Otherwise, repeat selection
		if game == '1':
			get_edpi('valorant')
			break
		elif game == '2':
			get_edpi('apex')
			break
		elif game == '3':
			get_edpi('csgo')
			break
		else:
			print('Invalid selection. Please select a number 1-3.\n')

if __name__ == "__main__":
	main()
