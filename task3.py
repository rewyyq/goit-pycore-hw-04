import sys
from pathlib import Path
from colorama import Fore

p = Path(sys.argv[1])
print(Fore.BLUE, str(p.name) + "/")
try:  
    def parse_folder(path: Path, indent: int):
        for el in path.iterdir():
            if el.is_dir():
                print(Fore.BLUE, "    " * indent, str(el.name) + "/")
                parse_folder(el, indent + 1)
            else:
               print(Fore.GREEN, "    " * indent, el.name)
    parse_folder(p, 1)
except FileNotFoundError:
    print("Incorrect path")
except NotADirectoryError:
    print("This file path, not a directory")