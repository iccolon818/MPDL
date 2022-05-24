import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import builder
import os.path
from os.path import exists
import subprocess

portcombobox = builder.get_object("portcombobox")
portlist = builder.get_object("portlist")
iwadcombobox = builder.get_object("iwadcombobox")
iwadlist = builder.get_object("iwadlist")

warpentry = builder.get_object("warpentry")
zdoomstylecheckbox = builder.get_object("zdoomstylecheckbox")
skillcombobox = builder.get_object("skillcombobox")
otherskillentry = builder.get_object("skillentry")
otherskillcheckbox = builder.get_object("otherskillcheckbox")
complevelcombobox = builder.get_object("complevelcombobox")
othercomplevelcheckbox = builder.get_object("othercomplevelcheckbox")
othercomplevelentry = builder.get_object("othercomplevelentry")
complevellist = builder.get_object("complevellist")

nomonsterscheckbox = builder.get_object("nomonsterscheckbox")
nomusiccheckbox = builder.get_object("nomusiccheckbox")
fastmonsterscheckbox = builder.get_object("fastmonsterscheckbox")
respawncheckbox = builder.get_object("respawncheckbox")
solonetcheckbox = builder.get_object("solonetcheckbox")
dehlumpcheckbox = builder.get_object("dehlumpcheckbox")
noautoloadcheckbox = builder.get_object("noautoloadcheckbox")
pistolstartcheckbox = builder.get_object("pistolstartcheckbox")

pwadlist = builder.get_object("pwadlist")
dehlist = builder.get_object("dehlist")

extraargsentry = builder.get_object("extraargsentry")

demoplayradiobutton = builder.get_object("demoplayradiobutton")
playdemofilechooser = builder.get_object("playdemofilechooser")
demorecordradiobutton = builder.get_object("demorecordradiobutton")
recorddemofolderchooser = builder.get_object("recorddemofolderchooser")
recorddemofilenameentry = builder.get_object("recorddemofilenameentry")

def launchgame(button):
    command = []

    # Get source port
    portiter = portcombobox.get_active_iter()
    print(portiter)
    portpath = portlist.get_value(portiter, 1)
    command.append(portpath)

    # Get IWAD
    iwaditer = iwadcombobox.get_active_iter()
    iwadpath = iwadlist.get_value(iwaditer, 1)
    command.append("-iwad")
    command.append(iwadpath)

    # Level Warp
    warp = warpentry.get_text().split()
    zdoom = zdoomstylecheckbox.get_active()

    if warp:
        if zdoom:
            command.append("+map")
        else:
            command.append("-warp")
        
        for arg in warp:
            command.append(arg)

    # Skill
    skill = skillcombobox.get_active()
    otherskill = otherskillcheckbox.get_active()
    otherskilltext = otherskillentry.get_text()

    if otherskill and otherskilltext:
        command.append("-skill")
        command.append(otherskilltext)
    elif not otherskill and skill > 0:
        command.append("-skill")
        command.append(str(skill))

    # Compatibility Level        
    complevel = complevelcombobox.get_active()
    othercomplevel = othercomplevelcheckbox.get_active()
    othercompleveltext = othercomplevelentry.get_text()

    if othercomplevel and othercompleveltext:
        command.append("-complevel")
        command.append(othercompleveltext)
    elif not othercomplevel and complevel > 0:
        command.append("-complevel")
        compleveliter = complevelcombobox.get_active_iter()
        complevelnum = complevellist.get_value(compleveliter, 1)
        command.append(str(complevelnum))

    # Bool args
    if (nomonsterscheckbox.get_active()):
        command.append("-nomonsters")
    if (nomusiccheckbox.get_active()):
        command.append("-nomusic")
    if (fastmonsterscheckbox.get_active()):
        command.append("-fast")
    if (respawncheckbox.get_active()):
        command.append("-respawn")
    if (solonetcheckbox.get_active()):
        command.append("-solo-net")
    if (dehlumpcheckbox.get_active()):
        command.append("-dehlump")
    if (noautoloadcheckbox.get_active()):
        command.append("-noautoload")
    if (pistolstartcheckbox.get_active()):
        command.append("-pistolstart")

    # PWADS
    mergelist = []
    filelist = []

    def addpwad(iter):
        wad = pwadlist.get_value(iter, 1)

        if pwadlist.get_value(iter, 2):
            mergelist.append(wad)
        else:
            filelist.append(wad)

    pwadlist.foreach(lambda model, path, iter, data: addpwad(iter), None)

    if mergelist:
        command.append("-merge")
        for wad in mergelist:
            command.append(wad)

    if filelist:
        command.append("-file")
        for wad in filelist:
            command.append(wad)

    # Dehacked
    def adddeh(iter):
        command.append("-deh")
        command.append(dehlist.get_value(iter, 1))
    
    dehlist.foreach(lambda model, path, iter, data: adddeh(iter), None)

    # Demos
    if demoplayradiobutton.get_active() and playdemofilechooser.get_file():
        command.append("-playdemo")
        command.append(playdemofilechooser.get_file().get_path())
    elif demorecordradiobutton.get_active():
        
        folder = recorddemofolderchooser.get_filename()
        demoname = recorddemofilenameentry.get_text()

        # This directory by default
        if not folder:
            folder = "."

        # Call demo "demo.lmp" by default
        if not demoname:
            demoname = "demo"

        path = folder + "/" + demoname
        
        # Increment demo names automatically if path is taken
        if exists(path + ".lmp"):
            counter = 2
            while exists(path + ".lmp"):
                path = folder + "/" + demoname + str(counter)
                counter += 1

        command.append("-record")
        command.append(path)



    # Extra args
    extraargs = extraargsentry.get_text().split()
    for arg in extraargs:
        command.append(arg)

    # Launch game
    print(command)
    subprocess.call(command)