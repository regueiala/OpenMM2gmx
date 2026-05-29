import numpy as np
import MDAnalysis as mda
from scipy.spatial.distance import cdist

# load the universe from the .gro file
u = mda.Universe("pthrp.gro")

# computig the center of mass of the protein
protein = u.select_atoms("protein")
com_protein = protein.center_of_mass()
print(f"center of mass : {com_protein}")

# searching for the residue closest to the center of mass
a = None
min_dist = float("inf")
for residu in protein.residues:
    com_residu = residu.atoms.center_of_mass()
    distance = np.linalg.norm(com_residu - com_protein)

    if distance < min_dist:
        min_dist = distance
        closest_residue = residu

print(
    f"The residue closest to the center of mass is : {closest_residue.resname} (Resid: {closest_residue.resid})"
)
