# Extract-Files-From-Folders
Extract files from folders but in Python

Directly open/run the python file, and it will open a tkinter file dialog window two times. The first time, is where you will need to select the root folder with the sub-folders to extract files from. The second time, is where all the files will be extracted into.

Alternatively use the terminal by running:
python extract_folders.py -src "" -dst ""

Example
python extract_folders.py -src "C:\Users\Anon\Pictures\GIF" -dst "C:\Users\Anon\Desktop\Extracted_GIFs"

Arguements:  
`-src`  
Source Folder to extract files from.  
`-dst`  
Destination Folder where the files will be extracted into.  
`-copy`  
Boolean: True = Copy files, False = Move files.  
 `-main`  
Boolean: If True, copy files from the root folder as well. (Not working at the moment)  
