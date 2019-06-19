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

        self.has_parents = False

    def has_parents(self):
        if self.patid != '0' 


class Family(object):

    def __init__(self, famid: str, fam_members: List):
        self.famid = famid
        self.individuals  = fam_members

    def family_check(self):



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


def find_family(individuals):
    fam_ids = list(set([x.famid for x in individuals]))
    print(fam_ids)

    for i in fam_ids:
        fam = [x for x in individuals if x.famid == i]
        print(fam)


individuals = []

with open('../examples/not_tab.ped', 'r') as f:
    for line in f:
        line = line.rstrip()
        # check if line starts with comment character (#) or is empty
        if not line or line.startswith('#'):
            continue
        else:
            a = split_pedline(line)
            print(a)

        ind = Individual(a[0], a[1], a[2], a[3], int(a[4]), int(a[5]))
        individuals.append(ind)


for i in individuals:
    print(i.indid)

find_family(individuals)
