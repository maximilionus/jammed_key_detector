import sys
from cx_Freeze import setup, Executable

include_files = ['config.ini']
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "include_files": include_files}

base = None
""" if sys.platform == "win32":
    base = "Win32GUI" """


setup(  name = "Jammed Key Detector",
        version = "1.1",
        description = "This application will detect the jammed key on keyboard.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, targetName='Jammed Key Detector')])