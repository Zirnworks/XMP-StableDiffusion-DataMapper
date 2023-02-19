import subprocess
from os import listdir
from os.path import isfile, join

# Usage: Place this file with the conf.ExifTool_config file. Place all images in the images folder. Run the script.

# Where should I look for the images?

print("XMPEditor.py Version 1.0.2.")

folderName = input(
    "Enter the fully qualified path to the folder containing the images, or press enter to use the folder this script is in:\n")
if folderName == "":
    folderName = "."

print("Now looking for images in " + folderName)

fileNames = 0

while fileNames == 0:
    fileNames = [f for f in listdir(folderName) if isfile(join(folderName, f))]
    # filter out all files that aren't png
    fileNames = [f for f in fileNames if f.split(".")[-1] == "png"]


def getFlags(fileName):
    command = f'.\exiftool.exe -Parameters "{fileName}"'
    result = subprocess.run(
        command, capture_output=True).stdout.decode('utf-8')
    # See if the word "Steps" is in the output
    if "Steps" not in result:
        print(f"ExifTool failed to parse: {fileName}")
        return ""

    # Remove the first 34 characters
    result = result[34:]

    negativePrompt = ""
    
    # Extract everything up to the word "Steps"
    if "Negative prompt" in result:
        prompt = result.split("Negative prompt")[0]
        # Extract everything after the word "Negative prompt", up to the word "Steps"
        negativePrompt = result.split("Negative prompt: ")[1]
        negativePrompt = negativePrompt.split("Steps")[0]
    else:
        prompt = result.split("Steps")[0]

    result = "Steps" + result.split("Steps")[1]

    # Extract keyvalue pairs from csv string
    keyValuePairs = result.split(",")

    keyValuePairs = [x.strip() for x in keyValuePairs]

    keyValuePairs = [x.split(":") for x in keyValuePairs]

    # Remove spaces from keys
    keyValuePairs = [[x[0].replace(" ", ""), x[1]] for x in keyValuePairs]
    # Remove empty key value pairs
    keyValuePairs = [x for x in keyValuePairs if len(x) == 2]
    keyValuePairs = [x for x in keyValuePairs if x[0] != ""]
    keyValuePairs = [x for x in keyValuePairs if x[1] != ""]

    # Remove spaces from values
    keyValuePairs = [[x[0], x[1].strip()] for x in keyValuePairs]

    keyValuePairs = [[x[0], x[1].replace("\'", "")]
                     for x in keyValuePairs]

    keyValuePairs = {x[0]: x[1] for x in keyValuePairs}

    # Turn the dictionary into one long string of file flags

    flags = [f"-{key}=\"{value}\"" for key, value in keyValuePairs.items()]
    flags = " ".join(flags)
    flags = "-Prompts=" + f'"{prompt}"' + " " + flags
    
    

    if negativePrompt != None:
        flags = flags + " " + "-NegativePrompt=" + f'"{negativePrompt}"'
    
    return flags

# command = f'.\exiftool.exe -config \conf.ExifTool_config {flags} TestImg.png'


# output = subprocess.run(command, capture_output=True).stdout.decode('utf-8')
failedFiles = []
# Iterate through all files in a directory
numFiles = len(fileNames)
currentProgress = 0
for fileName in fileNames:
    currentProgress += 1
    print("Processing " + fileName + f": File {currentProgress} of {numFiles}")
    fileName = f"{folderName}\\" + fileName
    flags = getFlags(fileName)
    if flags == "":
        failedFiles.append(fileName)
        continue
    # -overwrite_original'
    command = f'.\exiftool.exe -config \conf.ExifTool_config {flags} "{fileName}" -overwrite_original'

    output = subprocess.run(
        command, capture_output=True).stdout.decode('utf-8')


if len(failedFiles) > 0:
    print("Failed to parse the following files:")
    for file in failedFiles:
        print(file)
    print("These filenames have been added to FailedFiles.txt")
    failedFiles = "\n".join(failedFiles)
    with open("FailedFiles.txt", "w") as f:
        f.write(failedFiles)
    input("Press enter to exit")
else:
    print("All files parsed successfully")
    input("Press enter to exit")
