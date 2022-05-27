import builder

from objects import (pwadchooser, pwadlist, pwadlisttreeview, pwadpathentry)

def clearpwadsbuttonclicked(button):
    pwadlist.clear()

def addpwadbuttonclicked(button):
    pwadchooser.show()

def removepwadbuttonclicked(button):
    removelist = pwadlisttreeview.get_selection().get_selected_rows()[1]
    for path in reversed(removelist):
        pwadlist.remove(pwadlist.get_iter(path))

def pwadchooserselectionchanged(chooser):
    filelist = ""
    for name in chooser.get_filenames():
        filelist = (filelist + name + " ")
    
    pwadpathentry.set_text(filelist)

def pwadcancelbuttonclicked(button):
    pwadpathentry.set_text("")
    pwadchooser.hide()

def pwadselectbuttonactiate(button):
    pwadpathentry.set_text("")
    pwadchooser.hide()

    for file in pwadchooser.get_files():
        pwadlist.append([file.get_basename(), file.get_path(), False])
        print([file.get_basename(), file.get_path(), False])

def pwadmergecheckbuttontoggled(button, path):
    iter = pwadlist.get_iter(path)
    pwadlist.set_value(iter, 2, not pwadlist.get_value(iter, 2))