import argparse
from distutils.util import strtobool
import tkinter as tk
import tkinter.filedialog as tk_filedialog
from os import walk, path
from shutil import copy, move, Error, ExecError, ReadError, RegistryError, SameFileError, SpecialFileError

blacklist_file = [".zip"]
blacklist_folder = ["S"]

class ExtractFiles:
    def __init__(self, src: str, dst: str, mode: bool, main_folder: bool):
        self.src_folder = src
        self.dst_folder = dst
        self.mode = mode
        self.main_folder = main_folder
        self.walk_folders()

    def walk_folders(self):
        for i, (dirpath, dirs, files) in enumerate(walk(self.src_folder)):
            """
            dirpath: the current directory in the loop
            dirs: list of sub-directories in the currrent directory of the loop
            files list of files in the current directory of the loop
            """
            if self.check_blacklist_folder(dirpath) is True:
                if self.main_folder is True or dirpath is not self.src_folder:
                    for f in files:
                        if self.check_blacklist_file(f):
                            if self.mode is True:
                                self.copy_file(f, dirpath)
                            else:
                                self.move_file(f, dirpath)

    def check_blacklist_folder(self, folder):
        name = path.split(folder)[-1]
        if name in blacklist_folder:
            return False
        else:
            return True

    def check_blacklist_file(self, file):
        extension = path.splitext(file)[-1]
        if extension in blacklist_file:
            return False
        else:
            return True

    def copy_file(self, file, dirpath):
        try:
            src = path.join(dirpath, file)
            print(f"Copying: {src} ...")
            copy(src, path.join(self.dst_folder, file))
        except (Error, ExecError, ReadError, RegistryError, SameFileError, SpecialFileError):
            print("FAILED")

    def move_file(self, file, dirpath):
        try:
            src = path.join(dirpath, file)
            print(f"Moving: {src} ...")
            move(src, path.join(self.dst_folder, file))
        except (Error, ExecError, ReadError, RegistryError, SameFileError, SpecialFileError):
            print("FAILED")


def check_if_folder_exists(folder):
    if folder == "" or path.exists(folder) is False:
        return False
    else:
        return True


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-src",
                    default=None, type=str,
                    help="Source Folder to extract files from")
    ap.add_argument("-dst",
                    default=None, type=str,
                    help="Destination Folder where the files will be extracted into")
    ap.add_argument("-copy", type=lambda x: bool(strtobool(x)),
                    default=True,
                    help="True = Copy files, False = Move files")
    ap.add_argument("-main", type=lambda x: bool(strtobool(x)),
                    default=True,
                    help="Copy/Move main folder as well")
    args = vars(ap.parse_args())
    if args['src'] is not None and args['dst'] is not None:
        if check_if_folder_exists(args['src']) and check_if_folder_exists(args['dst']):
            ExtractFiles(args['src'], args['dst'], args['copy'], args['main'])
    else:
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-alpha", 0)
        src_path = tk_filedialog.askdirectory()
        if check_if_folder_exists(src_path):
            dst_path = tk_filedialog.askdirectory()
            if check_if_folder_exists(dst_path):
                ExtractFiles(src_path, dst_path, True, True)
            else:
                raise Exception("No Folder selected or folder does not exists.")
        else:
            raise Exception("No Folder selected or folder does not exists.")
