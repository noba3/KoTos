# -*- coding: utf-8 -*-

import sys,xbmcgui

class GUI(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 13]
        
        # get control ids
        self.control_id_button_exit = 3203
        self.textbox = 3201
        # set actions
        self.button_exit = self.getControl(self.control_id_button_exit)
        self.textlabel = self.getControl(self.textbox)

        zeile1 = 'Was ist neu in diesem Update ...'+'\n\n'
        zeile2 = 'in den Addon Einstellungen kann fuers LiveTV ein Puffer aktiviert werden'+'\n'
        zeile3 = 'der Puffer ist knapp 2 Minuten lang, bei Pause baut er sich weiter auf'+'\n'
        zeile4 = 'Achtung - bei Abbruch und Restart des Streams ueber 1,5 Stunden,'+'\n'
        zeile5 = 'stimmen die Pufferzeiten noch nicht'+'\n\n'
        zeile6 = 'wahlweise kann jetzt HQ, HD oder HQ und HD ausgewaehlt werden'+'\n\n'
        zeile7 = 'die Rueckschau / Replay funktioniert jetzt auch bei den HD Sendern'+'\n\n'
        zeile8 = 'Replay endet z.B. immer nach 25 Min und beginnt von vorne - ist gefixt'+'\n\n'
        zeile9 = 'WICHTIG! KODI MUSS VOR DER BENUTZUNG NEU GESTARTET WERDEN'+'\n\n'
        zeile10 = 'viel Spass vor der Glotze :-)'

        self.textlabel.setText(zeile1+zeile2+zeile3+zeile4+zeile5+zeile6+zeile7+zeile8+zeile9+zeile10)


    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.closeDialog()

    def onFocus(self, controlId):
        pass

    def onClick(self, controlId):
        if controlId == self.control_id_button_exit:
            self.closeDialog()

    def doAction(self):
        pass

    def closeDialog(self):
        self.close()
