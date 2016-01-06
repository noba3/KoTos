#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import sys,re,os,urllib2,urllib
import xbmcplugin,xbmcgui,xbmcaddon,xbmc
from BeautifulSoup import BeautifulSoup as BS
from cookielib import CookieJar
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
__settings__ = xbmcaddon.Addon(id="plugin.video.Evonic")
quality= __settings__.getSetting("quality")
url_start='http://evonic.tv/forum/content.php'
login= __settings__.getSetting("login")
password= __settings__.getSetting("password")
library_path=xbmc.translatePath(__settings__.getSetting("folder"))
library_serie=xbmc.translatePath(__settings__.getSetting("serfolder"))
library_serie=library_serie.replace("smb:","")
library_path=library_path.replace("smb:","")      
def url_opener(url):
        login= __settings__.getSetting("login")
        password= __settings__.getSetting("password") 
        data = {
                    'cookieuser':'1',
                    'vb_login_username': login,
                    'vb_login_password': password,
                    'do':'login',
                    'submit':'anmelden',
                    }
        login = 'http://evonic.tv/forum/login.php?do=login'
        opener.open(login, urllib.urlencode(data)).read()
        uri = opener.open(url).read()
        # print uri
        if str('<span style="color: #FF6600;">Premium Member</span>') in str(uri) or '.mkv' in str(uri) or '.mp4' in str(uri):
            print "Succesfully Loged in."
            return uri
        else:
            __settings__.openSettings()
            
        
def INDEX_GENRE(url):
        data = url_opener(url)
        enter_addDir(' Suche...','http://evonic.tv/forum/content.php?r=1969-Aktuelle-HD-Filme&page=','',2,'','','','','')
        enter_addDir(' Neueinsteiger',url,'',5,'','','','','')
        enter_addDir(' 3D Filme','http://evonic.tv/forum/content.php?r=4225-3d-filme','',5,'','','','','')
        enter_addDir(' HD Filme','http://evonic.tv/forum/content.php?r=1669-hd-filme','',5,'','','','','')
        enter_addDir(' HD Collection','http://evonic.tv/forum/content.php?r=3501-hd-collection','',5,'','','','','')
        enter_addDir(' HD Serien','http://evonic.tv/forum/content.php?r=5993-Serien','',5,'','','','','')
        enter_addDir(' Aktuelle HD Filme','http://evonic.tv/forum/content.php?r=3938-Aktuelle-HD-Filme','',5,'','','','','')
        enter_addDir(' 3D Charts','http://evonic.tv/forum/content.php?r=5440-3d-charts','',5,'','','','','')
        enter_addDir(' HD Charts','http://evonic.tv/forum/content.php?r=1989-HD-Charts','',5,'','','','','')
        enter_addDir(' Serien Charts','http://evonic.tv/forum/content.php?r=1997-serien-charts','',5,'','','','','')
        enter_addDir(' Cineline','http://evonic.tv/forum/list.php?r=category/169','',5,'','','','','')
        enter_addDir(' IMDB Ranking',url_start,'',11,'','','','','')
        enter_addDir(' HD Genres',url_start,'',10,'','','','','')
        enter_addDir(' Century',url_start,'',8,'','','','','')

def HD_GENRES(url):
        data = url_opener(url)
        match=re.compile('<div class="cat_main_menuitem">\n<a href="(.*?)">HD:(.*?)</a>\n</div>').findall(data)
        for url,name in match:
            # print name
            enter_addDir(str(name.decode('iso-8859-1').encode('utf-8')),url,'',5,'','','','','')
        xbmc.executebuiltin("Container.SetViewMode(300)")

def INDEX_IMDB(url):
        data = url_opener(url)
        match=re.compile('<div class="cat_main_menuitem">\n<a href="(.*?)">IMDB(.*?)</a>\n</div>').findall(data)
        for url,name in match:
            enter_addDir('IMDB'+str(name),url,'',5,'','','','','')
        xbmc.executebuiltin("Container.SetViewMode(300)")

def INDEX_CENTURY(url):
        data = url_opener(url)
        match=re.compile('<div class="cat_main_menuitem">\n<a href="(.*?)">(Jahr.*?)</a>').findall(data)
        for url,name in match:
            enter_addDir(str(name),url,'',5,'','','','','')
        xbmc.executebuiltin("Container.SetViewMode(300)")

