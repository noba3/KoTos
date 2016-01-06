#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,xbmcplugin,xbmcgui,xbmc,xbmcaddon

addonID = 'plugin.program.iptvxtra-as'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
profilePath = addon.getAddonInfo('profile')
__settings__ = addon

addon.openSettings()


