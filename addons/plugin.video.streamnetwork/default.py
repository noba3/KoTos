# -*- coding: utf-8 -*-

# StreamNetwork.tv plugin written by TV StreamNetwork special User 
# for more info please visit http://www.StreamNetwork.tv

import sys,xbmc,xbmcaddon,hashlib

if 'runstream' in sys.argv[2]:
    url = sys.argv[2].replace('?runstream=','') #.split('***')
    px = xbmc.translatePath("special://home/addons/plugin.video.streamnetwork/resources/lib/zapping.py")
    xbmc.executebuiltin('RunScript('+px+',url='+url+')')
    sys.exit(0)
if 'settings' in sys.argv[2]:
    xbmcaddon.Addon('plugin.video.streamnetwork').openSettings()
    sys.exit(0)

import xbmcplugin,xbmcgui,urllib,os,time,pickle
from datetime import date, datetime,timedelta
import resources.lib.requests as requests
from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
Addon = xbmcaddon.Addon('plugin.video.streamnetwork')
profile = xbmc.translatePath(Addon.getAddonInfo('profile'))
icondir = xbmc.translatePath("special://home/addons/plugin.video.streamnetwork/resources/icons/")
icon = xbmc.translatePath("special://home/addons/plugin.video.streamnetwork/icon.png")
xmltv2 = xbmc.translatePath("special://home/addons/plugin.video.streamnetwork/resources/epg/epg.xmx")
viewfile = xbmc.translatePath("special://temp/tvsnet.fi")
__settings__ = xbmcaddon.Addon(id="plugin.video.streamnetwork")
user = __settings__.getSetting("user")
pwd = __settings__.getSetting("password")
pwd = hashlib.md5(pwd).hexdigest()
setBack = __settings__.getSetting("setBack")
views_kg = __settings__.getSetting("views_kg")
views_s = __settings__.getSetting("views_s")
epg_on = __settings__.getSetting("epg_on")
epg_dl = __settings__.getSetting("epg_dl")
epg_title = __settings__.getSetting("epg_title")
epg_info = __settings__.getSetting("epg_info")
mode = sys.argv[2]
cat_on = 'true'
view = 's'
free = 0
eventleer = 0

if __settings__.getSetting("timeshift0") == 'true' and epg_on == 'true':
    try:
        import resources.lib.USTimeZone as USTimeZone
        LocalTimezone = USTimeZone.LocalTimezone()
        Europe = USTimeZone.GMT1()
        if '+01:00' in str(datetime.now(Europe)): euro = 1
        elif '+02:00' in str(datetime.now(Europe)): euro = 2
        else: euro = 0
        eurox = str(datetime.now(LocalTimezone))
        eurox = eurox.partition('.')
        if '+' in eurox[2] :  
            eurox = eurox[2].partition('+')
            eurox = eurox[2].partition(':')
            timeshift = str(int(eurox[0]) - euro)
        elif '-' in eurox[2] :
            eurox = eurox[2].partition('-')
            eurox = eurox[2].partition(':')
            timeshift = str(int('-'+eurox[0]) - euro)
        __settings__.setSetting("timeshift", timeshift)
    except:
        timeshift = __settings__.getSetting('timeshift')
        __settings__.setSetting('timeshift0','false')
        xbmc.executebuiltin('XBMC.Notification(autom. Zeitzonen Fehler , die Zeitzonenerkennung wurde auf manuell geschaltet ,8000,'+icon+')')
else:
    timeshift = __settings__.getSetting("timeshift")
    if timeshift == '': timeshift = '0'

