# -*- coding: utf-8 -*-

import xbmcgui,xbmc,xbmcaddon,os,sys,time,re,threading,shutil,hashlib
from datetime import date, datetime,timedelta
import requests as requests
xbmcPlayer = xbmc.Player()
xbmcPlayer.stop()
temp = xbmc.translatePath("special://temp/")
icon = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/iptv.png")
net = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/netx.png")
xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")
xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_segment_ok)")
xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_ok)")
__settings__ = xbmcaddon.Addon(id="plugin.video.iptvxtra-de")
record_active = __settings__.getSetting("record_live_active")
record_time = __settings__.getSetting("record_live_time")
record_endtime = __settings__.getSetting("record_live_endtime")
record_quali = __settings__.getSetting("hd_aktiv")
record_folderx = __settings__.getSetting("record_folder")
max2g = __settings__.getSetting("record_max2g")
fullscreen = __settings__.getSetting("setFull")
user= __settings__.getSetting("login").strip()
pwd= __settings__.getSetting("password").strip()
mdx = hashlib.md5('#user='+user+'pass='+pwd).hexdigest()
modex = sys.argv[1].replace("url=", "")
try: mode = modex.decode("hex")
except: mode = modex
idx = mode.split('***')
xbmcPlayer = xbmc.Player()
xbmcPlayer.stop()


def replay_pfad(record_folderx,temp):
        if record_folderx == 'Kodi Cache Verzeichnis': record_folderx = temp
        if not os.path.isdir(record_folderx):
            xbmc.executebuiltin( "Dialog.Close(infodialog)" ) 
            xbmc.executebuiltin('XBMC.Notification(der Download-Pfad wurde nicht gefunden , der Standard Temp Pfad von Kodi wurde gesetzt ,5000,'+icon+')')
            __settings__.setSetting("record_folder","Kodi Cache Verzeichnis")
            record_folderx = temp
        record_folder_neu = os.path.join(record_folderx,'IPTVxtraPL','lxa')
        record_folderx = os.path.join(record_folderx,'IPTVxtraPL','erfgbn.txt').replace('erfgbn.txt','')
        shutil.rmtree(record_folderx, ignore_errors=True)

        try: os.makedirs(record_folder_neu)
        except:
            try:
                shutil.rmtree(record_folderx, ignore_errors=True)
                os.makedirs(record_folder_neu)
            except: pass
	return record_folderx
	
