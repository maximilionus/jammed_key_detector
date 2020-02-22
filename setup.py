import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
	"packages": ["os"],
	"excludes": ["tkinter","unittest","logging","test","http","html","email","distutils","asyncio","pydoc_data"]
}

base = None
""" if sys.platform == "win32":
    base = "Win32GUI" """


setup(  name = "Jammed Key Detector",
        description = "This application will detect the jammed key on keyboard.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, targetName='Jammed Key Detector')])