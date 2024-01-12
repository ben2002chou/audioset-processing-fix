import pretty_midi
import h5py
import json
import os


def midi_to_pianoroll(midi_file, fs=100):
    """
    Convert MIDI file to piano roll.
    """
    pm = pretty_midi.PrettyMIDI(midi_file)
    pianoroll = pm.get_piano_roll(fs=fs).T
    return pianoroll


def save_pianoroll_h5(pianoroll, h5_file):
    """
    Save piano roll to an H5 file.
    """
    with h5py.File(h5_file, "w") as hf:
        hf.create_dataset("pianoroll", data=pianoroll)


def preprocess_midi_files(json_file):
    """
    Process all MIDI files listed in the JSON file.
    """
    with open(json_file, "r") as f:
        data = json.load(f)["data"]

    for entry in data:
        midi_file = entry["wav2"]
        if midi_file.endswith(".mid"):
            pianoroll = midi_to_pianoroll(midi_file)
            h5_file = midi_file.replace(".mid", ".h5")
            save_pianoroll_h5(pianoroll, h5_file)
            print(f"Processed: {midi_file}")


# Replace 'path_to_your_json_file.json' with the path to your JSON file
preprocess_midi_files(
    "/home/ben2002chou/code/cav-mae/data/cocochorals/cocochorals_valid.json"
)
