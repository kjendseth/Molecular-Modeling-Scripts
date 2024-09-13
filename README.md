# Molecular-Modeling-Scripts
Scripts for simplifying various MD and QM calculations

1) molparam.py usage: molparam.py [-h] -n NAME [-c CHARGE] [-m MULTIPLICITY]
2) Require that ORCA 6 and AmberTools24 are installed and that PATH is updated.
3) A python wrapper script that reads the output coordinates from a ORCA 6 geometry opimization, dervies partial charges with the new abcg2 method and build LIB and frcmod files based on the gaff2 force field.
4) This script should be fine for organic molecules (not metal comnplexes). I recommend to rub ORCA with ! BP86 def2-SVP OPT TightSCF CPCM(water).
