from download import downloadFile 
from zipfile import ZipFile
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove


def extractZipFile(zipFileToExtractFrom, csvFileToExtract, folderToWriteTo):
    with ZipFile(zipFileToExtractFrom, 'r') as zipObj:
        # Get a list of all archived file names from the zip
        listOfFileNames = zipObj.namelist()
        # Iterate over the file names
        for fileName in listOfFileNames:
            # Check filename endswith csv
            print(fileName)
            if fileName.lower() == csvFileToExtract.lower():
                # Extract a single file from zip
                zipObj.extract(fileName, folderToWriteTo)

def renameFile(existingFileName, newFileName):
    move(existingFileName,newFileName)

def replaceStringInFile(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                # replacing the header
                newLine = line.replace(pattern, subst)
                
                #TODO: move this to different method or see how can we include this logic within this method as right now it does not make sense with the name and we are doing two functionalities like replacing header and removing special characters at the end of the line
                
                #this is to remove the extra , at the end of the line. we cannot just strip it as we have \n \r at the end of the line already. so we have move from right to left until we find alnum() character. for non alphanum characters we see if it is comma(,) then we remove the comma(,) else we go to next character at the left. we are also handing cases like if there are two ,, then it is a valid empty column. so we are ignoring it and only replacing single comma in the end of the string
                specialCharacter = ","
                index = len((newLine)) -1 
                while(newLine[index].isalnum() == False):
                    if(newLine[index] == specialCharacter and newLine[index-1] == specialCharacter):
                        index = index -2
                    elif(newLine[index] == specialCharacter and newLine[index-1] != specialCharacter):
                        newLine = newLine[0 : index : ] + newLine[index + 1 : :]
                    else:
                        index = index -1
                
                # print("after striping: " + newLine)
                new_file.write(newLine)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


def getDownloadedFile(metadataToDownload):
    urlToDownload = metadataToDownload['urlToDowndoad']
    completZipFilePathToDownload = metadataToDownload['completZipFilePathToDownload']
    csvFileToExtract = metadataToDownload['csvFileToExtract']
    folderToExtract = metadataToDownload['folderToExtract']
    completeCsvFilePathToExtract = metadataToDownload['completeCsvFilePathToExtract']
    newCompleteCsvFilePathToRename = metadataToDownload['newCompleteCsvFilePathToRename']
    

    # download the zip
    print("Downloading " + completZipFilePathToDownload + " from " + urlToDownload)
    downloadFile(urlToDownload, completZipFilePathToDownload)


    #extract zip file
    print("Extracting " + csvFileToExtract + " from " + completZipFilePathToDownload  + " to " + folderToExtract)
    extractZipFile(completZipFilePathToDownload, csvFileToExtract, folderToExtract)

    # delete zip file
    print("Deleting " + completZipFilePathToDownload)
    remove(completZipFilePathToDownload)

    # rename file
    print("Renaming " + completeCsvFilePathToExtract + " to " + newCompleteCsvFilePathToRename)
    renameFile(completeCsvFilePathToExtract, newCompleteCsvFilePathToRename)

    # replacing headers
    # TODO: need to add some checks to validate existing headers and make sure we are getting proper headers and then replace them
    # TODO: move this logic to some csvutil or some other utsil. This should not be in download and extract
    print("Replacing headers in " + newCompleteCsvFilePathToRename)
    newHeader = metadataToDownload['newHeader']
    existingHeader = metadataToDownload['existingHeader']
    replaceStringInFile(newCompleteCsvFilePathToRename, existingHeader, newHeader)
    return newCompleteCsvFilePathToRename



