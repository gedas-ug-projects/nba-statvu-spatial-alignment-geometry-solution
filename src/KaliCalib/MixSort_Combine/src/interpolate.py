import csv
import pandas as pd

def read_keypoints(file_path):
    frames = []
    current_frame = {}

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == 'index':  # New frame starts
                if current_frame:
                    frames.append(current_frame)
                    current_frame = {}
            else:
                index = int(row[0])
                x = float(row[1])
                y = float(row[2])
                current_frame[index] = [x, y]

        # Append the last frame if not empty
        if current_frame:
            frames.append(current_frame)

    return frames

def get_frame_keypoints(file_path, frame_number):
    frames = read_keypoints(file_path)
    if frame_number < len(frames):
        return frames[frame_number]
    else:
        raise IndexError("Frame number out of range")

def get_keypoints_real_positions():
    # Initialize a dictionary to store keypoint indices and their positions
    keypoints = {}
    
    # Standard basketball court dimensions in feet
    court_length = 94  # Length from baseline to baseline
    court_width = 50   # Width from sideline to sideline
    
    # Dimensions based on the assumed distribution of points
    num_points_horizontal = 13  # From point 0 to 12 (inclusive), 13 points horizontally
    num_points_vertical = 7     # Estimated from point 0 to 90 with 13 points each row, leads to 7 points vertically
    
    # Calculate the spacing between each keypoint
    spacing_horizontal = court_length / (num_points_horizontal - 1)
    spacing_vertical = court_width / (num_points_vertical - 1)
    
    # Calculate the positions
    for i in range(num_points_vertical):
        for j in range(num_points_horizontal):
            # Calculate index of the point in the grid
            index = i * num_points_horizontal + j
            
            # Calculate the actual x and y coordinates
            # Transform such that (0,0) starts at point 78 (top left corner)
            x = j * spacing_horizontal
            y = (num_points_vertical - i-1) * spacing_vertical
            
            # Store in the dictionary
            keypoints[index] = [x, y]
    
    return keypoints

# Retrieve the keypoints positions

def get_position_by_frame_id(frame_id, csv_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path, header=None, names=['FrameID', 'PlayerID', 'X', 'Y'])
    
    # Filter the DataFrame to find the row with the matching frame ID
    position_data = df[df['FrameID'] == frame_id]
    
    # Check if the position data is found for the frame ID
    if not position_data.empty:
        # Extract the X and Y positions as a list of tuples
        positions = position_data[['X', 'Y']].values.tolist()
        return positions
    else:
        return None

def getInterpolationFourPoints(frame_id, player_id):
    p1 = [-1, 999999] # left top
    p2 = [-1, 999999] # right top
    p3 = [-1, 999999] # right bottom
    p4 = [-1, 999999] # left bottom
    keypoints = get_frame_keypoints('/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/positions_original.csv', frame_id)
    player_position = get_position_by_frame_id(frame_id, f"/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data/2024_04_23_10_12_49_player{player_id}_position.csv") # CHANGE THIS
    if(player_position is None):
        return p1, p2, p3, p4
    playerx = player_position[0][0]
    playery = player_position[0][1]
    for key, value in keypoints.items():
        kx = value[0]
        ky = value[1]
        distance = ((kx - playerx)**2 + (ky - playery)**2)**0.5
        if(kx > playerx):
            if(ky > playery):
                if(distance < p3[1]):
                    p3[0] = key
                    p3[1] = distance
                else:
                    continue
            else:
                if(distance < p2[1]):
                    p2[0] = key
                    p2[1] = distance
                else:
                    continue
        else:
            if(ky > playery):
                if(distance < p4[1]):
                    p4[0] = key
                    p4[1] = distance
                else:
                    continue
            else:
                if(distance < p1[1]):
                    p1[0] = key
                    p1[1] = distance
                else:
                    continue
    return p1, p2, p3, p4

def estimate_position(x_TL, y_TL, x_TR, y_TR, x_BL, y_BL, x_BR, y_BR, d_TL, d_TR, d_BL, d_BR):
    """
    Estimate the position of a point based on the inverse distance weighting method.
    
    :param x_TL, y_TL: Coordinates of the top-left keypoint.
    :param x_TR, y_TR: Coordinates of the top-right keypoint.
    :param x_BL, y_BL: Coordinates of the bottom-left keypoint.
    :param x_BR, y_BR: Coordinates of the bottom-right keypoint.
    :param d_TL, d_TR, d_BL, d_BR: Distances from the point to each keypoint respectively.
    :return: Estimated position (x, y) of the central point.
    """
    # Compute weights as inverse of distances
    w_TL = 1 / d_TL if d_TL > 0 else 0
    w_TR = 1 / d_TR if d_TR > 0 else 0
    w_BL = 1 / d_BL if d_BL > 0 else 0
    w_BR = 1 / d_BR if d_BR > 0 else 0

    # Calculate the sum of weights
    W = w_TL + w_TR + w_BL + w_BR

    # Compute weighted average if total weight is not zero
    if W != 0:
        x = (w_TL * x_TL + w_TR * x_TR + w_BL * x_BL + w_BR * x_BR) / W
        y = (w_TL * y_TL + w_TR * y_TR + w_BL * y_BL + w_BR * y_BR) / W
        return (x, y)
    else:
        return None  # Handle division by zero if all distances are zero

def main():

    for j in range(1, 11):
        with open(f'/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/real_court_pos_{j}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for i in range(280):
                p1, p2, p3, p4 = getInterpolationFourPoints(i, j)
                if(p1[0] == -1 or p2[0] == -1 or p3[0] == -1 or p4[0] == -1):
                    continue
                keypoints_positions = get_keypoints_real_positions()
                kp1 = keypoints_positions.get(p1[0])
                kp2 = keypoints_positions.get(p2[0])
                kp3 = keypoints_positions.get(p3[0])
                kp4 = keypoints_positions.get(p4[0])
                a = estimate_position(kp1[0], kp1[1], kp2[0], kp2[1], kp4[0], kp4[1], kp3[0], kp3[1], p1[1], p2[1], p4[1], p3[1])
                writer.writerow([i, a[0], a[1]])
            
def test():
    p1, p2, p3, p4 = getInterpolationFourPoints(28)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    # keypoints_positions = get_keypoints_real_positions()
    # kp1 = keypoints_positions.get(p1[0])
    # kp2 = keypoints_positions.get(p2[0])
    # kp3 = keypoints_positions.get(p3[0])
    # kp4 = keypoints_positions.get(p4[0])
    # a = estimate_position(kp1[0], kp1[1], kp2[0], kp2[1], kp4[0], kp4[1], kp3[0], kp3[1], p1[1], p2[1], p4[1], p3[1])
    # # writer.writerow([a[0], a[1]])
    # print(a)

if __name__ == "__main__":
    main()
    # test()