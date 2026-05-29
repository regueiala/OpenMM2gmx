#!/bin/bash

# Input trajectory (XTC)
TRAJ="$1"

# Output directory
mkdir -p ../centered_stripped_trajs

BASENAME="${TRAJ%.xtc}"

cpptraj ../step5_input.parm7 << EOF
trajin $TRAJ 1 last 10

# Remove solvent and ions
strip :WAT,Cl-,Na+,PA,PC,OL outprefix stripped

# Write output trajectory (XTC is supported via conversion workflow)
trajout ../centered_stripped_trajs/${BASENAME}_stripped.xtc
run
EOF
