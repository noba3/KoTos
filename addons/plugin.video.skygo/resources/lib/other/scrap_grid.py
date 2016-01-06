import urllib2
import urllib
from bs4 import BeautifulSoup
import util
import time
import marshal as pickle
import os
import datetime
import meta
import xbmcgui

def grid_scraper(menu_url, filename):
	
	sky_main = "http://go.sky.com/"
	full_url = sky_main+menu_url
	pDialog = xbmcgui.DialogProgress()

	
	grid_database = []
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
	req = urllib2.Request(full_url, None, headers)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html)
	
	
	gridItems = soup.find("div", "listRows ATI_listRows")
	
	noItems = int(len(gridItems)/2.00)
	percent_per_loop = 100.00/noItems
	progress = 1
	
	
	ret = pDialog.create('Skygo V2', ('Caching %s items' % noItems), "Will load instantly next time")
	for x in gridItems.findAll("div"):
		for menu in x.findAll('a', "teaserImageLnk", href=True):
			item_url = str(menu['href'])
		for t in x.findAll('span', "clickAttractor" , ['title']):
			title = str(t.next_sibling.encode('ascii', 'ignore'))
		#img = x.find('img')['src']
		startMode = item_url.find("tent/", 15) + 5
		endMode = item_url.find("Id", startMode) + 2
		nextMode = str(item_url[startMode:endMode])
		fullURL = sky_main+item_url
		if nextMode == "seriesId":
			meta_info = meta.scrap_meta_series(fullURL)
		else:
			meta_info = meta.scrap_meta_episode(fullURL)
		try:
			img = meta_info[1]
		except:
			img = ""
		grid_database.append([title, item_url, img, nextMode])
		progress = progress+1
		completed = int(progress*percent_per_loop)
		pDialog.update(completed)
	pickle.dump(grid_database, open(filename, "wb"))
	return grid_database