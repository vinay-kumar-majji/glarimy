import argparse

def deduplicate(duplicate_string):
    distinct_words_list = []
    string_list = duplicate_string.split()
    for word in string_list:
        if word not in distinct_words_list :
            distinct_words_list.append(word)
    return distinct_words_list
    
def sort(string_list):
    sorted_list = sorted(string_list)
    return sorted_list
    
def parse(string):
    file = open(string, "r")
    content = file.read()
    file.close()
    distinct_words_list = deduplicate(content)
    sorted_words_list = sort(distinct_words_list)
    sorted_words = " ".join(sorted_words_list)
    print(sorted_words)
 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputfile", required=True, help="Path to the input text file")
args = vars(ap.parse_args())
parse(args["inputfile"])
 