def INDEX(url,name):
        data = url_opener(url)
        origin_name= name
        # content = br.open(url)
        # data = content.read()
        if 'Collection' in name:
            value=[]
            link=data
            soup = BS(link.decode('iso-8859-1','ignore'))
            for div in soup.findAll('div',  {"class": "article_preview"},smartQuotesTo=None):
                attr= div.findAll('a')
                attribute=[]
                for i in attr:
                    attribute.append(i.string)
                name= div.find('span').find(text=True)
                name=name.encode('utf-8').replace('&amp;','&')###neu ## DarkZone Fix
                url= div.find('a')['href']
                url= url.encode('utf-8')###neu
                resim=div.find('img')['src']
                try:
                    value.append((str(name),resim,url,(attribute[2].replace("IMDB ",""))))
                except:
                    value.append((str(name),resim,url,''))
            for name, resim, url, imdb in value:
                enter_addDir(str(name+'[CR][I]imdb-'+str(imdb)+'[/I]'),url,'',7,resim,imdb,'','','')
            # match=re.compile('title="(.*?)">\r\n\t\t(.*?)\r').findall(data)
            match=re.compile('<span><a href=".*?" title=".*?Ergebnis (.*?) von.*?">(.*?)<').findall(data)
            for name, zahl in match:
                enter_addDir('Collections '+str(name),'http://evonic.tv/forum/content.php?r=3501-hd-collection&page='+str(zahl),'',5,'','','','','')

        else:
            value=[]
            link=data
            ##print link                
            soup = BS(link.decode('iso-8859-1','ignore'))
            for div in soup.findAll('div',  {"class": "article_preview"},smartQuotesTo=None):
                attr= div.findAll('a')
                attribute=[]
                for i in attr:
                    attribute.append(i.string)
                name= div.find('span').find(text=True)
                name=name.encode('utf-8').replace('&amp;','&') ###neu ## DarkZone Fix
                url= div.find('a')['href']
                url= url.encode('utf-8')###neu
                resim=div.find('img')['src']
                # print attribute[2],attribute[1].encode('utf-8'),attribute[3]
                try:
                    value.append((str(name),resim,url,attribute[2],str(attribute[1]),attribute[3]))
                except:
                    value.append((str(name),resim,url,'','',''))
            for name, resim, url, imdb, status,jahr in value:
                collection = ( "Saga","Trilogie","Collection","Trilogy","Quadrologie","Quadrilogy","Anthologie" )
                col = None
                for i in collection:
                    if i in name:
                        enter_addDir(str(name+'[CR]'+str(imdb)),url,'',7,resim,imdb,'','','')
                        col = i
                if col !=None:
                    pass
                if 'Serie' in status:
                    enter_addDir(str(name+'[CR][I]Serie von [/I]'+str(imdb)),url,'',6,resim,'','','','')
                elif '3D' in name:
                    enter_addDir(str(name+'[CR]'+str(imdb)+' - '+jahr.encode('utf-8')),url,'',6,resim,str(imdb),'','','')
                elif not (str(collection[0]) in name or str(collection[1]) in name or str(collection[2]) in name or str(collection[3]) in name or str(collection[4]) in name or str(collection[5]) in name or str(collection[6]) in name) and jahr==r'\d*':
                    # print imdb, status, jahr
                    enter_addDir(str(name+'[CR]'+str(imdb)+' - Jahr '+jahr.encode('utf-8')),url,'',6,resim,str(imdb),'','','')
                else:    
                    enter_addDir(str(name+'[CR]'+str(imdb)),url,'',6,resim,str(imdb),'','','')

            match=re.compile('<span><a href="(.*?)" title="(.*?)">').findall(data)
            for url1,name1 in match:
                try:
                    token=re.search('&(.*?)page=', url1).group(1)
                    url1 = url1.replace(token, "")
                except:
                    pass
                if 'Serie' in origin_name:
                		name1=name1+" Serie"
                enter_addDir(name1,url1,'',5,'','','','','')
        xbmc.executebuiltin("Container.SetViewMode(500)")

