# Molecular-Modeling-Scripts
Scripts for simplifying various MD and QM calculations

MOLPARAM:
1) molparam.py usage: molparam.py [-h] -n NAME [-c CHARGE] [-m MULTIPLICITY]
2) Require that ORCA 6 and AmberTools24 are installed and that PATH is updated.
3) A python wrapper script that reads the output coordinates from a ORCA 6 geometry opimization, dervies partial charges with the new abcg2 method and build LIB and frcmod files based on the gaff2 force field.
4) This script should be fine for organic molecules (not metal comnplexes). I recommend to rub ORCA with ! BP86 def2-SVP OPT TightSCF CPCM(water).

QMATOMS2ORCA:
1) Save the file qmatoms2orca.py to you PyMOL working dir.
2) Load the coordinate file in PyMOL.
3) Use PyMOL selection algebra to retain the wanted QM atoms in the selection named "sele"
4) Run the script by executing the following command in the PyMOL terminal: run qmatoms2orca.py
5) Copy the printed list into the orca imnput file (e.g.  QMAtoms {692:708 932:948 998:1017 1075:1091 3173:3189 3244:3260 3520:3539 3596:3612 4596:4623} end )
