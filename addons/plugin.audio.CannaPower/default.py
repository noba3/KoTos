# -*- coding: utf-8 -*-

import urllib,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import resources.lib.mechanize as mechanize

pluginhandle = int(sys.argv[1])
addon = xbmcaddon.Addon(id='plugin.audio.CannaPower')
home = addon.getAddonInfo('path').decode('utf-8')
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
iconpath = xbmc.translatePath(home+"/resources/icon/")


def CATEGORIES():
        addDir('DE Single Jahrescharts von 1930 bis heute',"http://ua.canna.to/canna/jahrescharts.php",4,iconpath+'jc_1930.png')
        addDir('verschiedene Jahrescharts - Black/Dance/Party/AT/CH',"http://ua.canna.to/canna/austria.php",2,iconpath+'me_mixed.png')
        addDir('aktuelle Charts aus versch. Laendern und Musikrichtungen',"http://ua.canna.to/canna/single.php",1,iconpath+'me_aktuell.png')

def Charts():
        addDir('TOP100 Single Charts',"http://ua.canna.to/canna/single.php",3,iconpath+'ac_single.png')
        addDir('Austria Single Charts',"http://ua.canna.to/canna/austria.php",3,iconpath+'ac_austria.png')
        addDir('Black Charts Top 40',"http://ua.canna.to/canna/black.php ",3,iconpath+'ac_black.png')
        addDir('US Billboard Country Charts Top 30',"http://ua.canna.to/canna/country.php",3,iconpath+'ac_uscountry.png')
        addDir('Offizielle Dance Charts Top 50',"http://ua.canna.to/canna/odc.php",3,iconpath+'ac_dance.png')
        addDir('Party Schlager Charts Top 30',"http://ua.canna.to/canna/psc.php",3,iconpath+'ac_party.png')
        addDir('Reggae Charts Top 20',"http://ua.canna.to/canna/reggae.php",3,iconpath+'ac_reggae.png')
        addDir('Rock & Metal Single Charts Top 40',"http://ua.canna.to/canna/metalsingle.php",3,iconpath+'ac_rockmetall.png')
        addDir('Swiss Single Charts Top 75',"http://ua.canna.to/canna/swiss.php",3,iconpath+'ac_swiss.png')
        addDir('UK Single Charts Top 40',"http://ua.canna.to/canna/uksingle.php",3,iconpath+'ac_uksingle.png')
        addDir('US Billboard Single Charts Top 100',"http://ua.canna.to/canna/ussingle.php",3,iconpath+'ac_ussingle.png')
              
def Jahrescharts():
        # addDir('Single Jahrescharts',"http://ua.canna.to/canna/jahrescharts.php",4,icon)
        addDir('Black Jahrescharts',"http://ua.canna.to/canna/blackjahrescharts.php",4,iconpath+'jc_black.png')
        addDir('Dance Jahrescharts',"http://ua.canna.to/canna/dancejahrescharts.php",4,iconpath+'jc_dance.png')
        addDir('Party Schlager Jahrescharts',"http://ua.canna.to/canna/partyjahrescharts.php",4,iconpath+'jc_party.png')
        addDir('Swiss Jahrescharts',"http://ua.canna.to/canna/swissjahrescharts.php",4,iconpath+'jc_swiss.png')
        addDir('Austria Jahrescharts',"http://ua.canna.to/canna/austriajahrescharts.php",4,iconpath+'jc_austria.png')
		
def Index(url):
        mainurl='http://ua.canna.to/canna/'
        req = mechanize.Request(url)
        req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = mechanize.urlopen(req)
        link=response.read().replace('\n', '')
        response.close()
        match=re.findall('<tr>.*?<font>(.*?)</font>.*?class="obutton" onClick="window.open..(.*?)...CannaPowerChartsPlayer.*?</tr>', link)
        for title,url in match:
          url=mainurl+url
          print url
          print title
          title = title.replace(":", "-")
          addLink(title,url,6,icon)
		#xbmcplugin.endOfDirectory(pluginhandle)

def Index1(url):
        if 'jahrescharts' in url:
            icon = iconpath+'jc_1930.png'
        mainurl='http://ua.canna.to/canna/'
        req = mechanize.Request(url)
        req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = mechanize.urlopen(req)
        link=response.read().replace('\n', '')
        response.close()
        match=re.compile('<b><font face="Arial" size="5" color="#FFCC00"><a href="(.*?)">(.*?)</a></font></b>').findall(link)
        for url, title in match:
          url=mainurl+url
          print url
          print title
          title = title.replace(":", "-")
          addDir(title,url,5,icon)		

def jahre(url):
     	mainurl='http://ua.canna.to/canna/'
        req = mechanize.Request(url)
        req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = mechanize.urlopen(req)
        link=response.read().replace('\n', '')
        response.close()
        match=re.compile('<td align="left" style="border-style:solid; border-width:1px;">.*?<b>(.*?)</b>.*?<b>(.*?)</b>.*?onClick="window.open..(.*?)...CannaPowerChartsPlayer.*?</span>').findall(link)
        for title1,title2,url in match:
          url=mainurl+url
          title=title1+' '+':'+' '+title2
          title = title.replace(":", "-")
          addLink(title,url,6,icon)		  
		
def VIDEOLINKS(url):
        content = getUrl(url)
        match=re.findall('flashvars.playlist = \'(.*?)\';', content)
        for url in match:
          url='http://ua.canna.to/canna/'+url
          content = getUrl(url)
          match=re.findall('<location>(.*?)</location>', content)
          for url in match:
            url='http://ua.canna.to/canna/'+url
            req = mechanize.Request('http://ua.canna.to/canna/single.php')
            response = mechanize.urlopen(req)
            req = mechanize.Request(url)
            req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = mechanize.urlopen(req)
            response.close()
            code=response.info().getheader('Content-Location')
            url='http://ua.canna.to/canna/avzt/'+code
            print url
            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            listitem = xbmcgui.ListItem(path=url)
            return xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)    

def getUrl(url):
        req = mechanize.Request(url)
        req.add_header('User-Agent', ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = mechanize.urlopen(req)
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

def addLink(name,url,mode,iconimage):
        name = name.replace(":", "-").replace("&quot;","")
        name = name.replace("&auml;","ae").replace("&ouml;","oe").replace("&uuml;","ue").replace("&Auml;","Ae").replace("&Ouml;","Oe").replace("&Uuml;","Ue").replace("&oslash;","o").replace("&szlig;","ss")
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Music", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        name = name.replace(":", "-").replace("&quot;","")
        name = name.replace("&auml;","ae").replace("&ouml;","oe").replace("&uuml;","ue").replace("&Auml;","Ae").replace("&Ouml;","Oe").replace("&Uuml;","Ue").replace("&oslash;","o").replace("&szlig;","ss")
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

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

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()

elif mode==1:
        print ""+url
        Charts()
elif mode==2:
        print ""+url
        Jahrescharts()		

elif mode==3:
        print ""+url
        Index(url)
		
elif mode==4:
        print ""+url
        Index1(url)

elif mode==5:
        print ""+url
        jahre(url)		
        
elif mode==6:
        print ""+url
        VIDEOLINKS(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
