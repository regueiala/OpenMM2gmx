#!/usr/bin/env python3
"""
Convert an OpenMM system to GROMACS format.

This script loads:
    - a topology file (eg an amber topology .parm7 file)
    - OpenMM coordinates/system information (last XML file from the production run)

and generates:
    - a GROMACS structure file (.gro)
    - a GROMACS topology file (.top)

Requirements
------------
- ParmEd

Notes
-----
OpenMM and GROMACS may handle box vectors differently,
especially for triclinic boxes or near-zero floating-point values.
That should be taken into account next when converting systems between the two formats.

Author
------
Alaa Reguei

Date
----
2026-05
"""

import parmed as pmd

PARM7_FILE = "step5_input.parm7"
XML_FILE = "pthrp_only_explicit_prod_final.xml"

# Output files
GRO_OUTPUT = "pthrp.gro"
TOP_OUTPUT = "pthrp.top"


print("Loading OpenMM topology and coordinates...")

system = pmd.load_file(PARM7_FILE, xyz=XML_FILE)

print("\nDetected box vectors:")
print(system.box)

print("\nWriting GROMACS files...")

system.save(GRO_OUTPUT, format="gro")
system.save(TOP_OUTPUT, format="gromacs")

print("\nConversion completed successfully.")
