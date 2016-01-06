# coding: utf-8

import xbmc,xbmcgui,xbmcaddon,subprocess,os,sys,time,shutil
from datetime import date,datetime,timedelta

addonID = 'plugin.program.iptvxtra'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')
__set_reload__ = addon
__set_reload__.setSetting("playerstatusinfo", '0')
__set_reload__.setSetting("def1","")
__set_reload__.setSetting("def2","")
__set_reload__.setSetting("def3","")
__set_reload__.setSetting("def4","")
__set_reload__.setSetting("def5","0")
rl_playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
xbmcPlayer = xbmc.Player()
playertimestatus = 0
playfile = ''
IPTVxtra = 0


class Playerstatus(xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)
        global __icon
        global __title
        global __stream
    def onPlayBackStarted(self):
        __set_reload__.setSetting("playerstatusinfo", '0')
        __set_reload__.setSetting("def1", xbmc.getInfoLabel('ListItem.Icon'))
        __set_reload__.setSetting("def2",xbmc.getInfoLabel('VideoPlayer.Title'))
        __set_reload__.setSetting("def3",xbmc.getInfoLabel('Player.Filenameandpath'))
        __set_reload__.setSetting("def5",str(int(xbmcPlayer.getTotalTime())))

        try:
            playfile = xbmcPlayer.getPlayingFile()
            if 'IPTVxtra.m3u8' not in playfile:
                xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_segment_ok)")
                temp = xbmc.translatePath("special://temp/")
                open(xbmc.translatePath(temp + "stop.stp"), "a").close()

        except: pass

        try:
            playfile = xbmcPlayer.getPlayingFile()
            if 'http://pebbles' in playfile or 'http://vevoplaylist' in playfile or 'http://c001.p' in playfile: xbmc.executebuiltin("Skin.SetBool(iptvxtra_running)")
            elif 'easytv.to' in playfile or 'giniko' in playfile or 'esioslive6' in playfile or '212.162.68.163' in playfile: xbmc.executebuiltin("Skin.SetBool(iptvxtra_running)")
            elif 'totiptv.com' in playfile or 'one2hd.com' in playfile or 'http://edge.newone2up' in playfile: xbmc.executebuiltin("Skin.SetBool(iptvxtra_running)")
            elif 'edge4.psitv' in playfile: xbmc.executebuiltin("Skin.SetBool(iptvxtra_running)")
            else: 
                xbmc.executebuiltin("Skin.SetString(iptvxtra_addon_aktuell,none )")
                xbmc.executebuiltin("Skin.Reset(iptvxtra_running)")
        except: pass
	
    def onPlayBackStopped(self):
        temp = xbmc.translatePath("special://temp/")
        open(xbmc.translatePath(temp + "stop.stp"), "a").close()
        __set_reload__.setSetting("playerstatusinfo", '0')
        __set_reload__.setSetting("def5", '0')
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaytext, "+''+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replaypuffer, 0)")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_replayplaytime, 0)")
        xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_segment_ok)")
        xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_ok)")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_live_ok, false)")
        runaddy = xbmc.getInfoLabel("Skin.String(iptvxtra_addon_aktuell)").replace('plugin://','')

        try:
            record_folder = xbmcaddon.Addon(id = runaddy).getSetting("record_folder")
            if record_folder == 'Kodi Cache Verzeichnis': record_folder = temp
            if not os.path.isdir(record_folder):
                record_folder = temp
                xbmcaddon.Addon(id = runaddy).setSetting("record_folder","Kodi Cache Verzeichnis")
        except: record_folder = temp
        record_folder = os.path.join(record_folder,'IPTVxtraPL','erfgbn.txt').replace('erfgbn.txt','')
        shutil.rmtree(record_folder, ignore_errors=True)
        try: os.remove(temp + "IPTVxtra.m3u8")
        except: pass
        try:
            if len(filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder))) > 0:
                for i in filter(lambda x: x.endswith("_stream.ts"), os.listdir(record_folder)):
                    try: os.remove(record_folder + i)
                    except: pass
        except: pass
        shutil.rmtree(record_folder, ignore_errors=True)
  
    def onPlayBackPaused(self):
        __set_reload__.setSetting("playerstatusinfo", '0')
        __set_reload__.setSetting("def5", '0')

    def onPlayBackResumed(self):
        __set_reload__.setSetting("playerstatusinfo", '0')
        __set_reload__.setSetting("def5", '0')

    def onPlayBackEnded(self):
        if 'rtmp://' in __set_reload__.getSetting("def3") or '.m3u8' in __set_reload__.getSetting("def3"):
            if __set_reload__.getSetting("playerstatusinfo") == '0':
                __set_reload__.setSetting("playerstatusinfo", '10')
        else:
            __set_reload__.setSetting("playerstatusinfo", '0')

 
