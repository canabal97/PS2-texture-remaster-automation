import os
from PIL import Image

def merge_images_with_itself_vertically(input_folder, output_folder):
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

            # Create a new blank image with three times the height of the original image
            merged_image = Image.new('RGB', (width, height * 3))

            # Merge the original image with itself three times vertically
            for i in range(3):
                merged_image.paste(original_image, (0, i * height))

            # Save the merged image
            output_filename = os.path.splitext(filename)[0] + '_merged.png'
            output_path = os.path.join(output_folder, output_filename)
            merged_image.save(output_path)

# Example usage
input_folder = 'original'
output_folder = 'triple_vertical'

merge_images_with_itself_vertically(input_folder, output_folder)