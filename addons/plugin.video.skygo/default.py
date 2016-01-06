#!/usr/bin/python
# -*- coding: utf-8 -*-
#import resources.lib.bs4
import urllib
import urllib2
import sys
import re
import os
import time
import shutil
import subprocess
import xbmcplugin
import xbmc
import xbmcgui
import xbmcaddon
import resources.lib.other.util as util
from resources.lib.other.channel_scrapping import *
import resources.lib.other.list_items as list_items


pluginhandle = int(sys.argv[1])
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonID = addon.getAddonInfo('id')
utilityPath = xbmc.translatePath('special://home/addons/'+addonID+'/resources/lib/other/skygov3.exe')
splashpath = xbmc.translatePath('special://home/addons/'+addonID+'/fanart.jpg')
addonUserDataFolder = xbmc.translatePath("special://profile/addon_data/"+addonID)
cacheFolder = os.path.join(addonUserDataFolder, "cache")
logostart = "http://epgstatic.sky.com/epgdata/1.0/newchanlogos/75/35/skychb"
sky_main = "http://go.sky.com/"

if not os.path.isdir(addonUserDataFolder):
    os.mkdir(addonUserDataFolder)
if not os.path.isdir(cacheFolder):
    os.mkdir(cacheFolder)


###main_urls###
catchup_main = "http://go.sky.com/vod/content/Catch_Up/content/default/promoPage.do"
tvboxsets_main = "http://go.sky.com/vod/content/TV_Box_Sets/content/default/promoPage.do"
movies_main = "http://go.sky.com/vod/content/Sky_Movies/content/l/l/content/1984/promoPage.do"


__settings__   = xbmcaddon.Addon(addonID)
username = __settings__.getSetting("username")
password = __settings__.getSetting("password")
sleep1 = __settings__.getSetting("sleep 1")
sleep2 = __settings__.getSetting("sleep 2")
mousex = __settings__.getSetting("Mousex") 
mousey = __settings__.getSetting("Mousey")
splashy = __settings__.getSetting("splashy")
focus = __settings__.getSetting("focus")
cache = __settings__.getSetting("cache")
	
def index():
		util.addDir("Live TV", "", 'listLive', "")
		util.addDir("Catch Up TV", "", 'listCatchuptv', "")
		util.addDir("TV Boxsets", "", 'tvBoxsetslist', "")
		util.addDir("Movies On Demand", "", 'movieslist', "")
		xbmcplugin.endOfDirectory(pluginhandle)
	
def playTVGuideLive(ID):
	filename = os.path.join(cacheFolder, "_Live_Channels__")	
	try:
		if util.get_mod(filename) == False:
			x = pickle.load(open(filename, "rb"))
		if util.get_mod(filename) == True:
			x = channel_scraper(filename)
	except:
		x = channel_scraper(filename)
	for i in x:
		for u in i:
			if ID == u:
				chn_URL = util.get_tvguide_playurl(i[2])
				exepass = [chn_URL, username, password, sleep1, sleep2, mousex, mousey, splashy, splashpath, focus]
				exepass2 = ' %s %s %s %s %s %s %s %s %s %s' % (chn_URL, username, password, sleep1, sleep2, mousex, mousey, splashy, splashpath, focus)
				cmd = "System.ExecWait"
				xbmc.executebuiltin("%s(\\\"%s\\\"%s\\\")" % (cmd, utilityPath, exepass2))
	
def playLiveVideo(url):
	xbmc.Player().stop()
	xbmc.executebuiltin('Notification(Loading....,Please Wait!,500,logo.png)')
	chn_URL = util.get_live_playurl(url)
	exepass = [chn_URL, username, password, sleep1, sleep2, mousex, mousey, splashy, splashpath, focus]
	subprocess.Popen([utilityPath]+exepass)
	
def playOnDemand(url):
	xbmc.Player().stop()
	xbmc.executebuiltin('Notification(Loading....,Please Wait!,500,logo.png)')
	content_url = util.get_on_playurl(url)
	exepass = [content_url, username, password, sleep1, sleep2, mousex, mousey, splashy, splashpath, focus]
	subprocess.Popen([utilityPath]+exepass)	
	
params = util.parameters_string_to_dict(sys.argv[2],1)
mode = urllib.unquote_plus(params.get('mode', ''))
url = urllib.unquote_plus(params.get('url', ''))
ID = urllib.unquote_plus(params.get('ID', ''))
epgid = urllib.unquote_plus(params.get('epgID', ''))


def main():
	if mode==None:
		pass
	if mode == "playTVGuide":
		playTVGuideLive(ID)
	if mode == "videoId":
		playOnDemand(url)
	if mode == 'playVideo':
		playLiveVideo(url)
	if mode == 'listLive':
		list_items.listLive(logostart, pluginhandle)
	elif mode == 'seriesId':
		list_items.listGrid(url, pluginhandle, sky_main)
	elif mode == 'listCatchuptv':
		list_items.listCatchuptv_menus(catchup_main, pluginhandle)
	elif mode == 'tvBoxsetslist':
		list_items.listCatchuptv_menus(tvboxsets_main, pluginhandle)
	elif mode == 'movieslist':
		list_items.listCatchuptv_menus(movies_main, pluginhandle)
	elif mode == "nomenu":
		list_items.listGrid(url, pluginhandle, sky_main)
	elif mode == "menu":
		list_items.listCatchtv_submenus(url, pluginhandle, sky_main)
	elif mode == "All":
		list_items.list_atozDir(url, pluginhandle, sky_main)
	elif mode == "atoz":
		list_items.list_atoz_series(url, pluginhandle, sky_main)
	elif mode == 'deleteCache':
		util.deleteCache()
	elif mode == 'nownnext':
		util.nownnext(epgid)
	else:
		index()

def password_check():
	if (username == "" or password == ""):
		util.pop_box("Username or Password not set","Please enter and try again","")
		addon.openSettings()
		main()
	else:
		return True

if __name__ == '__main__':
	if password_check() == True:
		main()