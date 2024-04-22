import os
from PIL import Image

def merge_images_in_folder(input_folder, output_folder, num_copies=9):
    
    # Iterate over the files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # Open the original image
            original_image_path = os.path.join(input_folder, filename)
            original_image = Image.open(original_image_path)

            # Get the width and height of the original image
            width, height = original_image.size

            # Calculate the dimensions of the grid
            grid_size = int(num_copies ** 0.5)

            # Calculate the total width and height of the merged image
            total_width = width * grid_size
            total_height = height * grid_size

            # Create a new blank image with the calculated size
            merged_image = Image.new('RGBA', (total_width, total_height))

            # Merge images in a grid
            for i in range(grid_size):
                for j in range(grid_size):
                    # Calculate the position to paste the current copy of the image
                    paste_position = (i * width, j * height)

                    # Paste a copy of the original image onto the merged image
                    merged_image.paste(original_image.copy(), paste_position)

            # Save the merged image
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)
            merged_image.save(output_path)

# Example usage
script_directory = os.path.dirname(__file__)
input_folder = os.path.join("triple", "triple-grid")
output_folder = os.path.join("triple", "triple-grid")

merge_images_in_folder(input_folder, output_folder, num_copies=9)