def SEARCH(url1):
        login= __settings__.getSetting("login")
        password= __settings__.getSetting("password") 
        kb = xbmc.Keyboard('', 'Search Evonic.tv', False)
        kb.doModal()
        search = kb.getText()
        search=search.decode('utf-8').encode('iso-8859-1')
        data = {
            'cookieuser':'1',
            'vb_login_username': login,
            'vb_login_password': password,
            'do':'login',
            'submit':'anmelden',
            }
        login = 'http://evonic.tv/forum/login.php?do=login'
        response = opener.open(login, urllib.urlencode(data)).read()
        main_url=opener.open('http://evonic.tv/forum/content.php').read()
        token = re.search('var SECURITYTOKEN = "(.+?)"',main_url).group(1)
        
        data = {
            'do' : 'search',
            'do' : 'search',
            'lsawithword' : '1',
            'lsatype' : '0',
            'lsazone' : '',
            'lsasort' : 'lastpost',
            'lsasorttype' : 'DESC',
            'keyword' : search,
            'securitytoken' : token,
            's' : ''
            }
        url = 'http://evonic.tv/forum/ajaxlivesearch.php?'
        suche = opener.open(url, urllib.urlencode( data)).read()
        match = re.compile('<span><a href=".*?" title="Stream">Stream</a></span>\r*\n*\r*\n*\s*<a href=".*?" title="Zum ersten ungelesenen Beitrag im Thema \'(.*?)\' gehen">.*?</a>.*?<a href="(.*?)" title=".*?">.*?<span class="highlight">.*?</span>.*?</a>').findall(suche)
        value=[]
        for name,url in match:
            enter_addDir(name.decode('iso-8859-1').encode('utf-8'),url.replace("&amp;","&"),'',13,'','','','','')
        xbmc.executebuiltin("Container.SetViewMode(400)")

def MANAGE_SEARCH(url,name):
        content = url_opener(url)
        link = re.search('<meta http-equiv="refresh" content="0; URL=(.*?)">',content).group(1)
        collection = ( "Saga","Trilogie","Collection","Trilogy","Quadrologie","Quadrilogy","Anthologie" )
        col = None
        for i in collection:
            if i in name:
                LINKS_COLLECTIONS(link)
                col = i
        if col !=None:
            pass
        else:
            VIDEOLINKS(link,name,'','','')

