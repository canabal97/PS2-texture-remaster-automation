import os

def create_folders():
    # Create the main folders
    folders = ['original', 'triple', 'single']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Create folders inside 'triple'
    triple_subfolders = ['triple-horizontal', 'triple-vertical', 'triple-grid']
    triple_path = os.path.join(os.getcwd(), 'triple')
    for subfolder in triple_subfolders:
        os.makedirs(os.path.join(triple_path, subfolder), exist_ok=True)

if __name__ == "__main__":
    create_folders()
