# XMP-StableDiffusion-DataMapper
A Data remapping tool that batch converts image metadata from the volatile format that Stable Diffusion has to the stable XMP format using ExifTool

## Requirements
Python 3.10+ 

## Usage
The app is set up to convert all images that within the designated directory. 

Open command prompt and run command:
python XMPEditor.py

Or doubleclick the XMPEditor.py script if you have Python installed.
Paste in the directory of the images you want to process.

This may take up to 1.5 seconds per image.

It may look like nothing happens, but all images in the /images folder will now have had their XMP Metadata that is specific to Stable Diffusion created and added. 

You can easily access this data using [XnView MP](https://www.xnview.com/en/xnviewmp/), or drag you file onto the "exiftool(-k).exe" file within the repo to view the metadata.  You are now free to edit the PNG file without destroying the stable diffusion parameters.     


### Acknowledgements
Thank you to Phil Harvey, who is insanely dedicated to still be working on ExifTool after all these years, and for which this tool is just a simple wrapper over.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">XMP Stable Diffusion Mapper</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://www.Zirnworks.com" property="cc:attributionName" rel="cc:attributionURL">Zirnworks LLC</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
Authorized for Commercial use, both personally and professionally, please attribute Zirnworks when you do.
