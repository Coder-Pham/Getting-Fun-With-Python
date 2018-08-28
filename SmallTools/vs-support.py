import os
import shutil
from colorama import Fore, init, Style

init()


def main():
    print(Fore.CYAN + '''  
     _   _______________  ___  ____  ______  _____  ___  ____  ___  ______
    | | / / __/ ___/ __ \/ _ \/ __/ / __/ / / / _ \/ _ \/ __ \/ _ \/_  __/
    | |/ /\ \/ /__/ /_/ / // / _/  _\ \/ /_/ / ___/ ___/ /_/ / , _/ / /   
    |___/___/\___/\____/____/___/ /___/\____/_/  /_/   \____/_/|_| /_/    ''')

    print(Fore.LIGHTBLUE_EX +
          "Dev by Coder-Pham\n".center(os.get_terminal_size().columns))
    print(Style.RESET_ALL)
    print('{:^44s}'.format("Option for support in VSCode:"))
    print('{:>15s}'.format("1. C++"))
    print('{:>17s}'.format("2. Java\n"))
    chose = input('{:>20s}'.format("Your option: "))
    dest = input('{:>32s}'.format("Your destination folder: "))

    # Select language folder
    if chose.upper() == 'C++':
        src = os.path.join("vscode-support", "C++")
    else:
        src = os.path.join("vscode-support", "Java")

    # Copy - create
    if not os.path.isdir(os.path.join(dest, ".vscode")):
        os.makedirs(os.path.join(dest, ".vscode"))
    dest = os.path.join(dest, ".vscode")
    files = os.listdir(src)
    for file_name in files:
        shutil.copy2(os.path.join(src, file_name), dest)

    # Done - Print warnings
    if chose.upper() == 'C++':
        print(Fore.YELLOW +
              '\nNow you can use VSCode to build, run, debug without any troubles')
        print('To terminal type: .\\{fileBasenameNoExtension}')
    else:
        print(Fore.YELLOW + '\nNow you can build and run Java file to Class file')
        print('To build:   Tasks >> Run Task >> JC')
        print('To run: Tasks >> Run Task >> JR')
        print(Fore.LIGHTRED_EX + '\nTo Debug: Debug >> Add Configuration')
        print('(launch.json) Change all occurences of ' + Fore.BLUE + '"console"' +
              Fore.LIGHTRED_EX + ' to ' + Fore.BLUE + '"integratedTerminal"')


if __name__ == '__main__':
    main()
    wait = input()
