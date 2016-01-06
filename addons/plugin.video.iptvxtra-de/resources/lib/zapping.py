# -*- coding: utf-8 -*-

import xbmcgui,xbmc,os,sys
import requests as requests
xbmcPlayer = xbmc.Player()
mode = sys.argv[1]
netx = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/netx.png")
xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell, plugin://plugin.video.iptvxtra-de)") 

idx = mode.replace("url=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").replace("referer", "Referer").split('***')
xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , einen Moment der Sender wird geladen ,30000,'+idx[2]+')')
payload = {'loc': idx[4],'la':'DE'}
r = requests.get("http://api.iptvxtra.net/check.php", params = payload )
x = int(r.text)
if x > 5:
    if x == 7:
        xbmc.executebuiltin('XBMC.Notification( verbotener Mehrfach-Login !!! , Dein Zugang wird gleichzeitig von mehreren Standorten aus benutzt - bei 5 Fehlern wird der Zugang bis 24.00 GMT-0 gesperrt - Kodi bitte neu starten ,60000,'+netx+')')
    if x == 8:
        xbmc.executebuiltin('XBMC.Notification( verbotener Mehrfach-Login !!! , Dein Zugang wurde automatisch bis 24.00 GMT-0 gesperrt ,60000,'+netx+')')
    if x == 9:
        xbmc.executebuiltin('XBMC.Notification( Fehler in den Zugangsdaten  !!! , Ein Fehler wurde in den Zugangsdaten erkannt - Passwort oder Username muss verkehrt sein ,60000,'+netx+')')
    if x == 10:
        xbmc.executebuiltin('XBMC.Notification( gesperrter Zugang !!! , Dein Zugang ist auf unbestimmte Zeit gesperrt - wende dich per EMail an uns ,60000,'+netx+')')
    if x == 11:
        xbmc.executebuiltin('XBMC.Notification( kein Zugang !!! , Dein Zugang ist aus einem anderen Land registriert worden - der Zugang ist vorläufig gesperrt ,60000,'+netx+')')
    sys.exit(0)

listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
playlist.clear()
playlist.add( idx[0] + idx[3], listitem )
xbmcPlayer.play(playlist,None,False)
xbmc.executebuiltin( "Dialog.Close(infodialog)" )
sys.exit(0)