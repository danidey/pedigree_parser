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

        if self.patid != '0':
            self.has_father = True
        else:
            self.has_mother = False

        if self.matid != '0':
            self.has_mother = True
        else:
            self.has_mother = False


class Family(object):

    def __init__(self, famid: str, fam_members: List):
        self.famid = famid
        self.individuals = fam_members

    def check_relations(self):
        pass
        #for ind in self.individuals:




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

    families = []
    for i in fam_ids:
        fam_individuals = [x for x in individuals if x.famid == i]
        fam = Family(i, fam_individuals)
        families.append(fam)

    return families



def read_pedfile(ped):
    individuals = []

    with open(ped, 'r') as f:
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

    return individuals


def main():
    ped = '../examples/not_tab.ped'
    individuals = read_pedfile(ped)

    for i in individuals:
        print(i.indid, i.has_parents)

    find_family(individuals)

if __name__ == '__main__':
    main()