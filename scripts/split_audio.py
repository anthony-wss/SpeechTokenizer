from argparse import ArgumentParser
import os
import soundfile as sf
import librosa
from tqdm import tqdm


def main(args):
    input_dir = args.input_dir
    output_dir = args.output_dir
    assert os.path.exists(input_dir), ""
    os.makedirs(output_dir, exist_ok=True)

    for audio_file in tqdm(os.listdir(input_dir)):
        data, samplerate = sf.read(os.path.join(input_dir, audio_file))
        assert len(data.shape) == 1

        ext = audio_file.split(".")[-1]
        audio_filename = "".join(audio_file.split(".")[:-1])

        chunk_size = 3*16000
        for i in range(0, data.shape[0]//chunk_size):
            if (i+1) * chunk_size <= data.shape[0]:
                sample_filename = audio_filename + "_" + str(i) + "." + ext
                sf.write(os.path.join(output_dir, sample_filename), data[i*chunk_size : (i+1)*chunk_size], samplerate)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)
    args = parser.parse_args()

    main(args)