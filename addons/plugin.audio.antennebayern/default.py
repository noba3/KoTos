# -*- coding: cp1254 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys
icondir = xbmc.translatePath("special://home/addons/plugin.audio.antennebayern/icons/")
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

add_video_item('http://mp3channels.webradio.antenne.de/antenne',{ 'title': 'Antenne Bayern'},img=icondir + 'ab_antennebayern.png')
add_video_item('http://mp3channels.webradio.antenne.de/oldies-but-goldies',{ 'title': 'Oldies but Goldies'},img=icondir + 'ab_oldies.png')
add_video_item('http://mp3channels.webradio.antenne.de/chillout',{ 'title': 'Chillout'},img=icondir + 'ab_chillout.png')
add_video_item('http://mp3channels.webradio.antenne.de/das-schlager-karussell',{ 'title': 'Schlagersahne'},img=icondir + 'ab_schlagersahne.png')
add_video_item('http://mp3channels.webradio.antenne.de/hits-fuer-kids',{ 'title': 'Hits für Kids'},img=icondir + 'ab_hitskids.png')
add_video_item('http://mp3channels.webradio.antenne.de/top-40',{ 'title': 'Top 40'},img=icondir + 'ab_top40.png')
add_video_item('http://mp3channels.webradio.antenne.de/lovesongs',{ 'title': 'Lovesongs'},img=icondir + 'ab_lovesongs.png')
add_video_item('http://mp3channels.webradio.antenne.de/black-beatz',{ 'title': 'Black Beatz'},img=icondir + 'ab_blackbeatz.png')
add_video_item('http://mp3channels.webradio.antenne.de/80er-kulthits',{ 'title': '80er Kulthits'},img=icondir + 'ab_80er.png')
add_video_item('http://mp3channels.webradio.antenne.de/classic-rock-live',{ 'title': 'Classic Rock Live'},img=icondir + 'ab_classicrock.png')
add_video_item('http://mp3channels.webradio.antenne.de/event',{ 'title': 'Das Antenne Bayern Event Radio'},img=icondir + 'ab_fussball.png')
add_video_item('http://mp3channels.webradio.rockantenne.de/rockantenne',{ 'title': 'ROCK ANTENNE'},img=icondir + 'ab_rockantenne.png')
add_video_item('http://mp3channels.webradio.rockantenne.de/rockantennelocal01',{ 'title': 'ROCK ANTENNE Erding / Freising / Ebersberg'},img=icondir + 'abra_local.png')
add_video_item('http://mp3channels.webradio.rockantenne.de/alternative',{ 'title': 'ROCK ANTENNE Alternative'},img=icondir + 'abra_alternativ.png')
add_video_item('http://mp3channels.webradio.rockantenne.de/heavy-metal',{ 'title': 'ROCK ANTENNE Heavy Metal'},img=icondir + 'abra_heavy.png')
add_video_item('http://mp3channels.webradio.rockantenne.de/classic-perlen',{ 'title': 'ROCK ANTENNE Classic Perlen'},img=icondir + 'abra_classic.png')

xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")