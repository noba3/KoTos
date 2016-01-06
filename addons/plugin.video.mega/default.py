# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------
# Mega for XBMC
# Version 1.0.3
#-----------------------------------------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#-----------------------------------------------------------------------------------------------
# Changelog:
# 1.0.0
# - First release
# 1.0.2
# - Default values for bufering has been raised
# 1.0.3
# - Small changes for making the stream function available to other addons (thanks to buster25)
#-----------------------------------------------------------------------------------------------

import os
import sys
import urlparse
import urllib
import locale
import threading
import time

import xbmc
import xbmcgui

import plugintools

plugintools.log("mega.init")

logged = False
tos_accepted = False

if plugintools.get_setting("tos_accepted")=="false":
    dialog = xbmcgui.Dialog()
    tos_accepted = dialog.yesno("Please read terms of service", "http://g.static.mega.co.nz/pages/terms.html", "Please read terms of service on the URL above","and accept them to continue")

    if tos_accepted:
        plugintools.set_setting("tos_accepted","true")

else:
    tos_accepted = True

if tos_accepted:
    maindialog = xbmcgui.DialogProgress()
    maindialog.create('Accessing MEGA', 'Initializing...')
    progress = 0
    maindialog.update(progress)

    # Get the platform and architecture
    system_platform = 'Unknown'
    architecture = ''

    # struct.calcsize("P") is 4 or 8 for 32 or 64 bit Python repectively
    # sys.maxsize > 2**32 would be nice to use but is only available from Pyton 2.6
    #if struct.calcsize("P") == 8:
    if sys.maxsize > 2**32:
        architecture = '64bit'
    else:
        architecture = '32bit'

    if xbmc.getCondVisibility( "system.platform.linux" ):
        system_platform = 'Linux'
        if 'arm' in os.uname()[4]:
            architecture = 'arm'
    elif xbmc.getCondVisibility( "system.platform.xbox" ):
        system_platform = 'Xbox'
        # No architecture directory for Xbox
        architecture = ''
    elif xbmc.getCondVisibility( "system.platform.windows" ):
        system_platform = 'Windows'

    elif xbmc.getCondVisibility( "system.platform.osx" ):
        system_platform = 'Darwin'
        if 'RELEASE_ARM' in os.uname()[3]:
            architecture = 'ios'
        else:
            # Crypto can be compiled as universal library with multiple
            # architectures for osx
            architecture = 'osx'

    elif xbmc.getCondVisibility( "system.platform.ios" ):
        # Need to check system.platform.osx for eden
        # Changed to system.platform.ios for frodo
        system_platform = 'Darwin'
        architecture = 'ios'

    elif xbmc.getCondVisibility( "system.platform.android" ):
        system_platform = 'Android'
        architecture = ''

    plugintools.log("mega.init system_platform="+system_platform)
    plugintools.log("mega.init architecture="+architecture)

    crypto_path = os.path.join( plugintools.get_runtime_path(), "resources", "lib", "platform_libraries", system_platform, architecture)
    plugintools.log("mega.init crypto_path="+crypto_path)
    sys.path.append(crypto_path)
    #plugintools.log("mega.init sys.path="+str(sys.path))

    # Import other libraries
    libraries = os.path.join( plugintools.get_runtime_path(), 'resources' , 'lib' )
    #plugintools.log("mega.init libraries="+libraries)
    sys.path.append (libraries)
    #plugintools.log("mega.init sys.path="+str(sys.path))

    try:
        from mega.mega import Mega
    except:
        import traceback,sys
        from pprint import pprint
        exc_type, exc_value, exc_tb = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_tb)
        for line in lines:
            line_splits = line.split("\n")
            for line_split in line_splits:
                plugintools.log(line_split)

    # Thumbnails for item list
    FILE_ICON = os.path.join( plugintools.get_runtime_path(), 'resources' , 'images' , 'file.png' )
    FOLDER_ICON = os.path.join( plugintools.get_runtime_path(), 'resources' , 'images' , 'folder.png' )
    IMAGE_ICON = os.path.join( plugintools.get_runtime_path(), 'resources' , 'images' , 'image.png' )
    MUSIC_ICON = os.path.join( plugintools.get_runtime_path(), 'resources' , 'images' , 'music.png' )
    VIDEO_ICON = os.path.join( plugintools.get_runtime_path(), 'resources' , 'images' , 'video.png' )
    DOWNLOAD_PATH = os.path.join( plugintools.get_data_path() ,"downloads")

    plugintools.log("mega.init Creating...")
    mega = Mega()

    maindialog.update(50,"Connecting...")
    plugintools.log("mega.init Login...")
    USERNAME = plugintools.get_setting("username")
    PASSWORD = plugintools.get_setting("password")
    #plugintools.log("mega.init USERNAME="+USERNAME)
    #plugintools.log("mega.init PASSWORD="+PASSWORD)

    try:
        m = mega.login( USERNAME , PASSWORD )
        logged = True
    except:

        if USERNAME=="":
            plugintools.open_settings_dialog()
            USERNAME = plugintools.get_setting("username")
            PASSWORD = plugintools.get_setting("password")
            #plugintools.log("mega.init USERNAME="+USERNAME)
            #plugintools.log("mega.init PASSWORD="+PASSWORD)

            try:
                m = mega.login( USERNAME , PASSWORD )
                logged = True
            except:
                plugintools.message("Invalid login","Wrong username or password")
                import traceback,sys
                from pprint import pprint
                exc_type, exc_value, exc_tb = sys.exc_info()
                lines = traceback.format_exception(exc_type, exc_value, exc_tb)
                for line in lines:
                    line_splits = line.split("\n")
                    for line_split in line_splits:
                        plugintools.log(line_split)

        else:
            plugintools.message("Invalid login","Wrong username or password")

