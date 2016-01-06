# Evonic plugin written by Mentality
# -*- coding: utf-8 -*-
import re,os,urllib,urllib2
import xbmcplugin,xbmcgui
import xbmcaddon
import evonic as enter
from BeautifulSoup import BeautifulSoup as BS

__settings__ = xbmcaddon.Addon(id="plugin.video.Evonic")
status = __settings__.getSetting("status")           

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

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

params=get_params()
url=None
url0=None
name=None
mode=None
iconimage=None
imdb=None
plot=None
mpaa=None
trailer=None

try:
        url=urllib.unquote_plus(params['url'])
except:
        pass
try:
        url0=urllib.unquote_plus(params['url0'])
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
        imdb=urllib.unquote_plus(params["imdb"])
except:
        pass
try:
        plot=urllib.unquote_plus(params["plot"])
except:
        pass
try:
        mpaa=urllib.unquote_plus(params["mpaa"])
except:
        pass
try:
        mpaa=urllib.unquote_plus(params["mpaa"])
except:
        pass
        
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        enter.INDEX_GENRE("http://evonic.tv/forum/content.php")
       
elif mode==1:
        
        enter.play_free_video(url,name,str(iconimage),imdb,mpaa)
        
elif mode==2:
        
        enter.SEARCH(url)

elif mode==3:
        
        enter.play_premium_video(url,name,str(iconimage),imdb,mpaa) 

elif mode==4:
        
        enter.INDEX_GENRE(url)

elif mode==5:
        
        enter.INDEX(url,name)

elif mode==6:
        
        enter.VIDEOLINKS(url,name,iconimage,imdb,trailer)

elif mode==7:
        
        enter.LINKS_COLLECTIONS(url)
        
elif mode==8:
        
        enter.INDEX_CENTURY(url)

elif mode==9:
        
        enter.STAFFEL(url)
        
elif mode==10:
        
        enter.HD_GENRES(url)
        
elif mode==11:
        
        enter.INDEX_IMDB(url)

elif mode==12:
        enter.play_trailer(url,name,iconimage)
        
elif mode==13:
        
        enter.MANAGE_SEARCH(url,name)
# elif mode==14:
        # from metahandler import metahandlers
        # metahandlers.display_settings()
        
elif mode==101:
			enter.PLAY_VID(url,iconimage,name)
		
elif mode==100:
		  enter.LIBRARY_MOVIE(name,url,iconimage)
		
elif mode==102:
		  enter.LIBRARY_SERIE(name,url,iconimage)
		  
xbmcplugin.endOfDirectory(int(sys.argv[1]))
