# -*- coding: utf-8 -*-

import xbmcgui,xbmcplugin,sys

xbmcgui.Dialog().ok('XBMC Log Viewer','Desinstale esta versão e instale a nova do','repositorio fightnight.')

xbmcplugin.endOfDirectory(int(sys.argv[1]))
