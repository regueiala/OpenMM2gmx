#!/bin/bash

# a script to center the trajectory and remove jumps, using gmx trjconv
# usage: gromacs_nojump_centering.sh <TPR file> <TRAJ file>
# Consider to change the group selection if needed , 

TPR=$1
TRAJ="$2"

BASENAME="${TRAJ%.xtc}"

echo 0 | gmx trjconv \
    -s "$TPR" \
    -f "$TRAJ" \
    -o "${BASENAME}_nojump.xtc" \
    -pbc nojump

echo -e "21\n0" | gmx trjconv \
    -s "$TPR" \
    -f "${BASENAME}_nojump.xtc" \
    -o "${BASENAME}_nojump_centered.xtc" \
    -pbc mol \
    -center \
    -ur compact \
    -n index.ndx
