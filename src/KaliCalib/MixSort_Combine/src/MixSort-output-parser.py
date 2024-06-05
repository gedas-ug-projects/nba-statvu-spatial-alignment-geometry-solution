def process_data(input_file_path, output_file_path):
    # Read data from the input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    output_lines = []

    for line in lines:
        # Split the line by comma to get individual values
        values = line.strip().split(',')

        frame_number = values[0]
        player_id = values[1]
        x_top_left = float(values[2])
        y_top_left = float(values[3])
        width = float(values[4])
        height = float(values[5])

        # Calculate center X and center Y of the bottom line
        center_x = x_top_left + width / 2
        center_y = y_top_left + height

        # Create the new line with the required data
        new_line = f"{frame_number},{player_id},{center_x:.2f},{center_y:.2f}"
        output_lines.append(new_line)

    # Write the processed data to the output file
    with open(output_file_path, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')

def extract_player_data(input_file_path, output_file_path, player_id):
    # Read data from the input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    output_lines = []

    for line in lines:
        # Split the line by comma to get individual values
        values = line.strip().split(',')

        frame_number = values[0]
        current_player_id = values[1]

        if current_player_id == player_id:
            output_lines.append(line.strip())  # Keep the original format or modify as needed

    # Write the filtered data to the output file
    with open(output_file_path, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')

def main():
    for i in range(1, 11):
        playernum = str(i);
        input_file_path = "/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data/2024_04_23_10_12_49.txt" # CHANGE THIS
        output_file_path_player2 = f'/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data/2024_04_23_10_12_49_player{playernum}.txt' # CHANGE THIS
        extract_player_data(input_file_path, output_file_path_player2, playernum)
    for i in range(1, 11):
        playernum = str(i);
        input_file_path = f'/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data/2024_04_23_10_12_49_player{playernum}.txt' # CHANGE THIS
        output_file_path_process = f'/playpen-storage/shanw25/src/KaliCalib/MixSort_Combine/data/2024_04_23_10_12_49_player{playernum}_position.txt' # CHANGE THIS
        process_data(input_file_path, output_file_path_process)
        
if __name__ == "__main__":
    main()
