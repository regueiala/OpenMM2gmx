import mdtraj as md
import numpy as np

traj = md.load("output.dcd", top="step5_input.parm7")

# sanitize box vectors
bv = traj.unitcell_vectors.copy()

bv[0]
bv[np.abs(bv) < 1e-5] = 0.0

traj.unitcell_vectors = bv
traj.save_xtc("trj_gromacs.xtc")
