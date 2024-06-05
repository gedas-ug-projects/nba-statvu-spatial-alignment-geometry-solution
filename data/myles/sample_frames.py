import cv2
import os
import sys

def sample_frames_from_video(video_path, frame_interval=30):
    # Extract the video name and create a folder for frames
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    frames_dir = os.path.join(os.path.dirname(video_path), video_name)
    
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    # Open the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file {video_path}")
        return

    frame_count = 0
    saved_frame_count = 0

    while True:
        # Read frame
        ret, frame = cap.read()
        if not ret:
            break

        # Save frames at the specified interval
        if frame_count % frame_interval == 0:
            frame_file = os.path.join(frames_dir, f"{saved_frame_count}.png")
            cv2.imwrite(frame_file, frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print(f"Frames extracted and saved to {frames_dir}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py video_path [frame_interval]")
        return

    video_path = sys.argv[1]
    frame_interval = 30  # Default frame interval

    if len(sys.argv) > 2:
        try:
            frame_interval = int(sys.argv[2])
        except ValueError:
            print("Frame interval must be an integer. Using default value of 30.")

    sample_frames_from_video(video_path, frame_interval)

if __name__ == "__main__":
    main()

