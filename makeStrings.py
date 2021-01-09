#!/usr/bin/env python3

import json

__author__ = 'Alexander Popov'
__version__ = '1.0.0'
__license__ = 'Unlicense'

# translateData = dict()


def loadTranslate():
    with open('[NEW]_strings.dat.txt', 'r', encoding='utf-8') as f:
            # translateData = f.read().split('\n\n')
            # translateStrings = dict()
            # # stringsArray = [row.strip() for row in f]
            # for item in translateData:
            #     text = item.split('\n')
            #     translateStrings[text[0]] = text[1]
            #     # print(text)

            return(json.loads(f.read()))


def replaceStrings():
    with open('mods/delver-pack-ru-ru/data/strings_orig.dat', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())

        translatedStings = loadTranslate()

        for item in data:
            # print(translatedStings[item])
            # print(translatedStings[item])
            data[item]['localizedName'] = translatedStings[item]['localizedName']
            # print(translatedStings[item])

        with open('strings.dat', 'w', encoding='utf-8') as f1:
            json.dump(data, f1, ensure_ascii=False)

if __name__ == '__main__':
    replaceStrings()

