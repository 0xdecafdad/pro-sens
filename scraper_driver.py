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
def calc_average(list):

# end calc_average
