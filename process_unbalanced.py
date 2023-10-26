# Processing utility for AudioSet dataset
# Sort, find and download the entire, or subsets of, AudioSet

# Aoife McDonagh

import argparse
import os
import core.utils_exp as utils


def find(args):
    """
    Function for finding all examples in a directory containing labels for given classes
    :param args:
    :return:
    """
    print("Finding all files labeled with classes" + args.classes + " in " + args.audio_data_dir)

    for class_name in args.classes:
        utils.find(class_name, args)
        print("Finished finding and sorting files for class: " + class_name)


def download(args):
    """
    Function for downloading all examples in AudioSet containing labels for given classes
    :param args:
    :return:
    """
    print("Downloading classes from AudioSet.")

   # Download videos for specified classes
    for class_name in args.classes:
        utils.download(class_name, args)


def download_all(args, start_from_row_n):
    """
    Function for downloading all examples in AudioSet 
    :param args:
    :return:
    """
    print("Downloading from AudioSet.")

   # Download videos for specified classes
    utils.download_all(args, start_from_row_n)

def download_all_multithreaded(args, start_from_row_n, offset):
    """
    Function for downloading all examples in AudioSet 
    :param args:
    :return:
    """
    print("Downloading from AudioSet.")

   # Download videos for specified classes
    utils.download_all_multithreaded(args, start_from_row_n, offset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=['find', 'download', 'download-all', 'download-all-multithreaded'])
    parser.add_argument('--offset', type=int, required=True, help='Offset value for distributing the rows (0-8).')
    parser.add_argument('-c', '--classes', nargs='+', type=str,
                        help='list of classes to find in a given directory of audioset files')
    parser.add_argument('-b', '--blacklist', nargs='+', type=str,
                        help='list of classes which will exclude a clip from being downloaded')
    parser.add_argument('-d', '--destination_dir', type=str,
                        help='directory path to put downloaded (or found) files into')
    parser.add_argument('--audio_data_dir', type=str,
                        help='directory path containing pre-downloaded files from AudioSet')
    parser.add_argument('-fs', "--sample_rate", type=int,
                        help="Sample rate of audio to download. Default 16kHz")
    parser.add_argument('-s', '--strict',
                        help='If used, only match exact string argument passed')
    parser.add_argument('--label_file', type=str,
                        help='Path to CSV file containing AudioSet labels for each class')
    parser.add_argument('--csv_dataset', type=str,
                        help='Path to CSV file containing AudioSet in YouTube-id/timestamp form')

    parser.set_defaults(
        label_file='./data/class_labels_indices.csv',
        csv_dataset='./data/unbalanced_train_segments_missing.csv',
        destination_dir='/grand/EVITA/ben/AudioSet/unbalanced/videos',
        exp_dir='/grand/EVITA/ben/AudioSet/videos',
        fs=16000
    )

    args = parser.parse_args()

    if args.mode == 'find':
        if args.destination_dir is not None and not os.path.isdir(args.destination_dir):
            os.makedirs(args.destination_dir)
        find(args)

    elif args.mode == 'download':
        if args.destination_dir is not None and not os.path.isdir(args.destination_dir):
            os.makedirs(args.destination_dir)
        download(args)
        
    elif args.mode == 'download-all':
        if args.destination_dir is not None and not os.path.isdir(args.destination_dir):
            os.makedirs(args.destination_dir)
        download_all(args, 0)

    elif args.mode == 'download-all-multithreaded':
        if args.destination_dir is not None and not os.path.isdir(args.destination_dir):
            os.makedirs(args.destination_dir)
        download_all_multithreaded(args, 0, args.offset)

#ffmpeg -ss 0 -t 10 -i $(yt-dlp -f 'b' -g https://www.youtube.com/watch?v=--4gqARaEJE) -ar 16000 -y "/grand/EVITA/ben/AudioSet/eval/videos/--4gqARaEJE.mp4"