def replay(stream,realtimestart):
        realtimejetzt = int(time.time())
        stream = stream.replace('&amp;','&')
        stream = stream.replace('?','')
        forw = stream.partition('|')
        forw = forw[2]
        start = stream.partition('start=')
        stream = start[0]
        start = start[2].partition('&end=')
        start = start[0]
        try: timedif = realtimejetzt - int(realtimestart)
        except: timedif = 15
        start = int(start) + timedif - 10
        end = start + 14400
        if end > realtimejetzt:
            end = realtimejetzt - 180
        stream = stream + '?start=' + str(start) + '&end=' + str(end) + '|' + forw
        #try:
        streamx = stream.replace('?','')
        streamx = streamx.replace('|','&&')
        xbmc.executebuiltin("Skin.SetString(iptvxtra_stream_aktuell, "+streamx+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_time_aktuell, "+str(int(time.time()))+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_starttime_aktuell, "+datetime.fromtimestamp(int(start)).strftime('%H:%M')+")")
        xbmc.executebuiltin("Skin.SetString(iptvxtra_endtime_aktuell, "+datetime.fromtimestamp(int(end)).strftime('%H:%M')+")")
        if xbmc.getInfoLabel("Skin.String(iptvxtra_replay_segment_ok)") == 'true': xbmc.executebuiltin("Skin.Reset(iptvxtra_replay_ok)")
        else: xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_ok)")
        return stream

   

player=Playerstatus()

while not xbmc.abortRequested and __set_reload__.getSetting("playerinfox") == 'true':

    plsi = __set_reload__.getSetting("playerstatusinfo")
    try: streamlaenge = int(__set_reload__.getSetting("def5"))
    except: streamlaenge = 0
    load_addon = 'none'
    playtime = -1

    try:
        if xbmc.getInfoLabel("Skin.String(iptvxtra_live_ok)") == 'true': LivePuffer = 1
        else: LivePuffer = 0
    except: LivePuffer = 0

    if xbmcPlayer.isPlaying():
        try: playertimestatus = int(xbmcPlayer.getTime())
        except: playertimestatus = 0

    if plsi == '10' and streamlaenge > 300 and playertimestatus > streamlaenge - 90:
        __set_reload__.setSetting("playerstatusinfo", '0')
        __set_reload__.setSetting("def5", '0')
        streamlaenge = 0
        playertimestatus = 0
        plsi = '0'
 
    if plsi == '10':
        __set_reload__.setSetting("playerstatusinfo", '5')

        try:
            tvx = __set_reload__.getSetting("playerdelay")
            if tvx == '0': tv = 500
            elif tvx > '10': tv = 10000
            else: tv = int(tvx) * 1000
            if tv > 10000: tv = 10000
            if tv < 500: tv = 500
        except:
            tv = 500

        title = __set_reload__.getSetting("def2")
        icon = __set_reload__.getSetting("def1")
        stream = __set_reload__.getSetting("def3")
        stream = stream.replace('&&','|')
        realtimestart = __set_reload__.getSetting("def4")

        tvy = tv + 4000
        xbmc.executebuiltin('XBMC.Notification(Video-Stream is broken,it is trying to start the Video again ,'+str(tvy)+','+icon+')')
        xbmc.sleep(tv)

        try: re_a = int(xbmc.getInfoLabel("Skin.String(iptvxtra_replayplaytime)"))
        except: re_a = 0
        try: re_b = xbmc.getInfoLabel("Skin.String(iptvxtra_replaytext)")
        except: re_b = ''
        if re_a > 120 and 'Video-Puffer' in re_b:
            playtime = re_a

        if 'end' in stream and 'start' in stream:
            stream = replay(stream,realtimestart)

        __set_reload__.setSetting("def3",stream)
        __set_reload__.setSetting("def4",realtimestart)

        if icon == '' and playtime > 10:
            icon = xbmc.getInfoLabel("Skin.String(iptvxtra_icon_aktuell)")

        listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
        rl_playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
        rl_playlist.clear()
        rl_playlist.add( stream, listitem )
        startfull = __set_reload__.getSetting("startfull")
        if startfull == 'true': xbmcPlayer.play(rl_playlist,None,False)
        else: xbmcPlayer.play(rl_playlist,None,True)

        if playtime > 120 and LivePuffer == 0:
            xbmcPlayer.seekTime(playtime-30)

        if xbmcPlayer.isPlayingVideo():
            __set_reload__.setSetting("playerstatusinfo", '0')
        else:
            xbmc.executebuiltin('XBMC.Notification(Video-Stream is broken, Sorry - Video could not be restarted ,4000)')


    xbmc.sleep(1000)




