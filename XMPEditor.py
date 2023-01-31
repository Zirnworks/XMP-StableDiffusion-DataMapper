import subprocess
from os import listdir
from os.path import isfile, join

# Usage: Place this file with the conf.ExifTool_config file. Place all images in the images folder. Run the script.

# Where should I look for the images?
folderName = "images"

fileNames = [f for f in listdir(folderName) if isfile(join(folderName, f))]


def getFlags(fileName):

    result = subprocess.run(
        f'.\exiftool.exe {fileName} -Parameters', capture_output=True).stdout.decode('utf-8')

    print(result)
    # Remove the first 34 characters
    result = result[34:]

    # Extract everything up to the word "Steps"
    prompt = result.split("Steps")[0]

    # Extract everything after the word "Steps", adding the word "Steps"
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

    return flags

# command = f'.\exiftool.exe -config \conf.ExifTool_config {flags} TestImg.png'


# output = subprocess.run(command, capture_output=True).stdout.decode('utf-8')

# Iterate through all files in a directory
for fileName in fileNames:
    fileName = f".\{folderName}\\" + fileName
    command = f'.\exiftool.exe -config \conf.ExifTool_config {getFlags(fileName)} {fileName} -overwrite_original'
    output = subprocess.run(
        command, capture_output=True).stdout.decode('utf-8')
    print(output)
