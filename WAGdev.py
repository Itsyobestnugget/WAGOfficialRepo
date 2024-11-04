import os
import pathlib
import argparse
import sys
import time
import shutil
import hashlib
import base64
import git
import inspect
from colorama import init as colorama_init
from colorama import Fore
from colorama import Back
from colorama import Style
import git.repo
from waginstall import depinstall
from waginstall import depupdate
from waginstall import uninstall
# from wagai import aios
colorama_init()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OK = '\033[92m'
    WARN = '\033[93m'
    ERR = '\033[31m'
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    BOLD = '\033[1m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

    HEADER = '\033[95m' + BOLD
    PASS = OK + BOLD
    FAIL = ERR + BOLD

    OKMSG = BOLD + OK + u'\u2705' + "  "
    ERRMSG = BOLD + FAIL + u"\u274C" + "  "
    WAITMSG = BOLD + WARN + u'\u231b' + "  "

    HELP = WARN
    BITALIC = BOLD + ITALIC
    BLUEIC = BITALIC + OK
    END = ENDC
def get_source_code():
    """
    Extracts the source code of the current file.
    """
    frame = inspect.currentframe()
    try:
        # Get the frame object of the caller
        caller_frame = inspect.getouterframes(frame)[1]
        # Extract the source code from the frame object
        source_code = inspect.getsource(caller_frame[0])
        return source_code
    finally:
        # Release the frame to avoid potential issues
        del frame
# Get the source code and print it

running = 0
user = "user"

def init():
    print("Using WAG Dev")


