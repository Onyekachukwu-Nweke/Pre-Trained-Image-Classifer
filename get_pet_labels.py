from os import listdir
import os.path

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from the image directory
    filename_list = listdir(image_dir)

    # Create an empty dictionary named results_dic
    results_dic = {}

    # Iterate through each filename
    for filename in filename_list:
        # Exclude hidden files starting with a dot
        if not filename.startswith('.'):
            # Set the file path
            file_path = os.path.join(image_dir, filename)

            # Check if the file is a regular file (not a directory or symlink)
            if os.path.isfile(file_path):
                # Convert filename to lowercase and remove file extension
                pet_name = os.path.splitext(filename)[0].lower()

                # Split the pet name by underscores to break into words
                word_list_pet_name = pet_name.split('_')

                # Create the pet label starting as an empty string
                pet_label = ''

                # Loop through each word in the pet name
                for word in word_list_pet_name:
                    # Check if the word consists of alphabetic characters only
                    if word.isalpha():
                        # Append the word to the pet label with a trailing space
                        pet_label += word + ' '

                # Strip leading/trailing whitespace characters from the pet label
                pet_label = pet_label.strip()

                # Add the pet label to the results_dic dictionary
                results_dic[filename] = [pet_label]
            else:
                print(f"** Warning: '{filename}' is not a regular file.")

    return results_dic
