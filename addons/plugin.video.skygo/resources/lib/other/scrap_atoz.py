from bs4 import BeautifulSoup
import urllib2
import util
import time
import marshal as pickle
import urllib
import os
import datetime
import meta
import xbmcgui
	
def scrap_itemorvideoid_atoz(url, filename):

		sky_main = "http://go.sky.com/"
		pDialog = xbmcgui.DialogProgress()
		
		atoz_database = []
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
		req = urllib2.Request(url, None, headers)
		html = urllib2.urlopen(req).read()
		soup = BeautifulSoup(html)
		
		all = soup.find("tbody", "ResultRows")
		progress = 0
		noItems = int(len(all)/2.00)
		z = 100/noItems
		percent_per_loop = 100.00/noItems
		progress = 1
		
		ret = pDialog.create('Skygo V2', ('Caching %s items' % noItems), "Will load instantly next time")
		
		for x in all.findAll("tr"):
			temp_list = []
			for y in x.findAll("td"):
				text = str(y.text)
				temp_list.extend([text])
			temp_list.pop(-1)
			for menu in x.findAll('a', href=True):
				item_url = str(menu['href'])
				startMode = item_url.find("ent/", 30) + 4
				endMode = item_url.find("Id", startMode) + 2
				nextMode = str(item_url[startMode:endMode])
				fullURL = sky_main+item_url
				if nextMode == "seriesId":
					meta_info = meta.scrap_meta_series(fullURL)
				else:
					meta_info = meta.scrap_meta_episode(fullURL)
				img = meta_info[1]
				temp_list.insert(1, item_url)
				temp_list.insert(2, nextMode)
				temp_list.insert(3, img)
			atoz_database.append(temp_list)
			progress = progress+1
			completed = int(progress*percent_per_loop)
			pDialog.update(completed)
		pickle.dump(atoz_database,  open(filename, "wb"))	
		return atoz_database
		
def scrap_atozdir(url):
	
		atoz = []
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
		req = urllib2.Request(url, None, headers)
		html = urllib2.urlopen(req).read()
		soup = BeautifulSoup(html)
		
		all = soup.find("ul", id="alphabet")
		for menu in all.findAll('a', href=True):
			item_url = menu['href']
			name = str(menu.text)
			atoz.append([item_url, name])
		return atoz