init()
running = 1
#command enabling system. these are ignored in admin. to turn off admin set cmd_enteraminenabled to 0
cmd_direnabled = 1
cmd_cdenabled = 1
cmd_fileinfoenabled = 1
cmd_mkfileenabled = 1
cmd_mkdirenabled = 1
cmd_gotoenabled = 1
cmd_feditenabled = 1
cmd_fdelenabled = 1
cmd_helpenabled = 1
cmd_infoenabled = 1
cmd_enteradminenabled = 1
cmd_systeminfoenabled = 1
cmd_whoamienabled = 1
print("Welcome to WAG Development")
while running == 1:
    i = input("user: ")
    if i == "dir":
        if cmd_direnabled == 1:
            print(os.listdir())
        else:
            print("command disabled")
    if i == "cd":
        if cmd_cdenabled == 1:
            os.chdir(input("path: "))
        else:
            print("command disabled")
    if i == "fileinfo":
        if cmd_fileinfoenabled == 1:
            fi = input("file: ")
            if os.path.isfile(fi):
                # Get file information using os.stat()
                file_stats = os.stat(fi)
                # Extract information from the stat_result object
                file_size = file_stats.st_size
                file_modified_time = time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(file_stats.st_mtime))
                file_created_time = time.strftime(
                    '%Y-%m-%d %H:%M:%S', time.localtime(file_stats.st_ctime))
                file_extension = os.path.splitext(fi)[1]
                # Print the information
                print(f"File Name: {fi}")
                print(f"File Size: {file_size} bytes")
                print(f"Date Modified: {file_modified_time}")
                print(f"Date Created: {file_created_time}")
                print(f"File Extension: {file_extension}")
            else:
                print(f"File '{fi}' not found.")
        else:
            print("command disabled")
    if i == "quit":
        running = 0
    if i == "mkfile":
        if cmd_mkfileenabled == 1:
            mkfile = input("file: ")
            if os.path.isfile(mkfile):
                print("file already exists")
            else:
                with open(mkfile, 'w') as f:
                    f.write('')
                    f.close()
                print("file created")
        elif cmd_mkfileenabled == 0:
            print("command disabled")
    if i == "mkdir":
        if cmd_mkdirenabled == 1:
            mkdir = input("directory: ")
            if os.path.isdir(mkdir):
                print("directory already exists")
            else:
                os.mkdir(mkdir)
                print("directory created")
        elif cmd_mkdirenabled == 0:
            print("command disabled")
    if i == "goto":
        if cmd_gotoenabled == 1:
            goto = input("path: ")
            if os.path.isdir(goto):
                os.chdir(goto)
            else:
                print("path not found")
        elif cmd_gotoenabled == 0:
            print("command disabled")
    if i == "fedit":
        if cmd_feditenabled == 1:
            fedit = input("file: ")
            if os.path.isfile(fedit):
                etype = input(
                    "edit type (a - append(adds information to a file), w - write(replaces everything in the file with input)): "
                )
                f = open(fedit, etype)
                print("opened file")
                fwritesys = input("input (use \\n for new lines :>): ")
                f.write(fwritesys)
                print("File Updated")
                f.close()
            else:
                print("file not found")
        elif cmd_feditenabled == 0:
            print("command disabled")
    if i == "fdel":
        if cmd_fdelenabled == 1:
            fdel = input("file: ")
            if os.path.isfile(fdel):
                os.remove(fdel)
                print("file deleted")
            else:
                print("file not found")
        elif cmd_fdelenabled == 0:
            print("command disabled")
    if i == "help":
        print(
            "welcome to WAG TOOLS help! here is a list of commands: \n dir - shows all files in current directory \n cd - changes directory \n fileinfo - shows file information\n help - shows this message \n quit - quits the program \n mkfile - creates a file \n mkdir - creates a directory \n goto - changes directory to a path \n fedit - edits a file \n fdel - deletes a file\n systeminfo - shows system information \n whoami - shows who you are \n editlevel - shows your edit level \n"
        )
    if i == "recycle":
        file_path = input("File path: ")
        dest_dir = "bin"
        if os.path.isfile(file_path):
            if os.path.isdir(dest_dir):
                try:
                    shutil.copy2(file_path, dest_dir)
                    print(f"File '{file_path}' recycled to '{dest_dir}'")
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error copying file: {e}")
            else:
                print(
                    f"bin '{dest_dir}' does not exist. try mkbin and then run this command again"
                )
        else:
            print(f"File '{file_path}' not found.")
    if i == "restore":
        file_name = input("File name: ")
        bin_dir = "bin"  # The directory where recycled files are stored
        current_dir = os.getcwd()  # Get the user's current directory
        source_path = os.path.join(bin_dir, file_name)
        dest_path = os.path.join(current_dir, file_name)
        if os.path.isfile(source_path):
            try:
                shutil.move(source_path, dest_path)  # Move the file
                print(f"File '{file_name}' restored to current directory.")
            except Exception as e:
                print(f"Error restoring file: {e}")
        else:
            print(f"File '{file_name}' not found in 'bin' directory.")
    if i == "emptybin":
        bin_dir = "bin"
        if os.path.isdir(bin_dir):
            try:
                # Get a list of files in the bin directory
                files = os.listdir(bin_dir)
                for file in files:
                    # Construct the full path to the file
                    file_path = os.path.join(bin_dir, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                print(f"bin directory '{bin_dir}' emptied.")
            except Exception as e:
                print(f"Error emptying bin directory: {e}")
        else:
            print(f"bin directory '{bin_dir}' does not exist.")
    if i == "mkbin":
        bin_dir = "bin"
        if not os.path.exists(bin_dir):
            try:
                os.mkdir(bin_dir)
                print(f"bin directory '{bin_dir}' created.")
            except Exception as e:
                print(f"Error creating bin directory: {e}")
        else:
            print(f"bin directory '{bin_dir}' already exists.")
    if i == "systeminfo":
        if cmd_systeminfoenabled == 1:
            print("info \nos: " + sys.platform + "\nversion: " + sys.version)
        else:
            print("command disabled")
    if i == "whoami":
        if cmd_whoamienabled == 1:
            print("user: " + os.environ['USER'])
        else:
            print("command disabled")
    if i == "syscall":
        if user == "admin":
            syscall = input("command: ")
            os.system(syscall)
        elif user != "admin":
            print("Cannot run SYSCALL in normal mode!")
    if i == "enteradmin":
        if cmd_enteradminenabled == 1:
            if user != "admin":
                print("entering admin mode")
                user = "admin"
            elif user == "admin":
                print("already in admin mode")
        else:
            print("command disabled")
    if i == "exitadmin":
        if cmd_enteradminenabled == 1:
            if user == "admin":
                user = "user"
            elif user != "admin":
                print("not in admin mode")
        else:
            print("command disabled")
    if i == "riplit":
        print("riplit allows you to see this packages source code. source will be displayed below. {bcolors.WARN}please only use source from the official git download unless it contains the licence and TOuse :){bcolors.ENDC} \n\n")
        source = get_source_code()
        print(source)
    if i == "update":
        depupdate()
    if i == "Lok":
        print(f"{bcolors.FAIL}LOK Command is not avalible! sadly the ai wants to not work. this is an active issue, if you want to work on it you can. your choice. please send a push with the issue fixed to the original repository{bcolors.ENDC}")
    if i == "git":
        i = input("git call: ")
        print(f"{bcolors.FAIL}git command is in progress! im completly self taught and dont often use git commmands (ever used them actually) if you want to implimemnt this command work on it yourself and send a push{bcolors.ENDC}")
    if i == "hashit":
        i = input("Please enter hashable object: ")
        print(hash(i))
    if i == "base64it":
        i = input("string: ")
        o = ""
        base64.encode(i, o)
        print(o)
    if i == "decrypt64":
        i == input.read("string: ")
        o = ""
        base64.decode(i, o)
        print(o)
    else:
        print(f"{bcolors.FAIL}No more commands avalible. or wrong command{bcolors.ENDC}")