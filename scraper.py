# Author(s):	Shaun Derstine
# Date Created:	4/21/2022
# Description:	Get all listed pro edpi's for VALORANT, Apex Legends, and CS:GO from prosettings.net

from bs4 import BeautifulSoup as bs

# Input:	url
# Output: 	bs4 object
def convert_url(url):
	# urlopen makes a request to webpage at url
	# result is an object which is saved as url_object
	url_object = urlopen(url)

	# the raw html from the webpage is saved in html_doc
	html_doc = url_object.read()

	# converts raw html to BeautifulSoup object 'soup'
	soup = bs(html_doc, "html.parser")

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

# Finds average edpi of all listed pro players for {game}
# Game is a string, either "valorant", "apex", or "csgo"
def get_edpi(game):
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

	print(url)
# end get_edpi()
