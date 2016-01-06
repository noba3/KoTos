import xbmcgui,xbmcplugin

plugin_handle = int(sys.argv[1])
_id = 'plugin.video.s.p.o.r.t'
_icondir = "special://home/addons/" + _id + "/icons/"

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

add_video_item('http://pebbles105-lh.akamaihd.net/i/eurosportde_1@97452/master.m3u8|X-Forwarded-For=195.186.145.47',{ 'title': 'Eurosport (DE)'}, '%s/es.png'% _icondir)
add_video_item('http://pebbles108-lh.akamaihd.net/i/sport1_1@97464/master.m3u8|X-Forwarded-For=195.186.145.47',{ 'title': 'Sport 1 (DE)'}, '%s/s1.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel1_800 live=1',{ 'title': 'SportTime TV 1 (DE)'}, '%s/st.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel2_800 live=1',{ 'title': 'SportTime TV 2 (DE)'}, '%s/st.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel3_800 live=1',{ 'title': 'SportTime TV 3 (DE)'}, '%s/st.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel4_800 live=1',{ 'title': 'SportTime TV 4 (DE)'}, '%s/st.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel5_800 live=1',{ 'title': 'SportTime TV 5 (DE)'}, '%s/st.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel6_800 live=1',{ 'title': 'SportTime TV 6 (DE)'}, '%s/st.png'% _icondir)
add_video_item('rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel7_800 live=1',{ 'title': 'SportTime TV 7 (DE)'}, '%s/st.png'% _icondir)

add_video_item('http://212.162.68.163/raisport+',{ 'title': 'Rai Sport1 (IT)'}, '%s/r1.png'% _icondir)
add_video_item('http://212.162.68.163/raisport2',{ 'title': 'Rai Sport2 (IT)'}, '%s/r2.png'% _icondir)

# add_video_item('http://202.75.23.37:1400/live/ch20/03.m3u8',{ 'title': 'Fight Sports (UK)'}, '%s/fight.png' % _icondir)
add_video_item('http://202.75.23.36:1400/live/ch44/03.m3u8',{ 'title': 'Setanta Sports (UK)'}, '%s/setana.png' % _icondir)
# add_video_item('http://202.75.23.37:1400/live/ch18/03.m3u8',{ 'title': 'Bein Sport 1 (UK)'}, '%s/bein.png' % _icondir)
# add_video_item('http://202.75.23.37:1400/live/ch19/03.m3u8',{ 'title': 'Bein Sport 2 (UK)'}, '%s/bein.png' % _icondir)
# add_video_item('http://202.75.23.37:1400/live/ch21/03.m3u8',{ 'title': 'EuroSport (UK)'}, '%s/es.png' % _icondir)
add_video_item('http://202.75.23.33:1400/live/ch26/03.m3u8',{ 'title': 'ASN Sport (UK)'}, '%s/asn.png' % _icondir)

add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12netw_delivery@132840/master.m3u8',{ 'title': 'PAC-12 Network (US)'}, '%s/pac12.png'% _icondir)
add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12ariz_delivery@132836/master.m3u8',{ 'title': 'PAC-12 Arizona (US)'}, '%s/pac12.png'% _icondir)
add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12baya_delivery@132837/master.m3u8',{ 'title': 'PAC-12 Bay Area (US)'}, '%s/pac12.png'% _icondir)
add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12losa_delivery@132838/master.m3u8',{ 'title': 'PAC-12 Los Angeles (US)'}, '%s/pac12.png'% _icondir)
add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12oreg_delivery@132835/master.m3u8',{ 'title': 'PAC-12 Oregon (US)'}, '%s/pac12.png'% _icondir)
add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12moun_delivery@132839/master.m3u8',{ 'title': 'PAC-12 Mountain (US)'}, '%s/pac12.png'% _icondir)
add_video_item('http://pac12hd2-lh.akamaihd.net/i/p12wash_delivery@132841/master.m3u8',{ 'title': 'PAC-12 Washington (US)'}, '%s/pac12.png'% _icondir)

xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")

