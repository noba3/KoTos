#!/bin/python
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys
import shutil
addon = xbmcaddon.Addon('plugin.video.iptvxtra-de')
pfad = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
icon = xbmc.translatePath(pfad + "/resources/lib/iptv.png")

dest = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de-more")
shutil.rmtree(dest, ignore_errors=True)
xbmc.executebuiltin('XBMC.Notification(IPTVxtra more TV Deinstallation, das IPTVxtra more TV Addon wurde deinstalliert - Kodi neu starten ,15000,'+icon+')')