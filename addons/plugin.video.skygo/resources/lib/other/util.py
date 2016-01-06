import xbmcplugin
import xbmc
import xbmcgui
import xbmcaddon
import sys
import urllib
import urllib2
import shutil
from bs4 import BeautifulSoup
from resources.lib.mechanize import Browser
import re
import datetime
import os
import meta


addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addonID = addon.getAddonInfo('id')
addonUserDataFolder = xbmc.translatePath("special://profile/addon_data/"+addonID)
cacheFolder = os.path.join(addonUserDataFolder, "cache")


__settings__   = xbmcaddon.Addon(addonID)
username = __settings__.getSetting("username")
password = __settings__.getSetting("password")
cache = int(__settings__.getSetting("cache"))

def pop_box(line1, line2, line3):
	xbmcgui.Dialog().ok(addonname, line1, line2, line3)
	
def parameters_string_to_dict(parameters,y):
    paramDict = {}
    if parameters:
        paramPairs = parameters[y:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict
	
def addDir(name, url, mode, iconimage):
	u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&thumb="+urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultTVShows.png", thumbnailImage=iconimage)
	liz.setInfo(type="video", infoLabels={"title": name, "Year": "", "Plot": "", "Genre" : ""})
	entries = []
	if mode == "playVideo":
		x = parameters_string_to_dict(url,0)
		epgid = urllib.unquote_plus(x.get('epgID', ''))
		entries.append(("What's On Now & Next", 'RunPlugin(plugin://plugin.video.skygo/?mode=nownnext&epgID='+epgid+')',))
	liz.addContextMenuItems(entries)
	ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
	return ok
	
def scrap_asset(url):
	LOGIN_URL = 'https://skyid.sky.com/signin/skygo'
	sky_main = "http://go.sky.com"
	chopped_url = url[:-35]
	full_url = sky_main+chopped_url+"l/l/content/videoActions.do"
	br = Browser() 					# Create a browser
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36')]
	br.open(LOGIN_URL)            # Open the login page
	br.select_form(name="signinform")  # Find the login form
	br['username'] = username     # Set the form values
	br['password'] = password
	resp = br.submit()	# Submit the form
	title = br.title()
	if title[0:15].lower() == "watch tv online":
		x = br.open(full_url)
		html = x.read()
	assetid_S = html.find("assetId") + 10
	assetid_E = html.find("'", assetid_S)
	assetID = html[assetid_S:assetid_E]
	return assetID
	
def get_on_playurl(url):
	video_url = urllib.unquote_plus(parameters_string_to_dict(url,0)['end_of_url'])
	vidID_s = video_url.find("videoId") + 8
	vidID_e = video_url.find("/", vidID_s)
	videoId = video_url[vidID_s:vidID_e]
	assetId = scrap_asset(video_url)
	ondemandplay_url = "http://go.sky.com/vod/content/Catch_Up/content/assetId/"+assetId+"____/videoId/"+videoId+"/l/l/content/progressivePlay.do"
	return ondemandplay_url
	
def get_live_playurl(url):
	url_split = parameters_string_to_dict(url,0)
	chn_URL = url_split['channel_url']
	BASE_URL = "http://go.sky.com/vod/content/Home/content/videoId/"
	ENDOFURL = "/l/l/content/detachedLiveTv.do"
	full_url = "".join((BASE_URL, chn_URL, "____", ENDOFURL))
	return full_url
	
def get_tvguide_playurl(chn_URL):
	BASE_URL = "http://go.sky.com/vod/content/Home/content/videoId/"
	ENDOFURL = "/l/l/content/detachedLiveTv.do"
	full_url = "".join((BASE_URL, chn_URL, "____", ENDOFURL))
	return full_url
	
def menu_check(url):
	sky_main = "http://go.sky.com"
	full_url = sky_main+url
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}
	req = urllib2.Request(full_url, None, headers)
	html = urllib2.urlopen(req).read()
	var = html.find("<h2>")
	var2 = html.find("</h2>")
	x = html[var:var2].lower()
	if "catch up" in x or "sky movies" in x or "tv box sets" in x:
		return True
		
