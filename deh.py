import builder

from objects import (dehchooser, dehpathentry, dehlist, dehlisttreeview)

def cleardehpatchesbuttonclicked(button):
    dehlist.clear()

def adddehpatchbuttonclicked(button):
    dehchooser.show()

def removedehpatchbuttonclicked(button):
    removelist = dehlisttreeview.get_selection().get_selected_rows()[1]
    for path in reversed(removelist):
        dehlist.remove(dehlist.get_iter(path))

def dehchooserselectionchanged(chooser):
    filelist = ""
    for name in chooser.get_filenames():
        filelist = (filelist + name + " ")

    dehpathentry.set_text(filelist)

def dehcancelbuttonclicked(button):
    dehpathentry.set_text("")
    dehchooser.hide()

def dehselectbuttonactiate(button):
    dehpathentry.set_text("")
    dehchooser.hide()
    for file in dehchooser.get_files():
        dehlist.append([file.get_basename(), file.get_path()])
        print([file.get_basename(), file.get_path()])
