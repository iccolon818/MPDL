from gi import require_version
require_version('Gtk', '3.0')
from gi.repository.Gtk import Builder
import os
import sys

builder = Builder()
dir = os.path.dirname(sys.argv[0])
builder.add_from_file(dir + "/MPDL.glade")

def get_object(obj):
    return builder.get_object(obj)

def connect_signals():
    import connect
    builder.connect_signals(connect.handlers)
