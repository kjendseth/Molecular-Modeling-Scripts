import argparse
import subprocess
import os
import shutil


# Initialize parser
parser = argparse.ArgumentParser(description="Run antechamber, parmchk2, and tleap commands")

# Adding arguments
parser.add_argument('-n', '--name', required=True, help='Name for the output files')
parser.add_argument('-c', '--charge', default='0', help='Charge of the molecule (default: 0)')
parser.add_argument('-m', '--multi', default='1', help='Multiplicity of the molecule (default: 1)')

# Parse the arguments
args = parser.parse_args()

# Access the command line arguments
name = args.name
charge = args.charge
multi = args.multi

# Path to antechamber, adjust as needed
#antechamber_path = "/path/to/antechamber/"

# Run the antechamber and parmchk2 commands
subprocess.run(["antechamber", "-i", "orca.out", "-fi", "orcout", "-o", name + ".mol2", "-fo", "mol2", "-at", "gaff2", "-pf", "y", "-nc", charge, "-c", "abcg2", "-m", multi])
subprocess.run(["parmchk2", "-i", name + ".mol2", "-f", "mol2", "-o", name + ".frcmod"])

# Define the content with the 'MOL' string dynamically replaced
content = f"""source leaprc.gaff2
{name} = loadmol2 {name}.mol2
loadamberparams {name}.frcmod
saveoff {name} {name}.lib
quit"""

# Write the content to a file named 'input_tleap'
with open('input_tleap', 'w') as file:
    file.write(content)

# Run tleap
subprocess.run(["tleap", "-f", "input_tleap"])


# Clean-up section
# Create 'ff_param' folder if it doesn't exist
if not os.path.exists('ff_param'):
    os.makedirs('ff_param')

# Move files to 'ff_param' folder
files_to_move = [f"{name}.mol2", f"{name}.frcmod", f"{name}.lib", "leap.log"]
for file in files_to_move:
    if os.path.exists(file):
        shutil.move(file, os.path.join('ff_param', file))

# Delete unwanted files
files_to_delete = ["input_tleap", "sqm.pdb", "sqm.out", "sqm.in"]
for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)

print("Clean-up completed.")
