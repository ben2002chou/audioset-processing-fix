# AudioSet Processing Fix

Welcome to the `audioset-processing-fix` repository, a toolkit built as an extension and refinement of the `audioset-processing` project by Aoife McDonagh. This repository aims to address specific challenges in processing and managing the AudioSet dataset, particularly focusing on downloading raw audio files, finding missing files, removing corrupted files, and filtering dataset entries.

## Introduction

The AudioSet dataset, created by Google, is a large-scale collection of audio clips drawn from YouTube videos, annotated with a wide range of sound labels. While the original `audioset-processing` project provided a robust method for downloading and managing these audio files, the `audioset-processing-fix` repository enhances this functionality by offering additional scripts for dataset cleaning and integrity checks.

## Repository Structure

This repository contains several Python scripts, each serving a specific purpose in the data processing pipeline:

- `find_missing_files.py`: Identifies missing audio or video files in the dataset.
- `remove_union.py`: Removes entries present in one CSV file that also appear in another.
- `remove_corrupted_files.py`: Deletes corrupted or invalid files from a specified directory.
- `filter_json.py`: Filters entries in a JSON file based on the existence of corresponding video files in a directory.

These scripts are designed for ease of use and can be run from the command line with customizable arguments for specific file paths and other parameters.



## Quick Start

To get started with the `audioset-processing-fix` toolkit, clone the repository and navigate to its directory:

```bash
git clone https://github.com/ben2002chou/audioset-processing-fix.git
cd audioset-processing-fix
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


## Project Overview
This toolkit was developed as part of a project for my Master's thesis. This project involved training a WaveGAN model on subsets of the AudioSet dataset.  

AudioSet is publicly available in two formats; as a list of YouTube-IDs structured as CSV files, or as 128-dimensional feature vectors stored as TFRecord files.
Neither of these formats could be used as training data for the model I was trying to train.
* The problem with using the dataset's audio feature vectors is that in general, audio feature representations are not invertible.
* The problem with using YouTube-IDs is that they are only references to where the audio can be found online, not the samples themselves.

However, using these identifiers is the only way to obtain raw audio to train a WaveGAN model for this project. 
Gathering all samples for an entire class would take an extremely long time and be prone to human error. It would involve a number of lengthy steps which would have to be repeated every time a new data needed to be downloaded;  
1. Parsing the CSV dataset for samples labelled with corresponding class identifier 

2. Storing YouTube-IDs labelled with class identifier. 

3. Putting all IDs into a separate URL addresses. 

4. Downloading YouTube video from which a sample originated 

5. Extract audio, discard video stream. 

6. Using timestamp information in CSV file to retrieve sample. 

7. Storing sample on local machine.  

Since these steps are repeatable for downloading any target class in AudioSet, it made sense to automate this process. A toolkit for downloading the raw audio samples in AudioSet was developed to solve this problem. The toolkit comprises of a set of Python scripts for taking user input, parsing through the dataset, and downloading the relevant audio clips.  

#### Downloading
To download a sub-set of AudioSet, the user can specify target classes they wish to download. Then the csv files distributed for the dataset are parsed for all YouTube-IDs which have a label associated with the given class. Using a number of Python packages, URLs are formed with the YouTube-IDs. Ten second audio clips are downloaded using the generated URLs and corresponding timestamps for each video. Clips are stored locally on the user's machine for future use.  

![alt text](https://github.com/aoifemcdonagh/audioset-processing/blob/master/src/pictures/audioset-processing-download.png "Download flowchart")

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
|   ├── unbalanced_train_segments.csv
|   └── eval_segments.csv
├── src
|   └── pictures
├── demo.ipynb
├── LICENCE
├── process.py
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
