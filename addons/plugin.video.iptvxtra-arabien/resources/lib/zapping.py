#!/bin/python
import xbmcgui,xbmc,os,sys,urllib2,re
xbmcPlayer = xbmc.Player()
mode = sys.argv[1]
idx = mode.replace("url=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").replace("referer", "Referer").split('***')
xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , einen Moment der Sender wird geladen ,5000,'+idx[2]+')')
url = idx[0]

def zapp(url):
    if 'iptv-planet' in url:
        import requests as requests
        url = find_between(url,'pageUrl=','swfUrl').replace(' ','').replace('notallowedinunitedstates','')
        #url = url.replace('alhayatnotallowedinunitedstates','Hi_Alhayat').replace('mbc1notallowedinunitedstates','Hi_mbc1')
        r=requests.get(url, headers={"User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"})
        r = r.text.strip().replace('\n',' ').replace(' ','').replace(',',';').replace("'",'"')
        #print r
        p1 = find_between(r,'varstreamer="','";')
        p2 = find_between(r,'"file":"','";')
        url = p1 + " playpath=" + p2 + ' swfUrl=http://iptv-planet.com/swfs/player.swf pageUrl=http://iptv-planet.com/embed.php'
        url = url.replace('=mbc1?','=Hi_mbc1?').replace('=alhayat?','=Hi_Alhayat?').replace('alhayatnotallowedinunitedstates','Hi_Alhayat').replace('mbc1notallowedinunitedstates','Hi_mbc1')
    if 'streaminghd.tn' in url:
        import requests as requests
        r=requests.get(url, headers={"User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"})
        r = r.text.strip().replace('\n',' ').replace(' ','').replace(',',';').replace("'",'"')
        url = find_between(r,'window.flashvars.src="','";')
    if 'krichitv' in url:	
        import requests as requests
        r=requests.get(url, headers={"User-Agent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"})
        r = r.text.strip().replace('\n',' ').replace(' ','').replace(',',';').replace("'",'"').replace("%20",'').replace("%3A",':').replace("%3F",'?').replace("%22",'"')
        if 'vart="' in r: r = find_between(r,'vart="','"').decode("hex")
        pattern = 'jwplayer.*?file:"([^"]+)"'
        try: 
            url = parse(r, pattern)[1][0]
            if 'rtmpt://' in url: url = url.replace('rtmpt://','rtmp://')
        except: url = ''


    if 'rtmp' in url and 'live=1' not in url: url = url + ' live=1'
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add( url, listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def parse(sHtmlContent, sPattern, iMinFoundValue = 1, ignoreCase = False):
        if ignoreCase:
            aMatches = re.compile(sPattern, re.DOTALL|re.I).findall(sHtmlContent)
        else:
            aMatches = re.compile(sPattern, re.DOTALL).findall(sHtmlContent)
        if (len(aMatches) >= iMinFoundValue):                
            return True, aMatches
        return False, aMatches

zapp(url)