def VIDEOLINKS(url,name,thumbnail,imdb,trailer):
        data = url_opener(url)
        soup = BS(data.decode('iso-8859-1','ignore'))
        name1=None
        try:
            status = re.search('Status:</span> &nbsp; <span style="color: #FF6600;">(.*?)</span>', data).group(1)
            if status == 'Premium Member':
                try:
                    trick = re.search('(\d\d\.\s.*?)<br />\r*\n*<div style="margin:.*?;">',data).group(1)
                    name1=re.compile('(\d\d\.\s.*?)<br />\r*\n*<div style="margin:.*?;">').findall(data)
                    print "Print 1 "+str(name1)
                except:
                    pass
                try:
                    match=re.compile('<a href="(.*?)" target="Videoframe.*?">.*?HD(.*?)</.*?>').findall(data)
                    print "Print 2 "+str(match)
                except:
                        pass
                if match == []:
                    try:
                        match=re.compile('<a href="(.*?)" target=".*?"><b><span style=".*?">(.*?)</span>').findall(data)
                    except:
                            pass
                plot=''
                mpaa=''
                thumbnail = thumbnail
                link_name = ''
                link_name1=''
                tmp_url = ''
                for div in soup.findAll('div',  {"class": "quote_container"}):
                    plot = str(div(text=True)[1])
                try:
                    for div in soup.findAll('div',  {"class": "article cms_clear restore postcontainer"}):
                        mpaa = str(div(text=True))
                        mpaa= re.search("FSK:(.*?),",mpaa).group(1)
                except:
                        pass
                nr=0
                serie = False
                # print "Print 3 "+str(match)
                for i, e in enumerate(match):
                    if 'server' in e[0] or 'Premium-Member' in e[0]:
                        tmp_url = tmp_url + str(e[0])
                        if name1:
                            link_name = (name1[i/2].decode('iso-8859-1').encode('utf-8')+' [I](HD'+e[1]+')[/I]')
                        else:
                            link_name = (name+' [I](HD'+e[1]+')[/I]')
                    # elif 'Non-Premium-Member' in e[0]:
                        # link_name = 'Kein Premium Mitglied'
                    # elif 'Free-Member' in e[0]:
                        # tmp_url = tmp_url + str(e[0])
                        # if name1:
                            # link_name = (name1[i/2].decode('iso-8859-1').encode('utf-8')+' [I](HD'+e[1]+')[/I]')
                        # else:
                            # link_name = (name+' [I](HD'+e[1]+')[/I]')
                    else:
                            pass
                    if link_name !='':
                        try:
                            try:
                                try:
                                    nr_vor = re.search('^(\d\d\.)\s*.*?$',e[1]).group(1)
                                    # print 'DENEME 1 : '+nr_vor
                                    serie = True
                                except:
                                    nr_vor = re.search('^.*?(\d\d)$', e[1]).group(1)
                                    nr_vor = str(nr_vor+'.')
                                    # print 'DENEME 2 : '+nr_vor
                                    serie = True
                                staffel_vor = re.search('.*\?mov=(\w+)(\d+)-.*',e[0])
                            except:
                                nr_vor = None
                                # print nr_vor
                            if trailer== None:
                                try:
                                    for object in soup.findAll('object', {"class": "restrain"},smartQuotesTo=None):
                                        code=re.search("http://www.youtube.com/v/(.*?)&fs=1", str(object.find('param')['value'])).group(1)
                                        url_tube='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)+"&hd=1"
                                        trailer= str(url_tube)
                                except:
                                        pass
                            if 'Staffel' not in name:
                                if staffel_vor != None and nr_vor != None:
                                    nombre = re.search('^.*?(\d+)-(\d+)-*(\d+)*-*(\d+)*$',e[0])
                                    # print "HIER :"+str(nombre.group(2))
                                    if '1' == str(nombre.group(2)):
                                    # if '01.' == str(nr_vor):
                                        nr=nr+1
                                        enter_addDir('Staffel '+str(nombre.group(1)),url,url,6,thumbnail,imdb,'','',trailer)
                                        
                            else:
                                staff = re.search('Staffel (\d+)', name).group(1)
                                if nr_vor != None and staff in staffel_vor.group(1)+staffel_vor.group(2):
                                    if '01.' == str(nr_vor):
                                        nr=nr+1
                                    if 'server' in e[0]:
                                        # print 'oldu la'
                                        enter_addDir(e[1].decode('iso-8859-1').encode('utf8'),tmp_url,url,3,thumbnail,'','','',trailer)
                                    if 'Free-Member' in e[0]:
                                        # print 'oldu la 2'
                                        enter_addDir(e[1].decode('iso-8859-1').encode('utf8'),tmp_url,url,1,thumbnail,'','','',trailer)
                            tmp_url = ''
                            link_name = ''
                        except:#nr=0
                            if 'Premium-Member' or 'Mobile' in e[0]: ## DarkZone Fix
                                try:
                                    nr_vor = re.search('(.*?\.) .*?',e[1]).group(1)
                                except:
                                    nr_vor = None
                                if nr_vor != None:
                                    if '01.'  == str(nr_vor):
                                        nr=nr+1
                                    enter_addDir(e[1].decode('iso-8859-1').encode('utf-8'),tmp_url,url,3,'','','','','')
                                else:
                                    if quality == '0' or quality == '2':
                                        trailer= ''
                                        try:
                                            for object in soup.findAll('object', {"class": "restrain"},smartQuotesTo=None):
                                                code=re.search("http://www.youtube.com/v/(.*?)&fs=1", str(object.find('param')['value'])).group(1)
                                                url_tube='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)+"&hd=1"
                                                trailer= str(url_tube)
                                        except:
                                                pass
                                        try:
                                            enter_addDir(link_name,e[0],url,3,thumbnail,imdb,plot,mpaa,trailer)
                                        except:
                                            enter_addDir('Dieser'+link_name,e[0],url,3,'','','','','')
                                    else:
                                            pass
                                tmp_url = ''
                                link_name = ''
                    else:
                            pass
                    tmp_url1=''
                    if quality == '1'or quality == '2':
                        if 'Free-Member' in e[0] and serie == False and nr == 0:
                            tmp_url1 = tmp_url1 + str(e[0])
                            if name1:
                                link_name1 = (name1[i/2].decode('iso-8859-1').encode('utf-8')+' [I](HD'+e[1]+')[/I]')
                            else:
                                link_name1 = (name+' [I](HD'+e[1]+')[/I]')
                        else:
                                pass
                        if link_name1 !='':
                                trailer= ''
                                try:
                                    for object in soup.findAll('object', {"class": "restrain"},smartQuotesTo=None):
                                        code=re.search("http://www.youtube.com/v/(.*?)&fs=1", str(object.find('param')['value'])).group(1)
                                        url_tube='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)+"&hd=1"
                                        trailer= str(url_tube)
                                except:
                                        pass
                                try:
                                    enter_addDir(link_name1,tmp_url1,url,1,thumbnail,imdb,plot,mpaa,trailer)
                                    tmp_url1=''
                                    link_name1=''
                                except:
                                    enter_addDir(link_name1,tmp_url1,url,1,'','','','','')
                                    tmp_url1=''
                                    link_name1=''
                        else:
                                pass
                    else:
                            pass
        except:
                raise
        """
        if 'Staffel' not in name:
            try:
                for object in soup.findAll('object', {"class": "restrain"},smartQuotesTo=None):
                    code=re.search("http://www.youtube.com/v/(.*?)&fs=1", str(object.find('param')['value'])).group(1)
                    url_tube='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)+"&hd=1"
                    enter_addDir('(Trailer) '+name,str(url_tube),'',12,'','','','')
            except:
                    pass
        """
        xbmc.executebuiltin("Container.SetViewMode(400)")