def alt_check(url):
	sky_main = "http://go.sky.com/"
	full_url = sky_main+url	
	html = urllib2.urlopen(full_url).read()
	soup = BeautifulSoup(html)
	h2 = soup.find("h2")	
	x = str(h2).lower()
	if "catch up" in x or "sky movies" in x or "tv box sets" in x:
		return True
		
def check_mode(menu_name, menu_url, level):		
		if level == 0:
			if menu_name != "All":
				mode_check = menu_check(menu_url)
				if mode_check == True and menu_name != "All":
					mode = "nomenu"
				else:
					mode = "menu"
			else:
				mode = "All"
			
		else:
			if menu_name != "All":
				mode = "nomenu"
			else:
				mode = "All"
		return mode

def unescapes(text):
    try:
        rep = {"%26":"&","&#38;":"&","&amp;":"&","&#044;": ",","&nbsp;": " ","\n": "","\t": "","\r": "","%5B": "[","%5D": "]",
               "%3a": ":","%3A":":","%2f":"/","%2F":"/","%3f":"?","%3F":"?","%3d":"=","%3D":"=","%2C":",","%2c":",","%3C":"<",
               "%20":" ","%22":'"',"%3D":"=","%3A":":","%2F":"/","%3E":">","%3B":",","%27":"'","%0D":"","%0A":"","%92":"'",
               "&lt;": "<","&gt;": ">","&quot": '"',"&rsquo;": "'","&acute;": "'"}
        for s, r in rep.items():
            text = text.replace(s, r)
        text = re.sub(r"<!--.+?-->", "", text)    
    except TypeError: pass
    return text
	
def get_mod(filename):
		today = datetime.datetime.today()
		modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
		duration = today - modified_date
		return duration > datetime.timedelta(days=cache)
		
def filename_creator(url):
	file = url.replace("/l/l/","")
	rep = {"/l/l/":"","http://go.sky.com/vod/content/":"_","/":"_","?":"",".":"","promoPage":"",
			"content":"","do":"","default":"","1984":"","aToZindex":""}
	for s, r in rep.items():
		file = file.replace(s, r)
	if "seriesId" in file:
		head, sep, tail = file.partition('seriesId')
		file = sep+tail
	else:
		pass	
	filename = os.path.join(cacheFolder, file,)
	return filename
	
def deleteCache():
	dialog = xbmcgui.Dialog()
	ret = dialog.yesno('Skygo V2', 'Do you want delete all cache files?')
	if ret:
		if os.path.exists(cacheFolder):
			try:
				shutil.rmtree(cacheFolder)
				pop_box("Cache has been deleted","","")
			except:
				shutil.rmtree(cacheFolder)
	else:
		pass

	
def TextBoxes(heading,anounce):
        class TextBox():
            """Thanks to BSTRDMKR for this code:)"""
                # constants
            WINDOW = 10147
            CONTROL_LABEL = 1
            CONTROL_TEXTBOX = 5

            def __init__( self, *args, **kwargs):
                # activate the text viewer window
                xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )
                # get window
                self.win = xbmcgui.Window( self.WINDOW )
                # give window time to initialize
                xbmc.sleep( 500 )
                self.setControls()


            def setControls( self ):
                # set heading
                self.win.getControl( self.CONTROL_LABEL ).setLabel(heading)
                try:
                        f = open(anounce)
                        text = f.read()
                except:
                        text=anounce
                self.win.getControl( self.CONTROL_TEXTBOX ).setText(text)
                return
        TextBox()
		
def nownnext(id):
	title, meta_info = meta.scrape_nownext(id)
	now_next = ""
	for x in meta_info:
		now_next += "[B]"+x[0]+"[/B] - [B]"+str(x[2])+"[/B] - [B]"+str(x[3])+" minutes [/B][CR]"+str(x[1])+"[CR]"
	TextBoxes("What's On - "+title,now_next)