# iPhone-backup-reconstructor
Python script that will reconstruct an unencrypted iPhone backup folder structure into original folder and file names

It was written and tested in windows but should be pretty easy to modify for use in other operating systems.

## Usage
Just edit the script to point PATH to your unencrypted iPhone backup folder.  Change NEW_PATH to point to an empty folder that you want to have the files copied into.
The script will not modify your backup folder in any way.  It just reads files from there and copies them to the new folder with their original path and file name.
