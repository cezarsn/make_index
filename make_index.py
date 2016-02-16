import os
import sys


def check_args():
    """
    Function that check if the files can be found and used

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


def parse_file(in_file, dict):
    """

    Function that parse the the file and fill out the dictionary with the appropriate indexes

    :param in_file:
    :param dict:
    :return: dict
    """
    file_name = os.path.basename(in_file)

    try:
        file_handler = open(in_file, "r")
    except IOError as e:
        print ('Failed to open the file because {}:'.format(e))
        sys.exit(1)

    for line in file_handler:
        elem =  line.split(";")
        if len(elem) > 1:
            for index in range(1, len(elem)):
                clean_elem = elem[index].strip().lower()
                if clean_elem not in dict.keys():
                    list_new = []
                else:
                    list_new = dict[clean_elem]
                list_new.append(file_name + '.' + str(elem[0]))
                dict[clean_elem] = list_new
        else:
            print("The file does not have the right format")
            sys.exit(1)
    file_handler.close()
    return dict


def show_results(index_dict):
    """
    Function that print the index

    :param index_dict:
    :return: None
    """
    for elem in sorted(index_dict.keys(), key=str.lower):
        print '{}: {}'.format(elem, " ".join(index_dict[elem]))


def main():
    dict = {}
    if check_args():
        for file in sys.argv[1:]:
            dict.update(parse_file(file, dict))
        show_results(dict)


if __name__ == "__main__":
    main()