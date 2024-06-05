import pandas as pd

def process_keypoints(input_file, output_file):
    # Initialize a list to hold all processed rows
    processed_rows = []
    
    # Define the scale factors based on the original and resized dimensions
    scale_x = 480 / 1280
    scale_y = 360 / 720

    # Open the file and process each line
    with open(input_file, 'r') as file:
        for line in file:
            if line.strip() == 'index,x,y':  # Check for header line
                processed_rows.append(line.strip())  # Append header directly
            else:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Ensure the line is a valid data line
                    # Scale the x and y coordinates
                    x_scaled = float(parts[1]) * scale_x
                    y_scaled = float(parts[2]) * scale_y
                    # Append the processed line to the list
                    processed_rows.append(f"{parts[0]},{x_scaled:.3f},{y_scaled:.3f}")

    # Write the processed lines to a new CSV file
    with open(output_file, 'w') as out_file:
        for row in processed_rows:
            out_file.write(row + '\n')

    print(f"Original keypoint positions, along with repeated headers, have been saved to {output_file}")

def main():
    input_csv = '/playpen-storage/shanw25/src/KaliCalib/output/evaluation_images/positions.csv'  # Path to the input CSV file
    output_csv = '/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/outputs/positions_original.csv'  # Path to the output CSV file
    
    process_keypoints(input_csv, output_csv)

if __name__ == "__main__":
    main()
