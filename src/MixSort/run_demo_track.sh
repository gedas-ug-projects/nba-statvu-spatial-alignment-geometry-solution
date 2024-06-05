#!/bin/bash

# Define the directory containing your videos
VIDEO_DIR="./datasets/myles/first_period"

# Loop through each mp4 file in the directory
for video_file in "$VIDEO_DIR"/*.mp4; do
    echo "Processing $video_file"
    python3 tools/demo_track.py -expn mylesall -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path "$video_file" --save_result video
done

