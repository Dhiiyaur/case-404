from django.db import models
from bs4 import BeautifulSoup
import requests

# ENG

def MH_manga_name(title):

	url = 'https://mangahub.io/search?q='
	
	url = url + f'{title}'
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')
	results     = soup.find_all(class_="media-heading")
	thumbnail_image = soup.find_all(class_="media-left")

	manga_name_results = []

	for num, result in enumerate(results):

		manga = {}
		manga['name']   = result.find('a').text
		manga['latest_chapter'] = result.next_sibling.find('a').text.strip('#')
		manga['status'] = 'Completed' if 'Completed' in result.next_sibling.get_text() else 'Ongoing'
		manga['link'] = result.find('a')['href'].rsplit('/', 1)[-1]
		manga['thumbnail_image'] = thumbnail_image[num].find(class_="manga-thumb")['src']

		manga_name_results.append(manga)

	return manga_name_results



def MH_manga_chapter(title):

	manga_chapter_results = []

	url = 'https://mangahub.io/manga/' 

	url = url + f'{title}'
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	empty = None

	if soup.find_all(class_="_287KE list-group-item"):
		
		results = soup.find_all(class_="_287KE list-group-item")

		for data in results:

			manga_chapter = {}
			manga_chapter['chapter_name'] = data.find('a')['href'].rsplit('/', 2)[-1]
			manga_chapter['link'] = data.find('a')['href'].rsplit('/', 2)[-1]
			manga_chapter_results.append(manga_chapter)

		return manga_chapter_results

	return empty

def MH_manga_image(manga_name, chapter):

	url = f'https://mangahub.io/chapter/'

	url = url + f'{manga_name}' + '/' + f'{chapter}'
	print(url)
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')
	results = soup.find_all(class_="PB0mN")[0]['src'].rsplit('/1.',1)

	base_url, type_image = results[0] + '/' , '.' + results[-1]
	list_image = []

	for i in range(1, 100):

		manga_url = {}
		manga_url['image'] = base_url + str(i) + type_image
		list_image.append(manga_url)

	return list_image




# IND


def ID_manga_name(title):

	url = 'https://komiku.co.id/?post_type=manga&s='
	
	url = url + f'{title}'
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	manga_name_results = []
	box_manga = []
	results = soup.find_all(class_="bge")

	for result in results:

		manga = {}
		manga['name'] = result.find('a')['href'].split('/')[-2].replace('-',' ')
		manga['latest_chapter'] = ''
		manga['status'] = ''
		#manga['link'] = result.find('a')['href']
		manga['link'] = result.find('a')['href'].split('/')[-2]
		for i in result.find_all('img'):
			manga['thumbnail_image'] = i.get('data-src')

		manga_name_results.append(manga)

	print(manga_name_results)
	return manga_name_results

	
def ID_manga_chapter(title):

	manga_chapter_results = []

	url = 'https://komiku.co.id/manga/' 

	url = url + f'{title}'
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	empty = None

	
	if soup.find_all(class_="popunder"):

		results = soup.find_all(class_="popunder")

		for data in results:

			note1 = data['href'].split('/')[3]
			note2 = data['href'].split('/')[-2]

			if note1 != 'manga'and note2 != '__trashed-19':

				manga_chapter = {}

				manga_chapter['chapter_name'] = data['href'].split('/')[-2]
				manga_chapter['link'] = data['href'].split('/')[-2]
				manga_chapter_results.append(manga_chapter)

		return manga_chapter_results

	return empty



def ID_manga_image(manga_name, chapter):


	url = f'https://komiku.co.id/{chapter}'
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')
	results = soup.find_all('img')

	list_image = []

	for data in results:

		
		note = data['src'].split('/')[3]
		note2 = len(data['src'].split(','))

		if note == 'cdn.komiku.co.id' and note2 <2:

			manga_url = {}
			manga_url['image'] = data['src']
			list_image.append(manga_url)

	return list_image