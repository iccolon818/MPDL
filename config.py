import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import builder
import json
import os.path
from os.path import exists
import touch

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

            portlist = builder.get_object("portlist")
            iwadlist = builder.get_object("iwadlist")

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
    print("dummy!")

def loadconfigbuttonclicked(button):
    print("dummy!")

def deleteconfigbuttonclicked(button):
    print("dummy!")

def cfgnamecancelbuttonclicked(button):
    print("dummy!")

def cfgnameokbuttonclicked(button):
    print("dummy!")