def main():
    if epg_on == 'true': xmltv_dl()
    mode = sys.argv[2]
    free = get_status()

    if not 'xcat' in mode and free == 2: 
        view = 'k'
        categorie()
        sys.exit(0)
    elif 'xcat' in mode and free == 2:
        mode = mode.partition('cat_')
        chxml = 'http://xbmc.streamnetwork.tv/xml/'+mode[2]+'.xml'
        view = 's'
    elif free == 1:
        chxml = 'http://xbmc.streamnetwork.tv/xml/regtv.xml'
        view = 's'
    else:
        free = 0
        chxml = 'http://xbmc.streamnetwork.tv/xml/freetv.xml'
        view = 's'
  
    if epg_on == 'true': iptvepg = xmltv()
    description = 'keine Sender Information verfügbar'

    chxml = get_url(chxml)
    soup = BeautifulSOAP(chxml, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    items = soup.findAll("item")

    for item in items:
        if not item.srv.string or item.srv.string <> 'none':

            try: videoTitle=item.title.string
            except: 'kein Titel vorhanden'

            try: url= 'plugin://plugin.video.streamnetwork/?runstream=' + user + '***' + pwd + '***' + item.link.string + '***' + item.srv.string  + '***' + videoTitle + '***' + item.thumbnail.string 
            except: pass

            try: thumbnail=item.thumbnail.string                
            except: thumbnail = icon

            try:
                description = item.description.string
                xmlepg = item.xmlepg.string
                if not description and not 'none' in xmlepg:
                    if epg_on == "true":
                        description = ''
                        zx = 0
                        for text in iptvepg:
                            text0 = text[0].strip() 
                            if xmlepg == text0 and int(text[4]) > int(time.time()):
                                laenge = len(text[5]) + len(text[6]) + 3
                                if laenge < 60:
                                    description = description + timestamp(text[8]) +'  '+ text[5]
                                    if text[6] != 'no Info': description = description + ' - ' + text[6]
                                    description = description + '\n'
                                else:
                                    description = description + timestamp(text[8]) +'  '+ text[5]
                                    if text[6] != 'no Info': 
                                        if len(text[6]) > 50 : 
                                            kuerz = len(text[6]) - 50
                                            text[6] = text[6][:-kuerz] + ' ...'
                                        description = description + '\n'+''+ text[6]
                                    description = description + '\n'
                                if zx == 0 and epg_title == "true":
                                    if ' - ' in text[5]:
                                        text5 = text[5].partition(" - ")
                                        videoTitle = videoTitle +'   - '+ text5[0]
                                    else: 
                                        videoTitle = videoTitle +'   - '+ text[5]
                                zx += 1
                            if zx == int(epg_info): break
                else:
                    if description and '.....' in description:
                        ex = description.split('.....')
                        description = ''
                        for i in range(len(ex)):
                            description = description + ex[i].strip() + '\n'
  
            except: description = 'keine EPG Information'


            addLink(videoTitle,url,thumbnail,description)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    if view == 's' and int(views_s) > 0: xbmc.executebuiltin("Container.SetViewMode("+views_s+")")
    try:
        if int(views_kg) > 0 and view == 'k' and not os.path.isfile(viewfile):
            open(viewfile, "a").close()
            xbmc.executebuiltin("Container.SetViewMode("+views_kg+")") 
    except: pass
    sys.exit(0)

def addLink(name,url,thumbnail,description):	
    try: name = name.encode('utf-8')
    except: pass
    try: description = description.encode('utf-8')
    except: pass

    liz=xbmcgui.ListItem(name, iconImage=thumbnail, thumbnailImage=thumbnail)
    liz.setInfo( type="Video", infoLabels={ "Label": name, "Title": name, "Plot": description} )
    if setBack == "true": liz.setProperty( "Fanart_Image", thumbnail )
    else: liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)

def addDir(name,url,iconimage):
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def get_status():
    load = {'name': user,'passwd': pwd}
    try:
        r = requests.get("http://xbmc.streamnetwork.tv/api.php", params=load)
    except:
        xbmc.executebuiltin('XBMC.Notification(Netzwerk Fehler , der Login Server ist nicht erreichbar ,7000,'+icon+')')
        sys.exit(0)
    lista = r.text
    lista = lista.strip()
    if 'freeuser' in lista: free = 0
    elif 'reguser' in lista: free = 1
    elif 'Premium' in lista: free = 2
    else: free = 0
    return free

