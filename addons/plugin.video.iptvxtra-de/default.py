# -*- coding: utf-8 -*-

# german television plugin written by IPTVxtra
# for more info please visit http://www.iptvxtra.net

import sys,xbmc
mode = 'False'
if 'extrafanart' in sys.argv[2]: sys.exit(0)
	




# ---------------------------------------------------------------------------------------------------- Sicherung der Settings - START

import os,shutil,xbmcaddon,hashlib,time

sxUser = 0
sxBackup = 0
txBackup = 0
saveset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/backup.xml')
orgset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/settings.xml')
csvset = xbmc.translatePath("special://userdata/addon_data/plugin.video.iptvxtra-de/set.csv")
icon = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/icon.png")
try: orgset_md5 = hashlib.md5(open(orgset, 'rb').read()).hexdigest()
except: orgset_md5 = '11111'
try: saveset_md5 = hashlib.md5(open(saveset, 'rb').read()).hexdigest()
except: saveset_md5 = '22222'

if os.path.isfile(saveset) and not os.path.isfile(orgset):
    try:
        shutil.copy(saveset, orgset)
        xbmc.executebuiltin('XBMC.Notification(Error Backup Funktion , IPTVxtra-DE Settings mussten wiederhergestellt werden,5000,'+icon+')')
        print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message 100'
        print ' --------------------------------------------------------------------------------------------------------------'
    except: pass

h = 0
while h <= 11:
    try:
        fobj = open(orgset, "r") 
        for line in fobj:
            if "login" in line and "xbmcuser" in line: 
                sxUser = 1
                break
            elif "login" in line and not "xbmcuser" in line: 
                sxUser = 2
                break
            else: sxUser = 3
        fobj.close()
    except: sxUser = 3
    if sxUser == 1 or sxUser == 2: break
    print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message 104-' + str(h)
    print ' --------------------------------------------------------------------------------------------------------------'
    h = h + 1
    time.sleep(1)
#if sxUser == 3: sys.exit(0)

if sxUser == 2 and orgset_md5 != saveset_md5:			# Backup anlegen
    try: os.remove(saveset)
    except: pass
    try: shutil.copy(orgset, saveset)
    except:
        print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message 101'
        print ' --------------------------------------------------------------------------------------------------------------'

if os.path.isfile(saveset) and sxUser == 1 or sxUser == 3:			# wiederherstellen
    try: os.remove(orgset)
    except: pass
    try: 
        shutil.copy(saveset, orgset)
        xbmc.executebuiltin('XBMC.Notification(Backup Funktion , IPTVxtra-DE Settings mussten wiederhergestellt werden ,5000,'+icon+')')
        print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message 102'
        print ' --------------------------------------------------------------------------------------------------------------'
    except:
        print ' ------------------------------------------------------------------------------ IPTVxtra Info-Message 103'
        print ' --------------------------------------------------------------------------------------------------------------'

# ---------------------------------------------------------------------------------------------------- Sicherung der Settings - ENDE



if '?'in sys.argv[2]:
    mode = sys.argv[2].replace('?','')
    if 'timeline' in mode:
        title_ch = xbmc.getInfoLabel('Listitem.Label')
        if ' - ' in title_ch:
            title_ch = title_ch.partition(' - ')
            title_ch = title_ch[0]
        icon_ch = xbmc.getInfoLabel('ListItem.Icon')
        xbmc.executebuiltin('XBMC.Notification('+title_ch+' , einen Moment der Sender wird geladen ,30000,'+icon_ch+')')
    if 'zapsidemenu'in mode:
        from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
        import pickle,hashlib
    if 'main'in mode:
        from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
        import base64,hashlib,pickle

else:
    from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSOAP
    import base64,hashlib,pickle


import urllib2,urllib,re,random,operator,xbmcplugin,xbmcgui
from datetime import date, datetime,timedelta
import resources.lib.requests as requests


try:
    __settingsreload__ = xbmcaddon.Addon(id="plugin.program.iptvxtra")
    __settingsreload__.setSetting("is_addon", "de")
except: pass
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
Addon = xbmcaddon.Addon('plugin.video.iptvxtra-de')
profile = xbmc.translatePath(Addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id="plugin.video.iptvxtra-de")

