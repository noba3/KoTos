#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib,urllib2,sys,os
import xbmcplugin,xbmcgui,xbmc,xbmcaddon

addon = xbmcaddon.Addon('plugin.program.ecoupd')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id="plugin.program.ecoupd")
lastupd = __settings__.getSetting("lastupd")
urlresPath = xbmc.translatePath("special://home/addons/script.module.urlresolver/lib/urlresolver/plugins/")
icon = xbmc.translatePath("special://home/addons/plugin.program.ecoupd/icon.png")

if not lastupd:
    lastupd = "201401010000"

Server01 = ('http://www.IPTVxtra.net/xbmc/_ecostream/','IPTVxtra.net')
Server02 = ('http://srv1.iptvxtra.net/xbmc/_ecostream/','IPTVxtra.net')
Server03 = ('http://www.bitsandtunes.de/ecostream/','Schwaller')
Server04 = ('','')
Server05 = ('','')
date   = '0'
date01 = '0'
date02 = '0'
date03 = '0'
date04 = '0'
date05 = '0'

if os.path.exists(urlresPath):
    if Server01[0]:
        try:
            data01 = urllib2.urlopen(Server01[0] + "eco.txt")
            file01 = data01.readlines()[0]
            date01 = file01.partition('-')
            date01 = date01[2].partition('.')
            date01 = date01[0]
            if len(date01) != 12:
                date01 = '201401010000'
        except:
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++  error - server 1 not found  ++++++++++++++++++++++++++'
            xbmc.executebuiltin('XBMC.Notification(EcoUpdater: Serverfehler, Server 1 ist offline,4000,'+icon+')')
    if Server02[0]:
        try:
            data02 = urllib2.urlopen(Server02[0] + "eco.txt")
            file02 = data02.readlines()[0]
            date02 = file02.partition('-')
            date02 = date02[2].partition('.')
            date02 = date02[0]
            if len(date02) != 12:
                date02 = '201401010000'
        except:
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++  error - server 2 not found  ++++++++++++++++++++++++++'
            xbmc.executebuiltin('XBMC.Notification(EcoUpdater: Serverfehler, Server 2 ist offline,4000,'+icon+')')
    if Server03[0]:
        try:
            data03 = urllib2.urlopen(Server03[0] + "eco.txt")
            file03 = data03.readlines()[0]
            date03 = file03.partition('-')
            date03 = date03[2].partition('.')
            date03 = date03[0]
            if len(date03) != 12:
                date03 = '201401010000'
        except:
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++  error - server 3 not found  ++++++++++++++++++++++++++'
            xbmc.executebuiltin('XBMC.Notification(EcoUpdater: Serverfehler, Server 3 ist offline,4000,'+icon+')')
    if Server04[0]:
        try:
            data04 = urllib2.urlopen(Server04[0] + "eco.txt")
            file04 = data04.readlines()[0]
            date04 = file04.partition('-')
            date04 = date04[2].partition('.')
            date04 = date04[0]
            if len(date04) != 12:
                date04 = '201401010000'
        except:
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++  error - server 4 not found  ++++++++++++++++++++++++++'
            xbmc.executebuiltin('XBMC.Notification(EcoUpdater: Serverfehler, Server 4 ist offline,4000,'+icon+')')
    if Server05[0]:
        try:
            data05 = urllib2.urlopen(Server05[0] + "eco.txt")
            file05 = data05.readlines()[0]
            date05 = file05.partition('-')
            date05 = date05[2].partition('.')
            date05 = date05[0]
            if len(date05) != 12:
                date05 = '201401010000'
        except:
            print '++++++++++++++++++++++++++++++++++++++++++++++++++++  error - server 5 not found  ++++++++++++++++++++++++++'
            xbmc.executebuiltin('XBMC.Notification(EcoUpdater: Serverfehler, Server 5 ist offline,4000,'+icon+')')


    if int(date01) > int(date):
        Server = Server01[0]
        user = Server01[1]
        file = file01
        date = date01
    if int(date02) > int(date):
        Server = Server02[0]
        user = Server02[1]
        file = file02
        date = date02
    if int(date03) > int(date):
        Server = Server03[0]
        user = Server03[1]
        file = file03
        date = date03
    if int(date04) > int(date):
        Server = Server04[0]
        user = Server04[1]
        file = file04
        date = date04
    if int(date05) > int(date):
        Server = Server05[0]
        user = Server05[1]
        file = file05
        date = date05


    if int(lastupd) < int(date):
        __settings__.setSetting("lastupd", date)
        urllib.urlretrieve (Server + "/" + file, urlresPath + "ecostream.py")
        datex = date[6:8]+'.'+date[4:6]+'.'+date[0:4]+' '+date[8:10]+':'+date[10:12]+' Uhr'
        xbmc.executebuiltin('XBMC.Notification(EcoUpdater: Download OK ,du hast von '+user+' auf die Dateiversion vom '+datex+' aktualisiert,10000,'+icon+')')
    else:
        xbmc.executebuiltin('XBMC.Notification(EcoUpdater: keine neue Datei gefunden, du bist auf dem neuesten Stand oder versuche es spaeter noch einmal,10000,'+icon+')')
else:
    xbmc.executebuiltin('XBMC.Notification(EcoUpdater:  Error, der UrlResolver ist nicht installiert oder das Verzeichnis existiert nicht,10000,'+icon+')')



