from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import util
import xbmcgui
import marshal as pickle



def scrapODmenus(url,level, filename):
	
		ondemand_menu_database = []
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
		req = Request(url, None, headers)
		html = urlopen(req).read()
		soup = BeautifulSoup(html)
		all_menus = soup.find("div", "leftNav")
		noItems = len(all_menus.findAll("li"))
		percent_per_loop = 100.00/noItems
		progress = 1
		pDialog = xbmcgui.DialogProgress()
		ret = pDialog.create('Skygo V2', ('Caching %s items' % noItems), "Will load instantly next time")
		for x in all_menus.findAll("li"):
			for menu in x.findAll('a', href=True):
				menu_name = str(menu.text)
				menu_url = menu['href']
				mode = util.check_mode(menu_name, menu_url, level)
				ondemand_menu_database.append([menu_name, menu_url, mode])
				progress = progress+1
				completed = int(progress*percent_per_loop)
				pDialog.update(completed)
		pickle.dump(ondemand_menu_database,  open(filename, "wb"))
		return ondemand_menu_database