def runstream(max2g,record_time,record_folderx,record_quali,record_active,idx,temp,record_endtime,fullsceen,mdx):	
    m3u8_files = getstream(mdx)
    if record_active.strip() != 'true' or 'http://c001.p' not in idx[0]:
        print idx
        if 'giniko.com' in idx[0]: idx[0] = ginico(idx[0])
        try: listitem = xbmcgui.ListItem( idx[4], iconImage=idx[5], thumbnailImage=idx[5])
        except: listitem = xbmcgui.ListItem( idx[4], iconImage=icon, thumbnailImage=icon)
        playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
        playlist.clear()
        playlist.add( idx[0]+ '|X-Forwarded-For=' + idx[3], listitem )
        xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell, plugin://plugin.video.iptvxtra-de)") 
        if fullsceen == 'false': xbmcPlayer.play(playlist,listitem,True)
        else: xbmcPlayer.play(playlist,listitem,False)	
        xbmc.executebuiltin( "Dialog.Close(infodialog)" )
        sys.exit(0)

    record_folder = replay_pfad(record_folderx,temp)
    if 'IPTVxtraPL' not in record_folder: record_folder = replay_pfad(record_folderx,temp)

    try: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' , einen Moment der Stream wird analysiert ,30000,'+idx[5]+')')
    except: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' , einen Moment der Stream wird analysiert ,30000,'+icon+')')
    m3u8_file = idx[0]
    pufferpause = 0

    xbmc.executebuiltin("Skin.SetString(iptvxtra_titel_aktuell, "+idx[4]+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_icon_aktuell, "+idx[5]+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell, plugin://plugin.video.iptvxtra-de)") 

    if record_endtime == '0': rend = 1440; rendx = '04:00'
    elif record_endtime == '1': rend = 2160; rendx = '06:00'
    elif record_endtime == '2': rend = 2880; rendx = '08:00'

    xbmc.executebuiltin("Skin.SetString(iptvxtra_starttime_aktuell, 00:00)")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_endtime_aktuell, "+rendx+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_stream_aktuell, "+m3u8_file.replace('|','&&')+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_time_aktuell, "+str(int(time.time()))+")")
    xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_segment_ok)")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_live_ok, true)")

    if record_active == 'true':

        try:
            if len(filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder))) > 0:
                for i in filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder)):
                    try: os.remove(record_folder + i)
                    except: pass
        except: pass


        if 'hd_1' in m3u8_file: quali = 'index_2500_av-p.m3u8'
        else: quali = 'index_1300_av-p.m3u8'
        url = m3u8_file.replace('master.m3u8',quali).split('###')


        try: r=requests.get(url[0], headers={"X-Forwarded-For":idx[3], "User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"})
        except:
            try: r=requests.get(url[0].replace('_av-p','_av-b'), headers={"X-Forwarded-For":idx[3], "User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"})
            except:	
                xbmc.executebuiltin( "Dialog.Close(infodialog)" )
                xbmc.executebuiltin('XBMC.Notification(Playlist Download Fehler ! , dieser Stream kann gerade nicht geladen werden ,7000,'+icon+')')
                sys.exit(0)
        print r.text


        try: segment_nr = re.findall(r'EXT-X-MEDIA-SEQUENCE:(\d*)',r.text)[0]
        except:
            xbmc.executebuiltin( "Dialog.Close(infodialog)" )
            xbmc.executebuiltin('XBMC.Notification(Segment Download Fehler ! , dieser Stream kann noch nicht geladen werden ,7000,'+icon+')')
            sys.exit(0)
        segmentx = re.findall(r'(http://.*?ts)',r.text)
        segment_part = segmentx[0].split(segment_nr)
        a = 0

        segment_urls = []
        for i in range(0,rend):
            new_segnr = str(int(segment_nr) + i)
            new_segment_part = segment_part[0] + new_segnr + segment_part[1]
            segment_urls.append(new_segment_part.replace('_av-b','_av-p'))

        if not os.path.isdir(record_folder): record_folder = replay_pfad(record_folderx,temp)
	
        segment_urlsx=[]
        for id in segment_urls:
            a = a + 1
            # xx = re.findall(r'(akamaihd.net/i/.*?.ts)',id)[0].replace('/','_').replace('akamaihd.net_i_',record_folder).replace('@','_')
            xx = re.findall(r'(edgesuite.net/i/c001/.*?.ts)',id)[0].replace('/','_').replace('edgesuite.net_i_c001_',record_folder).replace('@','_')
            segment_urlsx.append([id,xx.replace('_av-p',''),str(a)]) 
            if a == 2: a = 0
        segment_urls = segment_urlsx

        try:
            if max2g == 'false': max2g = 0
            else: max2g = 1
        except: max2g = 1
		
        try: os.remove(temp + "stop.stp")
        except: pass

        thread_IPTVxtraGrabber = ChunkGrabber(segment_urls, record_folder, idx[3], segment_part, max2g)
        thread_IPTVxtraGrabber.start()
        try: os.remove(record_folder + 'IPTVxtra.m3u8')
        except: pass
        m3u8_file = record_folder + 'IPTVxtra.m3u8'
        fobj_out = open(m3u8_file,"w")
        fobj_out.write('#EXTM3U'+'\n')
        fobj_out.write('#EXT-X-TARGETDURATION:10'+'\n')
        fobj_out.write('#EXT-X-ALLOW-CACHE:YES'+'\n')
        fobj_out.write('#EXT-X-VERSION:3'+'\n')
        fobj_out.write('#EXT-X-MEDIA-SEQUENCE:'+'\n')
        for id in segment_urlsx:
            fobj_out.write('#EXTINF:10.000,'+'\n')
            fobj_out.write(id[1] + '\n')
        fobj_out.write('#EXT-X-DISCONTINUITY'+'\n')
        fobj_out.write('#EXT-X-ENDLIST'+'\n')
        fobj_out.close()

        if record_time == '0': n = 20; puffersoll = 1
        elif record_time == '1': n = 30; puffersoll = 3
        elif record_time == '2': n = 40; puffersoll = 6

        i = 0
        while i <= n:
            pufferak = xbmc.getInfoLabel("Skin.String(iptvxtra_replaypuffer)")
            if pufferak == '': pufferak = '0'
            try: 
                if int(pufferak) > puffersoll: break
            except:
                i = 500
                break
            pufferaktuell = xbmc.getInfoLabel("Skin.String(iptvxtra_replaytext)")
            if pufferaktuell == '':
                try: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' ,der Download der Sendung ist gestartet ,100,'+idx[5]+')')
                except: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' ,der Download der Sendung ist gestartet ,100,'+icon+')')
            else:
                try: xbmc.executebuiltin('XBMC.Notification('+pufferaktuell+' ,der Download der Sendung ist gestartet ,100,'+idx[5]+')')
                except: xbmc.executebuiltin('XBMC.Notification('+pufferaktuell+' ,der Download der Sendung ist gestartet ,100,'+icon+')')
            time.sleep(1)
            i = i + 1
        if i > n: pufferpause = 1
        xbmc.executebuiltin( "Dialog.Close(infodialog)" )
	
    try: fobj_out.close()
    except: pass

    try: listitem = xbmcgui.ListItem( idx[4], iconImage=idx[5], thumbnailImage=idx[5])
    except: listitem = xbmcgui.ListItem( idx[4], iconImage=icon, thumbnailImage=icon)
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add( m3u8_file, listitem )
    if fullsceen == 'false': xbmcPlayer.play(playlist,listitem,True)
    else: xbmcPlayer.play(playlist,listitem,False)
    if pufferpause == 1: xbmcPlayer.pause()
    xbmc.executebuiltin( "Dialog.Close(infodialog)" )
    sys.exit(0)


