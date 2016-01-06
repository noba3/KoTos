#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon,shutil,urllib,time
import resources.lib.requests as requests

addonID = 'plugin.program.iptvxtra'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')

__settings__ = addon
icon = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra/icon.png")
iconb = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra/resources/iconb.png")
iconx = xbmc.translatePath("special://home/addons/plugin.program.iptvxtra/resources/iconx.png")
eco_dir = xbmc.translatePath("special://home/addons/service.xbmc.ecoupd/")
xmltv2de = xbmc.translatePath("special://temp/temp/xmltv_de_2.xmx")
xmltv2th = xbmc.translatePath("special://temp/temp/xmltv_th_2.xmx")

temp = xbmc.translatePath("special://temp/")
try:
    record_folder = xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').getSetting("record_folder")
    if record_folder == 'Kodi Cache Verzeichnis': record_folder = temp
    if not os.path.isdir(record_folder):
        xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').setSetting("record_folder","Kodi Cache Verzeichnis")
        record_folder = temp
except: record_folder = temp
record_folder = os.path.join(record_folder,'IPTVxtraPL','erfgbn.txt').replace('erfgbn.txt','')

popup = __settings__.getSetting("popup")
downloaded = 0

xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell,none)")
xbmc.executebuiltin("Skin.Reset(iptvxtra_running)")
xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")

def AutoStart():

    if __settings__.getSetting("popupx") == 'true':
        xbmc.executebuiltin('XBMC.Notification(IPTVxtra , diverse Auto-Starts werden vorbereitet ,4000,'+icon+')')


