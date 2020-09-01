from django.db import models
from bs4 import BeautifulSoup
import requests

# manga_hub

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