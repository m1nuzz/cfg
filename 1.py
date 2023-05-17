import os
import re

season_number = int(input("Enter the season number: "))
current_directory = os.getcwd()

for filename in os.listdir(current_directory):
    if os.path.isfile(filename):
        episode_number = None
        pattern = r"[-_. ](\d+)"
        match = re.search(pattern, filename)
        if match:
            episode_number = match.group(1)
        
        if episode_number is not None:
            new_filename = re.sub(pattern, f"S{season_number:02d}E{episode_number}", filename)
            os.rename(filename, new_filename)
            print(f"Renamed: {filename} to {new_filename}")
        else:
            print(f"No episode number found in the file: {filename}")