# Entry point
def run():
    plugintools.log("mega.run")
    
    # Get params
    params = plugintools.get_params()
    plugintools.log("mega.run params="+repr(params))

    if logged:
        if params.get("action") is None:
            main_list(params)
        else:
            action = params.get("action")
            exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("mega.main_list "+repr(params))

    folder(params)

# Folder listing
def folder(params):
    plugintools.log("mega.folder "+repr(params))

    maindialog.update(66,"Reading data...")
    plugintools.log("mega.folder Getting files...")
    files = m.get_files()

    maindialog.update(100)
    maindialog.close()

    plugintools.log("mega.folder %d items retrieved" % len(files))
    #plugintools.log("mega.folder "+repr(files))

    for entry in files:
        plugintools.log("mega.folder entry="+repr( files[entry] ))

        title = files[entry]['a']['n']
        url = files[entry]['a']['n']
        extension = url.lower()[-3:]

        is_image = extension in ("jpg","png","gif")
        is_music = extension in ("mp3","wma")
        is_video = extension in ("mkv","avi","mp4")

        is_folder = files[entry]['t']==1
        is_file = files[entry]['t']==0

        #if is_folder:
        #    plugintools.add_item( action="folder", title=title , url=url , thumbnail=FOLDER_ICON , folder=True )
        #el
        if is_file:
            size = files[entry]['s']

            if is_image:
                plugintools.add_item( action="show_picture", title=title+" ("+human_size(size)+")" , url=url , isPlayable=False, thumbnail=IMAGE_ICON , folder=False, extra=str(size) )
            elif is_music:
                plugintools.add_item( action="download_and_play", title=title+" ("+human_size(size)+")" , url=url , isPlayable=False, thumbnail=MUSIC_ICON , folder=False, extra=str(size) )
            else:
                plugintools.add_item( action="stream", title=title+" ("+human_size(size)+")" , url=url , isPlayable=False, thumbnail=VIDEO_ICON , folder=False, extra=str(size) )

def human_size(size):

    if size<1024:
        text_size="%dB" % size
    elif size<(1024*1024):
        text_size="%dKB" % (size / 1024)
    elif size<(1024*1024*1024):
        text_size="%dMB" % (size / (1024*1024) )
    elif size<(1024*1024*1024*1024):
        text_size="%dGB" % (size / (1024*1024*1024) )
    else:
        text_size="%dTB" % (size / (1024*1024*1024*1024) )

    return text_size

# Show a picture
def show_picture(params):
    plugintools.log("mega.show_picture "+repr(params))

    maindialog.update(100,"Reading data...")
    if not os.path.exists( DOWNLOAD_PATH ):
        os.makedirs(DOWNLOAD_PATH)
    plugintools.log("mega.show_picture DOWNLOAD_PATH="+DOWNLOAD_PATH)

    # Get file metadata
    file = m.find(params.get("url"))
    plugintools.log("mega.show_picture file="+repr(file))
    local_file = os.path.join( DOWNLOAD_PATH , params.get("url") )
    maindialog.close()

    download_thread = DownloadThread(file)
    download_thread.start()

    dialog = xbmcgui.DialogProgress()
    dialog.create('Downloading picture', 'Wait until download is completed')
    progress = 0
    dialog.update(progress)
    total_size = int(params.get("extra"))
    plugintools.log("mega.show_picture total size="+str(total_size))

    cancelled = False
    while download_thread.is_alive():
        #plugintools.log("mega.show_picture Download thread still alive...")
        if os.path.exists(local_file):
            actual_size = os.path.getsize( local_file )
        else:
            actual_size = 0
        #plugintools.log("mega.show_picture actual size="+str(actual_size))
        progress = (float(actual_size)/float(total_size))*100
        dialog.update(progress)
        xbmc.sleep(1000)

        if dialog.iscanceled():
            download_thread.force_stop()
            cancelled = True
            break

    dialog.close()

    plugintools.show_picture(local_file)

