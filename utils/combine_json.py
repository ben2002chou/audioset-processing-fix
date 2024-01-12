import json
import argparse


def combine_json_files(input_file1, input_file2, output_file):
    # Reading the first JSON file
    with open(input_file1, "r") as file:
        data1 = json.load(file)

    # Reading the second JSON file
    with open(input_file2, "r") as file:
        data2 = json.load(file)

    # Combining the 'data' lists from both JSON files
    combined_data = data1["data"] + data2["data"]

    # Creating a new dictionary to store combined data
    combined_json = {"data": combined_data}

    # Writing the combined data to the output JSON file
    with open(output_file, "w") as file:
        json.dump(combined_json, file, indent=4)

    print(f"Combined JSON file created at {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine two JSON files into one.")
    parser.add_argument("input_file1", help="Path to the first input JSON file")
    parser.add_argument("input_file2", help="Path to the second input JSON file")
    parser.add_argument(
        "output_file", help="Path to save the combined output JSON file"
    )
    args = parser.parse_args()

    combine_json_files(args.input_file1, args.input_file2, args.output_file)

# python combine_json.py /home/ben2002chou/code/cav-mae/data/audioset_eval_filtered_piano_roll.json /home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_valid_h5.json /home/ben2002chou/code/cav-mae/data/cocochorals/audioset_eval_cocochorals_valid_h5.json
