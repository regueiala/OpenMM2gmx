"""Convert an openmm trajectory to GROMACS format, with treating the box vectors as triclinic.
This is needed for the case when the box vectors are not exactly orthogonal, which can cause issues when converting to GROMACS format.

This script loads:
    - an OpenMM trajectory (.dcd) with a corresponding topology file (.parm7)
and generates:
    - a GROMACS trajectory (.xtc) with corrected box vectors.
Requirements
------------
- mdtraj
- numpy

Author
------
Alaa Reguei

Date
----
2026-05
"""

import mdtraj as md
import numpy as np

traj = md.load("output.dcd", top="step5_input.parm7")

# correct box vectors
bv = traj.unitcell_vectors.copy()

bv[0]
bv[np.abs(bv) <= 1e-2] = 0.0

traj.unitcell_vectors = bv
traj.save_xtc("trj_gromacs.xtc")
