import resources.lib.other.util as util
import sys
import urllib
import urllib2
import scrap_grid
import xbmcplugin
import xbmc
import xbmcgui
import xbmcaddon
from channel_scrapping import *
import scrap_menus
import util
import scrap_atoz
import marshal as pickle
import os

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonID = addon.getAddonInfo('id')
addonUserDataFolder = xbmc.translatePath("special://profile/addon_data/"+addonID)
cacheFolder = os.path.join(addonUserDataFolder, "cache")


def listLive(logostart, pluginhandle):
	filename = os.path.join(cacheFolder, "_Live_Channels__")	
	try:
		if util.get_mod(filename) == False:
			x = pickle.load(open(filename, "rb"))
		if util.get_mod(filename) == True:
			x = channel_scraper(filename)
	except:
		x = channel_scraper(filename)
	for i in x:
		name = i[0]
		channelID = i[1]
		channel_url = i[2]
		epg_id = i[3]
		nextMode = "playVideo"
		joined = "name="+urllib.quote_plus(name)+"&channel_id="+urllib.quote_plus(channelID)+"&channel_url="+urllib.quote_plus(channel_url)+"&epgID="+urllib.quote_plus(epg_id)
		thumbUrl = logostart+epg_id+".png"
		util.addDir(name, joined, nextMode, thumbUrl)
		added = True
	xbmcplugin.endOfDirectory(pluginhandle)

def listGrid(url, pluginhandle, sky_main):
	grid_url = urllib.unquote_plus(util.parameters_string_to_dict(url,0)['end_of_url'])
	filename = util.filename_creator(grid_url)	
	try:
		if util.get_mod(filename) == False:
			x = pickle.load(open(filename, "rb"))
		if util.get_mod(filename) == True:
			x = scrap_grid.grid_scraper(grid_url, filename)
	except:
		x = scrap_grid.grid_scraper(grid_url, filename)
	for i in x:
		name = i[0]
		url = i[1]
		thumb_end = i[2]
		nextMode = i[3]
		if thumb_end[0:2] == 'ht':
			thumbUrl = thumb_end
		else:
			x = urllib.quote(thumb_end)
			thumbUrl = sky_main+x
		joined = "name="+urllib.quote_plus(name)+"&end_of_url="+urllib.quote_plus(url)
		util.addDir(name, joined, nextMode, thumbUrl)
		added = True
	xbmcplugin.endOfDirectory(pluginhandle)
	
def listCatchuptv_menus(menu_url, pluginhandle):
	level = 0
	filename = util.filename_creator(menu_url)	
	try:
		if util.get_mod(filename) == False:
			x = pickle.load(open(filename, "rb"))
		if util.get_mod(filename) == True:
			x = scrap_menus.scrapODmenus(menu_url, level, filename)
	except:
		x = scrap_menus.scrapODmenus(menu_url, level, filename) #create cache files and returns the database
	for i in x:
		name = i[0]
		url = i[1]
		mode = i[2]
		join = "name="+urllib.quote_plus(name)+"&end_of_url="+urllib.quote_plus(url)
		thumbUrl = ""
		util.addDir(name, join, mode, thumbUrl)
		added = True
	xbmcplugin.endOfDirectory(pluginhandle)

def listCatchtv_submenus(url, pluginhandle, sky_main):
	sub_url = sky_main+urllib.unquote_plus(util.parameters_string_to_dict(url,0)['end_of_url'])
	level = 1
	filename = util.filename_creator(sub_url)	
	try:
		if util.get_mod(filename) == False:
			x = pickle.load(open(filename, "rb"))
		if util.get_mod(filename) == True:
			x = scrap_menus.scrapODmenus(sub_url, level, filename)
	except:
		x = scrap_menus.scrapODmenus(sub_url, level, filename) #create cache files and returns the database
	for i in x:
		name = i[0]
		url = i[1]
		mode = i[2]
		join = "name="+urllib.quote_plus(name)+"&end_of_url="+urllib.quote_plus(url)
		thumbUrl = ""
		util.addDir(name, join, mode, thumbUrl)
		added = True
	xbmcplugin.endOfDirectory(pluginhandle)
	
def list_atozDir(url, pluginhandle, sky_main):
	list_url = sky_main+urllib.unquote_plus(util.parameters_string_to_dict(url,0)['end_of_url'])
	x = scrap_atoz.scrap_atozdir(list_url)
	for i in x:
		name = i[1]
		url = i[0]
		mode = "atoz"
		thumbUrl = ''
		util.addDir(name, url, mode, thumbUrl)
		added = True
	xbmcplugin.endOfDirectory(pluginhandle)
	
def list_atoz_series(url, pluginhandle, sky_main):
	atoz_url = sky_main+url
	filename = util.filename_creator(atoz_url)
	try:
		if util.get_mod(filename) == False:
			x = pickle.load(open(filename, "rb"))
		if util.get_mod(filename) == True:
			x = scrap_atoz.scrap_itemorvideoid_atoz(atoz_url, filename)
	except:
		x = scrap_atoz.scrap_itemorvideoid_atoz(atoz_url, filename)
	for i in x:
		name = i[0]
		url = i[1]
		nextMode = i[2]
		thumb_end = i[3]
		if thumb_end[0:2] == 'ht':
			thumbUrl = thumb_end
		else:
			x = urllib.quote(thumb_end)
			thumbUrl = sky_main+x
		joined = "name="+urllib.quote_plus(name)+"&end_of_url="+urllib.quote_plus(url)
		util.addDir(name, joined, nextMode, thumbUrl)
		added = True
	xbmcplugin.endOfDirectory(pluginhandle)