# Download and play a file
def download_and_play(params):
    plugintools.log("mega.download_and_play "+repr(params))

    maindialog.update(100,"Reading data...")
    if not os.path.exists( DOWNLOAD_PATH ):
        os.makedirs(DOWNLOAD_PATH)
    plugintools.log("mega.download_and_play DOWNLOAD_PATH="+DOWNLOAD_PATH)

    # Get file metadata

    file = m.find(params.get("url"))
	
    plugintools.log("mega.download_and_play file="+repr(file))
    maindialog.close()

    local_file = os.path.join( DOWNLOAD_PATH , params.get("url") )
    plugintools.log("mega.download_and_play local_file="+repr(file))

    download_thread = DownloadThread(file)
    download_thread.start()

    dialog = xbmcgui.DialogProgress()
    dialog.create('Downloading file', 'Wait until download is completed')
    progress = 0
    dialog.update(progress)
    total_size = int(params.get("extra"))
    plugintools.log("mega.download_and_play total size="+str(total_size))

    cancelled = False
    while download_thread.is_alive():
        #plugintools.log("mega.download_and_play Download thread still alive...")
        if os.path.exists(local_file):
            actual_size = os.path.getsize( local_file )
        else:
            actual_size = 0
        #plugintools.log("mega.download_and_play actual size="+str(actual_size))
        progress = (float(actual_size)/float(total_size))*100
        dialog.update(progress)
        xbmc.sleep(1000)

        if dialog.iscanceled():
            download_thread.force_stop()
            cancelled = True
            break

    dialog.close()

    if not cancelled:
        player = xbmc.Player()
        player.play(local_file)

# Download a file and start playing while downloading
def stream(params):
    plugintools.log("mega.stream "+repr(params))

    maindialog.update(100)
    maindialog.close()

    if not os.path.exists( DOWNLOAD_PATH ):
        os.makedirs(DOWNLOAD_PATH)
    plugintools.log("mega.stream DOWNLOAD_PATH="+DOWNLOAD_PATH)

    # Delete existing files from download folder
    ficheros = os.listdir(DOWNLOAD_PATH)
    for fichero in ficheros:
        full_path = os.path.join( DOWNLOAD_PATH , fichero )
        plugintools.log("mega.stream Deleting " + full_path)
        os.remove(full_path)

    # Get file metadata
	
	
	
	
	
	
	
	##############################################################################################################################
    #file = m.find(params.get("url"))                                                      #########    ORIGINAL    ##############
	
	'''		
    if params.get("plot")<>"":
       file = params.get("plot")
       plugintools.log("mega.stream " +params.get("plot"))
    else:
       file = m.find(params.get("url"))
       plugintools.log("mega.stream " +params.get("url"))
	'''

    if params.get("url").startswith("http://") or params.get("url").startswith("https://"):
        file = params.get("url")
    else:
        file = m.find(params.get("url"))
	##############################################################################################################################
	
	
	
	
	
	
    
    plugintools.log("mega.stream file="+repr(file))
    maindialog.close()

    # Lanza thread
    plugintools.log("mega.stream Active threads "+str(threading.active_count()))
    plugintools.log("mega.stream "+repr(threading.enumerate()))
    plugintools.log("mega.stream Starting download thread...")
    download_thread = DownloadThread(file)
    download_thread.start()
    plugintools.log("mega.stream Download thread started")
    plugintools.log("mega.stream Active threads "+str(threading.active_count()))
    plugintools.log("mega.stream "+repr(threading.enumerate()))

    # Espera
    plugintools.log("mega.stream Waiting...")

    dialog = xbmcgui.DialogProgress()
    dialog.create('Streaming file', 'Buffering file before playing...')
    progress = 0
    buffering_time = int(float(plugintools.get_setting("buffering_time")))
    plugintools.log("mega.stream buffering_time="+str(buffering_time))
    dialog.update(progress)

    cancelled=False
    while progress <= buffering_time:
        dialog.update(int( float(float(progress) / float(buffering_time))*100 ) )
        
		#######################################################################################################################
        #xbmc.sleep(10000)
        xbmc.sleep(1000)
		#######################################################################################################################
		
        progress = progress + 1
        plugintools.log("mega.stream progress="+str(progress))
        if dialog.iscanceled():
            cancelled=True
            break

    dialog.close()

    plugintools.log("mega.stream End of waiting")

    if not cancelled:
        plugintools.log("mega.stream Playing...")
		
		
		
