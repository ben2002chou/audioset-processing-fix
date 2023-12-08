import csv

# List of your class names
classes = [
    "trumpet",
    "horn",
    "trombone",
    "tuba",
    "flute",
    "oboe",
    "clarinet",
    "bassoon",
    "violin",
    "viola",
    "cello",
    "saxophone",
    "double bass",
]

# Choose your custom prefix here
custom_prefix = "/instrument/"


# Function to generate CSV from classes list
def create_label_csv(filename, classes, prefix):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["index", "mid", "display_name"],
            quoting=csv.QUOTE_NONE,
            quotechar="",
            escapechar="\\",
        )
        writer.writeheader()
        for index, class_name in enumerate(classes):
            class_name = '"' + class_name + '"'
            writer.writerow(
                {
                    "index": index,
                    "mid": f"{prefix}{index:05d}",
                    "display_name": class_name,
                }
            )


# Usage
create_label_csv(
    "/home/ben2002chou/code/cav-mae/data/cocochorals/class_labels_indices.csv",
    classes,
    custom_prefix,
)
