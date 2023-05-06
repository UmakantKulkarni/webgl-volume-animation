#!/usr/bin/env python3

import os
import shutil

input_folder = '/tmp/ply2las/longdress/webp'
output_dir = '/tmp/ply2las/longdress/webgl-volume-animation-data'

# Create the output folder if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_frame = 1051
end_frame = 1350
fps = 30
folder_frame = start_frame + fps
folder_count = 1
output_image_id = 1
# Loop through all files in the input folder
for frame_num in range(start_frame, end_frame + 1):
    filename = "longdress_vox10_{}.webp".format(frame_num)
    input_file = "/tmp/ply2las/longdress/webp/{}".format(filename)

    # Check if the file is a webp image
    if filename.endswith('.webp'):
        if frame_num == folder_frame:
            folder_frame = frame_num + fps
            folder_count = folder_count + 1
            output_image_id = 1

        output_folder = "x__t00{}".format(folder_count)
        output_folder_path = "{}/{}".format(output_dir, output_folder)
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
        image_output_filename = "{}/{}_z{num:04d}.webp".format(
            output_folder_path, output_folder, num=output_image_id)
        output_image_id = output_image_id + 1

        shutil.copyfile(input_file, image_output_filename)


