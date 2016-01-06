# -*- coding: utf-8 -*-

import xbmcgui,xbmc,xbmcaddon,os,sys,time,re,threading,shutil
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
record_active = __settings__.getSetting("record_active")
record_time = __settings__.getSetting("record_time")
record_quali = __settings__.getSetting("record_quali")
record_folderx = __settings__.getSetting("record_folder")
segment_dl = int(__settings__.getSetting("segment_dl"))
timeshift = int(__settings__.getSetting("timeshift")) * 60 * 60
if segment_dl != 1 or record_active == 'false': segment_dl = 0
max2g = __settings__.getSetting("record_max2g")
modex = sys.argv[1].replace("url=", "")
mode = modex.decode("hex")
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
	
def runstream(max2g,record_time,record_folderx,record_quali,record_active,idx,temp,segment_dl,timeshift):	

    if record_active == 'true': 
        record_folder = replay_pfad(record_folderx,temp)
        if 'IPTVxtraPL' not in record_folder: record_folder = replay_pfad(record_folderx,temp)

    try: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' , einen Moment der Stream wird analysiert ,30000,'+idx[5]+')')
    except: xbmc.executebuiltin('XBMC.Notification('+idx[4]+' , einen Moment der Stream wird analysiert ,30000,'+icon+')')
    m3u8_file = getstream()
    pufferpause = 0

    xbmc.executebuiltin("Skin.SetString(iptvxtra_titel_aktuell, "+idx[4]+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_icon_aktuell, "+idx[5]+")")
    xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell, plugin://plugin.video.iptvxtra-de)") 
    xbmc.executebuiltin("Skin.SetString(iptvxtra_live_ok, false)")

    if record_active == 'false' or segment_dl == 1:
        xbmc.executebuiltin("Skin.SetString(iptvxtra_starttime_aktuell, "+datetime.fromtimestamp(int(idx[1])-timeshift).strftime('%H:%M')+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_endtime_aktuell, "+datetime.fromtimestamp(int(idx[2])-timeshift).strftime('%H:%M')+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_stream_aktuell, "+m3u8_file.replace('|','&&')+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_time_aktuell, "+str(int(time.time()))+")")
        if segment_dl == 0: xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_ok)")
        elif segment_dl == 1: xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_segment_ok)")

    if record_active == 'true':

        try:
            if len(filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder))) > 0:
                for i in filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder)):
                    try: os.remove(record_folder + i)
                    except: pass
        except: pass

        mp4_title = str(int(time.time())) + '_stream.ts'

        if 'hd_1' in m3u8_file: quali = 'index_2500_av-p.m3u8'
        elif record_quali == '1': quali = 'index_900_av-p.m3u8'
        else: quali = 'index_1300_av-p.m3u8'
        url = m3u8_file.replace('master.m3u8',quali).split('|')

        try: r=requests.get(url[0], headers={"X-Forwarded-For":idx[3]})
        except:
            try: r=requests.get(url[0], headers={"X-Forwarded-For":idx[3]})
            except:	
                xbmc.executebuiltin( "Dialog.Close(infodialog)" )
                xbmc.executebuiltin('XBMC.Notification(Playlist Download Fehler ! , dieser Stream kann gerade nicht geladen werden ,7000,'+icon+')')
                sys.exit(0)

        #print r.text

        try: segment_nr = re.findall(r'EXT-X-MEDIA-SEQUENCE:(\d*)',r.text)[0]
        except:
            xbmc.executebuiltin( "Dialog.Close(infodialog)" )
            xbmc.executebuiltin('XBMC.Notification(Segment Download Fehler ! , dieser Stream kann noch nicht geladen werden ,7000,'+icon+')')
            sys.exit(0)
        segment_urls = re.findall(r'(http://.*?on)',r.text)
        segment_part = segment_urls[0].split(segment_nr)
        a = 0
        segment_urlsx=[]

        if not os.path.isdir(record_folder): record_folder = replay_pfad(record_folderx,temp)

        for id in segment_urls:
            a = a + 1
            # xx = re.findall(r'(akamaihd.net/i/.*?.ts)',id)[0].replace('/','_').replace('akamaihd.net_i_',record_folder).replace('@','_')
            # http://c001.p112.edgesuite.net/i/c001/daserste_1@97481/segment144220776_1300_av-p.ts?sd=10&start=1442193840&end=1442208240&rebase=on
            xx = re.findall(r'(edgesuite.net/i/c001/.*?.ts)',id)[0].replace('/','_').replace('edgesuite.net_i_c001_',record_folder).replace('@','_')
            segment_urlsx.append([id,xx,str(a)]) 
            if a == 2: a = 0
        segment_urls =segment_urlsx

        try:
            if max2g == 'false': max2g = 0
            else: max2g = 1
        except: max2g = 1
		
        try: os.remove(temp + "stop.stp")
        except: pass

        thread_IPTVxtraGrabber = ChunkGrabber(segment_urls, record_folder, idx[3], segment_part, mp4_title, max2g, segment_dl, 0)
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
        if segment_dl == 1:
            for id in segment_urlsx:
                fobj_out.write('#EXTINF:10.000,'+'\n')
                fobj_out.write(id[1] + '\n')
                
        else:
            fobj_out.write('#EXTINF:'+str(int(idx[2])-int(idx[1]))+'.000,'+'\n')
            fobj_out.write(record_folder + mp4_title + '\n')
        fobj_out.write('#EXT-X-DISCONTINUITY'+'\n')
        fobj_out.write('#EXT-X-ENDLIST'+'\n')
        fobj_out.close()

        if record_time == '0': stream_mb = 1000000; n = 40; puffersoll = 1
        elif record_time == '1': stream_mb = 5000000; n = 60; puffersoll = 3
        elif record_time == '2': stream_mb = 10000000; n = 80; puffersoll = 6
        elif record_time == '3': stream_mb = 16000000; n = 100; puffersoll = 9
        elif record_time == '4': stream_mb = 21500000; n = 120; puffersoll = 12

        #xbmc.executebuiltin( "Dialog.Close(infodialog)" )
        i = 0
        while i <= n:
            pufferak = xbmc.getInfoLabel("Skin.String(iptvxtra_replaypuffer)")
            if pufferak == '': pufferak = '0'
            try: 
                if int(os.path.getsize(record_folder + mp4_title)) > stream_mb: break
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

    try: listitem = xbmcgui.ListItem( idx[4], iconImage=idx[5], thumbnailImage=idx[5])
    except: listitem = xbmcgui.ListItem( idx[4], iconImage=icon, thumbnailImage=icon)
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add( m3u8_file, listitem )
    xbmcPlayer.play(playlist,listitem,False)
    if pufferpause == 1: xbmcPlayer.pause()
    xbmc.executebuiltin( "Dialog.Close(infodialog)" )
    sys.exit(0)


