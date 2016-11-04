# TurboVina
This project will automate the processing of multiple ligands in autodock vina using a python script

It is used in conjunction with autodock vina found here: http://vina.scripps.edu/

It is assumed that the vina.exe program and all required files are stored in C://Program1/TSRI/Vina

The goal of the program is to allow user input of the static variables (see below) followed by running vina.exe iteratively for all ligand files in a particular folder without additional user input.  

Required static variables to be pulled from the user are:

receptor file in .pdbqt format
#receptor

ligand file in .pdbqt format
#ligand 

coordinates in angstroms
#center_x, center_y, center_z

dimensions of the search grid in angstroms
#size_x, size_y, size_z

number of cpu cores to use
#cpu

how hard / accurate the docking calculation is
#exhaustiveness

naming of the output file - should apend .pdbqt to the input string
#out

Optional static variables to be used as inputs

the path and file name of the ligand (for debug purposes only)
#ligand

The folder where ligands are stored.
#flig
