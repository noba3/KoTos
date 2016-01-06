#!/bin/python
import xbmc
xbmc.executebuiltin( "Dialog.Close(all,true)" )
icon = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra/icon.png") 
xbmc.executebuiltin('XBMC.Notification(manuelles Update , die Suche kann bis zu 2 Minuten dauern bis alle Updates gefunden wurden ,30000,'+icon+')')
xbmc.executebuiltin("UpdateLocalAddons")
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UpdateLocalAddons'
xbmc.executebuiltin("UpdateAddonRepos")
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UpdateAddonRepos'