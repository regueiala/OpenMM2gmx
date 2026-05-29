#! /usr/bin/env python
import parmed as pmd
openmm_top = pmd.load_file('step5_input.parm7', xyz='pthrp_only_explicit_prod_final.xml')
print(openmm_top.box)
openmm_top.save('pthrp.gro', format='gro')
openmm_top.save('pthrp.top', format='gromacs')
