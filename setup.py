import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(name = "MPDL",
	version = "0.1",
	description = "",
	executables = [Executable("main.py", base=base, 
		target_name="MPDL")],
	options = {
		"build_exe": {
			"includes": ["gi._error"],
			"include_files": ["./MPDL.glade"],
			'packages': ["gi"]
		}
	})