def play_trailer(url,name,thumbnail):
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        enter_addLink(name,url,thumbnail,'','')
        listitem = xbmcgui.ListItem(name,thumbnailImage=thumbnail)
        xbmc.PlayList(1).add(url, listitem)
        xbmc.Player().play(pl)

def play_premium_video(url,name,thumbnail,imdb,mpaa):
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        try:
            dir_vid = url_opener(url)
            try:
                link = re.search('type="video/divx" src="(.*?)"',dir_vid).group(1)
                enter_addLink(name,link,thumbnail,imdb,'')
            except:
                link = re.search('<source src="(.?)" type="video/mp4" />',dir_vid).group(1)
                enter_addLink(name,link,thumbnail,imdb,'')
            listitem = xbmcgui.ListItem(name,thumbnailImage=thumbnail)
            xbmc.PlayList(1).add(link, listitem)
            xbmc.Player().play(pl)
        except:
                pass

def play_free_video(url,name,thumbnail,imdb,mpaa):
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        try:
            video1 = url_opener(url)
            video_match1 = re.compile('src="(.*?)" type="video/mp4"').findall(video1)
            link = video_match1[0]
            # link = re.search('file=(http.*?)\.mp4.*?&', video1).group(1)
            enter_addLink(name,link,thumbnail,imdb,'')
            listitem = xbmcgui.ListItem(name,thumbnailImage=thumbnail)
            xbmc.PlayList(1).add(link, listitem)
            xbmc.Player().play(pl)
        except:
                pass

