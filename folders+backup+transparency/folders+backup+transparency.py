import os
import shutil
from PIL import Image

#CREATES FOLDERS:

def create_folders():
    # Create the main folders
    folders = ['originals', 'triple', 'single']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Create folders inside 'triple'
    triple_subfolders = ['triple-horizontal', 'triple-vertical', 'triple-grid']
    triple_path = os.path.join(os.getcwd(), 'triple')
    for subfolder in triple_subfolders:
        os.makedirs(os.path.join(triple_path, subfolder), exist_ok=True)

#GENERATE BACKUP:

def copy_images_to_originals():
    # Get a list of all files in the current directory
    files = os.listdir('.')
    
    # Iterate through each file
    for file in files:
        # Check if the file is an image (you might need to adjust the condition based on your image file extensions)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Copy the image file to the 'originals' folder
            shutil.copy(file, 'originals')

#REMOVE TRANSPARENCY:

def paste_copies_on_top_for_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over the files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # Open the original image
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            paste_copies_on_top(input_image_path, output_image_path)

def paste_copies_on_top(input_image_path, output_image_path):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Get the width and height of the original image
    width, height = original_image.size

    # Create a new blank image with the same size as the original image
    merged_image = Image.new('RGBA', (width, height))

    # Paste the original image onto the blank image
    merged_image.paste(original_image, (0, 0))

    # Paste copies of the original image on top of itself 8 times
    for i in range(1, 8):

        merged_image.alpha_composite(original_image, dest=(0, 0))

    # Save the merged image
    merged_image.save(output_image_path)


create_folders()


copy_images_to_originals()
print("Images copied to 'originals' folder successfully!")


script_directory = os.path.dirname(__file__)
input_folder = script_directory
output_folder = script_directory

paste_copies_on_top_for_folder(input_folder, output_folder)