if __settings__.getSetting("firstrun3") <> "1":
    __settings__.setSetting("firstrun3", "1")
    try:
        shutil.rmtree(xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de-serien"), ignore_errors=True)
        shutil.rmtree(xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de-sitcom"), ignore_errors=True)
        shutil.rmtree(xbmc.translatePath("special://userdata/addon_data/plugin.video.iptvxtra-de-serien"), ignore_errors=True)
        shutil.rmtree(xbmc.translatePath("special://userdata/addon_data/plugin.video.iptvxtra-de-sitcom"), ignore_errors=True)
        shutil.rmtree(xbmc.translatePath("special://userdata/addon_data/plugin.video.iptvxtra-de-tophits"), ignore_errors=True)
    except: pass

user= __settings__.getSetting("login").strip()
pwd= __settings__.getSetting("password").strip()
epg_on= __settings__.getSetting("epg_on")
epg_now= __settings__.getSetting("epg_title")
epg_dl= __settings__.getSetting("epg_dl")
epg_dlneu = __settings__.getSetting("epg_dlneu")
epg_info= __settings__.getSetting("epg_info")
no_epg_title = __settings__.getSetting("no_epg_title")
quali= __settings__.getSetting("quali")
servhost= __settings__.getSetting("servhost")
temp = xbmc.translatePath("special://temp/") + '040264-221'+servhost+'.fi'
viewfile = xbmc.translatePath("special://temp/0de.fi")
xmltv2 = xbmc.translatePath("special://temp/temp/xmltv_de_2.xmx")
IPTVxtraEPG = xbmc.translatePath("special://temp/") + 'IPTVxtraDEepg'
set_off= __settings__.getSetting("set_off")
replayDE= __settings__.getSetting("replayDE")
setHeader= __settings__.getSetting("setHeader")
record_active= __settings__.getSetting("record_active")
setBack= __settings__.getSetting("setBack")
views= __settings__.getSetting("views")
home = __settings__.getAddonInfo('path')
sBackup = __settings__.getSetting("sBackup")
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
net = xbmc.translatePath(home+"/resources/lib/net.png")
netx = xbmc.translatePath(home+"/resources/lib/netx.png")
thumbs = xbmc.translatePath("special://temp/temp/iptvxtra_thumbs/")
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
genre = "Live Stream"
uri = "http://s.IPTVxtra.net/regDE"
exitcode = "0"
MainList=[]
xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell, plugin://plugin.video.iptvxtra-de)") 
xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_ok)")
try: os.makedirs(xbmc.translatePath("special://temp/temp/iptvxtra_thumbs/"))
except: pass
	

if __settings__.getSetting("timeshift0") == 'true' and epg_on  == 'true':
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
        xbmc.executebuiltin('XBMC.Notification(Zeitzonen Fehler , die Zeitzone wurde auf den manuellen Wert gestellt ,8000,'+net+')')
else:
    timeshift= __settings__.getSetting("timeshift")
    if timeshift == '': timeshift = '0'
    __settings__.setSetting("timeshift", timeshift)
    if __settings__.getSetting("sommer") == 'true': euro = 2
    else: euro = 1

if user <> 'xbmcuser':
    csvsetin = user+'***'+pwd+'***'+hashlib.md5('#user='+user+'pass='+pwd).hexdigest()+'***'+timeshift+'***'
    my_file = open(csvset, 'w')
    my_file.write(csvsetin)
    my_file.close()

print '#########################################################################'
print str(hashlib.md5('#user='+user+'pass='+pwd).hexdigest()) + '     IPTVxtraDE'
print '#########################################################################'

def main():

    repox = repo()
    channels=[]
    chnum = ''	
    mode = 'true'
    exitcode = "0"
    fwx = '0'
    link=get_url()
    if epg_on == 'true': xmltv_dl()
    senderliste = create_senderliste()
    iptvepg = xmltv()
    try: os.remove(thumbs + 'logopack.zip')
    except: pass

    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    items = soup.findAll("item")
    for item in items:
        such = item.title.string
        for i in senderliste:
            if such == i[0]:
                    sorter = ('0000000'+i[2])[-6:]
                    #sorter = sorter[-6:]


                    try:
                        videoTitle = item.title.string
                        videoTitle = videoTitle.replace(' HD','[COLOR blue] in HD[/COLOR]')
                        vTitle = videoTitle
                    except: pass

                    try:
                        fwx=item.fw.string
                        if not fwx:
                            fwx = '0'
                    except: pass

                    try:
                        name2 = ''
                        description = ''
                        xmlepg = ''
                        if epg_on == "true":
                            if not item.xmlepg.string or item.xmlepg.string == '': item.xmlepg.string = 'abcdefgh'
                            xmlepg=item.xmlepg.string.strip() 
                            zx = 0
                            for text in iptvepg:
                                text0 = text[0].strip() 
                                if xmlepg == text0 and int(text[4])-(euro * 3600) > int(time.time()):
                                    laenge = len(text[5]) + len(text[6]) + 3
                                    if name2 == '' and no_epg_title == "false":
                                        name2 = text[5]
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
                                            description = description + '\n'+'             '+ text[6]
                                        description = description + '\n'
                                    if zx == 0 and epg_now == "true" and no_epg_title == "false":
                                        if ' - ' in text[5]:
                                            text5 = text[5].partition(" - ")
                                            videoTitle = vTitle +' - '+ text5[0]
                                        else: 
                                            videoTitle = vTitle +' - '+ text[5]
                                    zx += 1
                                    if zx == int(epg_info):
                                        break
                    except: pass
	
                    try:
                        if epg_now == "true": name2 = ''
                    except: pass

                    try:
                        url=item.link.string
                        url= 'plugin://plugin.video.iptvxtra-basic/?preview'+url
                    except: pass

                    try:
                        txc = item.thumbnail.string
                        thumbnail = thumbs + os.path.basename(txc)
                        if not os.path.isdir(thumbs) or __settings__.getSetting("thumbupd") == 'true' or len([item for item in os.listdir(thumbs) if os.path.isfile(os.path.join(thumbs, item))]) < 180:
                            __settings__.setSetting("thumbupd", 'false')
                            xbmc.executebuiltin('XBMC.Notification(Senderlogos werden aktualisiert, der komplette Logopack wird geladen und extrahiert,60000,'+net+')')
                            import zipfile
                            try: os.makedirs(thumbs)
                            except: pass
                            try: urllib.urlretrieve ('http://srv1.iptvxtra.net/xbmc/senderlogos_de/logopack.zip', thumbs + 'logopack.zip')
                            except: urllib.urlretrieve ('http://srv3.iptvxtra.net/xbmc/senderlogos_de/logopack.zip', thumbs + 'logopack.zip')
                            zfile = zipfile.ZipFile(thumbs + 'logopack.zip')
                            zfile.extractall(thumbs)
                            xbmc.executebuiltin( "Dialog.Close(infodialog)" )
                        if not os.path.isfile(thumbnail):
                            xbmc.executebuiltin('XBMC.Notification(Senderlogos werden aktualisiert, fehlende Logos werden geladen,1000,'+net+')')
                            urllib.urlretrieve (txc, thumbnail)
                    except: thumbnail=""

                    if chnum == '':
                        chnum = 'none'	
                    elif chnum == 'none':
                        chnum = ''	

                    channels.append([videoTitle,name2,url,thumbnail,description,fwx,vTitle,xmlepg,chnum,sorter])      
             
                    
    channels.sort(key=operator.itemgetter(9))
    for h in channels:
        addLink(h[0],h[1],h[2],h[3],h[4],h[5],h[6],h[7],h[8])
    write_listfile(xbmc.translatePath('special://temp/040264-1001.fi'),MainList)

    if not user or user == "xbmcuser":
        liz=xbmcgui.ListItem("Register", iconImage="http://srv1.iptvxtra.net/xbmc/senderlogos_de/_register_de.png", thumbnailImage="http://srv1.iptvxtra.net/xbmc/senderlogos_de/_register_de.png")
        liz.setInfo( type="Video", infoLabels={ "Title": "registrieren", "Plot": "Registriere dich fuer ueber 50 Kanaele.\nAutomatisch wirst du zu unserem Formular geleitet,\nausfuellen - senden - fertig\nDeine neuen Zugangsdaten kommen sofort per Email.\nBei Android muss der Registrierungslink leider noch selbst im Browser eingetragen werden,\nwir suchen aber nach einer Lösung!\n\n  - http://s.IPTVxtra.net/regDE -", "Genre": "Registrierung", "Year": time.strftime("%Y") } )
        if setBack == "true":
            liz.setProperty( "Fanart_Image", "http://srv1.iptvxtra.net/xbmc/senderlogos_de/_register_de.png" )
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url="http://srv1.iptvxtra.net/xbmc/_trailer/trailer.mp4",listitem=liz)

    repset()
    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

    try:
        if int(views) > 0 and not os.path.isfile(viewfile):
            open(viewfile, "a").close()
            xbmc.executebuiltin("Container.SetViewMode("+views+")") 
    except: pass
	
    if  os.path.isfile(xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/a.txt")):
        os.remove(xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/a.txt"))
        Addon = xbmcaddon.Addon('plugin.video.iptvxtra-de')
        __path__ = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/")
        if (__name__ == "__main__"):
            import resources.lib.window_info as window_info
            ui = window_info.GUI('Script.xml', __path__, 'default')
            ui.doModal()
            del ui

    sys.exit(0)

def repo():
    repos = xbmc.translatePath("special://home/addons/repository.iptvxtra")
    if not os.path.isdir(repos):
        xbmc.executebuiltin('XBMC.Notification(IPTVxtra Repo missing , the Repo of IPTVxtra is not installed - the addon can not be executed ,15000,'+icon+')')
        sys.exit(0)
    return 'ok'
    
def find_between_(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between(s,trennzeichen):
    try:
        first = '<' + trennzeichen + '>'
        last = '</' + trennzeichen + '>'
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def xmltv_dl():
    if epg_dl == '0': dltime = 3600*18
    elif epg_dl == '2': dltime = 3600*22
    elif epg_dl == '3': dltime = 3600*24
    else: dltime = 3600*20
    if not os.path.isfile(xmltv2) or os.stat(xmltv2)[8] < (time.time() - dltime) or os.path.getsize(xmltv2) < 1200000 or epg_dlneu == 'true':
        xbmc.executebuiltin('XBMC.Notification(EPG Information !, das neue EPG wird von Server geladen ,5000,'+net+')')
        if epg_dlneu == 'true': __settings__.setSetting("epg_dlneu", "false")
        try: urllib.urlretrieve ('http://srv1.iptvxtra.net/xmltv/xmltv_de_2.xmx', xmltv2)
        except: urllib.urlretrieve ('http://srv3.iptvxtra.net/xmltv/xmltv_de_2.xmx', xmltv2)
    return


def addLink(name,name2,url,iconimage,description,fwx,vTitle,xmlepg,chnum):
        qt = '900'
        chheader =  '&User-Agent=Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'

        if "ch" in fwx:
            s1 = random.randint(0,7)
            s2 = random.randint(0,255)
            s3 = random.randint(0,255)
            xff = "85.%s.%s.%s" % (s1,s2,s3)
            url = url.replace("|X-Forwarded-For=", "")
            url = url + "###X-Forwarded-For=" + xff
        if "us" in fwx:
            url = url.replace("|X-Forwarded-For=", "")
            url = url + "###X-Forwarded-For=209.239.112.104"
        if "uk" in fwx:
            url = url.replace("|X-Forwarded-For=", "")
            url = url + "###X-Forwarded-For=5.45.22.21"
        if "fr" in fwx:
            url = url.replace("|X-Forwarded-For=", "")
            url = url + "###X-Forwarded-For=2.10.2.17"
        if "de" in fwx:
            s1 = random.randint(0,255)
            s2 = random.randint(0,255)
            xff = "93.221.%s.%s" % (s1,s2)
            url = url.replace("|X-Forwarded-For=", "")
            url = url + "###X-Forwarded-For=" + xff
        if "none" in fwx:
            offset = time.strftime("%Y.%m.%d")
            url = url + "#x#offset="+offset+"###Referer=#h#client.easytv.to/StrobeMediaPlayback-lo.swf"
        if '&&&' in url:
            if quali == "0":
                qt = '400'
            elif quali == "1":
                qt = '900'
            elif quali == "2":
                qt = '1300'
            urlq = url.partition('&&&')
            url = urlq[0] + qt + urlq[2]
        elif 'index_1300' in url:
            if quali == "0":
                qt = 'index_400'
            elif quali == "1":
                qt = 'index_900'
            elif quali == "2":
                qt = 'index_1300'
            urlq = url.partition('index_1300')
            url = urlq[0] + qt + urlq[2]
        elif '_1536@' in url:
            if quali == "0":
                qt = '_768@'
            elif quali == "1":
                qt = '_768@'
            elif quali == "2":
                qt = '_1536@'
            urlq = url.partition('_1536@')
            url = urlq[0] + qt + urlq[2]
        elif 'index_1664_' in url:
            if quali == "0":
                qt = 'index_832_'
            elif quali == "1":
                qt = 'index_1328_'
            elif quali == "2":
                qt = 'index_1664_'
            urlq = url.partition('index_1664_')
            url = urlq[0] + qt + urlq[2]

        if setHeader == 'true' and not '212.162.68' in url:
            url = url + chheader

        timex = timenow("0000")  
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Label": name, "Title": name2, "Plot": description, "Genre": vTitle + " - " + genre + " - EPG von " + timex[0], "Year": time.strftime("%Y") } )
        if setBack == "true":
            liz.setProperty( "Fanart_Image", iconimage )
        if chnum == "none":
            liz.setProperty( "jetztimtv", chnum )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)

        MainList.append([vTitle+' ',iconimage,url,xmlepg])



def write_listfile(datei,liste):
    output = open(datei, 'w')
    pickle.dump(liste, output)
    output.close()

def read_listfile(datei):
    try:
        f = open(datei)
        liste = pickle.load(f)
        return liste
    except: 
        xbmc.executebuiltin('XBMC.Notification(EPG Fehler!,das EPG konnte nicht dekodiert werden ,5000,'+net+')')

def get_url():
    file = "none.xml"
    if os.path.isfile(temp):
        if os.stat(temp)[8] < time.time() - 86400:
            os.remove(temp)
        else:
            link = ''
            fobj = open(temp, "r") 
            for line in fobj: 
                line = (line.decode("hex"))
                link += line.strip() 
            fobj.close()
            return link
    
    try:
        wert = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
        payload = {'loc': wert,'h':'0','sh':servhost,'la':'DE'}
        r = requests.get("http://www.iptvxtra.net/xbmc/_form/rsx.php", params=payload)
        urln = r.text
        if 'not allowed' in urln:
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , der Zugang über einen Proxy oder Tor-IPs ist nicht erlaubt ,25000,'+net+')')
            sys.exit(0)
        if 'locked' in urln:
            xbmc.executebuiltin('XBMC.Notification(gesperrter Account , du wurdest nach einer Mehrfachregistrierung gesperrt - wende dich an info@iptvxtra.net ,25000,'+net+')')
            sys.exit(0)
        respx = [x for x in urln.split("###")]
        __settings__.setSetting("data2", respx[2])
        __settings__.setSetting("data3", respx[3])
        __settings__.setSetting("data4", respx[4])
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaydata_aktuell, Replay active until "+respx[4]+")")
        url = respx[1]
        url = url.replace(' ','')

        if url == 'none.xml':
            xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler HTTP-401 , Passwort oder User ist sehr wahrscheinlich verkehrt ,25000,'+net+')')
            sys.exit(0)
        if url == 'lockland.xml':
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , dieses Addon ist in deinem Land nicht verfügbar ,25000,'+net+')')
            sys.exit(0)
        if url == 'proxy.xml':
            xbmc.executebuiltin('XBMC.Notification(Login Fehler , der Zugang über einen Proxy oder Tor-IPs ist nicht erlaubt ,25000,'+net+')')
            sys.exit(0)
        http = requests.packages.urllib3.PoolManager()
        headers = requests.packages.urllib3.util.make_headers(keep_alive= True, user_agent= 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3', basic_auth=None)
        try: link = http.request('GET', url, headers=headers)
        except: link = http.request('GET', url.replace('rv1','rv3'), headers=headers)
        
        if '<epg>' in link.data:
            f = open(temp, "w")
            hurl = link.data.encode("hex")
            f.write(hurl)
            f.close()
            return link.data
        elif '401 Authorization Required' in link.data:
            print '                                                                                    [IPTVxtra ERROR - 401]'
            exitcode = "401"
            xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler HTTP-401 , Passwort oder User ist sehr wahrscheinlich verkehrt ,25000,'+net+')')
            sys.exit(0)
        elif '404 Not Found' in link.data:
            print '                                                                                    [IPTVxtra ERROR - 404]'
            exitcode = "404"
            xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler HTTP-404 , IPTVxtra.net Server nicht gefunden ,25000,'+net+')')
            sys.exit(0)
        elif '403 Forbidden' in link.data:
            print '                                                                                    [IPTVxtra ERROR - 403]'
            exitcode = "403"
            xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler HTTP-403 , Verbotener Zugriff auf IPTVxtra.net ,25000,'+net+')')
            sys.exit(0)
        elif 'Internal Server Error' in link.data:
            print '                                                                                    [IPTVxtra ERROR - 500]'
            exitcode = "500"
            xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler HTTP-500 , Interner Server-Fehler bei IPTVxtra.net ,25000,'+net+')')
            sys.exit(0)
        else:
            print '                                                                                    [IPTVxtra ERROR - Allgemein]'
            exitcode = "501"
            xbmc.executebuiltin('XBMC.Notification(allgemeiner Netzwerkfehler , pruefe dein Netzwerk oder die Routerkonfiguration - Router und Kabelmodem für 10 min vom Stromnetz nehmen,25000,'+net+')')
            sys.exit(0)

    except requests.packages.urllib3.exceptions.MaxRetryError, e:
            print '                                                                                    [IPTVxtra ERROR - die angeforderter URL ist nicht erreichbar]'
            exitcode = "501"
            xbmc.executebuiltin('XBMC.Notification(allgemeiner Netzwerkfehler , pruefe dein Netzwerk oder die Routerkonfiguration - Router und Kabelmodem für 10 min vom Stromnetz nehmen,25000,'+net+')')
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

