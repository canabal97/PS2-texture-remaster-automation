import os
from PIL import Image

def paste_copies_on_top(input_image_path, output_path):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Get the width and height of the original image
    width, height = original_image.size

    # Create a new blank image with the same size as the original image
    merged_image = Image.new('RGB', (width, height))

    # Paste the original image onto the blank image
    merged_image.paste(original_image, (0, 0))

    # Paste copies of the original image on top of itself 8 times
    for i in range(1, 9):
        # Calculate the position to paste the copy
        paste_position = (0, i * height)

        # Paste a copy of the original image onto the merged image
        merged_image.paste(original_image.copy(), paste_position)

    # Save the merged image
    merged_image.save(output_path)

# Example usage
input_image_path = 'transparent.png'
output_path = 'output_image.png'

paste_copies_on_top(input_image_path, output_path)
