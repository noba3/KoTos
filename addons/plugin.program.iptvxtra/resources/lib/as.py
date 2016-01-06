#!/bin/python
import xbmc,os,sys,shutil
icon = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra/icon.png")
from_x = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra/resources/data/advancedsettings.xml")
to_x = xbmc.translatePath("special://home/userdata/advancedsettings.xml")
try:
    shutil.copyfile(from_x, to_x)
    xbmc.executebuiltin('XBMC.Notification(Information !, die advancedsettings.xml wurde ins System kopiert ,5000,'+icon+')')
except:
    xbmc.executebuiltin('XBMC.Notification(Error !, die advancedsettings.xml konnte nicht kopiert werden ,5000,'+icon+')')