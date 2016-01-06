from bs4 import BeautifulSoup
import urllib2
import util
import time
import pickle
import urllib
import os
import datetime
import _strptime
import time

def scrap_meta_episode(url):
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
	req = urllib2.Request(url, None, headers)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html)
	program_syn = soup.find("div", "synopsis")
	program_info = soup.find("div", "playerArea")
	item_meta = []
	try:
		for syn in program_syn.findAll('p'):
			synopis = str(syn.text.encode('ascii', 'ignore'))
			item_meta.extend([synopis])
		img = program_info.find('img')['src']
		item_meta.append(str(img))
		for li in program_syn.findAll('li'):
			text = str(li.text.encode('ascii', 'ignore'))
			item_meta.extend([text])
		item_meta.pop(-1)
		for ul in program_info.findAll('ul'):
			for li in ul.findAll('li'):
				meta = util.unescapes(str(li.text.encode('ascii', 'ignore')))
				item_meta.extend([meta])
		img = program_info.find('img')['src']
		item_meta.append(str(img))
		return item_meta
	except:
		return item_meta
		pass
		
		
	
def scrap_meta_series(url):
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
	req = urllib2.Request(url, None, headers)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html)
	series_syn = soup.find("div", "promoRow seriesTopRow ATI_seriesHomepageTopRow")
	series_meta = []
	for syn in series_syn.findAll('p'):
		synopis = str(syn.text.encode('ascii', 'ignore'))
		series_meta.extend([synopis])
	series_meta.pop(-1)
	img = series_syn.find('img')['src']
	series_meta.append(str(img))
	return series_meta
	
def scrape_nownext(id):
	
	url = "http://go.sky.com/tvlistings-proxy/TvListingsApi/xml/v2/nowNextLater.do?channelIds="+id+"&siteId=4&accessKey=fdgJRTd345S4fKMER92mddSFJWERJ35285FDdm3412jdRTmsdd"

	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
	req = urllib2.Request(url, None, headers)
	xml = urllib2.urlopen(req).read()
	soup = BeautifulSoup(xml)
	
	channel_title = soup.find("title").text
	nownext = []
	for programs in soup.findAll("programme"):
		title = programs.find('title')
		title = title.text.encode('ascii', 'ignore')
		desc = programs.find('shortdesc')
		desc = desc.text.encode('ascii', 'ignore')
		start = programs.find('startdatetime').text
		try:
			s = datetime.datetime.strptime(start, "%Y%m%d%H%M%S")
		except:
			s = datetime.datetime(*(time.strptime(start, "%Y%m%d%H%M%S")[0:6]))
		dt = str(s.strftime('%H:%M %d %b %y'))
		duration = int(programs.find('duration').text)/60
		nownext.append([title, desc, dt, duration])
	return channel_title, nownext