# ------------------------------------------------------------------------------------------------------------------------------------------- wiederherstellen der DE Settings - START
    try:
        sxUser = 0
        sxBackup = 0
        saveset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/backup.xml')
        orgset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/settings.xml')

        if os.path.isfile(saveset) and not os.path.isfile(orgset):
            try:
                shutil.copy(saveset, orgset)
                if __settings__.getSetting("popup") == 'true': xbmc.executebuiltin('XBMC.Notification(Backup Funktion , IPTVxtra DE-Settings wurden wiederhergestellt ,5000,'+icon+')')
                print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message-Service 100'
                print ' -----------------------------------------------------------------------------------------------------------------'
            except: pass

        try:
            fobj = open(orgset, "r") 
            for line in fobj:
                if "login" in line and "xbmcuser" in line: sxUser = 1
                if "sBackup" in line and "true" in line: sxBackup = 1
            fobj.close()
        except: pass
        if sxBackup == 0 and sxUser == 1:
            try:
                fobj = open(saveset, "r") 
                for line in fobj:
                    if "sBackup" in line and "true" in line: sxBackup = 1
                    break
                fobj.close()
            except: pass

        if os.path.isfile(saveset) and sxBackup == 1 and sxUser == 1:        # wiederherstellen  
            try: os.remove(orgset)
            except: pass
            try: 
                shutil.copy(saveset, orgset)
                if __settings__.getSetting("popup") == 'true': xbmc.executebuiltin('XBMC.Notification(Backup Funktion , IPTVxtra-DE Settings mussten wiederhergestellt werden ,5000,'+icon+')')
                print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message-Service 102'
                print ' -----------------------------------------------------------------------------------------------------------------'
            except:
                print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message-Service 103'
                print ' -----------------------------------------------------------------------------------------------------------------'
    except: 
        print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message-Service 104'
        print ' -----------------------------------------------------------------------------------------------------------------'

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   ReplayPlayer

    try: os.remove(record_folder + 'IPTVxtra.m3u8')
    except: pass
    shutil.rmtree(record_folder, ignore_errors=True)
    try:
        if len(filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder))) > 0:
            for i in filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder)):
                try: os.remove(record_folder + i)
                except: pass
    except: pass
    shutil.rmtree(record_folder, ignore_errors=True)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   EcoStream updater
    if __settings__.getSetting("ecodel") == 'true':
        try:
            if os.path.isdir(eco_dir) == True:
                shutil.rmtree(eco_dir)
                print ' --------------------------------------------------------  Verzeichnis service.xbmc.ecoupd wurde gelöscht'
        except:
            print ' --------------------------------------------------------  alter EcoUpdater-Service konnte nicht gelöscht werden'
        __settings__.setSetting("ecodel", "false")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   deutsches EPG
    if __settings__.getSetting("epgde") == 'true':
        try:
            if not os.path.isfile(xmltv2de) or os.stat(xmltv2de)[8] < (int(time.time()) - 72000) or os.path.getsize(xmltv2de) < 1200000:
                ab = requests.get('http://iptvxtra.net/xbmc/_form/session/' + xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').getSetting("login").strip() + '.DE')
                if str(ab.status_code) == '200':
                    if __settings__.getSetting("popup") == 'true':
                        xbmc.executebuiltin('XBMC.Notification(XMLTV , deutsches EPG File wird geladen ,4000,'+iconx+')')
                    try: urllib.urlretrieve('http://srv1.iptvxtra.net/xmltv/xmltv_de_2.xmx', xmltv2de)
                    except: urllib.urlretrieve('http://srv3.iptvxtra.net/xmltv/xmltv_de_2.xmx', xmltv2de)
                    print ' --------------------------------------------------------  DE XMLTV geladen'
        except:
            print ' --------------------------------------------------------  DE I.XMLTV konnte nicht geladen werden'

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   thailändisches EPG
    if __settings__.getSetting("epgth") == 'true':
        try:
            if not os.path.isfile(xmltv2th) or os.stat(xmltv2th)[8] < (int(time.time()) - 72000) or os.path.getsize(xmltv2th) < 1800000:
                ab = requests.get('http://iptvxtra.net/xbmc/_form/session/' + xbmcaddon.Addon(id = 'plugin.video.iptvxtra-th').getSetting("login").strip() + '.TH')
                if str(ab.status_code) == '200':
                        if __settings__.getSetting("popup") == 'true':
                            xbmc.executebuiltin('XBMC.Notification(XMLTV , thailaendisches EPG File wird geladen ,4000,'+iconx+')')
                        try: urllib.urlretrieve('http://srv1.iptvxtra.net/xmltv/xmltv_th_2.xmx', xmltv2th)
                        except: urllib.urlretrieve('http://srv3.iptvxtra.net/xmltv/xmltv_th_2.xmx', xmltv2th)
                        print ' --------------------------------------------------------  TH XMLTV geladen'
        except:
            print ' --------------------------------------------------------  TH XMLTV konnte nicht geladen werden'

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   Programm Starter
    if __settings__.getSetting("de") == 'true':
        __settings__.setSetting("th", "false")
        __settings__.setSetting("sport", "false")
        try:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.iptvxtra-de)')
        except:
            __settings__.setSetting("de", "false")
            print ' --------------------------------------------------------  IPTVxtra-DE nicht installiert'

    if __settings__.getSetting("th") == 'true':
        __settings__.setSetting("de", "false")
        __settings__.setSetting("sport", "false")
        try:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.iptvxtra-th)')
        except:
            __settings__.setSetting("th", "false")
            print ' --------------------------------------------------------  IPTVxtra-TH nicht installiert'

    if __settings__.getSetting("sport") == 'true':
        __settings__.setSetting("th", "false")
        __settings__.setSetting("de", "false")
        try:
            print ' --------------------------------------------------------  Plugin s.p.o.r.t.TV'
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.s.p.o.r.t)')
        except:
            __settings__.setSetting("sport", "false")
            print ' --------------------------------------------------------  Plugin s.p.o.r.t.TV nicht installiert'

    if __settings__.getSetting("alt1") == 'true':
        try:
            print ' --------------------------------------------------------  alternatives Plugin'
            xbmc.executebuiltin('XBMC.RunAddon('+ __settings__.getSetting("alt2")+')')
        except:
            __settings__.setSetting("alt1", "false")
            print ' --------------------------------------------------------  alternatives Plugin nicht installiert'

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   Player Info
    if __settings__.getSetting("playerinfox") == 'true':
        try:
            print ' --------------------------------------------------------  Playerinfo gestartet'
            if __settings__.getSetting("popup") == 'true':
                xbmc.executebuiltin('XBMC.Notification(Stream Restart , Stream-Restarter wird geladen ,4000,'+iconb+')')
            xbmc.sleep(3000)
            xbmc.executescript('special://home/addons/plugin.program.iptvxtra/playerinfo.py')
        except:
            __settings__.setSetting("playerinfox", "false")
            print ' --------------------------------------------------------  Playerinfo kann nicht gestartet werden'

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   EcoUpdater
    if __settings__.getSetting("eco") == 'true':
        try:
            xbmc.executebuiltin('XBMC.RunPlugin(plugin://plugin.program.ecoupd)')
        except:
            __settings__.setSetting("eco", "false")
            xbmc.executebuiltin('XBMC.Notification(Error EcoUpdater, der EcoUpdater ist nicht installiert ,4000,'+icon+')')
            print ' --------------------------------------------------------  EcoUpdater nicht installiert'

# --------------------------------------------------------------------------------------------------------------------------------------------------------------   advancedsettings
    if __settings__.getSetting("as") == 'true':
        try:
            __settings__.setSetting("as", "false")
            xbmc.executebuiltin('XBMC.Notification(advancedsettings.xml, die advancedsettings.xml wurde kopiert - beim nächsten Neustart ist diese erst aktiv ,6000,'+icon+')')
        except:
            __settings__.setSetting("as", "false")
            xbmc.executebuiltin('XBMC.Notification(Error advancedsettings.xml, die advancedsettings.xml wurde nicht integriert ,4000,'+icon+')')
            print ' --------------------------------------------------------  advancedsettings.xml nicht installiert'


if 'start'in sys.argv[2]:
    AutoStart()
else:
    addon.openSettings()


