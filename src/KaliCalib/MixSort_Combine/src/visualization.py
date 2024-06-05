import pandas as pd
import cv2
import numpy as np

# Constants
background_image_path = '/playpen-storage/shanw25/data/myles/statvu/court.png'
video_path = '/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/output_video.avi'
frame_rate = 30  # frames per second
dot_color = (0, 0, 255)  # Red color in BGR format
text_color = (0, 0, 255)  # White color for the text
dot_radius = 10  # Size of the dot
num_files = 10  # Number of CSV files

# Function to scale coordinates
def scale_coordinates(x, y, img_shape, x_range, y_range):
    x_scaled = int((x - x_range[0]) / (x_range[1] - x_range[0]) * img_shape[1])
    y_scaled = int((y - y_range[0]) / (y_range[1] - y_range[0]) * img_shape[0])
    return x_scaled, y_scaled

# Load background image
background = cv2.imread(background_image_path)

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_path, fourcc, frame_rate, (background.shape[1], background.shape[0]))

# Load data from each CSV file and store in a list
data_frames = []
for i in range(1, num_files + 1):
    data = pd.read_csv(f'/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/real_court_pos_{i}.csv', header=None, names=['frameid', 'x', 'y'])
    data_frames.append(data)

# Determine the maximum frame number across all datasets
max_frame_id = max(df['frameid'].max() for df in data_frames)

# Generate frames and save to video
for frame_id in range(max_frame_id + 1):
    frame = background.copy()
    for i, data in enumerate(data_frames):
        frame_data = data[data['frameid'] == frame_id]
        if not frame_data.empty:
            row = frame_data.iloc[0]
            x_scaled, y_scaled = scale_coordinates(row['x'], row['y'], frame.shape, [0, 94], [0, 50])
            cv2.circle(frame, (x_scaled, y_scaled), dot_radius, dot_color, -1)
            cv2.putText(frame, str(i + 1), (x_scaled + 10, y_scaled + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1, cv2.LINE_AA)
    out.write(frame)

# Release the video writer
out.release()
print("Video created successfully!")
