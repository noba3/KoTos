# -*- coding: cp1254 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys
icondir = xbmc.translatePath("special://home/addons/plugin.audio.ballermann/icons/")
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

add_video_item('http://stream.bmr-radio.de/;stream.mp3',{ 'title': 'Radio Ballermann'},img=icondir + 'baller.png')
add_video_item('http://country.bmr-radio.com:8000/;stream.mp3',{ 'title': 'Radio Ballermann - Country'},img=icondir + 'baller-country.png')
add_video_item('http://party.bmr-radio.de:8100/;stream.mp3',{ 'title': 'Radio Ballermann - Party'},img=icondir + 'baller-party.png')
add_video_item('http://top100.bmr-radio.com:8000/;stream.mp3',{ 'title': 'Radio Ballermann - Top 100'},img=icondir + 'baller-top100.png')

xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")