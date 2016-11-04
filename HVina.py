#import whatever you need
import sys, string, os, subprocess, shlex

print ("Hello Vina")
print ("A helper program for automating autodoc vina")
#
### THE FOLLOWING ARE INPUTS FOR VINA.EXE###

#fill default strings for file names
receptor = "5j89.pdbqt"
ligand = "Amy_ligand.pdbqt"
out = "example_out.pdbqt"
log = "example_log.log"

#default values for screeneing
center_x = 1
center_y = 1
center_z = 1
size_x = 1
size_y = 1
size_z = 1

#default values for processing parameters
cpu = 10
exhaustiveness = 8
num_modes = 9

#optional user input for each variable

#number of ligands total
print("setting up default values")
ligandnum = input(["how many ligands?"])
print("you have " + ligandnum + " ligands!")

#receptor file name
receptor = input(["enter receptor file name"])
print("receptor file name is " + receptor + "!")

#Format Variables as Strings to use is subprocess.Popen

strcenter_x = str (center_x)
strcenter_y = str (center_y)
strcenter_z = str (center_z)
strsize_x = str (size_x)
strsize_y = str (size_y)
strsize_z = str (size_z)

#Output Vina Variables Here (For Debugging)
#" --receptor 5j89.pdbqt" + " --ligand Any_Ligand.pdbqt"
print (\
				 " --center_x " + strcenter_x \
				 + " --center_y " + strcenter_y \
				 + " --center_z " + strcenter_z \
				 + " --size_x " + strsize_x \
				 + " --size_y " + strsize_y \
				 + " --size_z " + strsize_z)

input("\n\nPress Enter to run Vina with these parameters")

#Call Vina
#Note: Vina needs to be installed in C:\Program1\TSRI\vina

subprocess.Popen(r"C:\Program1\TSRI\vina\vina.exe" + " --receptor " + receptor + " --ligand " + ligand\
				 + " --center_x " + strcenter_x \
				 + " --center_y " + strcenter_y \
				 + " --center_z " + strcenter_z \
				 + " --size_x " + strsize_x \
				 + " --size_y " + strsize_y \
				 + " --size_z " + strsize_z)

#pausing the end of program
input("\n\nPress Enter to Exit - As if you had a choice :)")