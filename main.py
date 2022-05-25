from builder import connect_signals
from config import configinit
from gi import require_version

require_version('Gtk', '3.0')
from gi.repository.Gtk import (main, main_quit)

import config

from objects import (complevelcombobox, configcombobox, iwadcombobox, 
    portcombobox, skillcombobox, window)

connect_signals()
configinit()

# This needs to be done manually since GLADE is bugged
complevelcombobox.set_active(0)
configcombobox.set_active(0)
iwadcombobox.set_active(0)
portcombobox.set_active(0)
skillcombobox.set_active(0)

window.show_all()
window.connect("delete-event", main_quit)

main()