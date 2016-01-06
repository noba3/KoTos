# -*- coding: utf-8 -*-
import urllib2,re,os,sys,codecs
from BeautifulSoup import BeautifulSoup as BS
from xml.dom.minidom import Document
import xml.dom.minidom as minidom
import mechanize,shutil
import xbmcaddon,xbmc,xbmcgui
addon_id = 'plugin.video.Stream-Oase.tv'
addon = xbmcaddon.Addon(addon_id)
__settings__ = xbmcaddon.Addon(id="plugin.video.Stream-Oase.tv")
status = __settings__.getSetting("status")
datapath = __settings__.getAddonInfo('path')
channels = xbmc.translatePath(os.path.join(datapath, 'resources', 'lib'))
sys.path.append(channels)
channels = xbmc.translatePath(os.path.join(datapath, 'database'))
sys.path.append(channels)

def hazirla(isim,bolum):
    try:
        sonuclar=[]
        if 'New' in isim:
                tmp = []
                for f in VIDEOLINKS_OASE(isim,bolum):
                        str(f)
                        tmp.append(f)
                for i in reversed(tmp):
                        sonuclar.append(i)
        else:
                sayfa = sayfalama(bolum)
                for i in sayfa:
                        for f in VIDEOLINKS_OASE(isim,i):
                            sonuclar.append(f)
    except:
            pass
    print sonuclar
    if sonuclar:
        xml_yap(isim,sonuclar)
    if len(sonuclar) > 0:
        dialog1 = xbmcgui.Dialog()
        dialog1.ok('Datenbank Update der Kategorie '+isim+' beendet!','[UPPERCASE][B]Es wurden '+str(len(sonuclar))+' Filme in '+isim+' hinzugefuegt[/B][/UPPERCASE]','Damit die Filme sichtbar werden, raus und rein!')
    print 'Update beendet !!!'
    __settings__.setSetting(str(isim.decode('latin1').encode('utf-8')), 'false')
                    
def VIDEOLINKS_OASE(name1,url):
        # link=get_url(url)
        # soup = BS(link)
        html = re.split(r'<div class="sp-component-area clearfix">',get_url(url))[1]
        match = re.findall(r' href="(.+?)">.*\n.*\n.* class="image" src="(.+?)" .*\n.* class="title">(.+?)<',html)
        value=[]
        value2=[]
        video_db = open( os.path.join(channels, str(name1)+".xml"),"r" )
        video_db_str = video_db.read()
        video_db.close()
        # print video_db_str
        for url, img, name in match:
        # for div in soup.find('div',  {"class": "sp-component-area-inner clearfix"},smartQuotesTo=None).findAll('div',  {"class": "avs_thumb"},smartQuotesTo=None):
                # url= div.find('a')['href']
                # img= div.find('img').findNext('img')['src']
                # name= (div.find('span').text).encode('utf-8')
                
                if name.replace("&","&amp;") in video_db_str:
                    pass
                else:
                    print 'UPDATER : '+name
                    value.append((url, img, name))
        if name1=='New Videos':
            for url1,thumbnail,name in reversed(value):
                try:
                        #print name
                        value2.append(PLAYLINK_OASE(url1,name.decode('utf-8'),thumbnail))
                except:
                        print 'hata1'
        else:
            for url1,thumbnail,name in value:
                try:
                        #print name
                        value2.append(PLAYLINK_OASE(url1,name.decode('utf-8'),thumbnail))
                except:
                        print 'hata2'
        return value2
        
def sayfalama(url_base):
        link=get_url(url_base)
        soup = BS(link)
        seiten = []
        seiten.append(url_base)
        for div in soup.find('div',  {"class": "sp-component-area-inner clearfix"},smartQuotesTo=None).findAll('li',smartQuotesTo=None):
                try:
                    url= div.find('a')['href']
                except:
                    url=""
                    
                name= div.find('a').find(text=True)
                if name != '1' and name!= 'Weiter' and name!='Ende':
                        seiten.append('http://stream-oase.tv'+url)
                
        return seiten
        
