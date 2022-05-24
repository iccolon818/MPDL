import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import builder
import config

window = builder.get_object("window")
window.show_all()
window.connect("delete-event", Gtk.main_quit)

builder.connect_signals()

config.configinit()

# This needs to be done manually since GLADE is bugged
portcombobox = builder.get_object("portcombobox")
portcombobox.set_active(0)

iwadcombobox = builder.get_object("iwadcombobox")
iwadcombobox.set_active(0)

skillcombobox = builder.get_object("skillcombobox")
skillcombobox.set_active(0)

complevelcombobox = builder.get_object("complevelcombobox")
complevelcombobox.set_active(0)

configcombobox = builder.get_object("configcombobox")
configcombobox.set_active(0)

Gtk.main()