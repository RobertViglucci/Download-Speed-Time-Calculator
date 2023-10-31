from cx_Freeze import setup, Executable

base = None    

executables = [Executable("downloadspeedtimecalc.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "DSTC",
    options = options,
    version = "1.0",
    description = 'download speed time calculator',
    executables = executables
)