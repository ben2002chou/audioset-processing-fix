import json
import argparse


def modify_json_field(file_path, data_name, new_value, output_file=None):
    """
    Modifies a specified entry in the JSON file.

    :param file_path: Path to the input JSON file.
    :param data_name: The name of the data field to be modified.
    :param new_value: New value to replace in the specified data field.
    :param output_file: Path to the output JSON file. If None, overwrite the input file.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        for item in data["data"]:
            if data_name in item:
                item[data_name] = new_value

        output_path = output_file if output_file else file_path
        with open(output_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"File updated successfully. Data saved in: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Modify a specific field in a JSON file."
    )
    parser.add_argument(
        "--file_path", help="Path to the input JSON file", required=True
    )
    parser.add_argument(
        "--data_name", help="The name of the data field to be modified", required=True
    )
    parser.add_argument(
        "--new_value",
        help="New value to replace in the specified data field",
        required=True,
    )
    parser.add_argument("--output", help="Path to the output JSON file", default=None)

    args = parser.parse_args()

    modify_json_field(args.file_path, args.data_name, args.new_value, args.output)


if __name__ == "__main__":
    main()
