import os
import shutil

def copy_images_to_originals():
    # Get a list of all files in the current directory
    files = os.listdir('.')
    
    # Iterate through each file
    for file in files:
        # Check if the file is an image (you might need to adjust the condition based on your image file extensions)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Copy the image file to the 'originals' folder
            shutil.copy(file, 'originals')

if __name__ == "__main__":
    copy_images_to_originals()
    print("Images copied to 'originals' folder successfully!")