# XMP-StableDiffusion-DataMapper
A Data remapping tool that batch converts image metadata from the volatile format that Stable Diffusion has to the stable XMP format using ExifTool

## Requirements
Python 3.10+ 

## Usage
The app is set up to convert all images that are placed in the /images directory within this repo. This can be edited fairly easily in the python script.

Copy all files in the folder, then open command prompt and run command:
python XMPEditor.py

Or doubleclick the XMPEditor.py script if you have Python installed.

This may take up to 1.5 seconds per image.

It may look like nothing happens, but all images in the /images folder will now have had their XMP Metadata that is specific to Stable Diffusion created and added. 

You can easily access this data using [XnView MP](https://www.xnview.com/en/xnviewmp/), or drag you file onto the "exiftool(-k).exe" file within the repo to view the metadata.  You are now free to edit the PNG file without destroying the stable diffusion parameters.     


### Acknowledgements
Thank you to Phil Harvey, who is insanely dedicated to still be working on ExifTool after all these years, and for which this tool is just a simple wrapper over.

(c) 2023 by Zirnworks LLC (Creative Commons)