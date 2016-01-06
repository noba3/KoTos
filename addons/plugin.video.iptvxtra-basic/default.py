# -*- coding: utf-8 -*-

import sys,xbmc,os,shutil

if 'extrafanart' in sys.argv[2]: sys.exit(0)	
if sys.argv[2] == '': sys.exit(0)
sysargv = sys.argv[2]
addon_idx = ''

# ------------------------------------------------------------------------------------------------------------------------------------------- wiederherstellen der DE Settings - START
try:
        sxUser = 0
        sxBackup = 0
        saveset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/backup.xml')
        orgset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/settings.xml')

        if os.path.isfile(saveset) and not os.path.isfile(orgset):
            try:
                shutil.copy(saveset, orgset)
                print ' ---------------------------------------------- IPTVxtra Info-Message-Basic 100'
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
                print ' ---------------------------------------------- IPTVxtra Info-Message-Basic 102'
                print ' ---------------------------------------------------------------------------------'
            except:
                print ' ---------------------------------------------- IPTVxtra Info-Message-Basic 103'
                print ' ---------------------------------------------------------------------------------'
except: 
        print ' ---------------------------------------------- IPTVxtra Info-Message-Basic 104'
        print ' ---------------------------------------------------------------------------------'

# ---------------------------------------------------------------------------------------------------- wiederherstellen der Settings - Ende


if '*plg*' in sysargv:
    sysargv = sys.argv[2].split('*plg*')[0]
    addon_id = sys.argv[2].split('*plg*')[1].replace('plugin://','').replace('/','')
    if addon_id == 'plugin.video.iptvxtra-de': addon_idx = 'ok'
    if addon_id == 'plugin.video.iptv-europe': addon_idx = 'ok'
	
if 'runstream' in sysargv:
    xbmc.executebuiltin('XBMC.Notification(IPTVxtra Info , einen Moment die Replay-Optionen werden berechnet ,15000,'+xbmc.translatePath(os.path.join('special://home/addons/plugin.video.iptvxtra-basic/resources/iptv.png'))+')')
    url = sysargv.replace('?runstream=','')
    pfadx = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/zapp.py")
    xbmc.executebuiltin('RunScript('+pfadx+',url='+url+')')
    sys.exit(0)

if 'zapping' in sysargv:
    xbmc.Player().stop()      
    url = sysargv.replace('?zapping','')
    pfadx = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/zapping.py")
    xbmc.executebuiltin('RunScript('+pfadx+',url='+url+')')
    sys.exit(0)

if 'preview' in sysargv and 'preview_eu' not in sysargv:
    try: xbmc.executebuiltin('XBMC.Notification('+xbmc.getInfoLabel('Listitem.Label')+', einen Moment der Sender wird geladen ,15000,'+xbmc.getInfoLabel('ListItem.Icon')+')')
    except: xbmc.executebuiltin('XBMC.Notification(IPTVxtra Info , einen Moment der Sender wird geladen ,15000,'+xbmc.translatePath(os.path.join('special://home/addons/plugin.video.iptvxtra-basic/resources/iptv.png'))+')')
    url = sysargv.replace('?zappingplugin://plugin.video.iptvxtra-basic/','').replace('zappingplugin://plugin.video.iptvxtra-basic/','')
    if '###' not in url: url = url + '###80.187.103.78'
    url = url.replace('?preview','').replace('X-Forwarded-For=','').split('###')
    url = url[0] +'***starttime***endtime***'+ url[1] +'***'+ xbmc.getInfoLabel('Listitem.Label') +'***'+ xbmc.getInfoLabel('ListItem.Icon')
    pfadx = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-de/resources/lib/zapplive.py")
    xbmc.executebuiltin('RunScript('+pfadx+',url='+url+')')
    sys.exit(0)

if 'preview_eu' in sysargv:
    url = sysargv.replace('?zappingplugin://plugin.video.iptvxtra-basic/','').replace('zappingplugin://plugin.video.iptvxtra-basic/','')
    xbmc.executebuiltin('RunPlugin('+'plugin://plugin.video.iptv-europe/'+url+')')
    sys.exit(0)

