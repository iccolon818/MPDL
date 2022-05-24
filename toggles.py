import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import builder


playdemofilechooser = builder.get_object("playdemofilechooser")
recorddemofolderchooser = builder.get_object("recorddemofolderchooser")
recorddemofilenameentry = builder.get_object("recorddemofilenameentry")

def otherskilltoggled(button):
    skillcombobox = builder.get_object("skillcombobox")
    otherskillentry = builder.get_object("otherskillentry")
    
    if button.get_active():
        otherskillentry.set_sensitive(True)
        skillcombobox.set_sensitive(False)
    else:
        otherskillentry.set_sensitive(False)
        skillcombobox.set_sensitive(True)

def othercompleveltoggled(button):
    complevelcombobox = builder.get_object("complevelcombobox")
    othercomplevelentry = builder.get_object("othercomplevelentry")
    
    if button.get_active():
        othercomplevelentry.set_sensitive(True)
        complevelcombobox.set_sensitive(False)
    else:
        othercomplevelentry.set_sensitive(False)
        complevelcombobox.set_sensitive(True)

def demononeradiobuttontoggled(button):
    playdemofilechooser.set_sensitive(False)
    recorddemofolderchooser.set_sensitive(False)
    recorddemofilenameentry.set_sensitive(False)

def demoplayradiobuttontoggled(button):
    playdemofilechooser.set_sensitive(True)
    recorddemofolderchooser.set_sensitive(False)
    recorddemofilenameentry.set_sensitive(False)

def demorecordradiobuttontoggled(button):
    playdemofilechooser.set_sensitive(False)
    recorddemofolderchooser.set_sensitive(True)
    recorddemofilenameentry.set_sensitive(True)