"""
NumberScript Package Manager
-------------------------
- created by Sas2k 2022 -
-------------------------
"""

import os
import argparse

ver = "0.1.0-beta"
parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest='command')

extends_libs = """%The-Extends-Library-For-NumberScript
%By-Sasen-Perera-2022
%
%This-library-is-used-to-make-the-normal-single-character-commands-into-more-readable-functions.
0
7print$string$2string
7print_char$string,index$2@string.index
7input$string$~string
7bool$val1,val2,sign$?sign==|4val1=val2|?sign=!|4val1!val2|?sign=>|4val1>val2|?sign=<|4val1<val2|2Error:Invalid-sign
1"""

#commands
# install = subparser.add_parser("install", help="install a package")
# uninstall = subparser.add_parser("uninstall", help="uninstall a package")
list = subparser.add_parser("list", help="list all installed packages")
version = subparser.add_parser("version", help="show version")

# setups
init = subparser.add_parser("init", help="initialize package manager")
setup = subparser.add_parser("setup", help="setup package manager")

#flags
# install.add_argument("-g", "--global", action="store_true", help="install globally")
# uninstall.add_argument("-g", "--global", action="store_true", help="uninstall globally")
setup.add_argument("-U", "--update", action="store_true", help="update setup")

args = parser.parse_args()

def main():
    if args.command == "init":
        if not os.path.exists("Libs"):
            os.mkdir("Libs")
            print("Package Initialized.")
        else:
            print("Package already initialized.")
    elif args.command == "version":
        print(f"Version: {ver}")
    elif args.command == "list":
        print("Installed Packages:")
        if os.path.exists("Libs"):
            for i in os.listdir("Libs"):
                print(i)
        else:
            for i in os.listdir("C:\\" + os.environ["homepath"] + "\\NumberScript\\Libs\\" if os.name == "nt" else os.environ["HOME"] + "/NumberScript/Libs/"):
                print(i)
    elif args.command == "setup":
        if os.name == "nt":
            if not os.path.exists("C:\\" + os.environ["homepath"] + "\\NumberScript\\Libs\\"):
                os.mkdir("C:" + os.environ["homepath"] + "\\NumberScript")
                os.mkdir("C:" + os.environ["homepath"] + "\\NumberScript\\Libs")
                with open("C:" + os.environ["homepath"] + "\\NumberScript\\Libs\\extends.ns", "w+") as f:
                    f.write(extends_libs)
                print("Package Manager Setup.")
            elif args.update:
                if not os.path.exists("C:\\" + os.environ["homepath"] + "\\NumberScript\\Libs\\"):
                    os.mkdir("C:" + os.environ["homepath"] + "\\NumberScript")
                    os.mkdir("C:" + os.environ["homepath"] + "\\NumberScript\\Libs")
                with open("C:" + os.environ["homepath"] + "\\NumberScript\\Libs\\extends.ns", "w+") as f:
                    f.write(extends_libs)
                print("Package Manager Setup Updated.")
            else:
                print("Package Manager already setup.")
        else:
            if not os.path.exists(os.environ["HOME"] + "/NumberScript/Libs/"):
                os.mkdir(os.environ["HOME"] + "/NumberScript/")
                os.mkdir(os.environ["HOME"] + "/NumberScript/Libs/")
                print("Package Manager Setup.")
            else:
                print("Package Manager already setup.")

if __name__ == "__main__":
    main()