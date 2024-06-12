import sys

argc = len(sys.argv)
vimFlag = False

if argc == 1 or argc != 2:
    print("Usage:")
    print("    python3 main.py /path/to/bindings.vim")
    print("    python3 main.py /path/to/bindings.lua")
    quit()

inputFile = sys.argv[1]

def read_vim_keybindings(filepath):
    keybindings = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("map") or line.startswith("nmap") or line.startswith("imap"):
                    parts = line.split()
                    if len(parts) >= 3:
                        command = parts[0]
                        keys = parts[1]
                        action = ' '.join(parts[2:])
                        keybindings[keys] = {'command': command, 'action': action}
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return keybindings


def read_lua_keybindings():
    return

if inputFile.endswith(".vim"):
    print("Vim Bindings File passed in.")
    keybindings = read_vim_keybindings(inputFile)
    print("Key      Command      Action")
    for keys, details in keybindings.items():
        print(f"{keys}, {details['command']}, {details['action']}")