def PLAYLINK_OASE(url,name,iconimage):
        nuna='http://stream-oase.tv'+url
        link=get_url(nuna)
        match=re.compile('<iframe src="(.*?)embed-(.*?)-.*?.html" frameborder=', re.I).findall(link)
        match2=re.compile('<iframe src="(.*?)" frameborder=', re.I).findall(link)
        try:
            youtbe = re.search('<strong>Trailer:</strong> <a ondragstart="return false;" href="(http://www.youtube.com/v.*?)&amp;hl=en&amp;fs=1&amp;rel=0&amp;autoplay=0" title="',link).group(1)
            print 'YOUTUBE LINK: '+youtbe
            code2 = re.search('^.*?/v/(.*?)$',youtbe).group(1)
            trailer = 'plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code2)+"&hd=1"
        except:
            trailer = ''
            print 'HAT NICHT FUNKTIONIERT TRAILER :'
        try:
            fanart = get_fanart(name)
        except:
            fanart = ''
        try:
            imdb = re.search('<p><strong>imdb-Bewertung:</strong> (.*?)/10<.*?', link).group(1)#.decode('utf-8')
            imdb = imdb.replace(",",".")
        except:
            imdb = ''
        try:
            darsteller = re.search('>Darsteller:</strong>(.*?)<.*?',link).group(1).decode('utf-8')
        except:
            darsteller = ''
        try:
            plot = re.search('<strong>\s*Inhalt:</strong>\s*</p>\r\n<p>(.*?)<.*?', link).group(1).decode('utf-8')
        except:
            plot = ''
        try:
            fsk = re.search('<p><strong>FSK:</strong> (.*?)</p>', link).group(1)#.encode('utf-8')
        except:
            fsk = ''
        try:
            code1 = re.search('http://www.imdb.com/title/(.*?)/', link).group(1)#.decode('utf8')
        except:
            code1 = ''
        direct_links = []
        for hoster, code in match:
            if 'vidplay' in hoster:
                try:
                        direct_links.append(str(hoster)+str(code))
                                
                except:
                        pass
            if '180upload' in hoster:
                try:
                        direct_links.append(str(hoster)+str(code))
                                
                except:
                        pass
        for src in match2:
            if 'mightyupload' in src:
                    try:
                            ref = re.search('http://(.*?)/',src).group(1)
                            ref = ref.replace("www.", '').replace(".com",'').replace(".net",'')
                            direct_links.append(src)
                    except:
                            pass
            if 'vk.com' in src:
                    try:
                            direct_links.append(src.decode('utf-8'))
                    except:
                            pass
        return(name,(direct_links),iconimage,fanart,imdb,darsteller,plot,fsk,code1,trailer)
                        
def get_fanart(name):
        name = name.decode('utf8')
        text = [ "\s*20\d+","\s*UNCUT","\s*Uncut","\s*Uncut","\s*Cut","\s*EXTENDED","\s*Extended Cut","\s*Directors Cut","\s*Extended"," \(\d+\)"," - .+","\s*Directors" ]
        for i in text:
                try:
                    reg = re.search('(?<=)'+i, name).group(0)
                    name = name.replace(reg,"")
                except:
                        pass
        try:
            name = name.replace("ü".decode('latin1'),"ue").replace("ö".decode('latin1'),"oe").replace("ä".decode('latin1'),"ae").replace("ß".decode('latin1'),"ss").replace("."," ").replace(' ','+')
        except:
                pass
        try:
            url='http://www.themoviedb.org/search/movie?query=' + name
            html = get_url(url)
            link = 'http://www.themoviedb.org'+ re.findall('<a href="(/movie/.*?)" title="',html)[0]
            html = get_url(link)
            fanart = re.findall('<img class="lightbox" id=".*?" src="(.+?)" width=".*?"',html)[0]
            img = fanart.replace("w300","original")
            return img
        except:
            print 'ERROR: get_Fanart ' + name

def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
        
