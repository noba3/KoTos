# Stream-Oase.tv plugin written by Mentality
# -*- coding: utf-8 -*-

import re,os,urllib,urllib2
import xbmcplugin,xbmcgui,xbmcaddon,xbmc
import cookielib
from BeautifulSoup import BeautifulSoup as BS
import xml.dom.minidom as minidom
import mechanize,gzip,shutil
from thread import start_new_thread

addon_id = 'plugin.video.Stream-Oase.tv'
addon = xbmcaddon.Addon(addon_id)
__settings__ = xbmcaddon.Addon(id="plugin.video.Stream-Oase.tv")
status = __settings__.getSetting("status")
datapath = __settings__.getAddonInfo('path')
channels = xbmc.translatePath(os.path.join(datapath, 'resources', 'lib'))
sys.path.append(channels)
channels = xbmc.translatePath(os.path.join(datapath, 'resources', 'images'))
sys.path.append(channels)
channels = xbmc.translatePath(os.path.join(datapath, 'database'))
sys.path.append(channels)
import Stream_Update as su
import jsunpack
from net import Net
import simplejson as json
net = Net()
files = os.listdir(channels)
global imps
imps = []
for i in range(len(files)):
    if 'xml' in files[i]:
        py_name = files[i].split('.')
        py_name = py_name[0]
        imps.append(py_name.decode('latin1').encode('utf-8'))
global my_threads
my_threads = []
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'   

