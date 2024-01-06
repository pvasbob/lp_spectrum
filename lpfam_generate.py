from __future__ import unicode_literals

import os
import numpy as np
import shutil
import tarfile


step = 0.10
nr_points = 200

directories = {
     'lpfam_run' : 'tests/pynfam_example/000000/hfb_soln/hfb_meta',
     'file_to_untar' : 'hfb_meta_solns.tar',
     'lpfam_input': 'lpfam_input',
     'qrpa_inp' : 'qrpa.inp',
     }

qrpa_lines = {
      'header' : '================qrpa.inp=============',
      'calc, mode, file io' : [1, 0],
      'O,T,L,K'  : [1, 1, 2, 0],
      'qrpa_eps' : 0.1,
      'max_iter_qrpa' : 100,
      'qrpa_nbroyden' : 40,
      'qrpa_alphamix' : 0.33,
      'line parameters' : [0.0, 0.5, 0.25, 0.0],
      'circle parameters' : [2.22, 0.0, 0.11],
      'half-circle parameters' : [0.0, 200.0],      
      'qrpa_points' : 1, 
     }

a = str(qrpa_lines['calc, mode, file io'])[1:-1]

parent_dir= os.getcwd() 

hfb_meta_dir = os.path.join(parent_dir, directories['lpfam_run'])

hfb_meta_dir_exists = os.path.exists(hfb_meta_dir)

tarfile_path = os.path.join(hfb_meta_dir, directories['file_to_untar'])

tarfile_exists = os.path.exists(tarfile_path)

lpfam_tasklist = os.listdir(hfb_meta_dir)

lpfam_input_path = os.path.join(parent_dir, directories['lpfam_input']) 

qrpa_inp_path = os.path.join(lpfam_input_path, directories['qrpa_inp'])
qrpa_inp_exists = os.path.exists(qrpa_inp_path)
print(qrpa_inp_exists)
if not qrpa_inp_exists:
    raise Exception('No qrpa.inp to generate from')


for task in lpfam_tasklist:
    omega_pos = int(task) 
    # isoscalar assignment from 0 to nr_points -1
    if omega_pos < nr_points:
        isosca_vec = 0
        omega = omega_pos*step
    # isovector assignment from nr_points to 2*nr_points -1
    else:
        isosca_vec = 1
        # omega - nr_points so that omega start from 0.0 for isovector.
        omega = (omega_pos - nr_points)*step

    # make change to qrpa_lines according to above.  
    qrpa_lines['O,T,L,K'][1] = isosca_vec
    qrpa_lines['line parameters'][0] = omega

    task_path=  os.path.join(hfb_meta_dir, task)
    task_qrpa_inp_path = os.path.join(task_path, directories["qrpa_inp"]) 
    if os.path.exists(task_qrpa_inp_path): os.remove(task_qrpa_inp_path)
    with open(task_qrpa_inp_path, "a") as file:
        file.write(qrpa_lines['header'] + '\n') 
        file.write(str(qrpa_lines['calc, mode, file io'])[1:-1] + '\n')
        file.write(str(qrpa_lines['O,T,L,K'])[1:-1] + '\n')
        file.write(str(qrpa_lines['qrpa_eps']) + '\n')
        file.write(str(qrpa_lines['max_iter_qrpa']) + '\n')
        file.write(str(qrpa_lines['qrpa_nbroyden']) + '\n')
        file.write(str(qrpa_lines['qrpa_alphamix']) + '\n')
        file.write(str(qrpa_lines['line parameters'])[1:-1] + '\n')
        file.write(str(qrpa_lines['circle parameters'])[1:-1] + '\n')
        file.write(str(qrpa_lines['half-circle parameters'])[1:-1] + '\n')
        file.write(str(qrpa_lines['qrpa_points']) + '\n')
        
    
      
        

