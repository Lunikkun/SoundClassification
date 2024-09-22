import sys, os
import librosa
import soundfile as sf
from my_utils import clone_hierarchy

def audio_cutter(file_name, dest_dir, split_lenght):

    audio, sr = librosa.load(file_name);
    audio = librosa.util.normalize(audio);
    buffer = split_lenght * sr
    samples_total = len(audio)
    samples_wrote = 0
    counter = 1

    while samples_wrote < samples_total:
        #print(counter)
        
        if buffer > (samples_total - samples_wrote):
            buffer = samples_total - samples_wrote

        block = audio[samples_wrote : (samples_wrote + buffer)]
        out_filename = os.path.dirname(dest_dir)+"/split_" + str(counter) + "_" + os.path.basename(file_name);
        #print(os.path.dirname(file_name));
        sf.write(out_filename, block, sr)
        counter += 1
        samples_wrote += buffer    


#MAIN TO USE CHIAMARE DA TERMINALE CON SOURCE FOLDER E DEST FOLDER COME PARAMETRI DI COMANDO
source_dir = sys.argv[1]
dest_dir = sys.argv[2]
split_lenght = int(sys.argv[3])
n_files = clone_hierarchy(source_dir, dest_dir);
count = 0;
for path, names, files in os.walk(source_dir):
    for file in files:
        if(file.endswith(".mp3") or file.endswith(".wav")):
                file_path = os.path.join(path, file)
                other_file_path = os.path.join(os.path.join(dest_dir, os.path.basename(path)), file)
                audio_cutter(file_path, other_file_path, split_lenght);
                #print(os.path.join(os.path.join(dest_dir, os.path.basename(path)), file));
                print("Done: "+str((count/n_files)*100)+"%")
                count=count+1;

print("Fils found: "+str(n_files));