def timenow(timex):
    strloc_min = str(time.localtime()[4])
    if len(strloc_min) == 1:
        strloc_min = '0' + strloc_min
    strloc_std = str(time.localtime()[3])   
    if len(strloc_std) == 1:
        strloc_std = '0' + strloc_std
    strloc_day = str(time.localtime()[2])
    if len(strloc_day) == 1:
        strloc_day = '0' + strloc_day
    strloc_mon = str(time.localtime()[1])
    if len(strloc_mon) == 1:
        strloc_mon = '0' + strloc_mon

    timex = timex.partition(':')
    timea = str(time.localtime()[3]) + ":" + strloc_min
    timeb = str(time.localtime()[3]) + strloc_min
    timec = timex[0] + timex[2]
    timed = str(time.localtime()[0]) + strloc_mon + strloc_day + strloc_std + strloc_min + '00'
    timenow = [timea,timeb,timec,timed] # Sytemzeit / SysZeit ohne : / übergebene Zeit ohne : / xmltv Zeit
    return timenow
  
def create_senderliste():
    hdx = 0
    try: 
        hdxx = int(__settings__.getSetting("hd_aktivx"))
        if hdxx > 0 and servhost == '0': hdx = hdxx
    except: hdx = 2
    senderliste = []
    if __settings__.getSetting("setCAT00") == 'true':
        if channelcheck("xch01") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ARD","ARD.de",__settings__.getSetting("xch01")])
        if channelcheck("xch01") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ARD HD","ARD.de",__settings__.getSetting("xch01")])
        if channelcheck("xch02") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ZDF","ZDF.de",__settings__.getSetting("xch02")])
        if channelcheck("xch02") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ZDF HD","ZDF.de",__settings__.getSetting("xch02")])	
        if channelcheck("xch03") > 0: senderliste.append(["SAT 1","Sat1.ch",__settings__.getSetting("xch03")])
        if channelcheck("xch04") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["PRO 7","Pro7.ch",__settings__.getSetting("xch04")])
        if channelcheck("xch04") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["PRO 7 HD","Pro7.ch",__settings__.getSetting("xch04")])
        if channelcheck("xch05") > 0: senderliste.append(["PRO 7 maxx","Pro7maxx.ch",__settings__.getSetting("xch05")])
        if channelcheck("xch06") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["RTL","RTL.de",__settings__.getSetting("xch06")])
        if channelcheck("xch06") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["RTL HD","RTL.de",__settings__.getSetting("xch06")])
        if channelcheck("xch07") > 0: senderliste.append(["RTL 2","RTL2.de",__settings__.getSetting("xch07")])
        if channelcheck("xch08") > 0: senderliste.append(["Super RTL","SRTL.de",__settings__.getSetting("xch08")])
        if channelcheck("xch09") > 0: senderliste.append(["RTL nitro","RTLNitro.de",__settings__.getSetting("xch09")])
        if channelcheck("xch10") > 0: senderliste.append(["VOX","Vox.de",__settings__.getSetting("xch10")])
        if channelcheck("xch11") > 0: senderliste.append(["DMAX","DMAX.ch",__settings__.getSetting("xch11")])
        if channelcheck("xch12") > 0: senderliste.append(["Sixx","Sixx.de",__settings__.getSetting("xch12")])
        if channelcheck("xch13") > 0: senderliste.append(["Kabel 1","Kabel.de",__settings__.getSetting("xch13")])
        if channelcheck("xch14") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["Phoenix","phoenix.de",__settings__.getSetting("xch14")])
        if channelcheck("xch14") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["Phoenix HD","phoenix.de",__settings__.getSetting("xch14")])
	
        if channelcheck("xch29") > 0: senderliste.append(["nickCC","NickComedy.de",__settings__.getSetting("xch29")])
        if channelcheck("xch30") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["KIKA","Kika.de",__settings__.getSetting("xch30")])
        if channelcheck("xch30") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["KIKA HD","Kika.de",__settings__.getSetting("xch30")])
        if channelcheck("xch31") > 0: senderliste.append(["Disney Channel","DisneyChannel",__settings__.getSetting("xch31")])
        if channelcheck("xch32") > 0: senderliste.append(["RIC","RIC.de",__settings__.getSetting("xch32")])		
	
        if channelcheck("xch108") > 0: senderliste.append(["das Neue TV","dasneuetv",__settings__.getSetting("xch108")])
        if channelcheck("xch109") > 0: senderliste.append(["Welt der Wunder","www.de",__settings__.getSetting("xch109")])
        if channelcheck("xch33") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ZDFneo","ZDFneo.de",__settings__.getSetting("xch33")])
        if channelcheck("xch33") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ZDFneo HD","ZDFneo.de",__settings__.getSetting("xch33")])
        if channelcheck("xch34") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ZDFinfo","ZDFinfo.de",__settings__.getSetting("xch34")])
        if channelcheck("xch34") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ZDFinfo HD","ZDFinfo.de",__settings__.getSetting("xch34")])
        if channelcheck("xch35") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ZDFkultur","zdf.kultur",__settings__.getSetting("xch35")])
        if channelcheck("xch35") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ZDFkultur HD","zdf.kultur",__settings__.getSetting("xch35")])
        if channelcheck("xch37") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ARTE","ARTE.de",__settings__.getSetting("xch37")])
        if channelcheck("xch37") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ARTE HD","ARTE.de",__settings__.getSetting("xch37")])	
        if channelcheck("xch38") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["3SAT","3sat.de",__settings__.getSetting("xch38")])
        if channelcheck("xch38") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["3SAT HD","3sat.de",__settings__.getSetting("xch38")])	
        if channelcheck("xch39") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["WDR","WDR.de",__settings__.getSetting("xch39")])
        if channelcheck("xch39") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["WDR HD","WDR.de",__settings__.getSetting("xch39")])
        if channelcheck("xch40") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["SWR","SWR.de",__settings__.getSetting("xch40")])
        if channelcheck("xch40") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["SWR HD","SWR.de",__settings__.getSetting("xch40")])
        if channelcheck("xch41") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["BR","BR.de",__settings__.getSetting("xch41")])
        if channelcheck("xch41") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["BR HD","BR.de",__settings__.getSetting("xch41")])
        if channelcheck("xch42") > 0: senderliste.append(["BRalpha","BR-alpha",__settings__.getSetting("xch42")])
        if channelcheck("xch43") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["HRfernsehen","hr-fernsehen",__settings__.getSetting("xch43")])
        if channelcheck("xch43") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["HRfernsehen HD","hr-fernsehen",__settings__.getSetting("xch43")])
        if channelcheck("xch44") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["RBB Berlin","rbb.de",__settings__.getSetting("xch44")])
        if channelcheck("xch44") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["RBB Berlin HD","rbb.de",__settings__.getSetting("xch44")])
        if channelcheck("xch107") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["MDR","mdr.de",__settings__.getSetting("xch107")])        
        if channelcheck("xch107") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["MDR HD","mdr.de",__settings__.getSetting("xch107")])                  
        if channelcheck("xch45") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["NDR","NDR.de",__settings__.getSetting("xch45")])              
        if channelcheck("xch45") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["NDR HD","NDR.de",__settings__.getSetting("xch45")])
        if channelcheck("xch106") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ServusTV (DE)","ServusTV.de",__settings__.getSetting("xch106")])
        if channelcheck("xch106") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ServusTV (DE) HD","ServusTV.de",__settings__.getSetting("xch106")])
        if channelcheck("xch133") > 0: senderliste.append(["Tele 5","Tele5.de",__settings__.getSetting("xch133")])
        if channelcheck("xch134") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ANIXE","anixe.de",__settings__.getSetting("xch134")])
        if channelcheck("xch134") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ANIXE HD","anixe.de",__settings__.getSetting("xch134")])
        if channelcheck("xch135") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["Eins plus","EinsPlus",__settings__.getSetting("xch135")])
        if channelcheck("xch135") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["Eins plus HD","EinsPlus",__settings__.getSetting("xch135")])
        if channelcheck("xch136") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["Eins festival","Einsfestival",__settings__.getSetting("xch136")])
        if channelcheck("xch136") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["Eins festival HD","Einsfestival",__settings__.getSetting("xch136")])
        if channelcheck("xch137") > 0: senderliste.append(["Deutsche Welle","dwelle.de",__settings__.getSetting("xch137")])	
    if __settings__.getSetting("setCAT10") == 'true':
        if channelcheck("xch22") > 0: senderliste.append(["Eurosport","Eurosport.de",__settings__.getSetting("xch22")])
        if channelcheck("xch23") > 0: senderliste.append(["Sport 1","Sport1HD.de",__settings__.getSetting("xch23")])
        if channelcheck("xch16") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["tagesschau24","tagesschau24.de",__settings__.getSetting("xch16")])
        if channelcheck("xch16") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["tagesschau24 HD","tagesschau24.de",__settings__.getSetting("xch16")])
        if channelcheck("xch17") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["N24","n24.de",__settings__.getSetting("xch17")])
        if channelcheck("xch17") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["N24 HD","n24.de",__settings__.getSetting("xch17")])
        if channelcheck("xch18") > 0: senderliste.append(["N-TV","ntv.de",__settings__.getSetting("xch18")])
        if channelcheck("xch19") > 0: senderliste.append(["Euronews","Euronews.nws",__settings__.getSetting("xch19")])
    if __settings__.getSetting("setCAT20") == 'true':
        if channelcheck("xch24") > 0: senderliste.append(["Viva","VivaGermany.de",__settings__.getSetting("xch24")])
        if channelcheck("xch93") > 0: senderliste.append(["Deluxe Music","deluxemusic",__settings__.getSetting("xch93")])
        if channelcheck("xch25") > 0: senderliste.append(["VEVO Music TV DE","none",__settings__.getSetting("xch25")])
        if channelcheck("xch26") > 0: senderliste.append(["VEVO Music Ch.1","none",__settings__.getSetting("xch26")])
        if channelcheck("xch27") > 0: senderliste.append(["VEVO Music Ch.2","none",__settings__.getSetting("xch27")])
        if channelcheck("xch28") > 0: senderliste.append(["VEVO Music Ch.3","none",__settings__.getSetting("xch28")])
        if channelcheck("xch105") > 0: senderliste.append(["Radio 105 TV italy","none",__settings__.getSetting("xch105")])
        if channelcheck("xch94") > 0: senderliste.append(["nex1 TV","nex1tv",__settings__.getSetting("xch94")])
    if __settings__.getSetting("setCAT30") == 'true':
        if channelcheck("xch47") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ORF1","ORF1.de",__settings__.getSetting("xch47")])
        if channelcheck("xch47") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ORF1 HD","ORF1.de",__settings__.getSetting("xch47")])
        if channelcheck("xch48") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ORF2","ORF2.de",__settings__.getSetting("xch48")])
        if channelcheck("xch48") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ORF2 HD","ORF2.de",__settings__.getSetting("xch48")])
        if channelcheck("xch49") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ServusTV","ServusTV.at",__settings__.getSetting("xch49")])
        if channelcheck("xch49") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ServusTV HD","ServusTV.at",__settings__.getSetting("xch49")])
        if channelcheck("xch50") > 0: senderliste.append(["ATV","ATV.de",__settings__.getSetting("xch50")])
    if __settings__.getSetting("setCAT40") == 'true':
        if channelcheck("xch51") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["SF 1","SF1.ch",__settings__.getSetting("xch51")])
        if channelcheck("xch51") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["SF 1 HD","SF1.ch",__settings__.getSetting("xch51")])
        if channelcheck("xch52") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["SF 2","SF2.ch",__settings__.getSetting("xch52")])
        if channelcheck("xch52") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["SF 2 HD","SF2.ch",__settings__.getSetting("xch52")])
        if channelcheck("xch53") > 0: senderliste.append(["SF info","SFInfo.ch",__settings__.getSetting("xch53")])
        if channelcheck("xch36") > 0: senderliste.append(["3 Plus","3plus.ch",__settings__.getSetting("xch36")])
        if channelcheck("xch142") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["S1 TV","s1tv.ch",__settings__.getSetting("xch142")])
        if channelcheck("xch142") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["S1 TV HD","s1tv.ch",__settings__.getSetting("xch142")])
        if channelcheck("xch54") > 0: senderliste.append(["JOIZ","joiz.de",__settings__.getSetting("xch54")])
        if channelcheck("xch55") > 0: senderliste.append(["Tele Basel","Telebasel",__settings__.getSetting("xch55")])
        if channelcheck("xch56") > 0: senderliste.append(["Tele Zuri","TeleZuri",__settings__.getSetting("xch56")])
        if channelcheck("xch57") > 0: senderliste.append(["Tele Barn","TeleBarn",__settings__.getSetting("xch57")])
        if channelcheck("xch58") > 0: senderliste.append(["TeleBieLingue","TeleBielingue",__settings__.getSetting("xch58")])
        if channelcheck("xch59") > 0: senderliste.append(["Tele 1","Tele1",__settings__.getSetting("xch59")])
        if channelcheck("xch60") > 0: senderliste.append(["TeleM1 West","TeleM1",__settings__.getSetting("xch60")])
        if channelcheck("xch61") > 0: senderliste.append(["TeleM1 Ost","TeleM1",__settings__.getSetting("xch61")])
        if channelcheck("xch62") > 0: senderliste.append(["Tele Top TG","TeleTop",__settings__.getSetting("xch62")])
        if channelcheck("xch63") > 0: senderliste.append(["Tele Top ZH","TeleTop",__settings__.getSetting("xch63")])
        if channelcheck("xch64") > 0: senderliste.append(["Tele Top SH","TeleTop",__settings__.getSetting("xch64")])
    if __settings__.getSetting("setCAT50") == 'true':
        if channelcheck("xch87") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["BBC one","BBC1",__settings__.getSetting("xch87")])
        if channelcheck("xch87") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["BBC one HD","BBC1",__settings__.getSetting("xch87")])
        if channelcheck("xch88") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["BBC two","BBC2",__settings__.getSetting("xch88")])
        if channelcheck("xch88") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["BBC two HD","BBC2",__settings__.getSetting("xch88")])
        if channelcheck("xch89") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["BBC three","BBC3",__settings__.getSetting("xch89")])
        if channelcheck("xch89") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["BBC three HD","BBC3",__settings__.getSetting("xch89")])
        if channelcheck("xch125") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["BBC four","BBC4",__settings__.getSetting("xch125")])
        if channelcheck("xch125") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["BBC four HD","BBC4",__settings__.getSetting("xch125")])
        if channelcheck("xch126") > 0: senderliste.append(["CNBC","CNBC",__settings__.getSetting("xch126")])
        if channelcheck("xch127") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["ITV 1","ITV1",__settings__.getSetting("xch127")])
        if channelcheck("xch127") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["ITV 1 HD","ITV1",__settings__.getSetting("xch127")])
        if channelcheck("xch128") > 0: senderliste.append(["ITV 2","ITV2",__settings__.getSetting("xch128")])
        if channelcheck("xch129") > 0: senderliste.append(["ITV 3","ITV3",__settings__.getSetting("xch129")])
        if channelcheck("xch130") > 0: senderliste.append(["ITV 4","ITV4",__settings__.getSetting("xch130")])
        if channelcheck("xch20") > 0: senderliste.append(["CNN","CNN.nws",__settings__.getSetting("xch20")])
        if channelcheck("xch21") > 0: senderliste.append(["Bloomberg","Bloomberg.nws",__settings__.getSetting("xch21")])
        if channelcheck("xch90") > 0: senderliste.append(["BBC Sport (SD)","bbcsport",__settings__.getSetting("xch90")])
        if channelcheck("xch91") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["BBC News","bbcnews",__settings__.getSetting("xch91")])
        if channelcheck("xch91") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["BBC News HD","bbcnews",__settings__.getSetting("xch91")])
        if channelcheck("xch92") > 0: senderliste.append(["BBC World","bbcworld",__settings__.getSetting("xch92")])	
        if channelcheck("xch119") > 0: senderliste.append(["London Live","london_live",__settings__.getSetting("xch119")])  
        if channelcheck("xch120") > 0: senderliste.append(["NBC Golf","nbc_golf",__settings__.getSetting("xch120")]) 	
        if channelcheck("xch112") > 0: senderliste.append(["Eurosport (UK)","Eurosport.uk",__settings__.getSetting("xch112")])
        if channelcheck("xch65") > 0: senderliste.append(["Film4","Film4",__settings__.getSetting("xch65")])
        if channelcheck("xch66") > 0: senderliste.append(["E4","E4",__settings__.getSetting("xch66")])
        if channelcheck("xch124") > 0: senderliste.append(["more4","more4",__settings__.getSetting("xch124")])
        if channelcheck("xch131") > 0 and (hdx == 0 or hdx == 2): senderliste.append(["Channel 4","channel4",__settings__.getSetting("xch131")])
        if channelcheck("xch131") > 0 and (hdx == 1 or hdx == 2): senderliste.append(["Channel 4 HD","channel4",__settings__.getSetting("xch131")])
        if channelcheck("xch132") > 0: senderliste.append(["Channel 5","channel5",__settings__.getSetting("xch132")])
    if __settings__.getSetting("setCAT60") == 'true':
        if channelcheck("xch138") > 0: senderliste.append(["Canale 5","canale5.it",__settings__.getSetting("xch138")])
        if channelcheck("xch67") > 0: senderliste.append(["RSI LA1","TSI1.ch",__settings__.getSetting("xch67")])
        if channelcheck("xch68") > 0: senderliste.append(["RSI LA2","TSI2.ch",__settings__.getSetting("xch68")])
        if channelcheck("xch118") > 0: senderliste.append(["LA5","la5.it",__settings__.getSetting("xch118")])
        if channelcheck("xch110") > 0: senderliste.append(["LA6","la6.it",__settings__.getSetting("xch110")])
        if channelcheck("xch121") > 0: senderliste.append(["LA7","la7.it",__settings__.getSetting("xch121")])
        if channelcheck("xch69") > 0: senderliste.append(["Rai 1","Rai1",__settings__.getSetting("xch69")])
        if channelcheck("xch115") > 0: senderliste.append(["Rai 2","Rai2",__settings__.getSetting("xch115")])
        if channelcheck("xch116") > 0: senderliste.append(["Rai 3","Rai3",__settings__.getSetting("xch116")])
        if channelcheck("xch97") > 0: senderliste.append(["Rai 4 (SD)","Rai4",__settings__.getSetting("xch97")])
        if channelcheck("xch98") > 0: senderliste.append(["Rai 5 (SD)","Rai5",__settings__.getSetting("xch98")])
        if channelcheck("xch117") > 0: senderliste.append(["Rai news24","Rainews",__settings__.getSetting("xch117")])	
        if channelcheck("xch95") > 0: senderliste.append(["Rai Movie (SD)","RaiMovie",__settings__.getSetting("xch95")])
        if channelcheck("xch96") > 0: senderliste.append(["Rai Premium (SD)","RaiPremium",__settings__.getSetting("xch96")])
        if channelcheck("xch99") > 0: senderliste.append(["Rai Storia","RaiStoria",__settings__.getSetting("xch99")])
        if channelcheck("xch100") > 0: senderliste.append(["Rai Scuola","RaiScuola",__settings__.getSetting("xch100")])
        if channelcheck("xch101") > 0: senderliste.append(["Rai Sport1","RaiS1",__settings__.getSetting("xch101")])
        if channelcheck("xch102") > 0: senderliste.append(["Rai Sport2","RaiS2",__settings__.getSetting("xch102")])
        if channelcheck("xch103") > 0: senderliste.append(["Rai Gulp","RaiGulp",__settings__.getSetting("xch103")])
        if channelcheck("xch104") > 0: senderliste.append(["Rai yoyo (SD)","Raiyoyo",__settings__.getSetting("xch104")])
        if channelcheck("xch70") > 0: senderliste.append(["Tele Ticino","none",__settings__.getSetting("xch70")])
        if channelcheck("xch140") > 0: senderliste.append(["TV Moda","none",__settings__.getSetting("xch140")])
        if channelcheck("xch141") > 0: senderliste.append(["Italia 1","none",__settings__.getSetting("xch141")])	
    if __settings__.getSetting("setCAT70") == 'true':
        if channelcheck("xch122") > 0: senderliste.append(["France 0","France0",__settings__.getSetting("xch122")])
        if channelcheck("xch71") > 0: senderliste.append(["France 2","France2",__settings__.getSetting("xch71")])
        if channelcheck("xch72") > 0: senderliste.append(["France 3","France3",__settings__.getSetting("xch72")])
        if channelcheck("xch123") > 0: senderliste.append(["France 4","France4",__settings__.getSetting("xch123")])
        if channelcheck("xch73") > 0: senderliste.append(["France 5","France5",__settings__.getSetting("xch73")])
        if channelcheck("xch139") > 0: senderliste.append(["Gulli","gulli.fr",__settings__.getSetting("xch139")])
        if channelcheck("xch111") > 0: senderliste.append(["Eurosport (FR)","Eurosport.fr",__settings__.getSetting("xch111")])
        if channelcheck("xch113") > 0: senderliste.append(["i24news","i24.fr",__settings__.getSetting("xch113")])
        if channelcheck("xch114") > 0: senderliste.append(["BFM TV","bfm.fr",__settings__.getSetting("xch114")])
        if channelcheck("xch74") > 0: senderliste.append(["RTS 1","TSR1.ch",__settings__.getSetting("xch74")])
        if channelcheck("xch75") > 0: senderliste.append(["RTS 2","TSR2.ch",__settings__.getSetting("xch75")])
        if channelcheck("xch76") > 0: senderliste.append(["CartoonNetwork","CartoonNetwork",__settings__.getSetting("xch76")])
        if channelcheck("xch77") > 0: senderliste.append(["ARTE (FR)","arte_fr",__settings__.getSetting("xch77")])
        if channelcheck("xch78") > 0: senderliste.append(["Canal 9","none",__settings__.getSetting("xch78")])
        if channelcheck("xch79") > 0: senderliste.append(["RTL 9","RTL9.ch",__settings__.getSetting("xch79")])
        if channelcheck("xch80") > 0: senderliste.append(["M6","M6",__settings__.getSetting("xch80")])
        if channelcheck("xch81") > 0: senderliste.append(["LaTele","none",__settings__.getSetting("xch81")])
        if channelcheck("xch82") > 0: senderliste.append(["TV5 Monde","TV5MONDE",__settings__.getSetting("xch82")])
        if channelcheck("xch83") > 0: senderliste.append(["TF1","TF1",__settings__.getSetting("xch83")])
        if channelcheck("xch84") > 0: senderliste.append(["LeManBleu","none",__settings__.getSetting("xch84")])
        if channelcheck("xch85") > 0: senderliste.append(["Canal Alpha JU","none",__settings__.getSetting("xch85")])
        if channelcheck("xch86") > 0: senderliste.append(["Canal Alpha NE","none",__settings__.getSetting("xch86")])
        if channelcheck("xch143") > 0: senderliste.append(["Rouge TV","RougeTV.fr",__settings__.getSetting("xch143")])
        if channelcheck("xch144") > 0: senderliste.append(["W 9","W9.fr",__settings__.getSetting("xch144")])
        if channelcheck("xch145") > 0: senderliste.append(["Montagne TV","Montagne.fr",__settings__.getSetting("xch145")])
        if channelcheck("xch146") > 0: senderliste.append(["D 8","D8.fr",__settings__.getSetting("xch146")])
        if channelcheck("xch147") > 0: senderliste.append(["D 17","D17.fr",__settings__.getSetting("xch147")])
        if channelcheck("xch148") > 0: senderliste.append(["NT 1","NT1.fr",__settings__.getSetting("xch148")])
        if channelcheck("xch149") > 0: senderliste.append(["NRJ 12","NRJ12.fr",__settings__.getSetting("xch149")])
        if channelcheck("xch150") > 0: senderliste.append(["Numero 23","No23.fr",__settings__.getSetting("xch150")])
        if channelcheck("xch151") > 0: senderliste.append(["Cherie 25","Cherie25.fr",__settings__.getSetting("xch151")])
        if channelcheck("xch152") > 0: senderliste.append(["Canal +","CANALplus.fr",__settings__.getSetting("xch152")])
        if channelcheck("xch153") > 0: senderliste.append(["TMC","TMC.fr",__settings__.getSetting("xch153")])
        if channelcheck("xch154") > 0: senderliste.append(["Euronews france","euronews.fr",__settings__.getSetting("xch154")])
        if channelcheck("xch155") > 0: senderliste.append(["France 24","France24.fr",__settings__.getSetting("xch155")])
        if channelcheck("xch156") > 0: senderliste.append(["i TELE","iTELE.fr",__settings__.getSetting("xch156")])
        if channelcheck("xch157") > 0: senderliste.append(["HD 1","HD1.fr",__settings__.getSetting("xch157")])
        if channelcheck("xch158") > 0: senderliste.append(["6 ter","6ter.fr",__settings__.getSetting("xch158")])
        if channelcheck("xch159") > 0: senderliste.append(["TV m3","TVM3.fr",__settings__.getSetting("xch159")])
        if channelcheck("xch160") > 0: senderliste.append(["RMC Decouverte","RMCd.fr",__settings__.getSetting("xch160")])
        if channelcheck("xch161") > 0: senderliste.append(["L'Equipe 21","Equipe.fr",__settings__.getSetting("xch161")])
        if channelcheck("xch162") > 0: senderliste.append(["KTO","none",__settings__.getSetting("xch162")])            # 162
        #senderliste.sort(key=operator.itemgetter(2))
    return senderliste

