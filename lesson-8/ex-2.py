import os
files = ['--settings', '--mainapp', '--authapp']
files1 = ['/--views.py', '/--models.py', '/--__init__.py']
files2 = ['/index.html', '/base.html']
files3 = ['--prod.py', '--dev.py', '--__init__.py']
if not os.path.exists('--my_project'):
   for f in files:
      os.makedirs(f'--my_project/{f}/')
   for f1 in files[1:]:
      for fi in files1:
         filename = f'--my_project/{f1}/{fi}'
         with open(filename, "w") as f:
            f.write("<?php include('generator.php'); ?>")
   for f3 in files3:
      filename = f'--my_project/--settings/{f3}'
      with open(filename, "w") as f:
         f.write("<?php include('generator.php'); ?>")

   os.makedirs(f'--my_project/--mainapp/--templates/--mainapp')
   os.makedirs(f'--my_project/--authapp/--templates/--authapp')
   for f2 in files2:
      filename = f'--my_project/--mainapp/--templates/--mainapp/{f2}'
      with open(filename, "w") as f:
         f.write("<?php include('generator.php'); ?>")

      filename = f'--my_project/--authapp/--templates/--authapp/{f2}'
      with open(filename, "w") as f:
         f.write("<?php include('generator.php'); ?>")


