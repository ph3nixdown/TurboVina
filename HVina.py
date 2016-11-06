#import whatever you need
import sys, string, os, subprocess, shlex

print ("          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" + "\n"\
	   + "          $                Vina Express                     $" + "\n"\
	   + "          $            (name under revision)                $" + "\n"\
	   + "          $                                                 $" + "\n"\
	   + "          $   A helper program for automating autodoc vina  $" + "\n"\
	   + "          $   by R.J. Mancini, Ph.D                         $" + "\n"\
	   + "          $                                                 $" + "\n"\
	   + "          $                  version 0.01                   $" + "\n"\
	   + "          $                                                 $" + "\n"\
	   + "          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" + "\n\n")

#To give the user an option to quit - also used to figure out if things will run
a = "b"
a = input(["q to quit or Press enter to continue..."])
if a == "q" : sys.exit ()

print ("\n" + "WARNING: This program makes the following assumptions:" + "\n\n"\
	   "1. Autodock Vina is installed in the directory C:\\Program1\\TSRI\\Vina" + "\n\n"\
	   "2. A pdbqt receptor file is stored in the directory C:\\Program1\\TSRI\\Vina" + "\n\n"\
	   "3. Ligands in library have the same root name followed by (number).pdbqt" + "\n"\
	   "   Example: a ligand name of 'root' would become 'root (1)', 'root (2)', etc... ")

a = "b"
a = input(["q to quit or Press enter to continue..."])
if a == "q" : sys.exit ()

### THE FOLLOWING ARE INPUTS FOR VINA.EXE###

#fill default strings for file names
receptor = "5j89.pdbqt"
ligpath = "C:\\Program1\\TSRI\\Vina"
ligfile = "1"
out = "example_out.pdbqt"
log = "example_log.log"
lignum = 1

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

#Add while loop to allow data revision
p = "r" #initialize as string

while p == "r":
	#number of ligands total
	print("setting up default values")
	lignum = input(["how many ligands?"])
	#string version because python cannot do this implicitly
	slignum = str(lignum)
	print("you have " + slignum + " ligands! \n\n")
	#folder where ligands are stored
	ligpath = input(["where are ligands stored? (enter directory with \\)"])
	print ("ligands are stored in " + ligpath + "! \n\n")
	#file name to have (number).pdbqt apended to it
	ligfile = input(["root name of first ligand? (eg. enter '1 (1).pdbqt' as 1 )"])
	print ("first ligand is " + ligfile + "! \n\n")
		
	#receptor file name
	receptor = input(["enter receptor file name"])
	print("receptor file name is " + receptor + "! \n\n")

	#processing parameters
	cpu = input(["how many cpu cores to use?"])
	print ("you will use " + cpu + " cores!" + "\n\n")

	exhaustiveness = input(["what level of exhaustiveness to use?"])
	print ("you will use " + exhaustiveness + " level of exhaustiveness! \n\n" )
	
	num_modes = input(["how many binding modes?"])
	print ("we will calculate " + num_modes + " binding modes \n\n")
	print ("receptor = " + receptor +"\n"\
	   + "ligand root = " + ligfile + "\n"\
	   + "number of ligands = " + slignum + "\n"\
	   + "path of ligands = " + ligpath + "\n"\
	   + "number of cpu cores = " + cpu + "\n"\
	   + "ehaustiveness = " + exhaustiveness + "\n"\
	   + "number of binding modes = " + num_modes + "\n")
	p = "Q"
	print ("\n\n")
	p = input (["Are these variables correct? Enter to continue type r to redo"])

#Add while loop to allow data revision
p = "r" #initialize as string

while p == "r":
	aligfile = str(ligfile + " (" + slignum + ").pdbqt")
	print ("first ligand = " + aligfile)
	print ("and will be called as " + '"' + ligpath + "\\" + aligfile + '"')
	#Add while loop to allow data revision
	p = "Q"
	print ("\n\n")
	p = input (["This is the first ligand. Press Enter to continue..."])

p = "r" #initialize as string
#user input of scanning grid center

while p == "r":
	center_x = input(["enter center_x in angstroms"])
	center_y = input(["enter center_y in angstroms"])
	center_z = input(["enter center_z in angstroms"])
	print ("center_x, center_y, and center_z is " + center_x + " " + center_y + " " + center_z)
	p = "Q"
	print ("\n\n")
	p = input (["Are these variables correct? Enter to continue type r to redo"])

p = "r" #setting from previous loop
while p == "r":
	#user input of grid dimensions
	size_x = input(["enter size_x in angstroms"])
	size_y = input(["enter size_y in angstroms"])
	size_z = input(["enter size_z in angstroms"])
	print ("size_x, size_y, and size_z is " + size_x + " " + size_y + " " + size_z)
	p = "Q"
	print ("\n\n")
	p = input (["Are these variables correct? Enter to continue type r to redo"])

#Format Variables as Strings to use in subprocess.Popen

strcenter_x = str (center_x)
strcenter_y = str (center_y)
strcenter_z = str (center_z)
strsize_x = str (size_x)
strsize_y = str (size_y)
strsize_z = str (size_z)
strcpu = str (cpu)
strexhaustiveness = str(exhaustiveness)
strnum_modes = str(num_modes)

#Add path to the receptor and ligand variables - note: must use "\\" instead of "\"
freceptor = str ("C:\\Program1\\TSRI\\Vina\\" + receptor)

#to set up fligand for printing
fligand = str ('"' + ligpath + "\\" + aligfile + '"')

#Output Vina Variables Here (For Debugging)
#" --receptor 5j89.pdbqt" + " --ligand Any_Ligand.pdbqt"
print (\
				 " --center_x " + strcenter_x \
				 + " --center_y " + strcenter_y \
				 + " --center_z " + strcenter_z \
				 + " --size_x " + strsize_x \
				 + " --size_y " + strsize_y \
				 + " --size_z " + strsize_z\
				 + " --receptor " + freceptor\
				 + " --ligand " + fligand)

#provides option to exit without running the calculation
a = "b"
a = input(["q to quit or Press enter to run vina with these parameters..."])
if a == "q" : sys.exit ()

#CALL VINA
#Note: Vina needs to be installed in C:\Program1\TSRI\vina

lignum1 = int(lignum)


while lignum1 > 0 :
	#to set up fligand in subsequent loops
	fligand = str ('"' + ligpath + "\\" + aligfile + '"')
	
	subprocess.call(r"C:\Program1\TSRI\vina\vina.exe" + " --receptor " + freceptor + " --ligand " + fligand\
					 + " --center_x " + strcenter_x \
					 + " --center_y " + strcenter_y \
					 + " --center_z " + strcenter_z \
					 + " --size_x " + strsize_x \
					 + " --size_y " + strsize_y \
					 + " --size_z " + strsize_z \
					 + " --cpu " + strcpu \
					 + " --exhaustiveness " + strexhaustiveness \
					 + " --num_modes " + strnum_modes\
					 + " --out C:\\Program1\\TSRI\\vina\\test2\\" + slignum + ".pdbqt")
	lignum1 = lignum1 - 1
	slignum = str(lignum1)

lignum1 = str(lignum1)
print ("program checksum = 0 if completed succesfully result = " + lignum1)
#pausing the end of program
input("\n\nPress Enter to Exit - As if you had a choice :)")
