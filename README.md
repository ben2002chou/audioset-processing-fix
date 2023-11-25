# AudioSet Download + Processing 

## Introduction

This repo is created for reproducing CAV-MAE. It helps download audioset and removed unused and corrupted videos.

## Additions

This repository contains several Python scripts, each serving a specific purpose in the data processing pipeline:
- `clean_unbalanced_regex.py`: Reformats unbalanced data CSV file so that it works with this repo
- `find_missing_files.py`: Identifies missing audio or video files in the dataset.
- `remove_union.py`: Removes entries present in one CSV file that also appear in another.
- `remove_corrupted_files.py`: Deletes corrupted or invalid files from a specified directory.
- `filter_json.py`: Filters entries in a JSON file based on the existence of corresponding video files in a directory.
- `update_datafiles.py`: Updates training datafiles (json format) after removal of corrupted files
  
Running remove_corrupted_missing.sh will remove all videos that are corrupted and cannot be extracted.
You have to change the file directories to your own.



## Quick Start

To get started with the `audioset-processing-fix` toolkit, clone the repository and navigate to its directory:

```bash
git clone https://github.com/ben2002chou/audioset-processing-fix.git
cd audioset-processing-fix/bin
```

Each script can be run from the command line. For example, to identify missing .mp4 video files, use:

```bash
python find_missing_files.py <input_csv_path> <output_csv_path> <directory_path> .mp4
```

Replace the placeholders with appropriate file paths and extensions.

## Usage

Detailed usage instructions for each script are available at the beginning of the script files. Ensure you have the necessary files and directories set up as per the requirements of each script.

## Dependencies
- python3
- ffmpeg
- youtube-dl 2019.7.2

## Quick start

To download files from AudioSet
```	
python3 process.py 
```
Uses CSV files found in `data/` by default. Execute `process.py` in its' own directory.


## AudioSet
AudioSet can be downloaded from Google [here](https://research.google.com/audioset/download.html) as a set of CSV files. For each element in the dataset the CSV files list an associated YouTube ID, start time, end time and class labels. The CSV files are used to download AudioSet as raw audio files (WAV).

## Structure
```
audioset-processing
├── procas
|   ├── utils.py
|   └── download.sh
├── data
|   ├── balanced_train_segments.csv
|   ├── class_labels_indices.csv
|   ├── unbalanced_train_segments.csv # Need to redownload
|   └── eval_segments.csv
├── src
|   └── pictures
├── demo.ipynb
├── LICENCE
├── process.py # download balanced videos
├── process_eval.py # download evaluation videos
├── process_unbalanced.py # download unbalanced videos
├── requirements.txt
└── README.md
```
## Acknowledgments

- Aoife McDonagh for the original `audioset-processing` project.
- Google for creating and maintaining the AudioSet dataset.

  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file in the original `audioset-processing` repository for details.

---

This README provides a brief overview of the `audioset-processing-fix` repository. For more detailed information about the original project, visit [audioset-processing](https://github.com/aoifemcdonagh/audioset-processing).
