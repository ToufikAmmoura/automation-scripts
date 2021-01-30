#! python3
import os, datetime, time, send2trash

# README: simple script that removes the files in the folder that are older than 1 day and puts the names of the removed files in a textfile

PATH = "C:\\Users\\toufi\\Downloads"                    # Enter the path of your Downloads-folder (or any other folder that you want to keep clean) e.g.: "C:\\Users\\name\\Downloads"
NR_SECONDS_DAY = 86400

def main():
    documentsList = os.listdir(PATH)                            # Getting all the filenames in the folder
    removedFiles = open(PATH + '\\removedFiles.txt', 'a')       # The file to save the removed file-names
    
    currentDate = datetime.datetime.now()
    removedFiles.write( currentDate.strftime("%H:%M %d %B %Y") + "\n\n" )

    nowEpoch = time.time()
    yesterDayEpoch = nowEpoch - NR_SECONDS_DAY

    for filename in documentsList:
        if( filename == "removedFiles.txt" ):
            continue
        creationTimeEpoch = os.path.getctime(PATH + "\\" + filename) # Epoch time of the file

        if( yesterDayEpoch > creationTimeEpoch ):
            removedFiles.write( filename + "\n" )               # Entering the filename in the removedFiles document
            send2trash.send2trash( PATH + "\\" + filename )     # Removing the file
    
    removedFiles.write("\n")
    removedFiles.close

main()