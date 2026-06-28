import os
import shutil

path = r"\\LMPC202507256L\Keeper\Daily's Report\DDD"

# os.makedirs(path.__add__("\DDD"), exist_ok=True)

for _ in os.listdir(path):
    to_file = os.path.join(path, _)
    if os.path.isfile(to_file):
        os.remove(to_file)