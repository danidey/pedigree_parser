import exceptions
from typing import List
import csv


class Individual(object):

    def __init__(self, famid: str, indid: str, patid: str, matid: str, sex: int, aff: int):
        self.famid = famid
        self.indid = indid
        self.patid = patid
        self.matid = matid
        self.sex = sex
        self.aff = aff


def split_pedline(line: str) -> List[str]:
    # try to split line on different possible separators
    separators = ['\t', ' ', ',', ';']

    for i in separators:
        split_line = line.split(i)
        if len(split_line) == 6:
            break
        else:
            continue

    if len(split_line) < 6:
        message = 'tried tab, space, comma and semicolon as separators, file format wrong'
        raise exceptions.FileFormatError(message)
    else:
        return split_line


with open('../examples/not_tab.ped', 'r') as f:
    for line in f:
        line = line.rstrip()
        # check if line starts with comment character (#) or is empty
        if not line or line.startswith('#'):
            continue
        else:
            a = split_pedline(line)
            print(a)

