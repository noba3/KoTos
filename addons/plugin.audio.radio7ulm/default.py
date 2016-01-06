# -*- coding: cp1254 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys
icondir = xbmc.translatePath("special://home/addons/plugin.audio.radio7ulm/icons/")
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

add_video_item('http://srv01.radio7.fmstreams.de/stream1/livestream.mp3',{ 'title': 'Radio 7 - Webradio'},img=icondir + 'radio-7_web.png')
add_video_item('http://srv02.radio7.fmstreams.de/radio7_upa',{ 'title': 'Radio 7 - 80er'},img=icondir + 'radio-7_80er.png')
add_video_item('http://srv02.radio7.fmstreams.de/radio7_downa',{ 'title': 'Radio 7 - Herz'},img=icondir + 'radio-7_herz.png')
add_video_item('http://str0.creacast.com/radio7_acta',{ 'title': 'Radio 7 - OnTour'},img=icondir + 'radio-7_ontour.png')
add_video_item('http://srv01.radio7.fmstreams.de/stream5/livestream.mp3',{ 'title': 'Radio 7 - Live'},img=icondir + 'radio-7_live.png')
xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")