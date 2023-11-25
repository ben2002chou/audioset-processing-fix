import json
import os
import argparse

def filter_json(input_json_path, output_json_path, video_directory):
    # Load JSON data
    with open(input_json_path, 'r') as file:
        data = json.load(file)

    # List to hold entries to keep
    filtered_data = []

    for entry in data['data']:
        video_id = entry['video_id']
        video_file_path = os.path.join(video_directory, video_id + '.mp4')
        
        # Check if the video file exists
        if os.path.exists(video_file_path):
            filtered_data.append(entry)

    # Update the data key with filtered entries
    data['data'] = filtered_data

    # Write the filtered data back to a new JSON file
    with open(output_json_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter JSON data based on the existence of corresponding video files.')
    parser.add_argument('input_json', help='Path to the input JSON file')
    parser.add_argument('output_json', help='Path to the output JSON file')
    parser.add_argument('video_directory', help='Path to the directory containing video files')

    args = parser.parse_args()

    filter_json(args.input_json, args.output_json, args.video_directory)
