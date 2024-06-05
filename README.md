
# MixSort and KaliCalib Workflow Documentation

## 1. Activate Conda Virtual Environment

Activate the `MixSort2` conda virtual environment:

```bash
conda activate MixSort2
```

## 2. Run MixSort

Navigate to the MixSort directory:

```bash
cd /playpen-storage/shanw25/src/MixSort
```

Run the MixSort tracking command:

```bash
python3 tools/demo_track.py -expn {experiment_name} -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path {path_to_video} --save_result video
```

**Example:**

```bash
python3 tools/demo_track.py -expn statvu -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path ./datasets/statvu/a.mp4 --save_result video
```

## 3. Copy MixSort Output

Copy the output file from MixSort to KaliCalib directory:

```bash
cp /playpen-storage/shanw25/src/MixSort/YOLOX_outputs/{experiment_name}/{current_time}.txt /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data
```

## 4. Run MixSort Output Parser

Update the variable value in the `main()` function to match the copied file name. Then, run the MixSort output parser:

```bash
cd /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src
python3 MixSort-output-parser.py
```

## 5. Run Sample Frames Script

Navigate to the data directory and run the sample frames script:

```bash
cd /playpen-storage/shanw25/data/myles
python3 sample_frames.py {path_to_video} 1
```

**Example:**

```bash
python3 sample_frames.py /playpen-storage/shanw25/src/MixSort/datasets/statvu/a.mp4 1
```

## 6. Run Image Size Script

Update the variables in the `main()` function and run the image size script:

```bash
python3 /playpen-storage/shanw25/data/myles/image_size.py
```

## 7. Activate KaliCalib Virtual Environment

Activate the `KaliCalib` conda virtual environment:

```bash
conda activate KaliCalib
```

## 8. Move Output Images

Move all images outputted from the image size script to the CHALLENGE directory:

```bash
mv /path/to/output/images/* /playpen-storage/shanw25/src/KaliCalib/CHALLENGE/
```

## 9. Run Challenge Evaluation Script

Navigate to the KaliCalib directory and run the challenge evaluation script:

```bash
cd /playpen-storage/shanw25/src/KaliCalib
./eval_challenge.sh
```

## 10. Run Real Position Script

Navigate to the MixSort_Combine/src directory and run the real position script:

```bash
cd /playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src
python3 get_real_position.py
```

## 11. Run Interpolation Script

Change the variable path in `interpolate.py`, then run the script:

```bash
python3 interpolate.py
```

## 12. Run Visualization Script

Run the visualization script:

```bash
python3 visualization.py
```

## 13. Copy Output Video

Copy the output video to your local machine:

```bash
scp shanw25@oprime.cs.unc.edu:/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/output_video.avi /Users/shanw25/Desktop/
```
