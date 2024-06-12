import sys

argc = len(sys.argv)
vimFlag = False

if argc == 1 or argc != 2:
    print("Usage:")
    print("    python3 main.py /path/to/bindings.vim")
    print("    python3 main.py /path/to/bindings.lua")
    quit()

inputFile = sys.argv[1]

if inputFile.endswith(".vim"):
    print("Vim Bindings File passed in.")
    vimFlag = True;

def vimFilePresent():
    return

def luaFilePresent():
    return

