from pymol import cmd

def format_atom_ids(atom_ids):
    # Sort the atom IDs first to ensure proper sequencing
    #atom_ids.sort()
    
    #print(atom_ids)
    formatted_ids = []
    start = atom_ids[0]
    end = atom_ids[0]

    for i in range(1, len(atom_ids)):
        # Check if the current ID is consecutive to the previous one
        if atom_ids[i] == end + 1:
            end = atom_ids[i]
        else:
            # Add the range or the single number to the formatted list
            if start == end:
                formatted_ids.append(f"{start}")
            else:
                formatted_ids.append(f"{start}:{end}")
            # Reset the start and end for the next range
            start = atom_ids[i]
            end = atom_ids[i]
    
    # Handle the last group
    if start == end:
        formatted_ids.append(f"{start}")
    else:
        formatted_ids.append(f"{start}:{end}")

    # Join all formatted parts with spaces
    return " ".join(formatted_ids)

def get_atom_ids():
    # Get the atom information for the current selection "sele"
    atom_ids = []
    
    # Iterate through the selected atoms and store their IDs
    model = cmd.get_model("as")
    for atom in model.atom:
        #print(atom.id)
        atom_ids.append(atom.id)  # Collect atom IDs without modifying them
    
    # Sort the atom IDs before subtracting 1
    atom_ids.sort()
    
    # Subtract 1 from each atom ID
    atom_ids = [id - 1 for id in atom_ids]
    
    # Format the atom IDs
    formatted_atom_ids = format_atom_ids(atom_ids)
    
    # Print the formatted atom IDs
    print("Atom IDs in selection 'sele' (after subtracting 1):", formatted_atom_ids)

# Execute the function
get_atom_ids()
