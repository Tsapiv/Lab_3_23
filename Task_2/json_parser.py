import json
import pprint
import copy


def read_json(path_to_file):
    """
    :param path_to_file: str
    :return: dict
    Return Twitter's API response that was stored as json a file
    in dict format
    """
    with open(path_to_file, "r", encoding="utf-8") as f:
        file = json.load(f)
    return file


def get_to(file, path):
    """
    :param file: dict or list
    :param path: list
    :return: dict or list
    Return file according to path
    """
    file = copy.deepcopy(file)
    for step in path:
        file = file[step]
    return file


def normalizer(file, verbose):
    """
    :param file: dict or list
    :param verbose: boolean
    :return: ()
    Make a pretty print of data structure
    """
    if verbose:
        if type(file[0]) == dict and len(file[0].keys()) > 4:
            print_list = file[:5]
            for dct in print_list:
                pprint.pprint(str(dct)[:100], width=30)
                print("  ...")
        else:
            pprint.pprint(file)
    else:
        pprint.pprint(list(file.keys()))


def navigator(file_json):
    """

    :param file_json: dict
    :return: list
    Navigates through the json file and returns
    path where user have been to. The last element of
    that list is key value. User can use commands 'back'
    and 'stop'.
    """
    update_value = []

    def manager(file, current_key):
        if current_key == "back":
            try:
                update_value.pop()
            except IndexError:
                inner_parser(file)
            file = get_to(file_json, update_value)
            inner_parser(file)
        elif current_key == "stop":
            return True
        else:
            try:
                update_value.append(current_key)
                inner_parser(file[current_key])
            except IndexError:
                inner_parser(file)
            except KeyError:
                inner_parser(file)
            except ValueError:
                inner_parser(file)

    def inner_parser(file):
        """
        :param file: dict
        Function looks for given key, and appends values
        with the same key to a external list
        """
        if isinstance(file, dict) and file:
            normalizer(file, False)
            current_key = input("Please, choose key: ")
            if manager(file, current_key):
                return
        elif isinstance(file, list) and file:
            print("It's a list, so select item by entering number from 0 to {}".format(len(file)))
            normalizer(file, True)
            ind = input("Choose the number: ")
            if manager(file, int(ind)):
                return
        else:
            update_value.append(file)

    inner_parser(file_json)
    return " -> ".join(list(map(str, update_value))).strip(" -> ")


if __name__ == "__main__":
    path = input("Enter path to your json file: ")
    json_dict = read_json(path)
    print(navigator(json_dict))
