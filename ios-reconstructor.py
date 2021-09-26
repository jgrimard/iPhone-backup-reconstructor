#! python3
# This python script will re-construct an unencrypted iOS backup folder into a readable folder structure and filenames.
# It does not modify the existing backup file in any way.  
# This script was developed to work on Windows.  With some modification you could use it on other systems.
# JGRIMARD

import sqlite3
import os
import time
from alive_progress import alive_bar
import subprocess
import sys
from shutil import copy2

start = time.time()

PATH = r"F:\iphone_backups\00008030-001A48CA34D8802E"
NEW_PATH = r"F:\iphone_reconstructed\\"

select_statement = """
SELECT
  fileID,
  domain,
  relativePath
FROM
  Files;"""

file_dict = {}
# Create dictionary of file names and paths 
for root, subFolder, files in os.walk(PATH):
    for item in files:
        fileNamePath = str(os.path.join(root,item))
        file_dict[item] = fileNamePath


conn = sqlite3.connect('Manifest.db')
cursor = conn.execute(select_statement)
rows = cursor.fetchall()
num_rows = len(rows)
with alive_bar(num_rows) as bar:
    for row in rows:
        bar()
        fileNamePath = ""
        fileID = str(row[0])
        domain = str(row[1])
        relativePath = str(row[2])
        domain_relativePath = domain + relativePath
        #remove invalid windows characters from path
        domain_relativePath = "".join(i for i in domain_relativePath if i not in ":*?<>|")
        new_filename = NEW_PATH + domain_relativePath
        old_filename = file_dict.get(fileID)
        try:
            if old_filename:
                os.makedirs(os.path.dirname(new_filename), exist_ok=True)
                copy2(old_filename, new_filename)
        except(FileNotFoundError, OSError):
            print("Skipping file :",new_filename)
            
        # print("fileID =",fileID)
        # print("old_filename =",old_filename)
        # print("new_filename =", new_filename)
        # print()



conn.close


print('Script took ', time.time()-start, ' seconds.')

