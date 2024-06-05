from PIL import Image

def get_image_size(image_path):
    """Retrieve and return the size (width, height) of the given image."""
    try:
        with Image.open(image_path) as img:
            return img.size  # Returns a tuple (width, height)
    except IOError:
        return "Error: The image could not be opened. Check the file path."
    

def resize_image(input_path, output_path, new_size):
    """
    Resize an image to the new dimensions and save it to a new file.

    Args:
    input_path (str): Path to the input image file.
    output_path (str): Path where the resized image will be saved.
    new_size (tuple): New size as a tuple, (width, height).
    """
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize(new_size)
            resized_img.save(output_path)
            return f"Image resized and saved to {output_path}"
    except IOError:
        return "Error: The image could not be opened. Check the file path."

def main():
    """Main method to execute the program logic."""
    base_input_path = '/playpen-storage/shanw25/src/MixSort/datasets/statvu/a/' # CHANGE THIS
    base_output_path = '/playpen-storage/shanw25/src/MixSort/datasets/statvu/a_adj/' # CHANGE THIS
    new_size = (1280, 720)  # Desired dimensions (width, height)

    # Loop over the image files by index
    # CHANGE THIS
    for i in range(1620):  # 1620 because it includes 0 through 1619
        input_path = f"{base_input_path}{i}.png"
        output_path = f"{base_output_path}{i}.png"
        
        # Resize the image
        result = resize_image(input_path, output_path, new_size)
        print(result)
    # print(get_image_size("/playpen-storage/shanw25/data/myles/statvu/court.png"))

# basketball court: (581, 325)
# origional: (480, 360)
# Width: 1280 pixels
# Height: 720 pixels
if __name__ == "__main__":
    main()