def getstream():
    import requests as requests
    try:
        r = requests.get("http://api.iptvxtra.net/tophits.php", params = {'loc': modex ,'app':idx[6]} )
        url = r.text.strip().decode("hex")
    except:
        xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler , fehlerhafter Zugang zum Login-Server,25000,'+net+')')
        sys.exit(0)
    if url == '':
        xbmc.executebuiltin('XBMC.Notification(Netzwerkfehler , fehlerhafter Zugang zum Login-Server,25000,'+net+')')
        sys.exit(0)
    elif 'lockland.xml' in url:
        xbmc.executebuiltin('XBMC.Notification(Login Fehler , dieses Addon ist in deinem Land nicht verfuegbar ,25000,'+net+')')
        sys.exit(0)
    elif 'noreplay.xml' in url:
        xbmc.executebuiltin('XBMC.Notification(Login Fehler , dein Addon ist fuer Replay nicht freigeschaltet ,25000,'+net+')')
        sys.exit(0)
    elif 'nopass.xml' in url:
        xbmc.executebuiltin('XBMC.Notification(Login Fehler , Passwort oder User ist sehr wahrscheinlich verkehrt oder du bist nicht registriert ,25000,'+net+')')
        sys.exit(0)
    elif 'mehrfach.xml' in url:
        xbmc.executebuiltin('XBMC.Notification(verbotener Mehrfach-Login !!! , Dein Zugang wird gleichzeitig von mehreren Standorten aus benutzt - bei 5 Fehlern wird der Zugang bis 24.00 GMT-0 gesperrt - Kodi bitte neu starten ,60000,'+net+')')
        sys.exit(0)
    return url