if 'datedown' in sysargv and addon_idx == 'ok':
    import xbmcgui,xbmcaddon
    __settings__ = xbmcaddon.Addon(id = addon_id)
    from datetime import date, datetime,timedelta
    idx =  int(sysargv.replace("?datedown", "")) 
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    datex = xel.getControl(idx).getLabel()
    if datex == 'today' or datex == '':
        datex = str(date.today())
    datex = datex.partition('-')
    datexx = datex[2].partition('-')
    datex = date(int(datex[0]), int(datexx[0]), int(datexx[2])) - timedelta(1)
    if datex == (date.today() - timedelta(8)):
        datex = 'today'
    xel.getControl(idx).setLabel(str(datex))
    __settings__.setSetting("rep2", str(datex))
    sys.exit(0)

if 'dateup' in sysargv and addon_idx == 'ok':
    import xbmcgui,xbmcaddon
    __settings__ = xbmcaddon.Addon(id = addon_id)
    from datetime import date, datetime,timedelta
    idx =  int(sysargv.replace("?dateup", "")) 
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    datex = xel.getControl(idx).getLabel()
    if datex == 'today' or datex == '':
        datex = str(date.today() - timedelta(8))
    datex = datex.partition('-')
    datexx = datex[2].partition('-')
    datex = date(int(datex[0]), int(datexx[0]), int(datexx[2])) + timedelta(1)
    if datex == date.today():
        datex = 'today'
    xel.getControl(idx).setLabel(str(datex))
    __settings__.setSetting("rep2", str(datex))	
    sys.exit(0)

if 'localtime' in sysargv and addon_idx == 'ok':
    import xbmcgui,xbmcaddon
    __settings__ = xbmcaddon.Addon(id = addon_id)
    idx =  int(sysargv.replace("?localtime", ""))
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    local = xel.getControl(idx).getLabel()
    if __settings__.getSetting("replayDE") == 'true':
        xel.getControl(idx).setLabel('deutsche Zeit')
        __settings__.setSetting("rep1", "deutsche Zeit")
        sys.exit(0)
    if local == 'local Time':
        xel.getControl(idx).setLabel('deutsche Zeit')
        __settings__.setSetting("rep1", "deutsche Zeit")
    else:
        xel.getControl(idx).setLabel('local Time')
        __settings__.setSetting("rep1", "local Time")
    sys.exit(0)

if 'cleartxt' in sysargv and addon_idx == 'ok':
    import xbmcgui,xbmcaddon
    __settings__ = xbmcaddon.Addon(id = addon_id)
    idx = sysargv.replace("?cleartxt", "")
    idxx = int(idx[4:8])
    idx = int(idx[0:4])
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    xel.getControl(idx).setLabel('Set Time:   ' + xbmc.getInfoLabel('System.Time'))
    timex = str(xbmc.getInfoLabel('System.Time'))
    slidex = int(timex[0:2])*3600 + int(timex[3:5])*60
    if idxx > 1300: xel.getControl(idxx).setPercent(slidex/864.00000000)
    repset2 = 'today'
    __settings__.setSetting("rep2", 'today')
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    try: xel.getControl(1301).setLabel(repset2)
    except: pass
    try: xel.getControl(1331).setLabel(repset2)
    except: pass
    try: xel.getControl(1361).setLabel(repset2)
    except: pass
    try: xel.getControl(1381).setLabel(repset2)
    except: pass
    sys.exit(0)

if 'timeset' in sysargv and addon_idx == 'ok':
    import xbmcgui
    idx =  sysargv.replace("?timeset", "")
    idxx = int(idx[4:8])
    idx = int(idx[0:4])
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    timex = xbmcgui.Dialog().numeric(2, 'Uhrzeit eingeben')
    timex = timex.replace(':','').strip()
    if timex:
        if len(timex) == 3:
            timex = '0' + timex[0:1] + ':'+ timex[1:3]	
        if len(timex) == 4:
            timex = timex[0:2] + ':'+ timex[2:4]
        elif len(timex) == 5:
            timex = timex[0:2] + ':'+ timex[3:5]
        elif len(timex) == 0:
            timex = '00:00'
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

