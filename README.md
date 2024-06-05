0, Activate conda virtual environment MixSort2

1, Run MixSort.
terminal location: /playpen-storage/shanw25/src/MixSort

command: python3 tools/demo_track.py -expn {experiment_name} -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path {path_to_video} --save_result video

command e.g.
python3 tools/demo_track.py -expn statvu -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path ./datasets/statvu/a.mp4 --save_result video

2, Copy /playpen-storage/shanw25/src/MixSort/YOLOX_outputs/{experiment_name}/{current_time}.txt TO /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data

3, Change the variable value in main() to match the name of the file copied in step 2. Run /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src/MixSort-output-parser.py. 

terminal location: /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src/

command: python3 ./MixSort-output-parser.py

4, Run sample_frames.py

terminal location: /playpen-storage/shanw25/data/myles

command: python3 sample_frames.py {path_to_video} 1

command e.g.
python3 sample_frames.py /playpen-storage/shanw25/src/MixSort/datasets/statvu/a.mp4 1

5, Change the variables in main(). Run /playpen-storage/shanw25/data/myles/image_size.py

6, conda activate KaliCalib

7, Move all images outputed in step 5 under /playpen-storage/shanw25/src/KaliCalib/CHALLENGE/

8, Run /playpen-storage/shanw25/src/KaliCalib/CHALLENGE

terminal location: /playpen-storage/shanw25/src/KaliCalib

command: ./eval_challenge.sh

9, Run get_real_position.py

terminal location: /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src

command: python3 get_real_position.py

10, Change variable path in interpolate.py. Run interpolate.py

terminal location: /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src

command: python3 interpolate.py

11, Run visualization.py

terminal location: /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src

command: python3 visualization.py

12, 
scp shanw25@oprime.cs.unc.edu:/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/output_video.avi /Users/shanw25/Desktop/
