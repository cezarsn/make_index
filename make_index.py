import os
import sys


def check_args():
    """


    :return:
    """
    if len(sys.argv) == 1:
        print('NOTE: Filenames will be used to create the index reference.\n'
              'Please enter the names of the files to create the index from, separated by spaces: "')
        sys.exit(1)
    for file in sys.argv:
        if not os.path.isfile(file):
            print 'The {} is not a file'.format(file)
            sys.exit(1)
    return True


def parse_file(in_file):
    """

    Function that parse the the file and fill out the dictionary with the appropriate indexes

    :param in_file:
    :return:
    """
    file_name = os.path.basename(in_file)

    try:
        file_handler = open(in_file, "r")
    except IOError as e:
        print ('Failed to open the file because {}:'.format(e))
        sys.exit(1)

    for line in file_handler:
        elem =  line.split(";")
        for index in range(1, len(elem)):
            clean_elem = elem[index].strip().lower()
            if clean_elem not in dict.keys():
                list_new = []
            else:
                list_new = dict[clean_elem]
            list_new.append(file_name + '.' + str(elem[0]))
            dict[clean_elem] = list_new
    file_handler.close()
    return dict



def show_results(index_dict):
    """
    Function that print the index

    :param index_dict:
    :return: None
    """
    for elem in  sorted(index_dict.keys(), key=str.lower):
        print '{}: {}'.format(elem, " ".join(index_dict[elem]))

def main():
    pass


if __name__ == "__main__":
    dict = {}
    if check_args():
        for file in sys.argv[1:]:
            dict.update(new_parse_file(file))
        show_results(dict)
