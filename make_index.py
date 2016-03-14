import os
import sys
from collections import defaultdict


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
        if not os.path.exists(file):
            raise IOError('The {} is not a valid file'.format(file))
    return True


def parse_file(in_file, dict):
    """

    Function that parse the the file and fill out the dictionary with the appropriate indexes

    :param in_file:
    :param dict:
    :return: dict
    """
    file_name = os.path.basename(in_file)

    with open(in_file, "r") as file_handler:
        for line in file_handler:
            text = line.split(";")
            page, tags = '.'.join([file_name, text[0]]), text[1:]

            if len(tags) > 0:
                for tag in tags:
                    clean_tag = tag.strip().lower()
                    dict[clean_tag].append(page)
            else:
                raise ValueError("The file does not have the right format\n {} \n. "
                                "The line format is: page_number; tag; tag, with subtag one or more times".format(line))

    return dict


def show_results(index_dict):
    """
    Function that print the index

    :param index_dict:
    :return: None
    """
    for elem in sorted(index_dict.keys(), key=str.lower):
        print '{}: {}'.format(elem, ", ".join(index_dict[elem]))


def main():
    dict = defaultdict(list)
    if check_args():
        for file_name in sys.argv[1:]:

            dict.update(parse_file(file_name, dict))
        show_results(dict)


if __name__ == "__main__":
    main()

