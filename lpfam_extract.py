#!/usr/bin/env python
#from __future__ import unicode_literals

import os
import numpy as np
import shutil
import tarfile


step = 0.10
nr_points = 200

directories = {
     'lpfam_run' : 'tests/pynfam_example/000000/hfb_soln/hfb_meta',
     'file_to_untar' : 'hfb_meta_solns.tar',
     'logfile' : 'logfile.dat',
     '46_amplitude' : '46_amplitude', 
     '46_amplitude_gather_isosca' : '46_amplitude_gather_0', 
     '46_amplitude_gather_isovec' : '46_amplitude_gather_1', 
     }


parent_dir= os.getcwd() 
print(parent_dir)

hfb_meta_dir = os.path.join(parent_dir, directories['lpfam_run'])
print(hfb_meta_dir)

hfb_meta_dir_exists = os.path.exists(hfb_meta_dir)
print('hfb_meta_dir_exists', hfb_meta_dir_exists)

tarfile_path = os.path.join(hfb_meta_dir, directories['file_to_untar'])
logfile_path = os.path.join(hfb_meta_dir, directories['logfile'])
print(tarfile_path)

tarfile_exists = os.path.exists(tarfile_path)
print('tarfile_exists', tarfile_exists)


if tarfile_exists:
    with tarfile.open(tarfile_path) as file:
        file.extractall(hfb_meta_dir)
        firsttask_path = os.path.join(hfb_meta_dir, '0000')
        if not os.path.exists(os.path.join(firsttask_path,  directories['46_amplitude'])):
            raise Exception('46_amplitude NOT exist, stat from sbatch slurm_dogwood.sh')

        os.remove(tarfile_path)
        os.remove(logfile_path)

lpfam_tasklist = os.listdir(hfb_meta_dir)
print(lpfam_tasklist)

gather_all_omega = {}

for task in lpfam_tasklist:
    omega = int(task)*step
    task_path = os.path.join(hfb_meta_dir, task)
    amplitude_path = os.path.join(task_path, directories['46_amplitude'])
    with open(amplitude_path, 'r') as file:
        gather_all_omega[task] = (file.readlines())[0]

for keys in gather_all_omega:
   #print(gather_all_omega[keys])
    print(keys)

 
enumerate_tasklist = list(range(0,2*nr_points))
    

if os.path.exists(os.path.join(parent_dir, directories['46_amplitude_gather_isosca'])): 
    os.remove(os.path.join(parent_dir, directories['46_amplitude_gather_isosca']))
    os.remove(os.path.join(parent_dir, directories['46_amplitude_gather_isovec']))

file_isosca = open(directories['46_amplitude_gather_isosca'], 'a') 
file_isovec = open(directories['46_amplitude_gather_isovec'], 'a')

for i in enumerate_tasklist:
    if i < nr_points:
        file_isosca.write(gather_all_omega['{0:04d}'.format(i)])
    else:
        file_isovec.write(gather_all_omega['{0:04d}'.format(i)])

