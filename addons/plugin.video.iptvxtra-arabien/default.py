# -*- coding: cp1254 -*-
# for more info please visit http://www.iptvxtra.net


import sys,xbmc,xbmcaddon
if 'extrafanart' in sys.argv[2]: sys.exit(0)

if 'runstream' in sys.argv[2]:
    url = sys.argv[2].replace('?runstream=','')
    px = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-arabien/resources/lib/zapping.py")
    xbmc.executebuiltin('RunScript('+px+',url='+url+')')
    sys.exit(0)
if 'settings' in sys.argv[2]:
    xbmcaddon.Addon('plugin.video.iptvxtra-arabien').openSettings()
    sys.exit(0)

import resources.lib.requests as requests
import base64,cookielib,urllib2,urllib,re,os,xbmcplugin,xbmcgui,hashlib
from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
Addon = xbmcaddon.Addon('plugin.video.iptvxtra-arabien')
profile = xbmc.translatePath(Addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id="plugin.video.iptvxtra-arabien")
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
net = xbmc.translatePath( os.path.join( home, 'resources/lib/net.png') )
user = __settings__.getSetting("user")
pwd = __settings__.getSetting("password")
setBack = __settings__.getSetting('setBack')
views = __settings__.getSetting('views')
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
mode = sys.argv[2]
xcat = 0

def main():
    xcat = 0
    if 'xcat1' in mode: 
        file = get_status(1)
        xcat = 1
        file = file.replace('arabien.xml','arabien1.xml')
        addLink('in this category operate about 70% of the channels','',icon)
    elif 'xcat2' in mode: 
        file = get_status(2)
        xcat = 2
        file = file.replace('arabien.xml','arabien2.xml')
    elif 'xcat3' in mode: 
        file = get_status(3)
        xcat = 3
        file = file.replace('arabien.xml','arabien3.xml')
    elif 'xcat4' in mode: 
        file = get_status(4)
        xcat = 4
        file = file.replace('arabien.xml','arabien4.xml')
    elif 'xcat5' in mode: 
        file = get_status(10)
        xcat = 5
        file = file.replace('arabien.xml','salem.xml')
    # elif 'xcat6' in mode: 
        # file = get_status(6)
        # xcat = 6
        # file = file.replace('arabien.xml','sport.xml')
    else:
        categorie()
        sys.exit(0)

    link = get_url(file)



    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    items = soup.findAll("item")
    for item in items:
            try:
                videoTitle=item.title.string
            except: pass
            try:
                thumbnail=item.thumbnail.string   
                if thumbnail == 'none': thumbnail = icon
                #elif xcat == 5: thumbnail = 'http://srv1.iptvxtra.net/_Salem/img/' + thumbnail
                #elif xcat == 6: thumbnail = 'http://srv1.iptvxtra.net/_Salem/img/' + thumbnail
            except:
                thumbnail = icon
            try:
                url = (item.link.string).replace('|','###').replace("?", "#x#")
                url= 'plugin://plugin.video.iptvxtra-arabien/?runstream=' + url + '***' + videoTitle + '***' + thumbnail
            except: pass

            addLink(videoTitle,url,thumbnail)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))

    try:
        if not os.path.isfile(xbmc.translatePath("special://temp/0_ar.fi")):
            open(xbmc.translatePath("special://temp/0_ar.fi"), "a").close()
            xbmc.executebuiltin("Container.SetViewMode("+views+")") 
    except: pass

    sys.exit(0)
    
def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        if setBack == "true": liz.setProperty( "Fanart_Image", iconimage )
        else: liz.setProperty( "Fanart_Image", icon )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,iconimage):
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def categorie():
    addDir('Salem Arabien & Sport TV', 'plugin://plugin.video.iptvxtra-arabien/?xcat5x', icon)		# Salem
    #addDir('Salem Sport TV', 'plugin://plugin.video.iptvxtra-arabien/?xcat6x', icon)				# Salem
    addDir('IPTV-Arabien x-IP', 'plugin://plugin.video.iptvxtra-arabien/?xcat2x', icon)				# arabien2.xml IPTV-Planet
    addDir('IPTV-Arabien x-Tn', 'plugin://plugin.video.iptvxtra-arabien/?xcat4x', icon)				# arabien4.xml StreamingHD.tn
    #addDir('IPTV-Arabien x-Kt', 'plugin://plugin.video.iptvxtra-arabien/?xcat1x', icon)				# arabien1.xml Krichi TV
    #addDir('TV Spice', 'plugin://plugin.video.iptvxtra-arabien/?xcat3x', icon)
    addDir('Settings', 'plugin://plugin.video.iptvxtra-arabien/?xcat_settings', icon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def get_url(url):
        #url = 'http://srv1.iptvxtra.net/xbmc/xml/salem.xml'
        response = urllib2.urlopen(url)
        link=response.read()
        response.close()
        return link

def get_status(stat):
    try:
        wert = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
        payload = {'loc': wert,'la':'AR','stat':str(stat)}
        r = requests.get("http://www.iptvxtra.net/xbmc/_form/rsx.php", params=payload)
        urln = r.text.strip() 
        if 'not allowed' in urln:
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , der Zugang über einen Proxy oder Tor-IPs ist nicht erlaubt ,25000,'+net+')')
            sys.exit(0)
        if 'none.xml' in urln:
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , du bist noch nicht registriert ,25000,'+net+')')
            sys.exit(0)
        if 'nonex.xml' in urln:
            xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler HTTP-401 , Passwort oder User ist sehr wahrscheinlich verkehrt ,25000,'+net+')')
            sys.exit(0)
        if 'lockland.xml' in urln:
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , dieses Addon ist in deinem Land nicht verfügbar ,25000,'+net+')')
            sys.exit(0)
        if 'proxy.xml' in urln:
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , der Zugang über einen Proxy oder Tor-IPs ist nicht erlaubt ,25000,'+net+')')
            sys.exit(0)
        url = urln.split('###')
        return url[1]

    except:
        xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler , fehlerhafter Zugang zum Login-Server,25000,'+net+')')
        sys.exit(0)

main()

