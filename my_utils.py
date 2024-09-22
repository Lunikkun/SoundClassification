import os;
import sys
def clone_hierarchy(source_dir, dest_dir):
    i=0;
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            i=i+1;
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(dest_dir, relative_path)

        if not os.path.exists(target_path):
            os.makedirs(target_path)
            print(f"Creata cartella: {target_path}")
    return i
