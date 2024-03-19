"""Task

dataset https://archive.ics.uci.edu/ml/datasets/Bag+of+Words

q1 try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count sample
    example [('sudh', 6), ('kumar',3)]
q2 = try to perform a reduce operation to get a count of all the word starting with same alphabet sample
    example = [(a,56), (b,34),]
q3 Try to filter out all the words from dataset.
    001.abstract = abstract
    =.002 = delete
q4 create a tuple set of all the records available in all the five file and then store it in sqlite DB. (aah,,354,fdsf,wer)
"""
# imports
import re
from collections import Counter

# access file of dataset
try:
    import os


    def extract_file_names(directory_path):
        # Check if the directory path exists
        if not os.path.isdir(directory_path):
            print(f"Error: {directory_path} is not a valid directory path.")
            return []

        # Get a list of all files and directories in the specified directory
        files_and_dirs = os.listdir(directory_path)

        # Filter out only the file names from the list
        file_names = ['E:\Git\Databases\dataset\\' + file for file in files_and_dirs
                      if
                      os.path.isfile(os.path.join(directory_path, file))]

        return file_names


    directory_path = 'E:\Git\Databases\dataset'

    # Call the function to extract file names
    file_paths = extract_file_names(directory_path)

except:
    print("your file cant be get")


# clean of words from files put tuple
def gets_words(filepath):
    try:
        with (open(filepath, "r", encoding="utf-8") as file):
            words = (file.read()).split()
            pattern = re.compile(r'[^\W\d_]+')

            def contains_alphabets(element):
                return bool(pattern.search(element))

            extracted_strings = [pattern.findall(text)[0] for text in words if contains_alphabets(text)]
            return extracted_strings
    except Exception as e:
        print("error with word cleaning", e)


def count_of_element(elements):
    element_counts = Counter(elements)
    list_for_count = []
    for i in element_counts:
        t = (i,element_counts[i])
        list_for_count.append(t)
    return list_for_count


list_of_words = []
for path in file_paths:
    a = gets_words(path)
    b = count_of_element(list_of_words)

