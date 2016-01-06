# -*- coding: utf-8 -*-
import urllib,urllib2,os,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,time
import json as api
from addon.common.net import Net

addon_id = 'plugin.video.KinoLeak'
addon = xbmcaddon.Addon(addon_id)
__settings__ = xbmcaddon.Addon(addon_id)
status = __settings__.getSetting("status")
datapath = __settings__.getAddonInfo('path')
channels1 = xbmc.translatePath(os.path.join(datapath, 'resources', 'images'))
sys.path.append(channels1)
channels = xbmc.translatePath(os.path.join(datapath, 'lib', 'metahandler'))
sys.path.append(channels)
channels = xbmc.translatePath(os.path.join(datapath, 'lib', 'db'))
sys.path.append(channels)
import metahandlers
import common
metaget = metahandlers.MetaData(preparezip=True)
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:36.0) Gecko/20100101 Firefox/36.0'

def CATEGORIES(url):
        addDir("Neu im Programm",url,1,str(channels1)+"\\New-icon.png","0","folder","",None,"")
        addDir("Abenteuer",url,1,str(channels1)+"\\Abenteuer-icon.png","0","folder","",0,"")
        addDir("Action",url,1,str(channels1)+"\\Action-icon.png","0","folder","",0,"")
        addDir("Drama",url,1,str(channels1)+"\\Drama-icon.png","0","folder","",0,"")
        addDir("Krieg",url,1,str(channels1)+"\\Krieg-icon.png","0","folder","",0,"")
        addDir("Thriller",url,1,str(channels1)+"\\Thriller-icon.png","0","folder","",0,"")
        addDir("Krimi",url,1,str(channels1)+"\\Krimi-icon.png","0","folder","",0,"")
        addDir("Horror",url,1,str(channels1)+"\\Horror-icon.png","0","folder","",0,"")
        addDir(u"Kom\xf6die",url,1,str(channels1)+"\\Komoedie-icon.png","0","folder","",0,"")
        addDir("Fantasy",url,1,str(channels1)+"\\Fantasy-icon.png","0","folder","",0,"")
        addDir("Sci-Fi",url,1,str(channels1)+"\\Sci-Fi-icon.png","0","folder","",0,"")
        addDir("Animation",url,1,str(channels1)+"\\Animation-icon.png","0","folder","",0,"")
        addDir("Western",url,1,str(channels1)+"\\Western-icon.png","0","folder","",0,"")
        addDir("FilmInfo sammeln (dauert etwas Geduld bitte!)",url,1,str(channels1)+"\\Update-icon.png","0","folder","",None,"")
        addDir("Search KinoLeak",url,3,str(channels1)+"\\Search-icon.png","0","folder","",None,"")
        xbmc.executebuiltin("Container.SetViewMode(500)")

def SEARCH(url,name,imdb,move,movegen):
        net = Net()
        link = net.http_GET(url).content
        link=link.replace('\r\n', '').replace('"},]', '"}]')
        magic = api.loads(link, encoding='latin1')
        kb = xbmc.Keyboard('', 'Search KinoLeak', False)
        kb.doModal()
        search = kb.getText()
        # search=urllib.quote(search)
        for e,i in enumerate(magic):
            if search.lower() in (i['titel'].encode('utf-8')).lower():
                try:
                    imdb=re.search(".*?/(tt\d+)/*.*?$", i['imdblink']).group(1)
                except:
                    imdb=""
                try:
                    sub=re.search("(.*?)\((\d+)\)", i['titel'])
                    addDir(sub.group(1),url,2,i['cover'],imdb,"movie".decode('utf-8'),sub.group(2),None,"")
                except:
                    addDir(i['titel'],url,2,i['cover'],imdb,"movie",'',None,"")
        xbmcplugin.setContent(int(sys.argv[1]), 'movies')
        xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.getSetting('MAIN') )

