import multiprocessing
import numpy
import rdkit
import argparse
import os
import subprocess

#prep takes input file and 
def target_process(receptor,ligand,exhaustiveness=8,autobox=True,add=None,output=None,scoring_path=None,custom_scoring=True):
    target_string = f"smina -r {receptor} -l {ligand} {'--autobox_ligand ' + ligand if autobox else ''} {'--autobox_add '+ add if add else ''} --exhaustiveness {exhaustiveness} {'--custom_scoring ' + scoring_path if custom_scoring else ''}"
    result = subprocess.run(target_string)


    return 0

def prep():

    pass

def dock_from_prep():

    pass

def dock():
    #takes in input file, makes temp file in memory from each smiles line. Output List of top candidates

    pass

def main(*args,**kwargs):
    if kwargs.get('prep'):
        prep()

    if kwargs.get('dock_from_prep'):
        dock_from_prep()

    if kwargs.get('dock'):
        dock()
        

    return 0



if __name__ == '__main__':
    
    p = argparse.ArgumentParser(prog='HTsmina.py',description='High Throughput Molecular Screening with smina')
    exclusive = p.add_mutually_exclusive_group(required=True)
    exclusive.add_argument('--prep',action="store_true",help="creates a directory and preps a file for each line in the input file. Requires a path to input file where each line is a smiles string")
    exclusive.add_argument('--dock_from_prep',action="store_true",help="performs docking on a previously prepped group of files. Requires a path to the directory containing the files")
    exclusive.add_argument('--dock', action="store_true",help='runs docking without saving any prepped files. Requires path to input file where each line is a SMILES format')
    p.add_argument('path_to_input_file')
    p.add_argument('-n','--num_results',action="store",help='sets the maximum number of top results to display. Default is 10.')
    p.add_argument('-o','--output',action="store",help="path to outut csv file")