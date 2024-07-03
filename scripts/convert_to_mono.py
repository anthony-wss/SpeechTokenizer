from argparse import ArgumentParser
import os
import soundfile as sf
import librosa
from tqdm import tqdm


def main(args):
    input_dir = args.input_dir
    target_sr = args.sr
    assert os.path.exists(input_dir), ""

    for audio_file in tqdm(os.listdir(input_dir)):
        data, samplerate = sf.read(os.path.join(input_dir, audio_file))
        data = data.squeeze()
        if len(data.shape) > 1:
            data = data.mean(-1)
        if samplerate != target_sr:
            data = librosa.resample(data, orig_sr=samplerate, target_sr=target_sr)
        sf.write(os.path.join(input_dir, audio_file), data, target_sr) # data should be 1-dim tensor


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input_dir", required=True, type=str)
    parser.add_argument("-sr", required=True, type=int, help="Target sample rate")
    args = parser.parse_args()

    main(args)