def get_url(url):
        r = requests.get(url)
        return r.text

def categorie():
    addDir('Free TV', 'plugin://plugin.video.streamnetwork/?xcat_freetv', 'http://xbmc.streamnetwork.tv/logos/1.png')
    addDir('Free HD TV', 'plugin://plugin.video.streamnetwork/?xcat_freehd', 'http://xbmc.streamnetwork.tv/logos/2.png')
    addDir('Premium HD TV', 'plugin://plugin.video.streamnetwork/?xcat_premium', 'http://xbmc.streamnetwork.tv/logos/3.png')
    addDir('Sport HD TV', 'plugin://plugin.video.streamnetwork/?xcat_sport', 'http://xbmc.streamnetwork.tv/logos/4.png')
    addDir('Neu und Exklusiv bei SNTV', 'plugin://plugin.video.streamnetwork/?xcat_news', 'http://xbmc.streamnetwork.tv/logos/news.png')
    addDir('Events & Extras in HD', 'plugin://plugin.video.streamnetwork/?xcat_event', 'http://xbmc.streamnetwork.tv/logos/event.png')
    addDir('Externer Sport SD/HD', 'plugin://plugin.video.streamnetwork/?xcat_balkan', 'http://xbmc.streamnetwork.tv/logos/event.png')	
    addDir('Settings', 'plugin://plugin.video.streamnetwork/?xcat_settings', 'http://xbmc.streamnetwork.tv/logos/10.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        if int(views_kg) > 0 and not os.path.isfile(viewfile):
            open(viewfile, "a").close()
            xbmc.executebuiltin("Container.SetViewMode("+views_kg+")") 
    except: pass
    sys.exit(0)

def timestamp(zeit):
    zeita = zeit.partition(":")
    zeitb = int(zeita[0]) + int(timeshift)
    if zeitb > 24:
        zeitb -= 24
    elif zeitb < 0:
        zeitb += 24       
    zeitc = str(zeitb)
    if zeitc == '24':
        zeitc = '00'
    if zeitb > 0 and zeitb < 10:
        zeitc = '0' + zeitc
    zeit = zeitc + '.' + zeita[2]  
    zeit = zeit.strip()
    return (zeit)

def read_listfile(datei):
    f = open(datei)
    liste = pickle.load(f)
    return liste

def xmltv_dl():
    dltime = 3600*20
    if not os.path.isfile(xmltv2) or os.stat(xmltv2)[8] < (time.time() - dltime) or os.path.getsize(xmltv2) < 20000 or epg_dl == 'true':
        xbmc.executebuiltin('XBMC.Notification(EPG Information !, das neue EPG wird von Server geladen ,8000,'+icon+')')
        if epg_dl == 'true': __settings__.setSetting("epg_dl", "false")
        try: urllib.urlretrieve ('http://epg.streamnetwork.tv/epg.xmx', xmltv2)
        except: 
            xbmc.executebuiltin('XBMC.Notification(EPG Error !, das EPG konnte nicht geladen werden die alternative wird heruntergeladen ,5000,'+icon+')')
            urllib.urlretrieve ('http://srv1.iptvxtra.net/xmltv/xmltv_de_2.xmx', xmltv2)
    return

def xmltv():
    iptvepg=[]
    if os.path.isfile(xmltv2):
        iptvepg = read_listfile(xmltv2)
        return iptvepg
    else:
        iptvepg.append([' ','0','0','0','0',' ',' ',' ','0'])
        iptvepg.append([' ','0','0','0','0',' ',' ',' ','0'])
        write_listfile(xbmc.translatePath(xmltv2),iptvepg)
        return iptvepg

main()






