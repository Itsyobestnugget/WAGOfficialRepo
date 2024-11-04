import os
import pathlib
import argparse
import sys
import time
import shutil

running = 0


def init():
    print("Using WAG Preview")


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
print("Welcome to WAG Full! Wag full is currently unfinished.")
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
    else:
        print("No more commands avalible. or wrong command")