def channelcheck(xch):
    try: xchx = __settings__.getSetting(xch).strip().replace(' ','')
    except:
        __settings__.setSetting(xch,'100')
        xchx = '100'
    if xchx == '' or xchx == ' ':
        __settings__.setSetting(xch,'100')
        xchx = '100'
    try: xchx = int(xchx)
    except: 
        __settings__.setSetting(xch,'100')
        xchx = 100
    return xchx


def channelx():
    mdx = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
    r = requests.get("http://api.iptvxtra.net/check.php", params = {'loc': mdx ,'la':'DE'} )
    return int(r.text)

def meldungen(rtx):
        if rtx == 7:
            xbmc.executebuiltin('XBMC.Notification( verbotener Mehrfach-Login !!! , Dein Zugang wird gleichzeitig von mehreren Standorten aus benutzt - bei 5 Fehlern wird der Zugang bis 24.00 GMT-0 gesperrt - Kodi bitte neu starten ,60000,'+netx+')')
        if rtx == 8:
            xbmc.executebuiltin('XBMC.Notification( verbotener Mehrfach-Login !!! , Dein Zugang wurde automatisch bis 24.00 GMT-0 gesperrt ,60000,'+netx+')')
        if rtx == 9:
            xbmc.executebuiltin('XBMC.Notification( Fehler in den Zugangsdaten  !!! , Ein Fehler wurde in den Zugangsdaten erkannt - Passwort oder Username muss verkehrt sein ,60000,'+netx+')')
        if rtx == 10:
            xbmc.executebuiltin('XBMC.Notification( gesperrter Zugang !!! , Dein Zugang ist auf unbestimmte Zeit gesperrt - wende dich per EMail an uns ,60000,'+netx+')')
        sys.exit(0)

