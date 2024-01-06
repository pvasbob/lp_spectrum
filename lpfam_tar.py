
import os
import shutil
import tarfile


step = 0.05
nr_points = 401

directories = {
     'lpfam_run' : 'tests/pynfam_example/000000/hfb_soln/hfb_meta',
     'tests' : 'tests',
     }

delete_files = [
     'amplitudes.dat',
     'hfbtho_output.hel',
     'thoout.dat'
    ]





parent_dir= os.getcwd() 
hfb_meta_dir = os.path.join(parent_dir, directories['lpfam_run'])


tasklist = list(range(0,nr_points))

for task in tasklist:
    task_path = os.path.join(hfb_meta_dir, '{0:04d}'.format(task))
    for delete in delete_files:
        delete_path = os.path.join(task_path, delete)
        if os.path.exists(delete_path) : os.remove(delete_path) 


os.system('tar -jcv -f tests.tar.bz2 ./tests')
os.system('rm -r ./tests')
