import os
import json

# Define your root directory path here
root_directory_path = (
    "/grand/EVITA/ben/cocochorales/cocochorales_full/main_dataset/test"
)

# This will store all your data entries
data_entries = []

# Class names and their corresponding machine IDs
class_to_machine_id = {
    "trumpet": "/instrument/00000",
    "horn": "/instrument/00001",
    "trombone": "/instrument/00002",
    "tuba": "/instrument/00003",
    "flute": "/instrument/00004",
    "oboe": "/instrument/00005",
    "clarinet": "/instrument/00006",
    "bassoon": "/instrument/00007",
    "violin": "/instrument/00008",
    "viola": "/instrument/00009",
    "cello": "/instrument/00010",
    "saxophone": "/instrument/00011",
    "double bass": "/instrument/00012",
}


# Function to replace class names with machine IDs
def replace_class_names_with_ids(labels_list, class_to_id_mapping):
    return [
        class_to_id_mapping.get(label.strip(), label.strip()) for label in labels_list
    ]


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
            root_audio_files = [
                f for f in os.listdir(video_id_path) if f.endswith(".wav")
            ]
            root_midi_files = [
                f for f in os.listdir(video_id_path) if f.endswith(".mid")
            ]
            labels = []
            # Pair and process files
            for audio_file in audio_files:
                label = audio_file.split("_")[1].split(".")[0]  # Extract label
                labels.append(label)
                midi_file = f"{audio_file.split('.')[0]}.mid"  # Corresponding midi file

                if midi_file in midi_files:
                    entry = {
                        "video_id": video_id,
                        "video_path": "arbitrary/path",  # Assign an arbitrary path or modify as needed
                        "labels": class_to_machine_id.get(
                            label, label
                        ),  # Replace class name with machine ID
                        "wav1": os.path.join(stems_audio_path, audio_file),
                        "wav2": os.path.join(stems_midi_path, midi_file),
                    }
                    data_entries.append(entry)
            # mixed audio and midi files
            for audio_file in root_audio_files:
                joined_labels = ",".join(labels)
                updated_labels = replace_class_names_with_ids(
                    joined_labels.split(","), class_to_machine_id
                )
                joined_updated_labels = ",".join(updated_labels)
                midi_file = f"{audio_file.split('.')[0]}.mid"

                if midi_file in root_midi_files:
                    entry = {
                        "video_id": video_id,
                        "video_path": "arbitrary/path",  # Assign an arbitrary path or modify as needed
                        "labels": joined_updated_labels,  # Labels replaced with machine IDs
                        "wav1": os.path.join(video_id_path, audio_file),
                        "wav2": os.path.join(video_id_path, midi_file),
                    }
                    data_entries.append(entry)

# Create the final structure
json_structure = {"data": data_entries}

# Write to JSON file
output_json_path = (
    "/home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_test_trial.json"
)
with open(output_json_path, "w") as outfile:
    json.dump(json_structure, outfile, indent=4)

# Print a message when done
print(f"JSON file created at {output_json_path}")