def INDEX(url,name,imdb,move,movegen):
        net = Net()
        link = net.http_GET(url).content
        link=link.replace('\r\n', '').replace('"},]', '"}]')
        magic = api.loads(link, encoding='latin1')
        progress = xbmcgui.DialogProgress()
        progress.create('Fortschritt', 'This is a progress bar.')
        genre=[]
        neu=[]
        sammeln=[]
        for e,i in enumerate(reversed(magic)):
            if name == "Neu im Programm" and e<27:
                neu.append(i)
        for e,i in enumerate(magic):
            if name in i['genre'].encode('utf-8'):
                genre.append(i)
        for e,i in enumerate(magic):
            if "sammeln" in name:
                sammeln.append(i)
        #----Neu im Programm----#
        for e,i in enumerate(neu):
            if e < len(neu):
                percent = int((e/len(neu))*100)
                message =   str(e) + " von "+str(len(neu))+" Filmen geladen"
                progress.update(percent, message, "Dies passiert bei noch nie eingelesenen Filmen")
            try:
                imdb=re.search(".*?/(tt\d+)/*.*?$", i['imdblink']).group(1)
            except:
                imdb=""
            try:
                sub=re.search("(.*?)\((\d+)\)", i['titel'])
                addDir(sub.group(1),url,2,i['cover'],imdb,"movie".decode('utf-8'),sub.group(2),None,"")
            except:
                addDir(i['titel'],url,2,i['cover'],imdb,"movie",'',None,"")
        #----GENRES die Filme----#
        for e,i in enumerate(sorted(genre, key=lambda genre: genre['titel'])):
            if move<=e<move+25:
                if e-move < move+25:
                    percent = ((e-move)/25*100)
                    message =   "FilmInfo des "+str(e-move) + ". von 25 Filmen geladen"
                    progress.update(percent, message, "Dies passiert bei noch nie eingelesenen Filmen")
                try:
                    imdb=re.search(".*?/(tt\d+)/*.*?$", i['imdblink']).group(1)
                except:
                    imdb=""
                try:
                    sub=re.search("(.*?)\((\d+)\)", i['titel'])
                    addDir(sub.group(1),url,2,i['cover'],imdb,"movie".decode('utf-8'),sub.group(2),None,"")
                except:
                    addDir(i['titel'],url,2,i['cover'],imdb,"movie",'',None,"")
        #----FilmInfo von allen Filmen Sammeln für die Datenbank----#
        for e,i in enumerate(sorted(sammeln, key=lambda sammeln: sammeln['titel'])):
            if e < len(sammeln):
                percent = int((e/len(sammeln))*100)
                message =   "FilmInfo des "+str(e) + ". von "+str(len(sammeln))+" Filmen geladen"
                progress.update(percent, message, "Dies passiert bei noch nie eingelesenen Filmen")
            try:
                imdb=re.search(".*?/(tt\d+)/*.*?$", i['imdblink']).group(1)
            except:
                imdb=""
            try:
                sub=re.search("(.*?)\((\d+)\)", i['titel'])
                addDir(sub.group(1),url,2,i['cover'],imdb,"movie".decode('utf-8'),sub.group(2),None,"")
            except:
                addDir(i['titel'],url,2,i['cover'],imdb,"movie",'',None,"")
        #----SEITENNAVIGATION----#
        if len(genre)>0:
            if move!=None and move==0 and len(genre)>25:
                print "<<<----OLDU-1---->>>"
                addDir("Next-->>",url,4,"","","folder","",move+25,name)
            if move!=None and move!=0 and move+25<=len(genre) and len(genre)-move>0:
                print "<<<----OLDU-2---->>>"
                addDir("Next-->>",url,4,"","","folder","",move+25,name)
                addDir("<<--Back",url,4,"","","folder","",move-25,name)
            if move+25>=len(genre) and move!=0:
                print "<<<----OLDU-3---->>>"
                addDir("<<--Back",url,4,"","","folder","",move-25,name)
            addDir("Home","",None,"","","folder","",None,"")
        progress.close()
        xbmcplugin.setContent(int(sys.argv[1]), 'movies')
        xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.getSetting('MAIN') )

def PLAYLIST(name, url, iconimage, imdb):
        net = Net()
        link = net.http_GET(url).content
        link=link.replace('\r\n', '').replace('"},]', '"}]')
        magic = api.loads(link, encoding='latin1')
        liste=[]
        stream1=[]
        stream2=[]
        dialog = xbmcgui.Dialog()
        for i in magic:
            if imdb in i['imdblink'].encode('utf-8'):
                try:
                    stream1=re.search("S*R*C*s*r*c*='(.*?)'.*?", i['streamlink1']).group(1)
                    vid1=re.search("S*R*C*s*r*c*='https*://(.*?)\.*c*o*m*t*o*/.*?'.*?",i['streamlink1'])
                    liste.append(vid1.group(1))
                except:
                    pass
                try:
                    stream2=re.search("S*R*C*s*r*c*='(.*?)'.*?", i['streamlink2']).group(1)
                    vid2=re.search("S*R*C*s*r*c*='https*://(.*?)\.*c*o*m*t*o*/.*?'.*?",i['streamlink2'])
                    liste.append(vid2.group(1))
                except:
                    pass
        hoster = dialog.select('HOSTER',liste)
        if hoster == 0:
            HOSTER(name,stream1,iconimage)
        elif hoster == 1:
            HOSTER(name,stream2,iconimage)
        else:
            pass

def HOSTER(name, url, iconimage):
        if 'vidhog' in url:
            resolve_vidhog(name,url,iconimage)
        elif 'mightyupload' in url:
            resolve_mightyupload(name,url,iconimage)
        elif 'vk.com' in url:
            resolve_VK(name,url,iconimage)
        elif '180upload' in url:
            resolve_180upload(name,url,iconimage)
        elif 'cloudyvideos' in url:
            resolve_cloudyvideos(name,url,iconimage)
        elif 'ilook' in url:
            resolve_ilook(name,url,iconimage)
        elif 'streamin' in url:
            resolve_streamin(name,url,iconimage)
        else:
            pass

