# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,xbmcaddon,xbmcvfs
import os,base64,araclar,cozucu,random

# -*- coding: iso-8859-9 -*-

__settings__ = xbmcaddon.Addon(id='plugin.video.tekosman')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))
sys.path.append(folders)


#!/usr/bin/python
# -*- coding: utf-8 -*-         #print ""+url
# Copyright (c) 2013
# Writer (c) 2013, xbmcTR Team by HappyFeets
# Turkiye, E-mail: androidmkersco@gmail.com

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

def CATEGORIES():
        addDir('[COLOR lightblue]<<< [COLOR orange]Onemli Bilgilendirme [COLOR lightblue]>>>[/COLOR]','INFO',2,"special://home/addons/plugin.video.tekosman/icon.png")
        addDir('[COLOR lightblue]<<< [COLOR yellow]Attention PLS [COLOR lightblue]>>>[/COLOR]','INFOO',3,"special://home/addons/plugin.video.tekosman/icon.png")
        addDir('[COLOR lightblue]<<< [COLOR beige]MagicTR [COLOR lightblue]>>>[/COLOR]','magictr()',4,"special://home/addons/plugin.video.dream-clup/resources/images/magictr.png")

def INFO(url):
  try:
        CATEGORIES()
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "[COLOR blue]PowerTV [/COLOR][COLOR yellow]KAPANMISTIR.[/COLOR] ","[COLOR pink]Dream Clup i veya MagicTR yi deneyiniz.[/COLOR]")
  except:
        
        pass

def INFOO(url):
  try:
        CATEGORIES()
        dialog = xbmcgui.Dialog()
        i = dialog.ok(url, "[COLOR blue]PowerTV [/COLOR][COLOR yellow]is NO LONGER  Avelable[/COLOR] ","[COLOR pink]You Should try Dream Club or MagicTR[/COLOR]")
  except:
        
        pass

from xbmcaddon import Addon
__YoutubePluginName__ = 'plugin.video.youtube'
__YoutubeAddon__ = Addon(__YoutubePluginName__)
youtubeVersion = __YoutubeAddon__.getAddonInfo('version')

def magictr():
        videolar = ['VrCMoBhVteI','R43eK2lkFtQ','AJYrwNbqIu0','2fzdxj7Zg7E']
        youtubeadres=random.choice(videolar)
        url='http://www.youtube.com/embed/'+str(youtubeadres).encode('utf-8', 'ignore')
        if youtubeVersion == "5":
            
            
            Youtube_Player(str(url))
        else:
            
            Youtube_Player2(str(url))


def Youtube_Player(url):
        playList.clear()   
        code=re.match(r"http://www.youtube.com/embed/(.*?)$", url).group(1)
        print '[code]'+str(code)
        url='plugin://plugin.video.youtube/play/?video_id=' + code
        name='MagicTR Reklam'
        araclar.addLink(name,url,'')
        araclar.playlist_yap(playList,name,url)
        xbmcPlayer.play(playList)


def Youtube_Player2(url):
        playList.clear()   
        code=re.match(r"http://www.youtube.com/embed/(.*?)$", url).group(1)
        print '[code]'+str(code)
        url='plugin://plugin.video.youtube/?action=play_video&videoid=' + code
        name='MagicTR Reklam'
        araclar.addLink(name,url,'')
        araclar.playlist_yap(playList,name,url)
        xbmcPlayer.play(playList)

#############################################
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

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
        CATEGORIES()

elif mode==2:
        INFO(url)

elif mode==3:
        INFOO(url)

elif mode==4:
        magictr()
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
