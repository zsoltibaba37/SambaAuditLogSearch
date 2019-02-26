#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Pető"
__license__ = "MIT"
__version__ = "1.0"

from inpcheck import *
import os
from os import walk
import sys
from sys import argv, platform
import codecs

if len(argv) < 3 :
    print("Missing argument! ! !")
    print("Usage:\n"
          "Windows > ausearch.py usernames.txt d:\\somewhere\\audit_log\n"
          "or\n"
          "Linux   $ ausearch.py usernames.txt /somewhere/audit_log")
    sys.exit(1)

c = 120
LogPath = argv[2]
FileNames = []
AllFileContent = []

def clearscreen():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


if platform == "linux" or platform == "linux2":
    fo='/'
elif platform == "win32":
    fo='\\'

def fline():
    print("#"*c)


def line():
    print("")


def beginl():
    fline()
    line()


def endl():
    line()
    fline()


beginl()
print("A log fájlok beolvasása eltarthat néhány másodpercig.".center(c))
print("It may take a few seconds to read the log files.".center(c))
print("[CTRL-C]-re kilép a programból. - Press [CTRL-C] to exit.".center(c))
endl()


# Read usernames from file
with codecs.open(argv[1], 'r', 'UTF-8') as f:
    UserNames = f.read().splitlines()


# Read Filenames
for (dirpath, dirnames, filenames) in walk(LogPath):
    FileNames.extend(filenames)
    break


# Read all Files content
for y in FileNames:
    with codecs.open(LogPath+fo+y, 'r', 'UTF-8') as f:
        for i in f:
            AllFileContent.append(i)


# Filter repeated message
FilElement = [s for s in AllFileContent if "message repeated" not in s]


# Main function
def main():
    try:
        while True:
            #############################################################################################################
            # Readout and ask the user name
            clearscreen()
            fline()
            for i, username in enumerate(UserNames):
                print(f"{i} - {username}")

            fline()
            User = range_check("Válassz felhasználót. - Choose a user. [Ex.: 1]: ", 0, len(UserNames)-1)

            # Collect the selected user data
            User = [s for s in FilElement if UserNames[User] in s]

            # Ask the filename or the file extension
            Data = []
            while len(Data) == 0:
                FindData = name_check("Mi a fájl neve vagy kiterjesztése? - What is the file name or extension? [Ex.: xls; 4012_1.pdf]: ")

                # This is the end result
                Data = [s for s in User if FindData in s]
                if len(Data) == 0:
                    print(f"Nem találta a(z) [{FindData}] fájlt! - Can't find [{FindData}] file!")

            # How many results to list
            bit = (range_check(f"Hány sort listázzon? - How many lines to list? [min:1 max: {len(Data)}]: ", 1, len(Data))) * -1

            beginl()
            # Writes out the requested last result
            y = 1
            for d in Data[bit:]:
                print(f"{y}. {d}", end='')
                y += 1

            endl()
            line()
            print("[CTRL-C]-re kilép a programból. - Press [CTRL-C] to exit.".center(c))
            input("Nyomj egy [Entert] a folytatáshoz! - Press [Enter] to continue!".center(c))
            clearscreen()
            #############################################################################################################
    except KeyboardInterrupt:
        sys.exit("\nViszlát - Bye Bye")


if __name__ == '__main__':
    main()
