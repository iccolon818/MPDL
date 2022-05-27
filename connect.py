import config
import deh
import dialogs
import play
import pwads
import toggles

handlers = {
    
    # Permanent Settings
    "on_addportbutton_clicked": dialogs.addportbuttonclicked,
    "on_removeportbutton_clicked": dialogs.removeportbuttonclicked,
    "on_portchooser_selection_changed": dialogs.portchooserselectionchanged,
    "on_portcancelbutton_clicked": dialogs.portcancelbuttonclicked,
    "on_portselectbutton_clicked": dialogs.portselectbuttonclicked,
    "on_portnamecancelbutton_clicked": dialogs.portnamecancelbuttonclicked,
    "on_portnameokbutton_clicked": dialogs.portnameokbuttonclicked,

    "on_addiwadbutton_clicked": dialogs.addiwadbuttonclicked,
    "on_removeiwadbutton_clicked": dialogs.removeiwadbuttonclicked,
    "on_iwadchooser_selection_changed": dialogs.iwadchooserselectionchanged,
    "on_iwadcancelbutton_clicked": dialogs.iwadcancelbuttonclicked,
    "on_iwadselectbutton_clicked": dialogs.iwadselectbuttonactiate,
    "on_iwadnamecancelbutton_clicked": dialogs.iwadnamecancelbuttonclicked,
    "on_iwadnameokbutton_clicked": dialogs.iwadnameokbuttonclicked,

    # PWAD List
    "on_clearpwadsbutton_clicked": pwads.clearpwadsbuttonclicked,
    "on_addpwadbutton_clicked": pwads.addpwadbuttonclicked,
    "on_removepwadbutton_clicked": pwads.removepwadbuttonclicked,
    "on_pwadchooser_selection_changed": pwads.pwadchooserselectionchanged,
    "on_pwadcancelbutton_clicked": pwads.pwadcancelbuttonclicked,
    "on_pwadselectbutton_clicked": pwads.pwadselectbuttonactiate,
    "on_pwadmergecheckbutton_toggled": pwads.pwadmergecheckbuttontoggled,

    # Dehacked List
    "on_cleardehpatchesbutton_clicked": deh.cleardehpatchesbuttonclicked,
    "on_adddehpatchbutton_clicked": deh.adddehpatchbuttonclicked,
    "on_removedehpatchbutton_clicked": deh.removedehpatchbuttonclicked,
    "on_dehchooser_selection_changed": deh.dehchooserselectionchanged,
    "on_dehcancelbutton_clicked": deh.dehcancelbuttonclicked,
    "on_dehselectbutton_clicked": deh.dehselectbuttonactiate,

    # Configs
    "on_saveconfigbutton_clicked": config.saveconfigbuttonclicked,
    "on_loadconfigbutton_clicked": config.loadconfigbuttonclicked,
    "on_deleteconfigbutton_clicked": config.deleteconfigbuttonclicked,
    "on_cfgnamecancelbutton_clicked": config.cfgnamecancelbuttonclicked,
    "on_cfgnameokbutton_clicked": config.cfgnameokbuttonclicked,
    "on_overwritenobutton_clicked": config.overwritenobuttonclicked,
    "on_overwriteyesbutton_clicked": config.overwriteyesbuttonclicked,

    # Misc button handlers
    "on_otherskillcheckbox_toggled": toggles.otherskilltoggled,
    "on_othercomplevelcheckbox_toggled": toggles.othercompleveltoggled,
    "on_demononeradiobutton_toggled": toggles.demononeradiobuttontoggled,
    "on_demoplayradiobutton_toggled": toggles.demoplayradiobuttontoggled,
    "on_demorecordradiobutton_toggled": toggles.demorecordradiobuttontoggled,
    
    # Play Button
    "on_playbutton_clicked": play.launchgame
}