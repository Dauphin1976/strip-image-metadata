#!/usr/bin/python3

# Everyone have these
from sys import argv
from os.path import isfile

# Make sure PIL and magic is installed
try:
	from PIL import Image
	from magic import Magic
except ImportError:
	print('Check if these packages are installed: PIL, magic')
	exit(1)


# Make sure a file is present
if len(argv) < 2:
	print('Please provide an image file')
	exit(1)

input_file	= argv[1]
extension	= '.' + input_file.split('.')[-1]

if not isfile(input_file):
	print('File not found: %s' % input_file)
	exit(1)


# Make sure the file is an image
mime = Magic(mime=True)
mediatype		= mime.from_file(input_file)
media_type		= mediatype.split('/')[0]
media_subtype	= mediatype.split('/')[-1]
if media_type != 'image':
	print('Not an image: %s' % input_file)
	exit(1)
if media_subtype != 'jpeg' and media_subtype != 'png':
	print('[!] Warning! This tool is currently only tested on jpeg and png images. The type of the current image (%s) is not tested' % media_subtype)


# Do the stripping
image = Image.open(input_file)

image_stripped = Image.new(image.mode, image.size)
image_stripped.putdata(list(image.getdata()))

stripped_filename = input_file.replace(extension, '') + '_stripped' + extension
image_stripped.save(stripped_filename)
print('Saved as %s' % stripped_filename)
