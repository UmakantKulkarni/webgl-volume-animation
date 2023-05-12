#!/usr/bin/env python3

import os
import shutil

mydir = "/home/kulkarnu"
model = "soldier"
input_folder = '{}/pcs_dataset/{}/webp'.format(mydir, model)
output_dir = '{}/pcs_dataset/{}/webgl-volume-animation-data'.format(mydir, model)

# Create the output folder if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_frame = 536
end_frame = 835
fps = 30
folder_frame = start_frame + fps
folder_count = 1
output_image_id = 1
# Loop through all files in the input folder
for frame_num in range(start_frame, end_frame + 1):
    filename = "{}_vox10_{}.webp".format(model, frame_num)
    input_file = "{}/pcs_dataset/{}/webp/{}".format(mydir, model, filename)

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


if 0:
    zip -r x__t001.zip x__t001
    zip -r x__t002.zip x__t002
    zip -r x__t003.zip x__t003
    zip -r x__t004.zip x__t004
    zip -r x__t005.zip x__t005
    zip -r x__t006.zip x__t006
    zip -r x__t007.zip x__t007
    zip -r x__t008.zip x__t008
    zip -r x__t009.zip x__t009
    zip -r x__t0010.zip x__t0010


    vi urllist.txt

    http://192.168.0.141/x__t001.zip
    http://192.168.0.141/x__t002.zip
    http://192.168.0.141/x__t003.zip
    http://192.168.0.141/x__t004.zip
    http://192.168.0.141/x__t005.zip
    http://192.168.0.141/x__t006.zip
    http://192.168.0.141/x__t007.zip
    http://192.168.0.141/x__t008.zip
    http://192.168.0.141/x__t009.zip
    http://192.168.0.141/x__t0010.zip