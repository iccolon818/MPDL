import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import builder
import config

from objects import (iwadchooser, iwadcombobox, iwadnamedialog, iwadnameentry,
    iwadlist, iwadpathentry, portchooser, portcombobox, portnamedialog,
    portnameentry, portlist, portpathentry)

# Add Source Port

def addportbuttonclicked(button):
    portchooser.show()

def removeportbuttonclicked(button):
    index = portcombobox.get_active()
    iter = portcombobox.get_active_iter()
    portlist.remove(iter)

    if index:
        portcombobox.set_active(index-1)
    else:
        portcombobox.set_active(0)

    del config.jsoncfg['ports'][index]
    config.writechanges()

def portchooserselectionchanged(chooser):
    portpathentry.set_text(chooser.get_filename())

def portcancelbuttonclicked(button):
    portpathentry.set_text("")
    portchooser.hide()

def portselectbuttonclicked(button):
    portnamedialog.show()

def portnamecancelbuttonclicked(button):
    portnamedialog.hide()

def portnameokbuttonclicked(button):
    portnamedialog.hide()
    portpathentry.set_text("")
    portchooser.hide()

    newport = {
        "name": portnameentry.get_text(),
        "path": portchooser.get_filename()
    }

    print("Before: ", config.jsoncfg)
    config.jsoncfg['ports'].append(newport)
    print("After: ", config.jsoncfg)
    portlist.append([newport['name'], newport['path']])
    config.writechanges()

# Add IWAD

def addiwadbuttonclicked(button):
    iwadchooser.show()

def removeiwadbuttonclicked(button):
    index = iwadcombobox.get_active()
    iter = iwadcombobox.get_active_iter()
    iwadlist.remove(iter)

    if index:
        iwadcombobox.set_active(index-1)
    else:
        iwadcombobox.set_active(0)

    del config.jsoncfg['iwads'][index]
    config.writechanges()

def iwadchooserselectionchanged(chooser):
    iwadpathentry.set_text(chooser.get_filename())

def iwadcancelbuttonclicked(button):
    iwadpathentry.set_text("")
    iwadchooser.hide()

def iwadselectbuttonactiate(button):
    iwadnamedialog.show()

def iwadnamecancelbuttonclicked(button):
    iwadnamedialog.hide()

def iwadnameokbuttonclicked(button):
    iwadnamedialog.hide()
    iwadpathentry.set_text("")
    iwadchooser.hide()

    newiwad = {
        "name": iwadnameentry.get_text(),
        "path": iwadchooser.get_filename()
    }

    print("Before: ", config.jsoncfg)
    config.jsoncfg['iwads'].append(newiwad)
    print("After: ", config.jsoncfg)

    iwadlist.append([newiwad['name'], newiwad['path']])
    config.writechanges()