
# import libraries

from django.shortcuts import render
from reader.models import *

# fuction

def home_page(request):

	templates = 'home.html'
	return render(request, templates)

def search_page(request):

	templates_search = 'search_page.html'
	templates_search_id = 'search_page_id.html'
	templates_home   = 'home.html'

	# change lang

	lang  = request.GET.get('manga_lang')
	title = request.GET.get('manga_title')

	if not title:
		return render(request, templates_home)

	if lang == 'ENG':
		print('ini bahasa english')
		manga_data = MH_manga_name(title)
		context = { 'manga' : manga_data }
		return render(request, templates_search, context)

	else:
		print('ini bahasa indonesia')
		manga_data = ID_manga_name(title)
		context = { 'manga' : manga_data }
		return render(request, templates_search_id, context)

# ENG


def manga_page(request, manga_name):

	templates = 'manga_page.html'
	templates_eror   = 'error.html'
	
	chapter = MH_manga_chapter(manga_name)

	if chapter == None:

		return render(request, templates_eror)

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


# IND


def ID_manga_page(request, manga_name):

	templates = 'manga_page_id.html'
	templates_eror   = 'error.html'
	
	chapter = ID_manga_chapter(manga_name)

	if chapter == None:

		return render(request, templates_eror)

	manga_title = f'{manga_name}'
	manga_title = manga_title.split('-')

	if len(manga_title)>2:

		manga_title = manga_title[0] + ' ' + manga_title[1] + ' ' + manga_title[2] + '...'
	else:
		manga_title = manga_title[0]


	context = { 'manga' : chapter, 'manga_name' : manga_name, 'manga_title' : manga_title}
	return render(request, templates, context)

def ID_chapter_page(request, manga_name, chapter):

	templates = 'chapter_page_id.html'
	templates_eror   = 'error.html'

	image = ID_manga_image(manga_name, chapter)

	if len(chapter.split('-')) < 4:
		chapter = chapter.split('-')[-1]
		chapter = 'chapter' + ' ' + chapter
	else:
		chapter = chapter.split('-')[-3]
		chapter = 'chapter' + ' ' + chapter

	context = {'manga' : image, 'chapter' : chapter}
	return render(request, templates, context)