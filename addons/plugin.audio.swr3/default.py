# -*- coding: utf-8 -*-
# please visit http://www.iptvxtra.net

import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon,urllib

addonID = 'plugin.audio.swr3'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')
icon = xbmc.translatePath( os.path.join( addonPath , 'icon.png' ) )
title = 'SWR3 Elch Radio'
stream = 'http://swr-mp3-m-swr3.akacast.akamaistream.net/7/720/137136/v1/gnl.akacast.akamaistream.net/swr-mp3-m-swr3'
xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
xbmc.executebuiltin("ActivateWindow(home)")
listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
playlist.clear()
playlist.add( stream, listitem )
xbmcPlayer.play(playlist)