if 't1900' in sysargv and addon_idx == 'ok':
    import xbmcgui
    idx =  sysargv.replace("?t1900", "") 
    idx = idx.split('#')
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    xel.getControl(int(idx[0])).setLabel('Set Time:   19:00')
    if int(idx[1]) > 1300: xel.getControl(int(idx[1])).setPercent(68400/864.00000000)
    sys.exit(0)

if 't2015' in sysargv and addon_idx == 'ok':
    import xbmcgui
    idx =  sysargv.replace("?t2015", "")
    idx = idx.split('#')
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    xel.getControl(int(idx[0])).setLabel('Set Time:   20:15')
    if int(idx[1]) > 1300: xel.getControl(int(idx[1])).setPercent(72900/864.00000000)
    sys.exit(0)

if 't2200' in sysargv and addon_idx == 'ok':
    import xbmcgui
    idx =  sysargv.replace("?t2200", "")
    idx = idx.split('#')
    xel = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    xel.getControl(int(idx[0])).setLabel('Set Time:   22:00')
    if int(idx[1]) > 1300: xel.getControl(int(idx[1])).setPercent(79200/864.00000000)
    sys.exit(0)

if 'gosetting' in sysargv and addon_idx == 'ok':
    import xbmcaddon
    xbmcaddon.Addon(addon_id).openSettings()
    xbmc.executebuiltin('Container.Refresh')
    sys.exit(0)

if 'seek' in sysargv:
    import xbmcaddon
    __settings__ = xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de')
    nr = int(sysargv.replace('?seek',''))
    if nr == 1: xskip = int('-' + __settings__.getSetting("skip3")) * 60
    elif nr == 2: xskip = int('-' + __settings__.getSetting("skip2")) * 60
    elif nr == 3: xskip = int('-' + __settings__.getSetting("skip1")) * 60
    elif nr == 4: xskip = int(__settings__.getSetting("skip1")) * 60+1
    elif nr == 5: xskip = int(__settings__.getSetting("skip2")) * 60+1
    elif nr == 6: xskip = int(__settings__.getSetting("skip3")) * 60+1	
    x = int(xbmc.getInfoLabel("Skin.String(iptvxtra_replaypuffer)"))*10 - int(xbmc.getInfoLabel("Skin.String(iptvxtra_replayplaytime)"))
    if x > xskip+30:
        xbmcPlayer = xbmc.Player()
        playtime = int(xbmcPlayer.getTime())
        xbmcPlayer.seekTime(playtime+xskip)
    else:
        xskip = x-30
        xbmcPlayer = xbmc.Player()
        playtime = int(xbmcPlayer.getTime())
        xbmcPlayer.seekTime(playtime+xskip)
    sys.exit(0)

if 'setmin' in sysargv:
    import xbmcaddon
    __settings__ = xbmcaddon.Addon(id = 'plugin.video.iptvxtra-de')
    nr = int(sysargv.replace('?setmin',''))
    if nr == 1: xskip = int('-' + __settings__.getSetting("skip3")) * 60
    elif nr == 2: xskip = int('-' + __settings__.getSetting("skip2")) * 60
    elif nr == 3: xskip = int('-' + __settings__.getSetting("skip1")) * 60
    elif nr == 4: xskip = int(__settings__.getSetting("skip1")) * 60+1
    elif nr == 5: xskip = int(__settings__.getSetting("skip2")) * 60+1
    elif nr == 6: xskip = int(__settings__.getSetting("skip3")) * 60+1	
    xbmc.executebuiltin("Skin.SetBool(iptvxtra_replay_ok)")
    xbmcPlayer = xbmc.Player()
    playtime = int(xbmcPlayer.getTime())
    xbmcPlayer.seekTime(playtime+xskip)
    sys.exit(0)


sys.exit(0)









