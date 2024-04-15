import os
from PIL import Image

def merge_images_in_folder(input_folder, output_folder, num_copies=9):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
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
            merged_image = Image.new('RGB', (total_width, total_height))

            # Merge images in a grid
            for i in range(grid_size):
                for j in range(grid_size):
                    # Calculate the position to paste the current copy of the image
                    paste_position = (i * width, j * height)

                    # Paste a copy of the original image onto the merged image
                    merged_image.paste(original_image.copy(), paste_position)

            # Save the merged image
            output_filename = os.path.splitext(filename)[0] + '_merged.png'
            output_path = os.path.join(output_folder, output_filename)
            merged_image.save(output_path)

# Example usage
input_folder = 'original'
output_folder = 'triple'

merge_images_in_folder(input_folder, output_folder, num_copies=9)
