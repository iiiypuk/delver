#!/usr/bin/env python3

import json

__author__ = 'Alexander Popov'
__version__ = '1.0.0'
__license__ = 'Unlicense'

exportData = list()


def loadStrings():
    with open('strings.dat', 'r', encoding='utf-8') as f:
            jsonData = json.loads(f.read())

            for string in jsonData:
                exportData.append('"%s":{\n"original": "%s",\n"localizedName": "%s"},' %
                                  (string,
                                   jsonData[string]['localizedName'].replace('\n', '<N3WL1NE>'),
                                   jsonData[string]['localizedName'].replace('\n', '<N3WL1NE>')))

    return('Complete!')


def saveStrings():
    with open('result.txt', 'w+', encoding='utf-8', newline='\n') as f:
            for string in exportData:
                f.write('%s%s' % (string, '\n' * 2,))

    return('Complete!')

if __name__ == '__main__':
    print('Loading strings...', loadStrings())
    print('Save strings for notabenoid...', saveStrings())
    print('\nComplete!')

