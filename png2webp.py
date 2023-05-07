#!/usr/bin/env python3

import os
from PIL import Image

mydir = "/home/kulkarnu"
input_folder = '{}/pcs_dataset/longdress/Png'.format(mydir)
output_folder = '{}/pcs_dataset/longdress/webp'.format(mydir)

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for img_file in os.listdir(input_folder):
    filename = os.path.basename(img_file)
    # Check if the file is a PNG image
    if filename.endswith('.png'):
        # Construct the input and output file paths
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder,
                                   os.path.splitext(filename)[0] + '.webp')

        # Open the input image and convert it to RGB mode
        with Image.open(input_file).convert('RGB') as img:
            # Save the image in WebP format with lossless compression
            img.save(output_file, 'webp', lossless=True)