def getstream(mdx):
    import requests as requests
    try:	
        r = requests.get("http://api.iptvxtra.net/check.php", params = {'loc': mdx ,'la':'DE'} )
        rtx = int(r.text)
    except:
        xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler , fehlerhafter Zugang zum Login-Server,25000,'+net+')')
        sys.exit(0)
    if rtx > 5:
        if rtx == 7:
            xbmc.executebuiltin('XBMC.Notification( verbotener Mehrfach-Login !!! , Dein Zugang wird gleichzeitig von mehreren Standorten aus benutzt - bei 5 Fehlern wird der Zugang bis 24.00 GMT-0 gesperrt - Kodi bitte neu starten ,60000,'+net+')')
        if rtx == 8:
            xbmc.executebuiltin('XBMC.Notification( verbotener Mehrfach-Login !!! , Dein Zugang wurde automatisch bis 24.00 GMT-0 gesperrt ,60000,'+net+')')
        if rtx == 9:
            xbmc.executebuiltin('XBMC.Notification( Fehler in den Zugangsdaten  !!! , Ein Fehler wurde in den Zugangsdaten erkannt - Passwort oder Username muss verkehrt sein ,60000,'+net+')')
        if rtx == 10:
            xbmc.executebuiltin('XBMC.Notification( gesperrter Zugang !!! , Dein Zugang ist auf unbestimmte Zeit gesperrt - wende dich per EMail an uns ,60000,'+net+')')
        sys.exit(0)

def ginico(url):
  
    if 'xxx&User' in url:
        x = url.partition('xxx&User')
        url = x[0] + 'xxx'
    x = url.partition('---')
    url = x[0]
    id = x[2].replace('xxx','')
    r = requests.get("http://giniko.com/watch.php?id=" + id)
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=37")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    r = requests.get("http://giniko.com/watch.php?id=220")
    if r.text.find('m3u8?'):
        s = r.text.partition('m3u8?')
        s = s[2].partition('"')
        if len(s[0]) > 120 and len(s[0]) < 134:
            s = url + '?' + s[0]
            return s
    else: return url

