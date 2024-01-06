#!/usr/bin/env python
from __future__ import unicode_literals

import os
import numpy as np
import shutil
import tarfile



directories = {
     'lpfam_run' : 'tests/pynfam_example/000000/hfb_soln/hfb_meta',
     'file_to_untar' : 'hfb_meta_solns.tar',
     'logfile' : 'logfile.dat',
     '46_amplitude' : '46_amplitude', 
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
        if os.path.exists(os.path.join(firsttask_path,  directories['46_amplitude'])):
            raise Exception('46_amplitude exist, run lpfam_extract.py')

        os.remove(tarfile_path)
        os.remove(logfile_path)

lpfam_tasklist = os.listdir(hfb_meta_dir)
print(lpfam_tasklist)

for task in lpfam_tasklist:
    task_path = os.path.join(hfb_meta_dir, task)
    print(task_path)
    for bottom_file in os.listdir(task_path):
        bottom_file_path = os.path.join(task_path, bottom_file)
        os.remove(bottom_file_path)
        
print('Next step: run lpfam_generate.py')
