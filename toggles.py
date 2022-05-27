import builder

from objects import (complevelcombobox, othercomplevelentry, otherskillentry,
    playdemofilechooser, recorddemofilenameentry, recorddemofolderchooser,
    skillcombobox)

def otherskilltoggled(button):
    if button.get_active():
        otherskillentry.set_sensitive(True)
        skillcombobox.set_sensitive(False)
    else:
        otherskillentry.set_sensitive(False)
        skillcombobox.set_sensitive(True)

def othercompleveltoggled(button):
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