class ChunkGrabber(threading.Thread):
    
    def __init__(self, segment_urls, record_folder, ip, segment_part, max2g):
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")
        threading.Thread.__init__(self)
        self._temp = xbmc.translatePath("special://temp/")
        self._temp_stopfi = xbmc.translatePath("special://temp/stop.stp")
        self._segment_part = segment_part
        self._segment_urls = segment_urls
        self._record_folder = record_folder
        self._m3u8 = record_folder + 'IPTVxtra.m3u8'
        self._ip = ip
        self._max2g = max2g
        self.segmente = 0
        self.puffer_end = 0
        self._neg = 0

    def run(self):  
        try: os.remove(temp + "stop.stp")
        except: pass
        in_stream = False
        pipe_ok = True
        self.puffer_end = 0
        self.segmente = 0
        puffera = 0
        pufferb = 0
        count = 0
        segmentcounter = 0
        ok = ''
        for i in self._segment_urls:
            segmentcount = 600
            if segmentcounter > segmentcount-1: 
                os.remove(self._segment_urls[segmentcounter-segmentcount][1])
                self._neg += 10
                abc = self.playlist(segmentcounter,segmentcount)
            segmentcounter += 1
            
            fifo = open(i[1], "ab")
            if i[0] == self._segment_urls[-1][0] or i[0] == self._segment_urls[-2][0] or i[0] == self._segment_urls[-3][0]: 
                xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, Video-Puffer: komplett)")
                self.puffer_end = 1
            if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
            while pipe_ok:
                if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                try: daten = requests.get(i[0], headers={"X-Forwarded-For":self._ip}, timeout=5)
                except: 
                    if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                    if self.puffer_end == 0: ok = self.set_puffer(0,0)
                    try: daten = requests.get(i[0].replace('_av-p','_av-b'), headers={"X-Forwarded-For":self._ip}, timeout=5)
                    except:
                        if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                        if self.puffer_end == 0: ok = self.set_puffer(0,0)
                        try: daten = requests.get(i[0], headers={"X-Forwarded-For":self._ip}, timeout=10)
                        except:
                            if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                            if self.puffer_end == 0: ok = self.set_puffer(0,0)
                            try: daten = requests.get(i[0].replace('_av-p','_av-b'), headers={"X-Forwarded-For":self._ip}, timeout=10)
                            except:
                                if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                                if self.puffer_end == 0: ok = self.set_puffer(0,0)
                                try: daten = requests.get(i[0], headers={"X-Forwarded-For":self._ip}, timeout=15)
                                except: 
                                    fifo.close()
                                    if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                                    if self.puffer_end == 0: ok = self.set_puffer(0,0)
                                    break
                                    print '-------------------------------------------------------------------- Daten Fehler - ein Live-Segment wurde uebersprungen'

                if (daten):
                    count = 0
                    if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                    try:
                        fifo.write(daten.content)
                        fifo.close()
                        if self.puffer_end == 0: 
                            ok = self.set_puffer(1,0)
                    except IOError:
                        pipe_ok = False
                        break
                    in_stream = True
                    break
                elif (in_stream):
                    time.sleep(1)
                    ok = self.set_puffer(0,0)
                    continue
                break 
            if not pipe_ok: break
            if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
        fifo.close()

        if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8):
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")

    def playlist(self, segmentcounter, segmentcount):
        start = 0
        fobj_out = open(self._m3u8,"w")
        fobj_out.write('#EXTM3U'+'\n')
        fobj_out.write('#EXT-X-TARGETDURATION:10'+'\n')
        fobj_out.write('#EXT-X-ALLOW-CACHE:YES'+'\n')
        fobj_out.write('#EXT-X-VERSION:3'+'\n')
        fobj_out.write('#EXT-X-MEDIA-SEQUENCE:'+'\n')
        for id in self._segment_urls:
            if start >= segmentcounter-segmentcount+2:
                fobj_out.write('#EXTINF:10.000,'+'\n')
                fobj_out.write(id[1] + '\n')
            start += 1
        fobj_out.write('#EXT-X-DISCONTINUITY'+'\n')
        fobj_out.write('#EXT-X-ENDLIST'+'\n')
        fobj_out.close()
        return 'ok'



    def set_puffer(self, zaehl, neg): 
        if zaehl <> 1: zaehl = 0
        puffer = int(xbmc.getInfoLabel("Skin.String(iptvxtra_replaypuffer)"))
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, "+str(puffer + zaehl)+")")
        try: puffera = int(xbmc.Player().getTime())
        except: puffera = 0
        seconds = ((puffer + zaehl) * 10) - puffera
        zaehl = 0
        minutes = seconds // 60
        seconds = seconds % 60
        secx = ''
        if seconds < 10: secx = '0'
        minx = ''
        if minutes < 10: minx = '0'
        pufferx = minx+str(minutes)+':'+secx+str(seconds)
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, Video-Puffer:  "+pufferx+" min)")
        if xbmc.Player.isPlaying and not '0-'in pufferx and puffera > 120 and puffer > -1:
            if neg == 0: xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, "+str(puffera)+")")
            elif self._neg > 0: xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, "+str(puffera-self._neg)+")")
        return 'ok'

    def stop(self):
        open(self._temp_stopfi, "a").close()


runstream(max2g,record_time,record_folderx,record_quali,record_active,idx,temp,record_endtime,fullscreen,mdx)
