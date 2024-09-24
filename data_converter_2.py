import sys, os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from my_utils import clone_hierarchy

source_dir = sys.argv[1];
dest_dir = sys.argv[2];
spectrogram_repr = sys.argv[3];

def create_spectrogram(audio_file, image_file, spectrogram_repr):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    y, sr = librosa.load(audio_file)
    if(spectrogram_repr == "mel"):
        ms = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=512, hop_length=128)
        log_ms = librosa.power_to_db(ms, ref=np.max)
    elif(spectrogram_repr == "mfcc"):
        ms = librosa.feature.mfcc(y=y, sr=sr)
        log_ms = librosa.power_to_db(ms, ref=np.max)
    elif(spectrogram_repr == "stft"):
        ms = np.abs(librosa.stft(y=y))
        log_ms = librosa.amplitude_to_db(ms, ref=np.max)
    else:
        print("mfcc for Mel-frequency cepstral coefficients - mel for Mel Spectrogram - stft for Short Fourier Transformation")
    librosa.display.specshow(log_ms, sr=sr, x_axis='time', y_axis='mel', fmax=8192, ax=ax);

    fig.savefig(image_file)
    plt.close(fig)


n_files = clone_hierarchy(source_dir, dest_dir);
count = 0;
for path, names, files in os.walk(source_dir):
    for file in files: 
        extension = os.path.splitext(file)[1];
        if(extension == ".mp3" or extension == ".wav"):
            file_img = file.replace(extension, ".png");
            other_file_path = os.path.join(os.path.join(dest_dir, os.path.basename(path)), file_img)
            create_spectrogram(os.path.join(path, file), other_file_path, spectrogram_repr);
            print("Done: "+str((count/n_files)*100)+"%");
            count=count+1;