import os

# Set the directory path and suffix to delete
directory = './processed_generated_shapes_plus_1000'
# suffix = '.txt'

# Iterate through all files in the directory
for file in os.listdir(directory):
    # Check if the file has the specified suffix
    if len(file.split('_')[-1])==9:
        # Construct the full file path
        file_path = os.path.join(directory, file)
        print(file_path)
        # Delete the file
        os.remove(file_path)