def xml_yap(isim,sonuclar):###xml yapim yeri
        doc = minidom.parse(os.path.join(channels, isim+'.xml'))
        video = doc.getElementsByTagName('item')
        value_xml=[]
        for node in video:
            try:
                name= (u'<title>'+(node.getElementsByTagName('title')[0].firstChild.data)+'</title>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;")
            except:
                name= '<title></title>'
            url_ray = []
            for i in node.getElementsByTagName('link'):
                try:
                    url_ray.append((u'<link>'+i.firstChild.data.encode('utf-8')+'</link>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;"))
                except:
                    pass
            try:
                img= (u'<thumbnail>'+(node.getElementsByTagName('thumbnail')[0].firstChild.data.encode('utf-8'))+'</thumbnail>').replace("\t","").replace("\r","").replace("\n","")
            except:
                img= u'<thumbnail></thumbnail>'
            try:
                fanart = (u'<fanart>'+(node.getElementsByTagName('fanart')[0].firstChild.data.encode('utf-8'))+'</fanart>').replace("\t","").replace("\r","").replace("\n","")
            except:
                fanart = u'<fanart></fanart>'
            try:
                imdb = (u'<imdb>'+(node.getElementsByTagName('imdb')[0].firstChild.data.encode('utf-8'))+'</imdb>').replace("\t","").replace("\r","").replace("\n","")
            except:
                imdb = u'<imdb></imdb>'
            try:
                darsteller = (u'<darsteller>'+(node.getElementsByTagName('darsteller')[0].firstChild.data.encode('utf-8'))+'</darsteller>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;")
            except:
                darsteller = u'<darsteller></darsteller>'
            try:
                plot = (u'<plot>'+(node.getElementsByTagName('plot')[0].firstChild.data)+'</plot>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;")
            except:
                plot = u'<plot></plot>'
            try:
                fsk = (u'<fsk>'+(node.getElementsByTagName('fsk')[0].firstChild.data.encode('utf-8'))+'</fsk>').replace("\t","").replace("\r","").replace("\n","")
            except:
                fsk = u'<fsk></fsk>'
            try:
                code = (u'<code>'+(node.getElementsByTagName('code')[0].firstChild.data.encode('utf-8'))+'</code>').replace("\t","").replace("\r","").replace("\n","")
            except:
                code = u'<code></code>'
            try:
                trailer = (u'<trailer>'+(node.getElementsByTagName('trailer')[0].firstChild.data.encode('utf-8'))+'</trailer>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;")
            except:
                trailer = u'<trailer></trailer>'
            if len(url_ray)==3:
                try:
                    value_xml.append((name,url_ray[0],url_ray[1],url_ray[2],img,fanart,imdb,darsteller,plot,fsk,code,trailer))
                except:
                    pass
            if len(url_ray)==2:
                try:
                    value_xml.append((name,url_ray[0],url_ray[1],img,fanart,imdb,darsteller,plot,fsk,code,trailer))
                except:
                    pass
            if len(url_ray)==1:
                try:
                    value_xml.append((name,url_ray[0],img,fanart,imdb,darsteller,plot,fsk,code,trailer))
                except:
                    pass
            
        for videoTitle,url,thumbnail,fanart,imdb,darsteller,plot,fsk,code,trailer in reversed(sonuclar):
            try:
                name= (u'<title>'+videoTitle+'</title>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;")
            except:
                name= u'<title></title>'
            url_arr = []
            for i in url:
                try:
                    url_arr.append((u'<link>'+i+'</link>').replace("\t","").replace("\r","").replace("\n","").replace("&amp;","&").replace("&","&amp;"))
                except:
                    pass           
            try:
                img= (u'<thumbnail>'+thumbnail+'</thumbnail>').replace("\t","").replace("\r","").replace("\n","")
            except:
                img= u'<thumbnail></thumbnail>'
            try:
                fanart = (u'<fanart>'+fanart+'</fanart>').replace("\t","").replace("\r","").replace("\n","")
            except:
                fanart = u'<fanart></fanart>'
            try:
                imdb = (u'<imdb>'+imdb+'</imdb>').replace("\t","").replace("\r","").replace("\n","").replace("&","&amp;")
            except:
                imdb = u'<imdb></imdb>'
            try:
                darsteller = (u'<darsteller>'+darsteller+'</darsteller>').replace("\t","").replace("\r","").replace("\n","").replace("&","&amp;")
            except:
                darsteller = u'<darsteller></darsteller>'
            try:
                plot = (u'<plot>'+plot+'</plot>').replace("\t","").replace("\r","").replace("\n","")
            except:
                plot = u'<plot></plot>'
            try:
                fsk = (u'<fsk>'+fsk+'</fsk>').replace("\t","").replace("\r","").replace("\n","").replace("&","&amp;")
            except:
                fsk = u'<fsk></fsk>'
            try:
                code = (u'<code>'+code+'</code>').replace("\t","").replace("\r","").replace("\n","")
            except:
                code = u'<code></code>'
            try:
                trailer = (u'<trailer>'+trailer+'</trailer>').replace("\t","").replace("\r","").replace("\n","").replace("&","&amp;")
            except:
                trailer = '<trailer></trailer>'
            if len(url_arr) == 3:
                try:
                    value_xml.append((name,url_arr[0],url_arr[1],url_arr[2],img,fanart,imdb,darsteller,plot,fsk,code,trailer))
                except:
                    pass
            if len(url_arr) == 2:
                try:
                    value_xml.append((name,url_arr[0],url_arr[1],img,fanart,imdb,darsteller,plot,fsk,code,trailer))
                except:
                    pass
            if len(url_arr) == 1:
                try:
                    value_xml.append((name,url_arr[0],img,fanart,imdb,darsteller,plot,fsk,code,trailer))
                    print 'DAS KLAPPT'
                except:
                    pass
        f = codecs.open(  os.path.join(channels, str(isim)+'.xml'),"wb","utf-8")
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<ArrayOfitem>\n')
        for i in value_xml:
            f.write('<item>\n')
            for e in i:
                f.write(e+'\n')
            f.write('</item>\n')
        f.write('</ArrayOfitem>')
        f.close()
