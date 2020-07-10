import json
from pprint import pprint


def test():
    print('klib test ok!')


def indexListAccordKey(list,key):
    indexedList = {}
    for item in list:
        key_val = item[key]
        item.pop(key, None)
        indexedList[key_val] = item
    return indexedList