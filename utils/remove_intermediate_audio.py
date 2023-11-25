import os

def remove_intermediate_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith("_intermediate.wav"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Removed file: {file_path}")

# Specify the directory where you want to remove files
directory_path = '/grand/EVITA/ben/AudioSet/unbalanced/audio_samples'

# Execute the function
remove_intermediate_files(directory_path)
