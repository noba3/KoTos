#!/bin/python
import xbmcgui,xbmc,os,sys
import requests as requests
icon = xbmc.translatePath("special://home/addons/plugin.video.streamnetwork/icon.png")
xbmcPlayer = xbmc.Player()
mode = sys.argv[1]
idx = mode.replace("url=", "").split('***')
try: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' , einen Moment der Sender wird geladen ,5000,'+idx[5]+')')
except: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' , einen Moment der Sender wird geladen ,5000,'+icon+')')
load = {'name': idx[0],'passwd': idx[1],'ch' : idx[2],'srv' : idx[3]}
try:
    r = requests.get("http://xbmc.streamnetwork.tv/api.php", params=load)
except:
    xbmc.executebuiltin('XBMC.Notification(Netzwerk Fehler , der Login Server ist nicht erreichbar ,7000,'+icon+')')
    sys.exit(0)
url_play = r.text.strip()
try: listitem = xbmcgui.ListItem( idx[4], iconImage=idx[5], thumbnailImage=idx[5])
except: listitem = xbmcgui.ListItem( idx[4], iconImage=icon, thumbnailImage=icon)
playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
playlist.clear()
playlist.add( url_play, listitem )
xbmcPlayer.play(playlist,None,False)
sys.exit(0)


