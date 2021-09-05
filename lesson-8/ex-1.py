import os
files = ['--mainapp', '--adminapp', '--authapp', '--settings']
if not os.path.exists('--my_project'):
   for f in files:
      os.makedirs(f'--my_project/{f}')