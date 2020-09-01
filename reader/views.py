
# import libraries

from django.shortcuts import render
from reader.models import *

# fuction

def home_page(request):

	templates = 'home.html'
	return render(request, templates)

def search_page(request):

	templates_search = 'search_page.html'
	templates_home   = 'home.html'

	title = request.GET.get('manga_title')
	if not title:
		return render(request, templates_home)

	manga_data = MH_manga_name(title)
	context = { 'manga' : manga_data }
	return render(request, templates_search, context)

def manga_page(request, manga_name):

	templates = 'manga_page.html'

	chapter = MH_manga_chapter(manga_name)

	manga_title = f'{manga_name}'
	manga_title = manga_title.split('-')

	if len(manga_title)>2:

		manga_title = manga_title[0] + ' ' + manga_title[1] + ' ' + manga_title[2] + '...'
	else:
		manga_title = manga_title[0]

	context = { 'manga' : chapter, 'manga_name' : manga_name, 'manga_title' : manga_title}
	return render(request, templates, context)

def chapter_page(request, manga_name, chapter):

	templates = 'chapter_page.html'
	
	image = MH_manga_image(manga_name, chapter)
	context = {'manga' : image, 'chapter' : chapter}
	return render(request, templates, context)