def resolve_mightyupload(name,url,iconimage):
        print "mightyupload"
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html=response.read()
        file = re.search('file:.*?\'(.*?)\',',html,re.DOTALL)
        print file.group(1)
        pl = xbmc.PlayList(1)
        pl.clear()
        try:
            try:
                listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
                listitem.setProperty('mimetype', 'video/x-msvideo')
                listitem.setProperty('IsPlayable', 'true')
                url = file.group(1) + '|User-Agent=%s' % (USER_AGENT)
                pl.add(url, listitem)
                xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
                xbmcPlayer.play(pl)
            except Exception, e:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')
                print '**** mightyupload Error occured: %s' % e
                raise
        except:
            pass

def resolve_ilook(name,url,iconimage):
        print "ilook"
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html=response.read()
        file = re.search('file:\s"(.*?)"',html)
        pl = xbmc.PlayList(1)
        pl.clear()
        try:
            try:
                listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
                listitem.setProperty('mimetype', 'video/x-msvideo')
                listitem.setProperty('IsPlayable', 'true')
                url = file.group(1)
                pl.add(url, listitem)
                xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
                xbmcPlayer.play(pl)
            except Exception, e:
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')
                print '**** ilook Error occured: %s' % e
                raise
        except:
            pass

def resolve_streamin(name,url,iconimage):
        print "streamin"
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html=response.read()
        n = re.search('config:{file:\'(.+?)\'',html,re.IGNORECASE | re.DOTALL)
        k = re.search('streamer: \"(.+?)\"',html,re.IGNORECASE | re.DOTALL)
        if n and k:
            url = '%s playpath=%s' % (k.group(1).strip(),n.group(1).strip())
        pl = xbmc.PlayList(1)
        pl.clear()
        try:
            listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
            listitem.setProperty('mimetype', 'video/x-msvideo')
            listitem.setProperty('IsPlayable', 'true')
            pl.add(url, listitem)
            xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
            xbmcPlayer.play(pl)
        except Exception, e:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')
            print '**** streamin Error occured: %s' % e
            raise

def resolve_cloudyvideos(name,url,iconimage):
        # print "cloudyvideos"
        url=re.sub('embed-|-.*?(?:\.html)','',url)
        net = Net()
        web_url = url
        headers = {'Referer': web_url}
        html = net.http_GET(web_url, headers=headers).content
        data={}
        time.sleep(3)
        for match in re.finditer(r'type="hidden".*?name="([^"]+)".*?value="([^"]+)', html):
            data[match.group(1)] = match.group(2)
            data.update ({'method_free': 'Continue'})
        htmla = net.http_POST(web_url, data).content
        r = re.search('file:\s*\'(.*?)\',+', htmla)
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        try:
            listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
            url = r.group(1)+'|Referer=http://cloudyvideos&User-Agent=%s' % (USER_AGENT)
            pl.add(url, listitem)
            xbmc.Player().play(pl)
        except Exception, e:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')
            print '**** cloudyvideo Error occured: %s' % e
            raise

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param

def addDir(name,url,mode,iconimage,imdb,status,year,move,movegen):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name.encode('utf-8'))+"&img="+urllib.quote_plus(iconimage)+"&imdb="+urllib.quote_plus(imdb)+"&move="+str(move)+"&movegen="+str(movegen)
        ok=True
        if status!="folder":
            meta = metaget.get_meta(status,name.encode('utf-8'),imdb.encode('utf-8'))
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels=meta )
            liz.setInfo( type="Video", infoLabels={"overlay": 7, "watched": True} )
            contextMenuItems = []
            contextMenuItems.append(('Film Information', 'XBMC.Action(Info)'))
            # contextMenuItems.append(('Metahandler Einstellung', 'RunScript(special://home/addons/plugin.video.KinoLeak/resources/meta.py)'))
            # print str(meta)
            # contextMenuItems.append(('FilmInfo update', "RunScript(special://home/addons/plugin.video.KinoLeak/resources/meta_update.py,status="+status+",name="+meta['title']+",imdb_id="+imdb.encode('utf-8')+",tmdb_id="+imdb.encode('utf-8')))
            liz.addContextMenuItems(contextMenuItems, replaceItems=False)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', "http://image.tmdb.org/t/p/original"+meta['backdrop_url'])
            else: liz.setProperty('fanart_image', '')
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            contextMenuItems = []
            contextMenuItems.append(('Metahandler Einstellung', 'RunScript(special://home/addons/plugin.video.KinoLeak/resources/meta.py)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=False)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

params=get_params()
url=None
name=None
mode=None
iconimage=None
imdb=None
move=None
movegen=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["thumbnailImage"])
except:
        pass
try:
        imdb=urllib.unquote_plus(params["imdb"])
except:
        pass
try:
        move=int(params["move"])
except:
        pass
try:
        movegen=urllib.unquote_plus(params["movegen"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        CATEGORIES('http://kinoleak.tv/api.php')
elif mode==1:
        INDEX(url,name,imdb,move,movegen)
elif mode==2:
        PLAYLIST(name, url, iconimage, imdb)
elif mode==3:
        SEARCH(url,name,imdb,move,movegen)
elif mode==4:
        print ""+url
        INDEX(url,movegen,imdb,move,movegen)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