##################################################################################################################################
##################################################################################################################################
		
        if params.get("plot")<>"":
           ficheros = os.listdir(DOWNLOAD_PATH)
           for fichero in ficheros:
               local_file = os.path.join( DOWNLOAD_PATH , fichero )
               plugintools.log("mega.stream Playing -public url-... " + local_file)
        else:
               local_file = os.path.join( DOWNLOAD_PATH , params.get("url") )
               plugintools.log("mega.stream Playing -private url-... " + local_file)
      
	  
##################################################################################################################################
##################################################################################################################################


		
        #plugintools.direct_play(local_file)
		
        #player = xbmc.Player( xbmc.PLAYER_CORE_AUTO )
        #player.play(local_file)
        xbmc.sleep(2000)

        player = CustomPlayer()
        player.set_download_thread(download_thread)
        player.PlayStream(local_file)

        '''
        while player.isPlaying():
            time.sleep(1000)
            plugintools.log("mega.play Download thread alive="+str(download_thread.is_alive()))

        if download_thread.is_alive():
            plugintools.log("mega.play Killing download thread")
            download_thread.force_stop()
        '''

    plugintools.log("mega.stream Download thread alive="+str(download_thread.is_alive()))
    if download_thread.is_alive():
        plugintools.log("mega.stream Killing download thread")
        download_thread.force_stop()

class CustomPlayer(xbmc.Player):
    def __init__( self, *args, **kwargs ):
        plugintools.log("mega.CustomPlayer.__init__")
        xbmc.Player.__init__( self )

    def PlayStream(self, url):  
        plugintools.log("mega.CustomPlayer.PlayStream url="+url)

        self.play(url)
        while self.isPlaying():
            xbmc.sleep(3000)

    def set_download_thread(self,download_thread):
        plugintools.log("mega.CustomPlayer.set_download_thread")
        self.download_thread = download_thread

    def force_stop_download_thread(self):
        plugintools.log("mega.CustomPlayer.force_stop_download_thread")

        if self.download_thread.is_alive():
            plugintools.log("mega.CustomPlayer.force_stop_download_thread Killing download thread")
            self.download_thread.force_stop()

            #while self.download_thread.is_alive():
            #    xbmc.sleep(1000)

    def onPlayBackStarted(self):
        plugintools.log("mega.CustomPlayer.onPlayBackStarted PLAYBACK STARTED")

    def onPlayBackEnded(self):
        plugintools.log("mega.CustomPlayer.onPlayBackEnded PLAYBACK ENDED")
        self.force_stop_download_thread()

    def onPlayBackStopped(self):
        plugintools.log("mega.CustomPlayer.onPlayBackStopped PLAYBACK STOPPED")
        self.force_stop_download_thread()

# Download in background
class DownloadThread(threading.Thread):
    
    def __init__(self, file):
        plugintools.log("mega.DownloadThread.__init__ "+repr(file))
        #plugintools.message("mega.DownloadThread.__init__ ",repr(file))
        self.file = file        
        threading.Thread.__init__(self)
        
    def run(self):
        plugintools.log("mega.DownloadThread.run Download starts..." + repr(self.file))
		
		
		
		####################################################################################################################
		#m.download(self.file , DOWNLOAD_PATH)                     #############     ORIGINAL    ###########################
        
        
		
        if 'https:' in repr(self.file):
           plugintools.log("mega.DownloadThread.run.... public url streaming")
           m.download_url(self.file , DOWNLOAD_PATH)
        else:
           plugintools.log("mega.DownloadThread.run.... private url streaming")
           m.download(self.file , DOWNLOAD_PATH)
		
		####################################################################################################################
		
		
		
		
		
		
		
		
        plugintools.log("mega.DownloadThread.run Download ends")

    def force_stop(self):
        plugintools.log("mega.DownloadThread.force_stop...")
        force_stop_file = open( os.path.join( DOWNLOAD_PATH , "force_stop.tmp" ) , "w" )
        force_stop_file.write("0")
        force_stop_file.close()

run()
