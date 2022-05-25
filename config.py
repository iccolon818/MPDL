import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import builder
import json
import os.path
from os.path import exists
import touch

from objects import *

cfg = "./.mpdl.cfg"

def configinit():

    global jsoncfg
    jsoncfg = {
        "ports": [],
        "iwads": [],
        "cfgs": []
    }

    if not exists(cfg):
        touch.touch(cfg)
    else:
        if os.path.getsize(cfg) > 0:
            f = open(cfg, "r")
            jsoncfg = json.load(f)
            f.close()

            for port in jsoncfg['ports']:
                portlist.append([port['name'], port['path']])

            for iwad in jsoncfg['iwads']:
                iwadlist.append([iwad['name'], iwad['path']])
        
def writechanges():
    f = open(cfg, "w")
    jsonstr = json.dumps(jsoncfg, indent = 4)
    f.write(jsonstr)
    f.close()

def saveconfigbuttonclicked(button):
    cfgnamedialog.show()

def loadconfigbuttonclicked(button):
    print("dummy!")

def deleteconfigbuttonclicked(button):
    print("dummy!")

def cfgnamecancelbuttonclicked(button):
    cfgnamedialog.hide()

def cfgnameokbuttonclicked(button):
    cfgnamedialog.hide()

    newconfig = {}
    newconfig['name'] = cfgnameentry.get_text()

    portiter = portcombobox.get_active_iter()
    newconfig['port'] = portlist.get_value(portiter, 0)

    iwaditer = iwadcombobox.get_active_iter()
    newconfig['iwad'] = iwadlist.get_value(iwaditer, 0)
    
    if (demononeradiobutton.get_active()):
        newconfig['demo'] = 0
        newconfig['playdemo'] = ""
        newconfig['demofolder'] = ""
        newconfig['recorddemo'] = ""

    elif (demoplayradiobutton.get_active()):
        newconfig['demo'] = 1
        newconfig['playdemo'] = playdemofilechooser.get_filename()
        newconfig['demofolder'] = ""
        newconfig['recorddemo'] = ""

    elif (demorecordradiobutton.get_active()):
        newconfig['demo'] = 2
        newconfig['playdemo'] = ""
        newconfig['demofolder'] = recorddemofolderchooser.get_filename()
        newconfig['recorddemo'] = recorddemofilenameentry.get_text()

    newconfig['warp'] = warpentry.get_text()
    newconfig['zdoomwarp'] = zdoomstylecheckbox.get_active()

    if otherskillcheckbox.get_active():
        newconfig['skill'] = [True, otherskillentry.get_text()]
    else:
        newconfig['skill'] = [False, skillcombobox.get_active()]

    if othercomplevelcheckbox.get_active():
        newconfig['complevel'] = [True, othercomplevelentry.get_text()]
    else:
        newconfig['complevel'] = [False, skillcombobox.get_active()]
    
    newconfig['args'] = [
        nomonsterscheckbox.get_active(),
        nomusiccheckbox.get_active(),
        fastmonsterscheckbox.get_active(),
        respawncheckbox.get_active(),
        solonetcheckbox.get_active(),
        dehlumpcheckbox.get_active(),
        noautoloadcheckbox.get_active(),
        pistolstartcheckbox.get_active()
    ]

    newconfig['pwads'] = []

    def addpwad(list, path, iter, data):
        cfgpwad = {}
        cfgpwad['name'] = list.get_value(iter, 0)
        cfgpwad['path'] = list.get_value(iter, 1)
        cfgpwad['merge'] = list.get_value(iter, 2)
        newconfig['pwads'].append(cfgpwad)

    pwadlist.foreach(addpwad, None)

    newconfig['dehs'] = []

    def adddeh(list, path, iter, data):
        cfgdeh = {}
        cfgdeh['name'] = list.get_value(iter, 0)
        cfgdeh['path'] = list.get_value(iter, 1)
        newconfig['dehs'].append(cfgdeh)

    dehlist.foreach(adddeh, None)

    newconfig['extraargs'] = extraargsentry.get_text()

    jsoncfg['cfgs'].append(newconfig)
    writechanges()