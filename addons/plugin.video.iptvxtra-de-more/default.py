# -*- coding: utf-8 -*-
# for more info please visit http://www.iptvxtra.net

import sys,xbmc,os,shutil,xbmcaddon

# ------------------------------------------------------------------------------------------------------------------------------------------- wiederherstellen der DE Settings - START
try:
        sxUser = 0
        sxBackup = 0
        saveset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/backup.xml')
        orgset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/settings.xml')

        if os.path.isfile(saveset) and not os.path.isfile(orgset):
            try:
                shutil.copy(saveset, orgset)
                print ' ---------------------------------------------- IPTVxtra Info-Message-more TV 100'
                print ' ---------------------------------------------------------------------------------'
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
                print ' ---------------------------------------------- IPTVxtra Info-Message-more TV 102'
                print ' ---------------------------------------------------------------------------------'
            except:
                print ' ---------------------------------------------- IPTVxtra Info-Message-more TV 103'
                print ' ---------------------------------------------------------------------------------'
except: 
        print ' ---------------------------------------------- IPTVxtra Info-Message-more TV 104'
        print ' ---------------------------------------------------------------------------------'

# ---------------------------------------------------------------------------------------------------- wiederherstellen der Settings - Ende

import resources.lib.requests as requests
from datetime import date, datetime,timedelta
import urllib,re,xbmcplugin,xbmcgui,hashlib,pickle,time

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
addon = xbmcaddon.Addon('plugin.video.iptvxtra-de-more')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id="plugin.video.iptvxtra-de")
user = __settings__.getSetting("login").strip()
pwd = __settings__.getSetting("password").strip()
puffer = __settings__.getSetting("record_active")
datenholen = __settings__.getSetting("datenholen")
mdx = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
home = xbmcaddon.Addon(id="plugin.video.iptvxtra-de-more").getAddonInfo('path')
icondir = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de-more/resources/lib/")
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
net = xbmc.translatePath( os.path.join( home, 'resources/lib/net.png') )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
mode = sys.argv[2]


if __settings__.getSetting("timeshift0") == 'true':
    try:
        import resources.lib.USTimeZone as USTimeZone
        LocalTimezone = USTimeZone.LocalTimezone()
        Europe = USTimeZone.GMT1()
        if '+01:00' in str(datetime.now(Europe)): euro = 1
        elif '+02:00' in str(datetime.now(Europe)): euro = 2
        else: euro = 1
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
        xbmc.executebuiltin('XBMC.Notification(Zeitzonen Fehler , die Zeitzone wurde nicht erkannt - die Vorgabewerte werden vom DE Addon geholt ,8000,'+net+')')
else:
    timeshift= __settings__.getSetting("timeshift")
    if timeshift == '': timeshift = '0'
    __settings__.setSetting("timeshift", timeshift)
    if __settings__.getSetting("sommer") == 'true': euro = 2
    else: euro = 1
	


def main():	

    if 'xcat01' in mode: xt = str(datetime.now()).partition(' ')
    elif 'xcat02' in mode: xt = str(datetime.now() - timedelta(days=1)).partition(' ')
    elif 'xcat03' in mode: xt = str(datetime.now() - timedelta(days=2)).partition(' ')
    elif 'xcat04' in mode: xt = str(datetime.now() - timedelta(days=3)).partition(' ')
    elif 'xcat05' in mode: xt = str(datetime.now() - timedelta(days=4)).partition(' ')
    elif 'xcat06' in mode: xt = str(datetime.now() - timedelta(days=5)).partition(' ')
    elif 'xcat07' in mode: xt = str(datetime.now() - timedelta(days=6)).partition(' ')
    elif 'xcatc01' in mode: categorie('Top Hits','tophits')
    elif 'xcatc02' in mode: categorie('US Serien','serien')
    elif 'xcatc03' in mode: categorie('US Sitcom`s & Soap`s','sitcom')
    elif 'xcatc04' in mode: categorie('Talk Shows','talkshow')
    elif 'xcatc05' in mode: categorie('Dokus','doku')
    elif 'xcatc06' in mode: categorie('Sport','sport')
    elif 'xcatc07' in mode: categorie('News','news')
    elif 'xcatc08' in mode: categorie('Pseudo-Dokus','gerichtdetektiv')
    elif 'xcatc09' in mode: categorie('TV Shows','tvshows')
    elif 'xcatc10' in mode: categorie('Motor Dokus','motors')
    elif 'xcatc11' in mode: categorie('Kid`s TV','kids')
    elif 'xcatc12' in mode: categorie('DE Doku Soap`s','de_dokusoap')
    elif 'xcatc13' in mode: categorie('DE Serien, Sitcom`s & Soap`s','de_serien')
    elif 'xcatc14' in mode: categorie('Koch-Shows und Essen','kochshows')

    elif 'xcatc99' in mode: puffer_on_off()
    else:
        categoriex()
        try:
            if not os.path.isfile(xbmc.translatePath("special://temp/0_more.fi")):
                open(xbmc.translatePath("special://temp/0_more.fi"), "a").close()
                xbmc.executebuiltin("Container.SetViewMode(504)") 
        except: pass
        sys.exit(0)

    file_cat = mode.split('xxx')[1]
    file = get_status()
    link = get_url(file.replace('serien',file_cat) + xt[0] + '.xmx')
    endtime = xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').getSetting("record_endtime")
    if endtime == '0': endtime = 600
    elif endtime == '1': endtime = 1800
    elif endtime == '2': endtime = 3600
    elif endtime == '3': endtime = 7200
    elif endtime == '4': endtime = 10800

    for item in link:
        if int(item[7]) < (int(time.time())+(int(timeshift)*3600)):
            try:
                videoTitle = item[3] +' - '+ item[1]
                videoTitle2 = item[1]
                videoTitle = videoTitle
            except: videoTitle = 'no Titel'
            try:
                desc = item[2].replace('(n)','')
            except: desc = ''
            try:
                thumbnail = item[4]  
                thumbnail = xbmc.translatePath("special://temp/temp/iptvxtra_thumbs/") + os.path.basename(item[4])
                if item[4] == 'none': thumbnail = icon
            except: thumbnail = icon
            try:	
                try: videoTitlex = videoTitle.encode('utf-8')
                except: videoTitlex = ' ...'
                endtimex = int(item[7])-(euro * 3600)+endtime
                starttimex = int(item[6])-(euro * 3600)
                if endtimex - starttimex > 14400: endtimex = starttimex + 14400
                if endtimex > int(time.time()): endtimex = int(time.time()) - 300                
                url = item[5].replace('http://pebbles','http://c001.p').replace('-lh.akamaihd.net/i/','.edgesuite.net/i/c001/') + '***' + str(starttimex) + '***' + str(endtimex) + '***' + item[8] + '***' + videoTitlex + '***' + thumbnail + '***' + 'tophits2' + '***' + mdx
                url = 'plugin://plugin.video.iptvxtra-basic/?runstream=' + url.encode("hex")
            except: url = ''

            addLink(videoTitle,videoTitle2,url,thumbnail,desc)

    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    xbmc.executebuiltin("Container.SetViewMode(504)") 

    sys.exit(0)
    
