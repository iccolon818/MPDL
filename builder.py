import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("MPDL.glade")

def get_object(obj):
    return builder.get_object(obj)

def connect_signals():
    import connect
    builder.connect_signals(connect.handlers)