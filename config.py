import builder
import json
import os.path
from os.path import exists
import touch

from objects import *

cfgpath = "./.mpdl.cfg"

def configinit():

    global jsoncfg
    jsoncfg = {
        "ports": [],
        "iwads": [],
        "cfgs": []
    }

    if not exists(cfgpath):
        touch.touch(cfgpath)
    else:
        if os.path.getsize(cfgpath) > 0:
            f = open(cfgpath, "r")
            jsoncfg = json.load(f)
            f.close()

            for port in jsoncfg['ports']:
                portlist.append([port['name'], port['path']])

            for iwad in jsoncfg['iwads']:
                iwadlist.append([iwad['name'], iwad['path']])

            for cfg in jsoncfg['cfgs']:
                configlist.append([cfg['name']])
        
def writechanges():
    f = open(cfgpath, "w")
    jsonstr = json.dumps(jsoncfg, indent = 4)
    f.write(jsonstr)
    f.close()

def saveconfigbuttonclicked(button):
    cfgnamedialog.show()

def loadconfigbuttonclicked(button):
    index = configcombobox.get_active()
    loadcfg = jsoncfg['cfgs'][index]
    
    port = loadcfg['port']
    def searchports(list, path, iter, data):
        if portlist.get_value(iter, 0) == port:
            portcombobox.set_active_iter(iter)

    portlist.foreach(searchports, None)

    iwad = loadcfg['iwad']
    def searchiwads(list, path, iter, data):
        if iwadlist.get_value(iter, 0) == iwad:
            iwadcombobox.set_active_iter(iter)

    iwadlist.foreach(searchiwads, None)

    if (loadcfg['demo'] == 1):
        demoplayradiobutton.set_active(True)
        playdemofilechooser.select_filename(loadcfg['playdemo'])
    elif (loadcfg['demo'] == 2):
        demorecordradiobutton.set_active(True)
        recorddemofolderchooser.select_filename(loadcfg['demofolder'])
        recorddemofilenameentry.set_text(loadcfg['recorddemo'])
    else:
        demononeradiobutton.set_active(True)

    warpentry.set_text(loadcfg['warp'])
    zdoomstylecheckbox.set_active(loadcfg['zdoomwarp'])

    if loadcfg['skill'][0]:
        otherskillcheckbox.set_active(True)
        otherskillentry.set_text(loadcfg['skill'][1])
    else:
        otherskillcheckbox.set_active(False)
        skillcombobox.set_active(loadcfg['skill'][1])

    if loadcfg['complevel'][0]:
        othercomplevelcheckbox.set_active(True)
        othercomplevelentry.set_text(loadcfg['complevel'][1])
    else:
        othercomplevelcheckbox.set_active(False)
        complevelcombobox.set_active(loadcfg['complevel'][1])

    nomonsterscheckbox.set_active(loadcfg['args'][0])
    nomusiccheckbox.set_active(loadcfg['args'][1])
    fastmonsterscheckbox.set_active(loadcfg['args'][2])
    respawncheckbox.set_active(loadcfg['args'][3])
    solonetcheckbox.set_active(loadcfg['args'][4])
    dehlumpcheckbox.set_active(loadcfg['args'][5])
    noautoloadcheckbox.set_active(loadcfg['args'][6])
    pistolstartcheckbox.set_active(loadcfg['args'][7])

    pwadlist.clear()
    for pwad in loadcfg['pwads']:
        pwadlist.append([pwad['name'], pwad['path'], pwad['merge']])

    dehlist.clear()
    for deh in loadcfg['dehs']:
        dehlist.append([deh['name'], deh['path']])

    extraargsentry.set_text(loadcfg['extraargs'])

    cfgnameentry.set_text(loadcfg['name'])

def deleteconfigbuttonclicked(button):
    index = configcombobox.get_active()
    cfgiter = configcombobox.get_active_iter()
    configlist.remove(cfgiter)

    if index:
        configcombobox.set_active(index-1)
    else:
        configcombobox.set_active(0)

    del jsoncfg['cfgs'][index]
    writechanges()

def cfgnamecancelbuttonclicked(button):
    cfgnamedialog.hide()

def cfgnameokbuttonclicked(button):
    isnewconfig = True

    for cfg in jsoncfg['cfgs']:
        if cfg['name'] == cfgnameentry.get_text():
            isnewconfig = False
            break
    
    if not isnewconfig:
        overwritedialog.show()
    else:
        cfgnamedialog.hide()
        saveconfig(True, -1)

def overwritenobuttonclicked(button):
    overwritedialog.hide()

def overwriteyesbuttonclicked(button):
    overwritedialog.hide()
    cfgnamedialog.hide()
    index = 0

    for cfg in jsoncfg['cfgs']:
        if cfg['name'] == cfgnameentry.get_text():
            break
        else:
            index += 1


    saveconfig(False, index)

def saveconfig(isnewconfig, index):
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
        newconfig['complevel'] = [False, complevelcombobox.get_active()]
    
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

    if isnewconfig:
        jsoncfg['cfgs'].append(newconfig)
        configlist.append([newconfig['name']])
    else:
        jsoncfg['cfgs'][index] = newconfig
        configindex = configcombobox.get_active()
        configlist.clear()

        for cfg in jsoncfg['cfgs']:
            configlist.append([cfg['name']])

        configcombobox.set_active(configindex)
    
    writechanges()