class ChunkGrabber(threading.Thread):
    
    def __init__(self, segment_urls, record_folder, ip, segment_part, mp4_title, max2g, segment_dl, turbo):
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")
        threading.Thread.__init__(self)
        self._temp = xbmc.translatePath("special://temp/")
        self._temp_stopfi = xbmc.translatePath("special://temp/stop.stp")
        self._segment_part = segment_part
        self._segment_urls = segment_urls
        self._record_folder = record_folder
        self._segment_dl = segment_dl
        self._turbo = turbo
        self._m3u8 = record_folder + 'IPTVxtra.m3u8'
        self._mp4_title = mp4_title
        self._ip = ip
        self._max2g = max2g
        self.segmente = 0
        self.puffer_end = 0

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
        ok = ''
        open(xbmc.translatePath(self._record_folder + self._mp4_title), "a").close()
        for i in self._segment_urls:
            if self._segment_dl == 1: fifo = open(i[1], "ab")
            else: fifo = open(self._record_folder + self._mp4_title, "ab")
            if i[0] == self._segment_urls[-1][0] or i[0] == self._segment_urls[-2][0] or i[0] == self._segment_urls[-3][0]: 
                xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, Video-Puffer: komplett)")
                self.puffer_end = 1
            if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
            try:
                if self._max2g == 1 and int(os.path.getsize(self._record_folder + self._mp4_title)) > 2045000000:
                    xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, Video-Puffer: 2GB komplett)")
                    break
            except: pass
            while pipe_ok:
                if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                try: daten = requests.get(i[0], headers={"X-Forwarded-For":self._ip}, timeout=5)
                except: 
                    if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                    if self.puffer_end == 0: ok = self.set_puffer(0)
                    try: daten = requests.get(i[0].replace('_av-p','_av-b'), headers={"X-Forwarded-For":self._ip}, timeout=5)
                    except:
                        if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                        if self.puffer_end == 0: ok = self.set_puffer(0)
                        try: daten = requests.get(i[0], headers={"X-Forwarded-For":self._ip}, timeout=10)
                        except:
                            if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                            if self.puffer_end == 0: ok = self.set_puffer(0)
                            try: daten = requests.get(i[0].replace('_av-p','_av-b'), headers={"X-Forwarded-For":self._ip}, timeout=10)
                            except:
                                if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                                if self.puffer_end == 0: ok = self.set_puffer(0)
                                try: daten = requests.get(i[0], headers={"X-Forwarded-For":self._ip}, timeout=15)
                                except: 
                                    fifo.close()
                                    if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                                    if self.puffer_end == 0: ok = self.set_puffer(0)
                                    break
                                    print '-------------------------------------------------------------------- Daten Fehler - ein Replay-Segment wurde uebersprungen'

                if (daten):
                    count = 0
                    if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
                    try:
                        fifo.write(daten.content)
                        fifo.close()
                        if self.puffer_end == 0: 
                            ok = self.set_puffer(1)
                    except IOError:
                        pipe_ok = False
                        break
                    in_stream = True
                    break
                elif (in_stream):
                    count += 1
                    if count == 7: 
                        count = 0
                        in_stream = False
                        pipe_ok = True
                        print '-------------------------------------------------------------------- Daten Fehler - ein Replay-Segment wurde leer gespeichert'
                    ok = self.set_puffer(0)
                    time.sleep(1)
                    continue
                break 
            if not pipe_ok: break
            if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8): break
        fifo.close()

        if os.path.isfile(self._temp_stopfi) or not os.path.isfile(self._m3u8):
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")
            while os.path.isfile(self._record_folder + self._mp4_title):
                os.remove(self._record_folder + self._mp4_title)
                time.sleep(1)

    def set_puffer(self, zaehl): 
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
            xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, "+str(puffera)+")")

        return 'ok'

    def stop(self):
        open(self._temp_stopfi, "a").close()


runstream(max2g,record_time,record_folderx,record_quali,record_active,idx,temp,segment_dl,timeshift)
