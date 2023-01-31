# XMP-StableDiffusion-DataMapper
A Data remapping tool that batch converts image metadata from the volatile format that Stable Diffusion has to the stable XMP format using ExifTool

# Requirements
Python 3.10+ 

# Usage
The app is set up to convert all images that are placed in the /images directory. This can be edited fairly easily in the python script.

Copy all files in this repo, then open command prompt and run comand:

python XMPEditor.py

This may take up to 1.5 seconds per image.

It may look like nothing happens, but all images in the /images folder will now have had their XMP Metadata that is specific to Stable Diffusion created and added. 

### Acknowledgements
Thank you to Phil Harvey, who is insanely dedicated to still be working on ExifTool after all these years, and for which this tool is just a simple wrapper over.
