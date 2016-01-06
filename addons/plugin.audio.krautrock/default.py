# -*- coding: utf-8 -*-
# please visit http://www.iptvxtra.net

import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon,urllib

addonID = 'plugin.audio.krautrock'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')
icon = xbmc.translatePath( os.path.join( addonPath , 'icon.png' ) )
title = 'Krautrock-Radio'
stream = 'http://www.krautrock-world.com/Files/krw_96.asx'
#stream = 'http://94.249.254.14:7592'
xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
xbmc.executebuiltin("ActivateWindow(home)")
listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
playlist.clear()
playlist.add( stream, listitem )
xbmcPlayer.play(playlist)

