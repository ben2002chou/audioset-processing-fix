import json
import argparse

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


def replace_class_names_with_ids(json_data, class_to_id_mapping):
    for entry in json_data["data"]:
        labels = entry["labels"].split(",")
        updated_labels = [class_to_id_mapping.get(label, label) for label in labels]
        entry["labels"] = ",".join(updated_labels)
    return json_data


def main(input_file, output_file):
    # Read the JSON data from the file
    with open(input_file, "r") as file:
        json_data = json.load(file)

    # Replace class names with machine IDs
    modified_json = replace_class_names_with_ids(json_data, class_to_machine_id)

    # Save the modified JSON to the output file
    with open(output_file, "w") as file:
        json.dump(modified_json, file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace class names with machine IDs in JSON file."
    )
    parser.add_argument("input_file", help="Path to the input JSON file")
    parser.add_argument("output_file", help="Path to save the output JSON file")
    args = parser.parse_args()

    main(args.input_file, args.output_file)
