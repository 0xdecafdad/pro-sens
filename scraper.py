# Author(s):	Shaun Derstine
# Date Created:	4/21/2022
# Description:	Get all listed pro edpi's for VALORANT, Apex Legends, and CS:GO from prosettings.net

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

# Input:	url
# Output: 	bs4 object
def convert_url(url):
	# Make custom request to webpage
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	
	# Save webpage
	webpage = urlopen(req).read()	

	# Convert webpage to bs object
	soup = bs(webpage, 'html.parser')

	return soup
# end convert_url()

# Recursive function to calculate the average of a list of ints
def calc_average(ints, i, size):
	if i == size-1:
		return ints[i]
	elif i == 0:
		return ( ints[i] + calc_average(ints, i+1, size) ) / size
	else:
		return ints[i] + calc_average(ints, i+1, size)
# end calc_average

# Build url to access appropriate webpage based on game
def build_url(game):
	# Gather components to craft url of webpage with approriate edpi list
	pre = 'https://prosettings.net/'
	game_name = ''
	# Will have to have input validation in driver code
	if game == 'valorant':
		game_name = 'valorant'
	elif game == 'apex':
		game_name = 'apex-legends'
	elif game == 'csgo':
		game_name = 'cs-go'
	else:
		# Later, raise (maybe custom) exception here
		# InvalidGame("Game must be 'valorant', 'apex', or 'csgo'")
		print('Error: Invalid Game!')
	post = '-pro-settings-gear-list/'
	url = '{pre}{game_name}{post}'.format(pre=pre, game_name=game_name, post=post)

	return url
# end build_url

# Finds average edpi of all listed pro players for {game}
# Game is a string, either "valorant", "apex", or "csgo"
def get_edpi(game):
	# Get url for correct webpage
	url = build_url(game)

	# Convert url to bs object
	soup = convert_url(url)

	# Get list of all edpis from webpage
	# PROBLEM HERE!!!
	# Does not return anything
	edpis = soup.find_all('td', {'class' : ' numdata integer  column-edpi'})

	# Print all edpis (debugging)
	for edpi in edpis:
		print(edpi)
# end get_edpi()
