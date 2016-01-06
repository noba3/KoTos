import xbmc
import xbmcaddon


addon = xbmcaddon.Addon('plugin.video.skygo')
addonname = addon.getAddonInfo('name')
addonID = addon.getAddonInfo('id')
ini_add = xbmc.translatePath('special://home/addons/'+addonID+'/resources/TVGuide/add.ini')



def textadd():
	try:
		TV_ini = xbmc.translatePath('special://home/addons/script.tvguide/resources/addons.ini')
		infile = open (ini_add, 'r')
		filestr = infile.read()
		outfile = open(TV_ini, 'a')
		outfile.write(filestr)
		xbmc.executebuiltin('Notification(Skygo sucessfully added to TVGuide addons,400,logo.png)')
	except:	
		xbmc.executebuiltin('Notification(Failed!, Skygo not added!,200)')
		
textadd()