def LINKS_COLLECTIONS(url):
        data = url_opener(url)
        data = (data.decode('iso-8859-1').encode('utf-8')).replace('&amp;','&').replace('<font size="4">','').replace('<font size="3">	','').replace('</font','')
        match=re.compile('<a href="(.*?)" target=".*?">').findall(data)
        match1=re.compile('<*b*>*<font size=".*?">(.*?)</font><*/*b*>*<br /><div style="margin: 5px;">').findall(data)
        match2=re.compile('\r\n<.*?>\r*\n*(.*?)<*b*r*\s*/*>*\r*\n*<*b*r*\s*/*>*\r*\n*\s*<div style=".*?">').findall(data)
        # for i in match2:
            # print i
        if match1:
            match_name = match1
        elif match2:
            match_name = match2

        soup = BS(data.decode('iso-8859-1','ignore'))
        value=[]
        for index, div in enumerate(soup.findAll('div',  {"class": "alt2"},smartQuotesTo=None)):
            try:
                img= div.find('img')['src']
                value.append(img)
            except:
                    pass
            if 'none;">Platzhalter</div>' in str(div) or 'Kein Film vorhanden!' in str(div):
                # del value[index]
                del match_name[index]
                print match_name[index]
        match_video_HDPlus=[]
        match_video_Free=[]
        free = 0
        plus = 0
        try:
            status = re.search('Status:</span> &nbsp; <span style="color: #FF6600;">(.*?)</span>', data).group(1)
            if status == 'Premium Member':
                for index, i in enumerate(match):
                    # print ("Free: ",free)
                    # print ("Plus: ",plus)
                    tmp_url = ''
                    if quality == '0' or quality == '2':
                        if 'Premium-Member' in i: ## DarkZone fix
                            if plus==free:
                                plus=plus+1
                            elif plus<free+1:
                                plus=plus+1
                            elif plus==free+1:
                                free=free+1
                                plus=plus+1
                            elif plus==free+2:
                                free=free+3
                                plus=plus+1
                            tmp_url = tmp_url + str(i)
                            trailer= ''
                            try:
                                for object in soup.findAll('object', {"class": "restrain"},smartQuotesTo=None):
                                    code=re.search("http://www.youtube.com/v/(.*?)&fs=1", str(object.find('param')['value'])).group(1)
                                    url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)+"&hd=1"
                                    trailer= str(url)
                            except:
                                    pass
                            try:
                                enter_addDir(match_name[plus-1]+'[CR] [I](HD Plus)[/I]',tmp_url,url,3,value[plus-1],'','','',trailer)
                            except:
                                    pass
                    if quality == '1' or quality == '2':
                        if 'Free-Member' in i:
                            if free==plus:
                                free=free+1
                            elif free<plus+1:
                                free=free+1
                            elif free==plus+1:
                                plus=plus+1
                                free=free+1
                            elif free==plus+2:
                                plus=plus+3
                                free=free+1
                            tmp_url = tmp_url + str(i)
                            match_video_Free.append(tmp_url)
                            trailer= ''
                            try:
                                for object in soup.findAll('object', {"class": "restrain"},smartQuotesTo=None):
                                    code=re.search("http://www.youtube.com/v/(.*?)&fs=1", str(object.find('param')['value'])).group(1)
                                    url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)+"&hd=1"
                                    trailer= str(url)
                            except:
                                    pass
                            try:
                                enter_addDir(match_name[free-1]+'[CR] [I](HD Free)[/I]',tmp_url,url,1,value[free-1],'','','',trailer)
                            except:
                                enter_addLink('Ueberlastet'+match_name[free],i,'','','')
        except:
                pass
        xbmc.executebuiltin("Container.SetViewMode(500)")

def write_attr(url):
        data = url_opener(url)
        link=data.replace('\xf6',"oe").replace('&amp;',"&").replace('\xd6',"Oe").replace('\xdc',"Ue").replace('\xfc',"ue").replace('\xc4',"Ae").replace('\xe4',"ae").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g").replace('\xdf',"ss").replace('\xe9',"e")
        value=[]
        soup = BS(link)
        for ol in soup.findAll('ol',  {"class": "commalist"},smartQuotesTo=None):
            attr= ol.findAll('a')
            attribute=[]
            for i in attr:
                attribute.append(i.string)
            value.append(attribute)
        return value

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

def enter_addLink(name,url,iconimage,imdb,plot):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Rating": imdb, "Plot": plot, "MPAA": imdb} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def enter_addDir(name,url,url0,mode,iconimage,imdb,plot,mpaa,trailer):
		  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&url0="+urllib.quote_plus(url0)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&imdb="+str(imdb)+"&mpaa="+str(mpaa)
		  ok=True
		  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		  liz.setInfo( type="Video", infoLabels={ "Title": name,"Rating": imdb, "Plot": plot, "MPAA": mpaa, "Trailer": trailer } )
		  menu=[]
		  if mode == 3 or mode == 1:
		  		menu.append(('Add To Library','XBMC.RunPlugin(%s?mode=100&name=%s&url=%s&iconimage=%s)'% (sys.argv[0], urllib.quote_plus(name),urllib.quote_plus(url), urllib.quote_plus(iconimage))))
		  if "Serie" in name:
		  		menu.append(('Serie in Library','XBMC.RunPlugin(%s?mode=102&name=%s&url=%s&iconimage=%s)'% (sys.argv[0], urllib.quote_plus(name),urllib.quote_plus(url), urllib.quote_plus(iconimage))))
		  liz.addContextMenuItems(items=menu, replaceItems=False)
		  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		  return ok
       
