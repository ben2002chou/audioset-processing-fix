import os
import json

# Define your root directory path here
root_directory_path = (
    "/grand/EVITA/ben/cocochorales/cocochorales_full/main_dataset/valid"
)

# This will store all your data entries
data_entries = []

# Traverse through the directory
for video_id in os.listdir(root_directory_path):
    video_id_path = os.path.join(root_directory_path, video_id)
    if os.path.isdir(video_id_path):
        stems_audio_path = os.path.join(video_id_path, "stems_audio")
        stems_midi_path = os.path.join(video_id_path, "stems_midi")

        # Check if both directories exist
        if os.path.exists(stems_audio_path) and os.path.exists(stems_midi_path):
            audio_files = [
                f for f in os.listdir(stems_audio_path) if f.endswith(".wav")
            ]
            midi_files = [f for f in os.listdir(stems_midi_path) if f.endswith(".mid")]

            # Pair and process files
            for audio_file in audio_files:
                label = audio_file.split("_")[1].split(".")[0]  # Extract label
                midi_file = f"{audio_file.split('.')[0]}.mid"  # Corresponding midi file

                if midi_file in midi_files:
                    entry = {
                        "video_id": video_id,
                        "video_path": "arbitrary/path",  # Assign an arbitrary path or modify as needed
                        "labels": label,
                        "wav1": os.path.join(stems_audio_path, audio_file),
                        "wav2": os.path.join(stems_midi_path, midi_file),
                    }
                    data_entries.append(entry)

# Create the final structure
json_structure = {"data": data_entries}

# Write to JSON file
output_json_path = (
    "/home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_valid.json"
)
with open(output_json_path, "w") as outfile:
    json.dump(json_structure, outfile, indent=4)

# Print a message when done
print(f"JSON file created at {output_json_path}")
