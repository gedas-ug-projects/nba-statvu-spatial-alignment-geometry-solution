1. **Activate** `conda` virtual environment `MixSort2`
2. **Run MixSort**
    - **Terminal Location:** `/playpen-storage/shanw25/src/MixSort`
    
    ```bash
    command: python3 tools/demo_track.py -expn {experiment_name} -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path {path_to_video} --save_result video
    ```
    **Example:**
    ```bash
    python3 tools/demo_track.py -expn statvu -f exps/example/mot/yolox_x_sportsmot.py -c pretrained/yolox_x_sports_mix.pth.tar -n MixFormer_sports_mix.pth.tar --path ./datasets/statvu/a.mp4 --save_result video
    ```

3. **Copy** `/playpen-storage/shanw25/src/MixSort/YOLOX_outputs/{experiment_name}/{current_time}.txt` **TO** `/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data`
4. **Change the variable value in main()** to match the name of the file copied in step 3. Run `/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src/MixSort-output-parser.py`.

    - **Terminal Location:** `/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src/`
    ```bash
    command: python3 ./MixSort-output-parser.py
    ```

5. **Run** `sample_frames.py`
    - **Terminal Location:** `/playpen-storage/shanw25/data/myles`
    
    ```bash
    command: python3 sample_frames.py {path_to_video} 1
    ```
    **Example:**
    ```bash
    python3 sample_frames.py /playpen-storage/shanw25/src/MixSort/datasets/statvu/a.mp4 1
    ```

6. **Change the variables in main()**. Run `/playpen-storage/shanw25/data/myles/image_size.py`
7. **Activate** `conda` virtual environment `KaliCalib`
    ```bash
    conda activate KaliCalib
    ```

8. **Move all images** outputted in step 6 to `/playpen-storage/shanw25/src/KaliCalib/CHALLENGE/`
9. **Run** `/playpen-storage/shanw25/src/KaliCalib/CHALLENGE`
    - **Terminal Location:** `/playpen-storage/shanw25/src/KaliCalib`
    ```bash
    command: ./eval_challenge.sh
    ```

10. **Run** `get_real_position.py`
    - **Terminal Location:** `/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src`
    ```bash
    command: python3 get_real_position.py
    ```

11. **Change variable path** in `interpolate.py`. **Run** `interpolate.py`
    - **Terminal Location:** `/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src`
    ```bash
    command: python3 interpolate.py
    ```

12. **Run** `visualization.py`
    - **Terminal Location:** `/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/src`
    ```bash
    command: python3 visualization.py
    ```

13. **Copy** the output video:
    ```bash
    scp shanw25@oprime.cs.unc.edu:/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/output_video.avi /Users/shanw25/Desktop/
    ```
