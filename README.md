# Pedigree File Parser

Python package to parse pedigree files and check family constellations.

Code is generally inspired by the Pedigree Parser by Moonso (https://github.com/moonso/ped_parser). 

## What is a ped file?

Description: https://gatk.broadinstitute.org/hc/en-us/articles/360035531972

Basic text file that consists of 6 mandatory columns: 

1. Family ID
2. Individual ID
3. Paternal ID
4. Maternal ID
5. Sex (1 = m, 2 = f)
6. Phenotype (Affection status, 1 = unaffected, 2 = affected, 0/-9 = missing)


Example:
```
FAM001  1  0 0  1  2
FAM001  2  0 0  1  2
```
