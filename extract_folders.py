import tkinter as tk
import tkinter.filedialog as tk_filedialog
import os
from shutil import copy, Error, ExecError, ReadError, RegistryError, SameFileError, SpecialFileError

blacklist_file = [".zip"]
blacklist_folder = ["S"]

class ExtractFiles:
    def __init__(self, src: str, dst: str, mode: bool):
        self.src_folder = src
        self.dst_folder = dst
        self.mode = mode
        self.walk_folders()

    def walk_folders(self):
        for i, (dirpath, dirs, files) in enumerate(os.walk(self.src_folder)):
            """
            dirpath: the current directory in the loop
            dirs: list of sub-directories in the currrent directory of the loop
            files list of files in the current directory of the loop
            """
            if dirpath is not self.src_folder and self.check_blacklist_folder(dirpath) is True:
                for f in files:
                    if self.check_blacklist_file(f):
                        self.copy_file(f, dirpath)

    def check_blacklist_folder(self, folder):
        name = os.path.split(folder)[-1]
        if name in blacklist_folder:
            return False
        else:
            return True

    def check_blacklist_file(self, file):
        extension = os.path.splitext(file)[-1]
        if extension in blacklist_file:
            return False
        else:
            return True

    def copy_file(self, file, dirpath):
        try:
            src = os.path.join(dirpath, file)
            print(f"Copying: {src} ...")
            copy(src, os.path.join(self.dst_folder, file))
        except (Error, ExecError, ReadError, RegistryError, SameFileError, SpecialFileError):
            print("FAILED")


if __name__ == "__main__":
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-alpha", 0)
    src_path = tk_filedialog.askdirectory()
    if src_path == "" or os.path.exists(src_path) is False:
        raise Exception("No Folder selected or folder does not exists.")
    else:
        dst_path = tk_filedialog.askdirectory()
        if dst_path == "" or os.path.exists(dst_path) is False:
            raise Exception("No Folder selected or folder does not exists.")
    ExtractFiles(src_path, dst_path, True)