def addLink(name,name2,url,iconimage,desc):
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Label": name, "Title": name, "Genre": name2, "Plot": desc } )
    liz.setProperty( "Fanart_Image", iconimage )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    
def addDir(name,url,iconimage,desc):
    desc = desc.decode("iso-8859-1")
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Plot": desc } )
    liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def categorie(cattitle,file_cat):
    t0 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600) ).strftime('%d.%m.%Y')
    t1 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-86400 ).strftime('%d.%m.%Y')
    t2 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-(86400*2) ).strftime('%d.%m.%Y')
    t3 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-(86400*3) ).strftime('%d.%m.%Y')
    t4 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-(86400*4) ).strftime('%d.%m.%Y')
    t5 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-(86400*5) ).strftime('%d.%m.%Y')
    t6 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-(86400*6) ).strftime('%d.%m.%Y')
    t7 = datetime.fromtimestamp( int(time.time())-(int(timeshift)*3600)+(euro * 3600)-(86400*7) ).strftime('%d.%m.%Y')
    d = t0.split('.'); d0 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t1.split('.'); d1 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t2.split('.'); d2 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t3.split('.'); d3 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t4.split('.'); d4 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t5.split('.'); d5 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t6.split('.'); d6 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]
    d = t7.split('.'); d7 = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[date(int(d[2]), int(d[1]), int(d[0])).weekday()]

    addDir(cattitle+' von heute - '+d0, 'plugin://plugin.video.iptvxtra-de-more/?xcat01xxx' + file_cat, icon, '\n'+cattitle+' vom\n'+d0+' den '+t0+'\n\nwird cirka um 10.00 Uhr jeden Tag aktualisiert\n\nalle Zeiten sind deutsche Zeiten')
    addDir(cattitle+' von gestern - '+d1, 'plugin://plugin.video.iptvxtra-de-more/?xcat02xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d1+' den '+t1+'\n\nalle Zeiten sind deutsche Zeiten')
    addDir(cattitle+' vor 2 Tagen - '+d2, 'plugin://plugin.video.iptvxtra-de-more/?xcat03xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d2+' den '+t2+'\n\nalle Zeiten sind deutsche Zeiten')
    addDir(cattitle+' vor 3 Tagen - '+d3, 'plugin://plugin.video.iptvxtra-de-more/?xcat04xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d3+' den '+t3+'\n\nalle Zeiten sind deutsche Zeiten')
    addDir(cattitle+' vor 4 Tagen - '+d4, 'plugin://plugin.video.iptvxtra-de-more/?xcat05xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d4+' den '+t4+'\n\nalle Zeiten sind deutsche Zeiten')
    addDir(cattitle+' vor 5 Tagen - '+d5, 'plugin://plugin.video.iptvxtra-de-more/?xcat06xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d5+' den '+t5+'\n\nalle Zeiten sind deutsche Zeiten')
    addDir(cattitle+' vor 6 Tagen - '+d6, 'plugin://plugin.video.iptvxtra-de-more/?xcat07xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d6+' den '+t6+'\n\nalle Zeiten sind deutsche Zeiten')
    #addDir(cattitle+' vor 7 Tagen - '+d7, 'plugin://plugin.video.iptvxtra-de-more/?xcat08xxx' + file_cat, icon,'\n'+cattitle+' vom\n'+d7+' den '+t7+'\n\nsind aber nicht alle verfügbar, da manche älter als 7 Tage sind')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    xbmc.executebuiltin("Container.SetViewMode(503)") 
    sys.exit(0)

def categoriex():
    addDir('Top Hits', 'plugin://plugin.video.iptvxtra-de-more/?xcatc01x', icondir + 'icon1.png', '\n') # xcatc13x
    addDir('Kid`s TV', 'plugin://plugin.video.iptvxtra-de-more/?xcatc11x', icondir + 'icon11.png','\n')
    addDir('US Serien', 'plugin://plugin.video.iptvxtra-de-more/?xcatc02x', icondir + 'icon2.png','\n')
    addDir('US Sitcom`s und Soap`s', 'plugin://plugin.video.iptvxtra-de-more/?xcatc03x', icondir + 'icon3.png','\n')
    addDir('DE Serien, Sitcom`s und Soap`s', 'plugin://plugin.video.iptvxtra-de-more/?xcatc13x', icondir + 'icon2.png','\n')
    addDir('Gerichts und Detektiv Pseudo-Dokus', 'plugin://plugin.video.iptvxtra-de-more/?xcatc08x', icondir + 'icon8.png','\n')
    addDir('deutsche Doku Soap`s', 'plugin://plugin.video.iptvxtra-de-more/?xcatc12x', icondir + 'icon12.png','\n')
    addDir('Reportagen, Magazine, Talk und Late Night Shows', 'plugin://plugin.video.iptvxtra-de-more/?xcatc04x', icondir + 'icon4.png','\n')
    addDir('TV-Shows, Game-Shows und Musik Sendungen', 'plugin://plugin.video.iptvxtra-de-more/?xcatc09x', icondir + 'icon9.png','\n')
    addDir('Dokumentationen und Doku-Serien', 'plugin://plugin.video.iptvxtra-de-more/?xcatc05x', icondir + 'icon5.png','\n')
    addDir('Motor Magazine und Dokus', 'plugin://plugin.video.iptvxtra-de-more/?xcatc10x', icondir + 'icon10.png','\n')
    addDir('Sport und Sportnachrichten', 'plugin://plugin.video.iptvxtra-de-more/?xcatc06x', icondir + 'icon7.png','\n')
    addDir('Koch-Shows und Essen', 'plugin://plugin.video.iptvxtra-de-more/?xcatc14x', icondir + 'icon5.png','\n')
    addDir('News, Nachrichten und Politik', 'plugin://plugin.video.iptvxtra-de-more/?xcatc07x', icondir + 'icon6.png','\n')
    if puffer == 'true': addDir('IPTVxtra DE - Replay-Puffer ausschalten', 'plugin://plugin.video.iptvxtra-de-more/?xcatc99x', icon,'\n\ndie kompletten Einstellungen sind im\nIPTVxtra DE Addon\neinzusehen')
    if puffer == 'false': addDir('IPTVxtra DE - Replay-Puffer einschalten', 'plugin://plugin.video.iptvxtra-de-more/?xcatc99x', icon,'\n\ndie kompletten Einstellungen sind im\nIPTVxtra DE Addon\neinzusehen')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def get_url(url):
    try:
        xmx = xbmc.translatePath("special://temp/3496-2216be.fi")
        urllib.urlretrieve (url, xmx)
        f = open(xmx)
        liste = pickle.load(f)
        f.close()
        os.remove(xmx)
        return liste
    except:
        try:
            xmx = xbmc.translatePath("special://temp/3496-2216be.fi")
            urllib.urlretrieve (url.replace('rv1','rv3'), xmx)
            f = open(xmx)
            liste = pickle.load(f)
            f.close()
            os.remove(xmx)
            return liste
        except: sys.exit(0)

def get_status():
    try:
        r = requests.get("http://api.iptvxtra.net/tophits.php", params = {'loc': mdx ,'la':'DE','app':'serien1'} )
        url = r.text.strip().decode("hex") 
    except:
        xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler , fehlerhafter Zugang zum Login-Server,25000,'+net+')')
        sys.exit(0)
    if url == '':
        xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler , fehlerhafter Zugang zum Login-Server,25000,'+net+')')
        sys.exit(0)
    return url

def puffer_on_off():
    puffer = xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').getSetting("record_active")
    if puffer == 'true':
        xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').setSetting('record_active','false')
        xbmc.executebuiltin('XBMC.Notification(Replay-Puffer , ist jetzt ausgeschaltet,5000,'+icon+')')
    elif puffer == 'false':
        xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de').setSetting('record_active','true')
        xbmc.executebuiltin('XBMC.Notification(Replay-Puffer , ist jetzt eingeschaltet,5000,'+icon+')')
    xbmc.executebuiltin('Container.Refresh')
    sys.exit(0)


main()

