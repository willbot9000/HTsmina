import multiprocessing
import numpy
import rdkit
import argparse
import os
import subprocess


def target_process(receptor, ligand,exhaustiveness=8,autobox=True,add=None):

    target_string = f"smina -r {receptor} -l {ligand} {'--autobox_ligand ' + ligand if autobox else ''} {'--autobox_add '+ add if add else ''} "
    result = subprocess.run(target_string)


    return 0

def main(*args,**kwargs):


    return 0