# -*- coding: utf-8 -*-

import xbmc,os,sys,re,shutil

def setset():
    datax=[]
    sxUser = 0
    orgset = xbmc.translatePath('special://userdata/addon_data/plugin.video.iptvxtra-de/settings.xml')
    defset = xbmc.translatePath('special://home/addons/plugin.video.iptvxtra-de/resources/settings.xml')
    bakset = xbmc.translatePath('special://home/addons/plugin.video.iptvxtra-de/resources/settings.xml.bak')

    try: dataa = open(orgset).readlines()
    except: sys.exit(0)
    for line in dataa:
        if "login" in line:
            if "xbmcuser" in line or 'value=""' in line or 'value=" "' in line: sxUser = 0
            else: sxUser = 1
            break

    if sxUser == 1:
        data = open(orgset).read()
        default = open(defset).readlines()
        default_neu = open(defset,'w')
        data = data.replace(' ','')
        datax = re.findall(r'(settingid="([^"]+)"value="([^"]+)")',data)
        for i in default:
            for k in datax:
                if k[1].strip() == find_between(i,'id="','"'):
                    i = i.replace('default="' + find_between(i,'default="','"') + '"' , 'default="' + k[2].strip() + '"')
                    break
            default_neu.write(i)
        default_neu.close()


def find_between(s,first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

setset()