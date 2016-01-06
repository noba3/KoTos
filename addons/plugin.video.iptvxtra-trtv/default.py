# -*- coding: utf-8 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys,urllib2
from resources.lib.BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
icons = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-trtv/resources/icons/")
icon = xbmc.translatePath("special://home/addons/plugin.video.iptvxtra-trtv/icon.png")
plugin_handle = int(sys.argv[1])
mode = sys.argv[2]

	
def ginico(url):
    import resources.lib.requests as requests

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
	
def canlitvlive(url):
    import resources.lib.requests as requests
    r = requests.get(url)
    r = r.text.replace(' ','').strip()
    # print r
    r = find_between(r,'file:"http','"')
    #r = 'http'+r+'|referer=http://www.canlitvlive.com/tvplayer.swf'
    r = 'http'+r+'|User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0&referer=http://www.canlitvlive.org/jwplayer.flash.swf'
    return r



def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
	
def add_video_item(title,url,img):
    # if '://' not in url: url = 'http://none.stream'
    url = 'plugin://plugin.video.iptvxtra-trtv/?playtrk=' + url + '***' + title + '***' + img
    listitem = xbmcgui.ListItem(title, iconImage=img, thumbnailImage=img)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return

def addDir(name,url,iconimage):
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "Fanart_Image", icon )
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

def categorie():
    addDir('IPTVxtra MuMaTi TV ', 'plugin://plugin.video.iptvxtra-trtv/?xcat0x', icon)
    addDir('IPTVxtra TR - TV 1 - sorry offline', 'plugin://plugin.video.iptvxtra-trtv/?xcat1x', icon)
    addDir('IPTVxtra TR - TV 2', 'plugin://plugin.video.iptvxtra-trtv/?xcat2x', icon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
def playginico():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?playtrk=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , einen Moment der Sender wird geladen ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    if 'giniko' in idx[0]: url = ginico(idx[0])
    elif 'www.canlitvlive.com' in idx[0]: url = canlitvlive(idx[0])
    else: url = idx[0]
    playlist.add( url, listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def get_url(url):
        response = urllib2.urlopen(url)
        link=response.read()
        response.close()
        return link

def main():	
    xcat = 0
    if 'xcat1' in mode: 
        url = "http://185.62.188.116/xbmc/xml/turk2.xml"
    elif 'xcat2' in mode: 
        url = "http://185.62.188.116/xbmc/xml/turk.xml"
    elif 'xcat0' in mode: 
        url = "http://melart.de/tv/turk3.xml"
        #url = "http://185.62.188.116/xbmc/xml/turk3.xml"
    else:
        categorie()
        sys.exit(0)


    link = get_url(url)
    soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)

    items = soup.findAll("item")
    for item in items:
            try:
                videoTitle=item.title.string
                videoTitle = videoTitle
            except: pass
            try:
                if item.thumbnail.string == 'none': thumbnail = icon	
                elif 'http://' in item.thumbnail.string: thumbnail = item.thumbnail.string 
                else: thumbnail = icons + item.thumbnail.string   
            except:
                thumbnail = icon
            try:
                url = item.link.string
                if not url: url = 'http://none.stream'
                if url == '': url = 'http://none.stream'
            except: url = 'http://none.stream'

            add_video_item(videoTitle,url,thumbnail)
    xbmcplugin.endOfDirectory(plugin_handle)
    sys.exit(0)


if 'playtrk' in mode:
    playginico()
else:
    main()