def zapsidemenu():
    iptvepg = xmltv()
    zaplist = read_listfile(xbmc.translatePath('special://temp/040264-1001.fi'))
    mdx = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
    for entry in zaplist:
            try:
                videoTitle = entry[0].strip()
            except: videoTitle = ''
            try:
                thumbnail = entry[1].strip()
            except: thumbnail = ''
            try:
                url = entry[2].strip().replace('plugin://plugin.video.iptvxtra-basic/?preview','')
                #print url
                x = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()

                url= 'plugin://plugin.video.iptvxtra-basic/?zapping'+ url + '***' + videoTitle + '***' + thumbnail + '***  ***' + mdx + '***'
            except: url = ''

            try:
               name2 = ''
               if epg_on == "true":
                    xmlepg = entry[3].strip() 
                    for text in iptvepg:
                        text0 = text[0].strip() 
                        if text0 == '' or text0 == 'abcdefgh' : break
                        if xmlepg == text0 and int(text[4]) > (int(time.time())-(int(timeshift)*3600)):
                            laenge = len(text[5]) + len(text[6]) + 3
                            name2 = text[5]
                            break
            except: name2 = 'no Info'
            addzaplink(videoTitle,name2,url,thumbnail)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    sys.exit(0)

def addzaplink(name,name2,url,iconimage):
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Label": name, "Title": name2 } )
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)

