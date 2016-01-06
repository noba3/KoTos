#!/bin/python
import xbmc,xbmcaddon,os,sys
icon = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/iptv.png")

try: os.remove(xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/backup.xml'))
except: pass
try: os.remove(xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/set.csv'))
except: pass
xbmc.executebuiltin('XBMC.Notification(IPTVxtra Backup Deinstallation, das IPTVxtra Backup der Settings wurde deinstalliert - Kodi neu starten ,15000,'+icon+')')