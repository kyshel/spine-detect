# klibX.py
# X means version here
# v1 indexListAccoed key
# v2 save_obj and load_obj




import json
from pprint import pprint

import pickle


def test():
    print('klib test ok!')


def indexListAccordKey(list,key):
    indexedList = {}
    for item in list:
        key_val = item[key]
        item.pop(key, None)
        indexedList[key_val] = item
    return indexedList


def save_obj(obj_name,file_name):
    with open(file_name, 'wb') as config_dictionary_file:
        pickle.dump(obj_name, config_dictionary_file)

        print(file_name + ' saved!')
        return


def load_obj(file_name):
    with open(file_name, 'rb') as config_dictionary_file:
        config_dictionary = pickle.load(config_dictionary_file)
        print(file_name + ' loaded!')
        return config_dictionary