def INDEX_OASE(url):
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            addDir('OASE Suche...','http://stream-oase.tv/',16,str(channels)+'/Transparenz.png','','','','','','','')
            addDir('New Videos','/index.php/hd-oase/video/latest',6,str(channels)+'/Transparenz.png','','','','','','0','')
            addDir('Serien','http://stream-oase.tv/index.php/serien',1,str(channels)+'/Transparenz.png','','','','','','','')
            addDir('Livestreams','http://stream-oase.tv/index.php/serien',9,str(channels)+'/Transparenz.png','','','','','','','')
            # addDir('Oasen HD Highlights'.decode('latin-1').encode('utf8'),'http://stream-oase.tv/index.php/component/allvideoshare/video/featured',6,str(channels)+'/Transparenz.png','','','','','','','0')
            # addDir('Top 30 HD Filme'.decode('latin-1').encode('utf8'),'http://stream-oase.tv/index.php/component/allvideoshare/video/popular',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Action'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/action',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Abenteuer'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/abenteuer',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Drama'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/drama',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Krieg'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/krieg',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Thriller'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/thriller',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Horror'.encode('utf8'),'/index.php/hd-oase/category/horror',6,str(channels)+'/Transparenz.png','','','','','','0','')
            addDir('Komödie'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/komoedie',6,str(channels)+'/Transparenz.png','','','','','','0','')
            addDir('Zeichentrick'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/zeichentrick',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Sci-Fi'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/sci-fi',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Doku´s'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/doku-s',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Western'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/western',6,str(channels)+'/Transparenz.png','','','','','','','0')
            addDir('Fantasy'.decode('latin-1').encode('utf8'),'/index.php/hd-oase/category/fantasy',6,str(channels)+'/Transparenz.png','','','','','','','0')            
            addDir('Cartoons','http://stream-oase.tv/index.php/cartoon',1,str(channels)+'/Transparenz.png','','','','','','','')
        except:
            addDir('Livestreams','yok bisi',9,str(channels)+'/Transparenz.png','','','','','','','')
            for i in imps:
                addDir(i,'yok bisi',6,str(channels)+'/Transparenz.png','','','','','','','')

def VIDEOLINKS_OASE(name,url_base,page,kateg):
        if kateg == None:
            namea = name
        else:
            namea = kateg
        if url!='yok bisi':
            nuna='http://stream-oase.tv'+url_base
        else:
            dialog2 = xbmcgui.Dialog()
            dialog2.ok('www.Stream-Oase.tv ist nicht erreichbar!','[B]Die Datenbank wird geladen, damit du trotzdem schauen kannst!!![/B]','Die Seite wird bald gefixt!!!')
        name0 = namea.replace("Komödie".decode('latin-1').encode('utf-8'),"Komodie").replace("Doku´s".decode('latin-1').encode('utf-8'),"Dokus")
        name1 = name0
        try:
            xmldoc = minidom.parse(os.path.join(channels, name1+'.xml'))
            shutil.copyfile(os.path.join(channels, name1+'.xml'),os.path.join(channels, (name1+'.bak')))
        except:
            shutil.copyfile(os.path.join(channels, name1+'.bak'),os.path.join(channels, (name1+'.xml')))
            xmldoc = minidom.parse(os.path.join(channels, name1+'.xml'))
        try:
            thread_name = __settings__.getSetting(str(name1.decode('latin1').encode('utf-8')))
            if thread_name == 'true':
                pass
            else:
                __settings__.setSetting(str(name1.decode('latin1').encode('utf-8')), 'true')
                start_new_thread(su.hazirla,(name1,nuna))
        except:
                print "sayfa yuklenemiyor"
        
        value = []
        video = xmldoc.getElementsByTagName('item')
        for node in video:
            try:
                name= node.getElementsByTagName('title')[0].firstChild.data.encode('utf-8')
            except:
                name=''
            url_ray = []
            for i in node.getElementsByTagName('link'):
                try:
                    url_ray.append((i.firstChild.data.encode('utf-8')))
                except:
                    pass
            try:
                img= node.getElementsByTagName('thumbnail')[0].firstChild.data
            except:
                img=''
            try:
                fanart = node.getElementsByTagName('fanart')[0].firstChild.data
            except:
                fanart = ''
            try:
                imdb = node.getElementsByTagName('imdb')[0].firstChild.data.encode('utf-8')
            except:
                imdb = ''
            try:
                darsteller = node.getElementsByTagName('darsteller')[0].firstChild.data.encode('utf-8')
            except:
                darsteller = ''
            try:
                plot = node.getElementsByTagName('plot')[0].firstChild.data.encode('utf-8')
            except:
                plot = ''
            try:
                fsk = node.getElementsByTagName('fsk')[0].firstChild.data.encode('utf-8')
            except:
                fsk = ''
            try:
                code = node.getElementsByTagName('code')[0].firstChild.data.encode('utf-8')
            except:
                code = ''
            try:
                trailer = node.getElementsByTagName('trailer')[0].firstChild.data
            except:
                trailer = ''
            # print trailer
            if len(url_ray) == 3:
                try:
                    value.append((';'.join([url_ray[0],url_ray[1],url_ray[2]]),str(fanart.replace("\r*\n*","")), str(img.replace("\r*\n*","")), name, imdb, darsteller, plot, fsk, code, str(trailer) ))
                except:
                    pass
            if len(url_ray) == 2:
                try:
                    value.append((';'.join([url_ray[0],url_ray[1]]),str(fanart.replace("\r*\n*","")), str(img.replace("\r*\n*","")), name, imdb, darsteller, plot, fsk, code, str(trailer) ))
                except:
                    pass
            if len(url_ray) == 1:
                try:
                    value.append((url_ray[0],str(fanart.replace("\r*\n*","")), str(img.replace("\r*\n*","")), name, imdb, darsteller, plot, fsk, code, str(trailer) ))
                except:
                    pass
                
        if name1=='New Videos':
            for i,(url1,fanart,thumbnail,name,imdb,darsteller,plot,fsk,code,trailer) in enumerate(reversed(value)):
                try:
                        # print trailer
                        addDir(name,url1,4,thumbnail,fanart,imdb,darsteller,plot,fsk,code,trailer)
                except:
                        pass 
        else:
            for i,(url1,fanart,thumbnail,name,imdb,darsteller,plot,fsk,code,trailer) in enumerate(reversed(value)):
                try:
                        addDir(name,url1,4,thumbnail,fanart,imdb,darsteller,plot,fsk,code,trailer)
                except:
                        pass
        xbmc.executebuiltin("Container.SetViewMode(500)")

def SEARCH_OASE(url):
        kb = xbmc.Keyboard('', 'Search Stream-oase.tv', False)
        kb.doModal()
        search = kb.getText()
        br = mechanize.Browser()
        br.open(url)
        br.select_form("hsearch")
        br["avssearch"] = search
        response = br.submit()
        link = response.read()
        response.close()
        soup = BS(link)
        value=[]
        for div in soup.find('div',  {"class": "sp-component-area-inner clearfix"},smartQuotesTo=None).findAll('div',  {"class": "avs_thumb"},smartQuotesTo=None):
            url= div.find('a')['href']
            # print url
            img= div.find('img').findNext('img')['src']
            name= div.find('span').find(text=True)
            name=name.encode('utf8')
            try:
                fanart = get_fanart(name)
            except:
                fanart = ''
            value.append((url, img, name, fanart))
        for url1,thumbnail,name, fanart in value:
            try:
                    addDir(name,url1,5,thumbnail,fanart,'','','','','','')
            except:
                    addDir(name,url1,5,thumbnail,'','','','','','','')
        xbmc.executebuiltin("Container.SetViewMode(500)")

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
        
def PLAY_SEARCH(url,name,iconimage,fanart):
        nuna='http://stream-oase.tv'+url
        link=get_url(nuna)
        match=re.compile('<iframe src="(.*?)embed-(.*?)-.*?.html" frameborder=', re.I).findall(link)
        match2=re.compile('<iframe src="(.*?)" frameborder=', re.I).findall(link)
        for hoster, code in match:
                if 'vidplay' in hoster:
                    ref = re.search('http://(.*?)/.*?',hoster).group(1)
                    ref = ref.replace("www.", '').replace(".com",'').replace(".net",'')
                    try:
                        addDir(name+'[CR][I]'+ref+'[/I]',str(hoster)+str(code),10,iconimage,fanart,'','','','','','')
                    except:
                        addDir(name+'[CR][I]'+ref+'[/I]',str(hoster)+str(code),10,iconimage,'','','','','','','')
        for src in match2:
            if 'mightyupload' in src:
                    try:
                            ref = re.search('http://(.*?)/',src).group(1)
                            ref = ref.replace("www.", '').replace(".com",'').replace(".net",'')
                            try:
                                addDir(name+'[CR][I]'+ref+'[/I]',str(src),10,iconimage,fanart,'','','','','','')
                            except:
                                addDir(name+'[CR][I]'+ref+'[/I]',str(src),10,iconimage,'','','','','','','')
                    except:
                            pass
            if 'vk.com' in src:
                    try:
                            ref = re.search('http://(.*?)/.*?$',src).group(1)
                            try:
                                addDir(name+'[CR][I]'+ref+'[/I]',str(src.replace("&amp;","&")),10,iconimage,fanart,'','','','','','')
                            except:
                                addDir(name+'[CR][I]'+ref+'[/I]',str(src.replace("&amp;","&")),10,iconimage,'','','','','','','')
                    except:
                            pass    

def hoster(link):
        if 'vk.com'in link:
            host='[CR][I]VK[/I]'
        elif 'mightyupload' in link:
            host='[CR][I]Mightyupload[/I]'
        elif '180upload' in link:
            host='[CR][I]180upload[/I]'
        elif 'hugefiles' in link:
            host='[CR][I]Hugefiles[/I]'
        else:
            host = 'unbekannt'
        return host

def PLAYLINK_OASE(url,name,iconimage,fanart,imdb,darsteller,plot,fsk,code,trailer):
        url1 = url.split(';')
        # print str(url1)
        for link in url1:
            try:
                # print 'BENIM : '+link
                ref = re.search('http://(.*?)/.*?',link).group(1)
                ref = ref.replace("www.", '').replace(".com",'').replace(".net",'')
                # print ref
                try:
                    if trailer == 'None' and plot == 'None':
                        addDir(name+'[CR][I]'+ref+'[/I]',str(link),10,iconimage,fanart,imdb,darsteller,'',fsk,code,'')
                    else:
                        addDir(name+'[CR][I]'+ref+'[/I]',str(link),10,iconimage,fanart,imdb,darsteller,plot,fsk,code,trailer)
                except:
                    addDir(name+'[CR][I]'+ref+'[/I]',str(link),10,iconimage,'','','','','','','')
            except:
                    pass

def SERIE_INDEX(url):
        bro=br()
        link=bro.open(url)
        ser_idx=link.read()
        soup = BS(ser_idx)
        if 'serien' in url:
            for td in soup.find('table',  {"class": "category"},smartQuotesTo=None).findAll('td',  {"class": "list-title"},smartQuotesTo=None):
                url= td.find('a')['href']
                name = (td.find('a').find(text=True)).encode('utf-8')            
                addDir(name,url,2,'','','','','','','','')
            for page in soup.find('div', {"class": "pagination"},smartQuotesTo=None).findAll('li'):
                try:
                    url1 = page.find('a')['href']
                    name1 = page.find('a').text
                    addDir(name1,url1,1,'','','','','','','','')
                except:
                        pass
        elif 'cartoon' in url:
            for td in soup.find('table',  {"class": "category"},smartQuotesTo=None).findAll('td',  {"class": "list-title"},smartQuotesTo=None):
                url= td.find('a')['href']
                url2 = "http://stream-oase.tv"+url
                name = (td.find('a').find(text=True)).encode('utf-8').replace("\n","")          
                addDir(str(name),url2,8,'','','','','','','','')
            for page in soup.find('div', {"class": "pagination"},smartQuotesTo=None).findAll('li'):
                try:
                    url1 = page.find('a')['href']
                    name1 = page.find('a').text
                    addDir(name1,url1,1,'','','','','','','','')
                except:
                        pass
        xbmc.executebuiltin("Container.SetViewMode(300)")
                    
            
def SERIE_STAFF(url):
        bro=br()
        url1 = "http://stream-oase.tv"+url
        link=bro.open(url1)
        ser_staff=link.read()
        try:
            match = re.compile('<option value="(.*?)">(.*?)</option>').findall(ser_staff)
        except:
                pass
        if match:
            for url,name in match:
                addDir(name,url,3,'','','','','','','','')
        else:
            SERIE_EPI(url)
        xbmc.executebuiltin("Container.SetViewMode(300)")
            
            
def SERIE_EPI(url):
        bro=br()
        if "http://" in url:
            link=bro.open(url)
        else:
            link=bro.open("http://stream-oase.tv"+str(url))
        ser_episodes = link.read()
        match = re.compile('<iframe src="(.*?)" frameborder="0" scrolling="no" width=".*?" height=".*?">').findall(ser_episodes)
        for embed in match:
            html = net.http_GET(embed).content
            name = (re.search('<title>(.*?)</title>',html).group(1)).replace("SockShare - ", "").replace("PutLocker - ","").replace("VideoSlasher - ","").replace(".mkv","").replace(".avi","")
            if name !="":
                addDir(str(name),embed,7,'','','','','','','','')
            else:
                addDir("Folge ist gelöscht".decode('latin1').encode('utf-8'),link,3,'','','','','','','','')
        xbmc.executebuiltin("Container.SetViewMode(300)")

    
def PLAY_SERIE(url,name):
        video = resolve_Putlocker(url)
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        addLink(str(name),str(video),'','','','','','','')
        listitem = xbmcgui.ListItem(str(name),thumbnailImage='')
        listitem.setInfo('video', {'name': str(name) } )
        xbmc.PlayList(1).add(video, listitem)
        
def CARTOON_play(name,url):
        bro = br()
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        link = bro.open(url)
        video_lnk = link.read()
        try:
            match_url = re.search('"(http://www.sockshare.com.*?)"',video_lnk).group(1)
        except:
                pass
        video = resolve_Putlocker(match_url)
        addLink(str(name),str(video),'','','','','','','')
        listitem = xbmcgui.ListItem(name, iconImage="", thumbnailImage="")
        listitem.setInfo('video', {'name': str(name) } )
        xbmc.PlayList(1).add(video, listitem=listitem)
        xbmc.Player().play(pl)

def LIVE_STREAMS(url):
        livestreams = [{"Name":"KNALLFROSCH", "Code":"5268f5ceede77"},{"Name":"NANOs Movies","Code":"52076e41a102c"},{"Name":"ZOOCOMPANY", "Code":"519442ebaa08c"},{"Name":"Deutsches Kino1", "Code":"51c8c89aceebd"},{"Name":"LoseBoss Movie World", "Code":"520d2a118e702"},{"Name":"END78", "Code":"5268377e7c106"},{"Name":"j2Ps HD", "Code":"5283d6b24c307"},{"Name":"j2Ps Movies & Series 24/7", "Code":"50f85d9b9b14c"},{"Name":"DHunters Movies", "Code":"5168332337333"},{"Name":"SGSII Movies World", "Code":"519386d85e8e4"},{"Name":"::: EDELS Movies :::", "Code":"50ffb17983d40"},{"Name":"FunTV Movies", "Code":"50ffb17983d40"},{"Name":"Serie Supernaturals", "Code":"52613245eef83"},{"Name":"Serie Taahm", "Code":"50ffb17983d40"},{"Name":"How I Met Your Mother", "Code":"5230ca2d942e4"},{"Name":"Walking Dead HD", "Code":"5229e7fb51985"},{"Name":"Falling Skies HD", "Code":"52486ddfccbad"},{"Name":"Big Bang Theory", "Code":"524872e3b30e8"},{"Name":"Desperate Housewives", "Code":"524c82c57cb6f"},{"Name":"Die Wilder Siebziger", "Code":"5256d66eb124c"}]
        for i in livestreams:
            try:
                link = get_stream_url(i['Code'])
                addLink(i['Name'],link,'','','','','','','')
            except:
                print i['Name']
        
def br():
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1)"
        " Gecko/20100101 Firefox/10.0.1"
        __settings__ = xbmcaddon.Addon(id="plugin.video.Stream-Oase.tv")
        login= __settings__.getSetting("login")
        password= __settings__.getSetting("password")
        url_start='http://stream-oase.tv/'
        if not login:
                __settings__.openSettings()
        else:
                pass
        br = mechanize.Browser()
        br.set_handle_robots( False )
        br.addheaders = [('User-agent', 'Firefox')]
        br.open(url_start)
        br.select_form(nr=0)
        br["username"] = str(login)
        br["password"] = str(password)
        br["remember"] = ["yes",]
        response1 = br.submit()
        fc = response1.read()
        # print fc
        if str(login.lower()) in str(fc.lower()):
            print "Succesfully Loged in."
        else:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('LOGIN-ERROR','[B]                Benutzername oder Passwort falsch!!![/B]')
            __settings__.openSettings()
            br()

        return br
        
def get_ajax_json(url):
        response = urllib2.urlopen(url)
        print 'getting: ' + url
        try:
            stream_json = json.loads(response.read())    
        except ValueError, error_info:
            stream_json = {'success': False, 'payload': str(error_info)}
        if stream_json['success']:
            return stream_json['payload']
        else:
            print 'Problem getting info from: ' + url
            print 'Error returned: '+ stream_json['payload']
            return False  

def get_stream_url(channel_id):
        BASE_URL = 'http://www.veetle.com'
        CHANNEL_LISTING = BASE_URL + '/channel-listing-cross-site.js'
        return get_ajax_json(BASE_URL + '/index.php/channel/ajaxStreamLocation/' + 
                         str(channel_id) + '/flash')        
        
def resolve_mightyupload(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html=response.read()
        file = re.search('file:.*?\'(.*?)\',',html,re.DOTALL)
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        try:
                addLink(name,file.group(1),iconimage,str(fanart),imdb,darsteller,plot,fsk,code)
                listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
                url = file.group(1)
                xbmc.PlayList(1).add(url, listitem)
                xbmc.Player().play(pl)
        except Exception, e:
            dialog = xbmcgui.DialogProgress()
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')
            print '**** mightyupload Error occured: %s' % e
            raise
            
def resolve_180upload(name1,url,iconimage,fanart,imdb,darsteller,plot,fsk,code):
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        try:
            dialog = xbmcgui.DialogProgress()
            if '180upload' in url:
                dialog.create('Resolving', 'Resolving 180Upload Link...')
            else:
                dialog.create('Resolving', 'Resolving vidplay Link...')
            dialog.update(0)
            puzzle_img = os.path.join(datapath, "180_puzzle.png")
            
            print '180Upload - Requesting GET URL: %s' % url
            html = net.http_GET(url).content

            dialog.update(50)
                    
            data = {}
            r = re.findall(r'type="hidden" name="(.+?)" value="(.+?)">', html)

            if r:
                for name, value in r:
                    data[name] = value
            else:
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')
            
            #Check for SolveMedia Captcha image
            solvemedia = re.search('<iframe src="(http://api.solvemedia.com.+?)"', html)

            if solvemedia:
                dialog.close()
                html = net.http_GET(solvemedia.group(1)).content
                hugekey=re.search('id="adcopy_challenge" value="(.+?)">', html).group(1)
                open(puzzle_img, 'wb').write(net.http_GET("http://api.solvemedia.com%s" % re.search('<img src="(.+?)"', html).group(1)).content)
                img = xbmcgui.ControlImage(450,15,400,130, puzzle_img)
                wdlg = xbmcgui.WindowDialog()
                wdlg.addControl(img)
                wdlg.show()
            
                xbmc.sleep(3000)

                kb = xbmc.Keyboard('', 'Type the letters in the image', False)
                kb.doModal()
                capcode = kb.getText()
       
                if (kb.isConfirmed()):
                    userInput = kb.getText()
                    if userInput != '':
                        solution = kb.getText()
                    elif userInput == '':
                        Notify('big', 'No text entered', 'You must enter text in the image to access video', '')
                        return False
                else:
                    return False
                   
                wdlg.close()
                if '180upload' in url:
                    dialog.create('Resolving', 'Resolving 180Upload Link...')
                else:
                    dialog.create('Resolving', 'Resolving vidplay Link...')
                dialog.update(50)
                if solution:
                    data.update({'adcopy_challenge': hugekey,'adcopy_response': solution})

            print '180Upload - Requesting POST URL: %s' % url
            html = net.http_POST(url, data).content
            dialog.update(100)
            if '180upload'in url:
                link = re.search('<a href="(.+?)" onclick="thanks\(\)">Download now!</a>', html)
            else:
                link = re.search('href="(.*?)" title="Direct download the file"', html)
            link = link.group(1)
            link = link.replace(" ", "_")
            if link:
                print '180Upload Link Found: %s' % link.encode('utf8')
                addLink(name1,link,iconimage,str(fanart),imdb,darsteller,plot,fsk,code)
                listitem = xbmcgui.ListItem(name1,thumbnailImage=iconimage)
                url = link
                print ("film LINKI : )",url)
                xbmc.PlayList(1).add(url, listitem)
                xbmc.Player().play(pl)
            else:
                raise Exception('Unable to resolve 180Upload Link')

        except Exception, e:
            print '**** 180Upload Error occured: %s' % e
            raise
        finally:
            dialog.close()
            
def resolve_vidhog(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code):
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        try:
            dialog = xbmcgui.DialogProgress()
            dialog.create('Resolving', 'Resolving VidHog Link...')
            dialog.update(0)
            
            print 'VidHog - Requesting GET URL: %s' % url
            html = net.http_GET(url).content

            dialog.update(50)
            if re.search('This server is in maintenance mode', html):
                print '***** VidHog - Site reported maintenance mode'
                raise Exception('File is currently unavailable on the host')
            if re.search('<b>File Not Found</b>', html):
                print '***** VidHog - File not found'
                raise Exception('File has been deleted')

            filename = re.search('<strong>\(<font color="red">(.+?)</font>\)</strong><br><br>', html).group(1)
            extension = re.search('(\.[^\.]*$)', filename).group(1)
            guid = re.search('http://vidhog.com/(.+)$', url).group(1)
            
            vid_embed_url = 'http://vidhog.com/vidembed-%s%s' % (guid, extension)
            
            request = urllib2.Request(vid_embed_url)
            request.add_header('User-Agent', USER_AGENT)
            request.add_header('Referer', url)
            response = urllib2.urlopen(request)
            redirect_url = re.search('(http://.+?)video', response.geturl()).group(1)
            download_link = redirect_url + filename
            
            dialog.update(100)

            dialog.close()
            addLink(name,download_link,iconimage,fanart,imdb,darsteller,plot,fsk,code)
            listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
            url = download_link
            print ("film LINKI : )",url)
            xbmc.PlayList(1).add(url, listitem)
            xbmc.Player().play(pl)
            
        except Exception, e:
            dialog1 = xbmcgui.Dialog()
            dialog1.ok('error','[UPPERCASE][B]                Sorry but the video is deleted!!![/B][/UPPERCASE]')

def resolve_Putlocker(url):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('Referer',url),
                ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1') ]
        if 'embed' in url:
            if 'videoslasher' in url:
                url = url.replace("embed", "video")
            url = url.replace("embed", "file")
        else:
            pass
        try:
            html = net.http_GET(url).content
        except urllib2.URLError, e:
            xbmc.executebuiltin('Notification("1","2")')
            return False
        if not'videoslasher' in url:
            try:
                r = re.search('value="([0-9a-f]+?)" name="hash"', html)
            except:
                pass
        else:
            try:
                r = re.search('input type="hidden" value="(.*?)" name="foo"', html)
            except:
                pass
        if r:
            session_hash = r.group(1)
        else:
            xbmc.executebuiltin('Notification("1","3")')
            return False
        if not'videoslasher' in url:
            try:
                html = net.http_POST(url, form_data={'hash': session_hash, 
                                                               'confirm': 'Continue as Free User'}).content
            except urllib2.URLError, e:
                xbmc.executebuiltin('Notification("1","4")')
        else:
            try:
                html = opener.open(url,urllib.urlencode({'foo': 'bar','confirm': 'Continue as Free User'})).read()
            except:
                pass 
        r = re.search("key: '\#\$0c4de(.*?)'", html)
        player_key = ""
        if not'videoslasher' in url:
            r = re.search('\?stream=(.+?)\'', html)
        else:
            r = re.search('/playlist/(.+?)\'', html)
        if not'videoslasher' in url:
            if r:
                playlist_code = r.group(1)
            else:
                r = re.search('key=(.+?)&',html)
                playlist_code = r.group(1)
        else:
            if r:
                playlist_code = r.group(1)
            else:
                r = re.search('/playlist/(.*?)',html)
                playlist_code = r.group(1)
        if not'videoslasher' in url:
            xml_url = re.sub('/(file|embed)/.+', '/get_file.php?stream=', url)
        else:
            xml_url = re.sub('/(video|embed)/.+', '/playlist/', url)
        xml_url += playlist_code
        try:
            html = opener.open(xml_url).read()
        except urllib2.URLError, e:
            xbmc.executebuiltin('Notification("1","5")')
            return False
        # print html
        if not'videoslasher' in url:
            r = re.search('url="(.+?)"', html)
        else:
            r = re.search('Video</title>.*?url="(.+?)(\?|\/)(.+?)"', html)
        cookies = []
        for cookie in cj:
          cookies.append((cookie.name,cookie.value))
        if 'videoslasher' in url:
            if r:
                flv_url = r.group(1) + r.group(2) + r.group(3)
                if 'videoslasher' in url:
                  flv_url=flv_url+"|Host="+urllib.quote(r.group(1))+"&User-Agent="+urllib.quote("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0")+"&Accept="+urllib.quote("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")+"&Accept-Language="+urllib.quote("en-US,en;q=0.5")+"&Accept-Encoding="+urllib.quote("gzip, deflate")+'&Connection='+urllib.quote("keep-alive")+'&Referer='+urllib.quote("http://www.videoslasher.com/static/player/flowplayer.commercial-3.2.7.swf")+"&Cookie="+urllib.quote("__utma=95369115.1962767463.1353956692.1355571129.1355639190.6; __utmz=95369115.1355639190.6.4.utmcsr=gozlan.me|utmccn=(referral)|utmcmd=referral|utmcct=/play/4375/2012--%D7%A2%D7%99%D7%93%D7%9F-%D7%94%D7%A7%D7%A8%D7%97-%D7%9C%D7%A6%D7%A4%D7%99%D7%99%D7%94-%D7%99%D7%A9%D7%99%D7%A8%D7%94-3533.html; __utmb=95369115.6.10.1355639190; __utmc=95369115; authsid=sr2ac9bunt46fieitfj79sg611")
                else:
                   flv_url = flv_url + '|Accept='+urllib.quote('text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')+'&User-Agent=' + urllib.quote('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1')+'&Accept-Encoding='+urllib.quote('gzip, deflate')+'&Cookie='+urllib.quote('__utma=163708862.388085895.1342125893.1344639465.1344641726.10; __utmz=163708862.1344634373.8.8.utmcsr=gozlan.me|utmccn=(referral)|utmcmd=referral|utmcct='+urllib.quote(web_url)+'; __utmb=163708862.15.10.1344641726; __utmc=163708862') + '&Connection=' +urllib.quote('Keep-Alive')
                   if player_key!="":
                     flv_url=flv_url+"&Referer="+urllib.quote('http://static.putlocker.com/video_player.swf?0.'+player_key)
        else:
            if r:
                try:
                    flv_url = (r.group(1)).replace('&amp;','&')
                except:
                    pass
            else:
                xbmc.executebuiltin('Notification("1","6")')
                return False
        
        return str(flv_url)

def resolve_VK(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code):
        hd = re.search('.*?(hd=\d)$',url).group(1)
        url1 = url.replace(hd,"hd=3")
        print url1
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        liste=[]
        fixed=''
        gecis=0
        link=get_url(url1)
        host=re.compile("host=([^\&]+)").findall(link)
        uid=re.compile("uid=([^\&]+)").findall(link)
        vtag=re.compile("vtag=([^\&]+)").findall(link)
        hd = re.compile("hd_def=([^\&]+)").findall(link)
        if not hd or hd[0]=="-1":
            hd = re.compile("hd=([^\&]+)").findall(link)
        flv = re.compile("no_flv=([^\&]+)").findall(link)
        vkstream='%su%s/videos/%s' % (host[0],uid[0],vtag[0])
        x=(int(hd[0])+1)
        if hd >0 or flv == 1:
                for i in range (x):
                        streamkalite = ["240", "360", "480", "720", "1080"] 
                        i=streamkalite[i]+' p'
                        liste.append(i) 
                if gecis==0:
                        dialog = xbmcgui.Dialog()
                        ret = dialog.select('kalite secin...',liste)
                        for i in range (x):
                                if ret == i:
                                        url=vkstream+'.'+str(streamkalite[i])+'.mp4'
                                        fixed=str(streamkalite[i])
                                else:
                                        pass
                else:
                        url=vkstream+'.'+fixed+'.mp4'
                addLink(name,url,iconimage,str(fanart),imdb,darsteller,plot,fsk,code)
                listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
                xbmc.PlayList(1).add(url, listitem)
                xbmc.Player().play(pl)
  
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
        
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

def addLink(name,url,iconimage,fanart,imdb,darsteller1,plot,fsk,code):
        ok=True
        try:
            if '|' in darsteller1:
                darsteller = darsteller1.split('|',10)
            else:
                darsteller = darsteller1.split(',',10)
        except:
                darsteller = ''
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Rating": imdb, "Plot": plot, "MPAA": fsk, "Cast": darsteller, "Code": code } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage,fanart,imdb,darsteller1,plot,fsk,code,trailer):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&imdb="+urllib.quote_plus(imdb)+"&fsk="+urllib.quote_plus(fsk)+"&darsteller="+urllib.quote_plus(darsteller1)+"&plot="+urllib.quote_plus(str(plot))+"&code="+urllib.quote_plus(code)+"&trailer="+urllib.quote_plus(trailer)
        ok=True
        if '|' in darsteller1:
            darsteller = darsteller1.split('|',10)
        else:
            darsteller = darsteller1.split(',',10)
        die = "[B]Darsteller : "+str(darsteller1)+"[/B]\n\n"+str(plot)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=str(iconimage))
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Rating": imdb, "Plot": die, "MPAA": fsk, "Cast": darsteller, "Code": code, "Trailer": trailer } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

params=get_params()
url=None
name=None
mode=None
iconimage=None
imdb=None
plot=None
fanart=None
darsteller=None
fsk=None
code=None
trailer=None

try:
        url=urllib.unquote_plus(params['url'])
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
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        fanart=urllib.unquote_plus(params["fanart"])
except:
        fanart='keine Angabe'
try:
        imdb=urllib.unquote_plus(params["imdb"])
except:
        imdb = '0.0'
try:
        plot=urllib.unquote_plus(params["plot"])
except:
        pass
try:
        darsteller=urllib.unquote_plus(params["darsteller"])
except:
        darsteller='keine Angabe'
try:
        fsk=urllib.unquote_plus(params["fsk"])
except:
        fsk = 'keine Angabe'
try:
        code=urllib.unquote_plus(params["code"])
except:
        pass
try:
        trailer=urllib.unquote_plus(params["trailer"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Trailer: "+str(trailer)
print "IMDB: "+str(imdb)
print "PLOT: "+str(plot)
print "DARSTELLER: "+str(darsteller)
print "FANART: "+str(fanart)
print "CODE :"+str(code)
print "FSK: "+str(fsk)
print "TRAILER: "+str(trailer)

if mode==None or url==None or len(url)<1:
        print ""
        for i in imps:
            __settings__.setSetting(i,"false")
        url = 'http://stream-oase.tv/index.php/hd-oase'
        INDEX_OASE(url)
        
elif mode==1:
        SERIE_INDEX(url)

elif mode==2:
        SERIE_STAFF(url)
        
elif mode==3:
        SERIE_EPI(url)
        
elif mode==4:
        PLAYLINK_OASE(url,name,iconimage,fanart,imdb,darsteller,plot,fsk,code,str(trailer))
        
elif mode==5:
        print fanart
        PLAY_SEARCH(url,name,iconimage,fanart)
        
elif mode==6:
        if url !=None:
            VIDEOLINKS_OASE(name,url,code,plot)
        else:
            VIDEOLINKS_OASE(name,'',code,plot)
            
elif mode==7:
        PLAY_SERIE(url,name)
        
elif mode==8:
        CARTOON_play(name,url)
        
elif mode==9:
        LIVE_STREAMS(url)
        
elif mode==10:
        if 'vidhog' in url:
            resolve_vidhog(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code)
        elif 'mightyupload' in url:
            resolve_mightyupload(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code)
        elif 'vk.com' in url:
            resolve_VK(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code)
        else:
            resolve_180upload(name,url,iconimage,fanart,imdb,darsteller,plot,fsk,code)

elif mode==11:
        AKTUALISIEREN(url)
        
elif mode==16:
        SEARCH_OASE(url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
