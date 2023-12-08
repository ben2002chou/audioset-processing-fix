import json
import os
import argparse


def modify_json_midi(original_json_file_path):
    # Load the original JSON data
    with open(original_json_file_path, "r") as file:
        data = json.load(file)

    # Modify the data
    for item in data["data"]:
        wav_path = item["wav"]
        item["wav1"] = wav_path  # Set wav1 to the original wav path
        item["wav2"] = wav_path  # Set wav2 to the same path as wav1
        del item["wav"]  # Remove the original wav key

    # Create a new filename with '_midi' appended before the file extension
    base_name, ext = os.path.splitext(original_json_file_path)
    new_json_file_path = base_name + "_midi" + ext

    # Save the modified data to the new JSON file
    with open(new_json_file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Modified JSON saved to {new_json_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify JSON for AudioSet Dataset")
    parser.add_argument("path", help="Path to the original JSON file")
    args = parser.parse_args()

    modify_json_midi(args.path)