def timeline():
    if record_active == 'true':
        xbmc.executebuiltin('XBMC.Notification('+title_ch+' , einen Moment der Sender wird geladen ,30000,'+icon_ch+')')
    idx =  mode.replace("timeline", "")
    idx = idx.split('#')
    timedelay = 0
    rtx = channelx()

    if record_active == 'true': replaylang = 14400
    else: replaylang = 14400

    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    xel.getControl(int(idx[0])).setLabel('Replay active until ' + __settings__.getSetting("data4") )
    if  __settings__.getSetting("data2") == '0':
        xbmc.executebuiltin('XBMC.Notification(Replay Error , Sorry - the time for replay expired on '+__settings__.getSetting("data4")+' ,10000)')
        sys.exit(0)

    try:
        timex = xel.getControl(int(idx[1])).getLabel()      # Zeit
        local = xel.getControl(int(idx[2])).getLabel()		# lokal oder de-zeit
        datex = xel.getControl(int(idx[3])).getLabel()		# Datum
        stream = xel.getControl(int(idx[4])).getLabel() 	# stream
    except:
        timex = idx[1]
        local = idx[2]
        datex = idx[3]
        stream = idx[4]

    if int(idx[5]) > 1300:
        seconds = int(xel.getControl(int(idx[5])).getPercent() * 864)
        HOUR = 60 * 60
        MINUTE = 60
        hours = str(seconds // HOUR)
        seconds = seconds % HOUR
        minutes = str(seconds // MINUTE)
        if len(hours) == 1: hours = '0'+ hours
        if len(minutes) == 1: minutes = '0'+ minutes
        timex = hours+':'+minutes
        xel.getControl(int(idx[1])).setLabel('Set Time:   '+timex)
    stream =  stream.replace('plugin://plugin.video.iptvxtra-de/?preview','').replace('plugin://plugin.video.iptvxtra-de/preview','')
    stream =  stream.replace('plugin://plugin.video.iptvxtra-basic/?preview','').replace('plugin://plugin.video.iptvxtra-basic/preview','')
    stream =  stream.replace("###", "|")
    stream =  stream.replace("***", "|")
    stream =  stream.replace("#x#", "?")
    stream =  stream.replace("#h#", "http://")
    stream =  stream.replace("referer", "Referer")
    timediff = int(timeshift) * 3600
    timenow = int(time.time())
    timex = timex.replace(' ','')
    timex = timex.replace('SetTime:','')
    if datex == 'today':
        datex = str(date.today())
    zeit_string = datex + ' ' + timex
    timestart = int(time.mktime(time.strptime(zeit_string, "%Y-%m-%d %H:%M")))
    timeend = timestart + replaylang

    if rtx > 5: meldungen(rtx)
    if local == 'deutsche Zeit' or local == 'de' or __settings__.getSetting("replayDE") == 'true':
        timestart = timestart + timediff  
        timeend = timestart + replaylang
    if timestart < timenow-604800:
        timestart = timenow-604300
        timeend = timestart + replaylang
    if timeend > timenow:
        timeend = timenow - 180
    if timestart > timenow-180:					# wird live wiedergegeben - nach delay-befehl wird noch gesucht
        timestart = timenow - 180
        timeend = timenow + 180
    if timestart > timenow-7200:
        timedelay = timenow - timestart
    if '|' in stream:
        stream = stream.partition('|')
        stream = stream[0] + '?start=' + str(timestart) + '&end=' + str(timeend) + '|' + stream[2]
    else:
        stream = stream + '?start=' + str(timestart) + '&end=' + str(timeend)
    stream = stream.replace('m3u8start','m3u8?start')
    __settings__.setSetting("rep3", str(timestart))
    __settings__.setSetting("rep4", str(timeend))

    if record_active == 'true':
        url = stream.split('?')[0] + '***' + str(timestart) + '***' + str(timeend) + '***' + stream.split('X-Forwarded-For=')[1] + '***' + title_ch + '***' + icon_ch + '***' + 'tophits2' + '***' + hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
        url = url.encode("hex")
        px = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/zapp.py")
        xbmc.executebuiltin('RunScript('+px+',url='+url+')')
        sys.exit(0)


    try: __settingsreload__.setSetting("is_addon", "de")
    except: pass

    listitem = xbmcgui.ListItem( title_ch, iconImage=icon_ch, thumbnailImage=icon_ch)
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add( stream, listitem )

    try: __settingsreload__.setSetting("def4", str(int(time.time())))
    except: pass

    stream = stream.replace('|','&&')
    xbmc.executebuiltin("Skin.SetString(iptvxtra_starttime_aktuell, "+datetime.fromtimestamp(timestart).strftime('%H:%M')+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_endtime_aktuell, "+datetime.fromtimestamp(timeend).strftime('%H:%M')+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_stream_aktuell, "+stream+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_time_aktuell, "+str(int(time.time()))+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_titel_aktuell, "+title_ch+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_icon_aktuell, "+icon_ch+")")
    xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_ok)")

    if __settings__.getSetting("setFull") == 'true': xbmcPlayer.play(playlist,None,False)
    else: xbmcPlayer.play(playlist,None,True)
    xbmc.executebuiltin( "Dialog.Close(infodialog)" )
    sys.exit(0)

def timeset():
    idx =  mode.replace("timeset", "")
    idxx = int(idx[4:8])
    idx = int(idx[0:4])
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    dialog = xbmcgui.Dialog()    	
    keyboard = xbmc.Keyboard()
    keyboard.setHiddenInput(False)
    keyboard.setHeading('Set Play Time - examples 20:15 or 2015 or 20x15 ')
    keyboard.doModal()
    if keyboard.isConfirmed():        	
       	timex = keyboard.getText()
        if len(timex) == 3:
            timex = '0' + timex[0:1] + ':'+ timex[1:3]	
        if len(timex) == 4:
            timex = timex[0:2] + ':'+ timex[2:4]
        elif len(timex) == 5:
            timex = timex[0:2] + ':'+ timex[3:5]
        elif len(timex) == 0:
            timex = time.strftime("%H:%M")
        else:
           xbmc.executebuiltin('XBMC.Notification(Error , incorrect time information ,5000,'+net+')')
           sys.exit(0)
        if int(timex[0:2]) > 23:
            timex = '00:'+ timex[3:5]
        if int(timex[3:5]) > 59:
            timex = timex[0:2] + ':59'
        slidex = int(timex[0:2])*3600 + int(timex[3:5])*60
        timex = 'Set Time:   ' + timex
        xel.getControl(idx).setLabel(timex)
        if idxx > 1300:
            xel.getControl(idxx).setPercent(slidex/864.00000000)
    sys.exit(0)

def repset():
    repset1 = __settings__.getSetting("rep1")
    repset2 = __settings__.getSetting("rep2")
    if repset1 == '': repset1 = 'local Time'
    if repset2 == '': repset2 = 'today'
    if __settings__.getSetting("replayDE") == 'true': 
        repset1 = 'deutsche Zeit'
        __settings__.setSetting("rep1","deutsche Zeit")

    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    try: xel.getControl(1307).setLabel(repset1)
    except: pass
    try: xel.getControl(1301).setLabel(repset2)
    except: pass
    try: xel.getControl(1337).setLabel(repset1)
    except: pass
    try: xel.getControl(1331).setLabel(repset2)
    except: pass
    try: xel.getControl(1367).setLabel(repset1)
    except: pass
    try: xel.getControl(1361).setLabel(repset2)
    except: pass
    try: xel.getControl(1387).setLabel(repset1)
    except: pass
    try: xel.getControl(1381).setLabel(repset2)
    except: pass

def setslidx():
    idx =  mode.replace("setslidx", "") 
    idx = idx.split('#')
    x = int(idx[2]) * 60 * 60
    if x == 0: x = 1
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    xel.getControl(int(idx[0])).setPercent(x/864.00000000)
    xel.getControl(int(idx[1])).setLabel('Set Time:   '+idx[2]+':00')
    sys.exit(0)

def setslidmin():
    idx =  mode.replace("setslidmin", "")
    idx = idx.split('#')
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    x = int(xel.getControl(int(idx[0])).getPercent() * 864)
    if idx[2] == '+60': xskip = int(__settings__.getSetting("skip1")) * 60
    elif idx[2] == '-60': xskip = int('-' + __settings__.getSetting("skip1")) * 60
    elif idx[2] == '+300': xskip = int(__settings__.getSetting("skip2")) * 60
    elif idx[2] == '-300': xskip = int('-' + __settings__.getSetting("skip2")) * 60
    elif idx[2] == '+600': xskip = int(__settings__.getSetting("skip3")) * 60
    elif idx[2] == '-600': xskip = int('-' + __settings__.getSetting("skip3")) * 60
    x = x + xskip
    xel.getControl(int(idx[0])).setPercent(x/864.00000000)
    HOUR = 60 * 60
    MINUTE = 60
    hours = str(x // HOUR)
    x = x % HOUR
    minutes = str(x // MINUTE)
    if len(hours) == 1: hours = '0'+ hours
    if len(minutes) == 1: minutes = '0'+ minutes
    timex = hours+':'+minutes
    if '-' in timex: timex = '00:01'
    if int(timex[0:2]+timex[3:5]) > 2359 : timex = '23:59'
    xel.getControl(int(idx[1])).setLabel('Set Time:   '+timex)
    sys.exit(0)

def setmin():
    realtimejetzt = int(time.time())
    idx =  mode.replace("setmin#", "")
    idx = idx.split('#')
    if   idx[0] == '+60': xskip = int(__settings__.getSetting("skip1")) * 60
    elif idx[0] == '-60': xskip = int('-' + __settings__.getSetting("skip1")) * 60
    elif idx[0] == '+300': xskip = int(__settings__.getSetting("skip2")) * 60
    elif idx[0] == '-300': xskip = int('-' + __settings__.getSetting("skip2")) * 60
    elif idx[0] == '+600': xskip = int(__settings__.getSetting("skip3")) * 60
    elif idx[0] == '-600': xskip = int('-' + __settings__.getSetting("skip3")) * 60
	
    local = int(__settings__.getSetting("timeshift")) * 3600
    local = 0

    realtimestart = int(idx[1])
    timedif = realtimejetzt - realtimestart
    ida = idx[2].partition('start=')
    stream = ida[0]
    idb = ida[2].partition('&end=')
    start = str(int(idb[0]) + timedif + xskip)
    idc = idb[2].partition('&&')
    end = int(start ) + 14400
    if end > realtimejetzt:
        end = realtimejetzt - 180
    forw = idc[2]
    stream = stream + '?start=' + start + '&end=' + str(end) + '|' + forw

    __settings__.setSetting("rep3", start)
    __settings__.setSetting("rep4", str(end))

    streamx = stream.replace('?','')
    streamx = streamx.replace('|','&&')
    xbmc.executebuiltin("Skin.SetString(iptvxtra_stream_aktuell, "+streamx+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_time_aktuell, "+str(int(time.time()))+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_starttime_aktuell, "+datetime.fromtimestamp(int(start)+local).strftime('%H:%M')+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_endtime_aktuell, "+datetime.fromtimestamp(int(end)+local).strftime('%H:%M')+")")
    xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_ok)")

    title = idx[3]
    icon = idx[4]
    listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add( stream, listitem )

    try: __settingsreload__.setSetting("def4", str(int(time.time())))
    except: pass

    xbmcPlayer.play(playlist,None,False)
    xbmc.executebuiltin( "Dialog.Close(infodialog)" )
    sys.exit(0)

def refresh():
    print '---------------------------------'
    print mode
    print '---------------------------------'

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





if 'refresh' in mode: refresh()
elif 'zapsidemenu' in mode: zapsidemenu()
elif 'timeline' in mode: timeline()
elif 'timeset' in mode: timeset()
elif 'setslidx' in mode: setslidx()
elif 'setslidmin' in mode: setslidmin()
elif 'setmin' in mode: setmin()

else: main()
mode = 'true'