def PLAY_VID(url,iconimage,name):
		dir_vid = url_opener(url)
		url = re.search('src="(.*?)"',dir_vid).group(1)
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name} )
		liz.setProperty("IsPlayable","true")
		strm = True
		if not strm:
				pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
				pl.clear()
				pl.add(url, liz)
				xbmc.Player().play(pl)
				return

		liz.setPath(url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		
def cleanFilename(filename):
	try:
		nam1 = filename.split(": ")
		nam2 = nam1[1].split("[CR]")
		try:
			nam2[1]
			nam2 = nam1[1].split("[CR]")
		except:
			nam2 = nam1[1].split("[i]")
		print nam2[0]
		filename = urllib.quote(nam2[0])
	except:
		try:
			nam1 = filename.split("HD ")
			filename = nam1[1]
		except:
			filename = filename
	return re.sub('[:\\/*?\<>|"]+', '', filename)
		

def LIBRARY_MOVIE(name,url,iconimage):#  cause mode is empty in this one it will go back to first directory
		name = cleanFilename(str(name))
		global library_path
		if library_path == 'false':
			dialog = xbmcgui.Dialog()
			library_path = dialog.browse(3, 'Movie Folder', 'files', '', False, False, "")
		strm=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=101&name="+name+"&iconimage="+urllib.quote_plus(iconimage)
		foldername=os.path.join(library_path)
		filename = name + '.strm'
		file     = os.path.join(foldername,filename)

		a = open(file, "w")
		a.write(strm)
		a.close()
		
def LIBRARY_SERIE(name,url,iconimage):#  cause mode is empty in this one it will go back to first directory
		name = cleanFilename(str(name))
		data = url_opener(url)
		soup = BS(data.decode('iso-8859-1','ignore'))
		match=re.compile('<a href="(.*?)" target=".*?"><b><span style=".*?">(.*?)</span>').findall(data)
		global library_serie
		if library_serie == 'false':
			dialog = xbmcgui.Dialog()
			library_serie = dialog.browse(3, 'Serien Folder', 'files', '', False, False, "")
		foldermain=os.path.join(library_serie)
		foldername = os.path.join(foldermain, name)
		if not os.path.exists(foldername):
			os.mkdir(foldername)
		nr=0
		y=1
		serie = False
		seasonfolder=''
		for i, e in enumerate(match):
			try:
				try:
					nr_vor = re.search('^(\d\d\.)\s*.*?$',e[1]).group(1)
					# print 'DENEME 1 : '+nr_vor
					serie = True
				except:
					nr_vor = re.search('^.*?(\d\d)$', e[1]).group(1)
					nr_vor = str(nr_vor+'.')
					# print 'DENEME 2 : '+nr_vor
					serie = True
				staffel_vor = re.search('.*\?mov=(\w+)(\d+)-.*',e[0])
			except:
				nr_vor = None
			if 'Staffel' not in name:
				if staffel_vor != None and nr_vor != None:
					nombre = re.search('^.*?(\d+)-(\d+)',e[0])
					# print "HIER :"+str(nombre.group(2))
				if '1' == str(nombre.group(2)):
					# if '01.' == str(nr_vor):
					y=1
					nr=nr+1
					seasonfolder = os.path.join(foldername, 'Staffel '+str(nombre.group(1)))
					if not os.path.exists(seasonfolder):
						os.mkdir(seasonfolder)
						#enter_addDir('Staffel '+str(nombre.group(1)),url,url,6,thumbnail,imdb,'','',trailer)
				etitle=e[1]
				if not e[1][0].isdigit():
					etitle=str(y)+"."+e[1]
					y=y+1
				print "S"+str(nr)+"E"+etitle
				strm=sys.argv[0]+"?url="+urllib.quote_plus(e[0])+"&mode=101&name="+urllib.quote_plus(etitle)+"&iconimage="+urllib.quote_plus(iconimage)
				ename = cleanFilename("S"+str(nr)+"E"+etitle)				
				filename = urllib.quote(ename) + '.strm'
				file     = os.path.join(seasonfolder,filename)
				a = open(file, "w")
				a.write(strm)
				a.close()