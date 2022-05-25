import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from builder import get_object

# Toplevels
cfgnamedialog = get_object("cfgnamedialog")
dehchooser = get_object("dehchooser")
iwadchooser = get_object("iwadchooser")
iwadnamedialog = get_object("iwadnamedialog")
portchooser = get_object("portchooser")
portnamedialog = get_object("portnamedialog")
pwadchooser = get_object("pwadchooser")
window = get_object("window")


# Liststores
complevellist = get_object("complevellist")
configlist = get_object("configlist")
dehlist = get_object("dehlist")
iwadlist = get_object("iwadlist")
portlist = get_object("portlist")
pwadlist = get_object("pwadlist")
skilllist = get_object("skilllist")

# Widgets
cfgnameentry = get_object("cfgnameentry")
complevelcombobox = get_object("complevelcombobox")
configcombobox = get_object("configcombobox")
dehlumpcheckbox = get_object("dehlumpcheckbox")
dehpathentry = get_object("dehpathentry")
dehlisttreeview = get_object("dehlisttreeview")
demononeradiobutton = get_object("demononeradiobutton")
demoplayradiobutton = get_object("demoplayradiobutton")
demorecordradiobutton = get_object("demorecordradiobutton")
extraargsentry = get_object("extraargsentry")
fastmonsterscheckbox = get_object("fastmonsterscheckbox")
iwadcombobox = get_object("iwadcombobox")
iwadnameentry = get_object("iwadnameentry")
iwadpathentry = get_object("iwadnameentry")
noautoloadcheckbox = get_object("noautoloadcheckbox")
nomonsterscheckbox = get_object("nomonsterscheckbox")
nomusiccheckbox = get_object("nomusiccheckbox")
othercomplevelcheckbox = get_object("othercomplevelcheckbox")
othercomplevelentry = get_object("othercomplevelentry")
otherskillcheckbox = get_object("otherskillcheckbox")
otherskillentry = get_object("skillentry")
pistolstartcheckbox = get_object("pistolstartcheckbox")
playdemofilechooser = get_object("playdemofilechooser")
portcombobox = get_object("portcombobox")
portnameentry = get_object("portnameentry")
portpathentry = get_object("portpathentry")
pwadlisttreeview = get_object("pwadlisttreeview")
pwadpathentry = get_object("pwadpathentry")
recorddemofilenameentry = get_object("recorddemofilenameentry")
recorddemofolderchooser = get_object("recorddemofolderchooser")
respawncheckbox = get_object("respawncheckbox")
skillcombobox = get_object("skillcombobox")
solonetcheckbox = get_object("solonetcheckbox")
warpentry = get_object("warpentry")
zdoomstylecheckbox = get_object("zdoomstylecheckbox")