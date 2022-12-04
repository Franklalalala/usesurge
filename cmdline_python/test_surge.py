import os
import subprocess


surge_path = r'..\bin\surge.exe'
surge_path = os.path.abspath(surge_path)
cmdline_list = [surge_path, '-S', '-Y', '-B1,2,3,4,5,6,7,8,9', 'C3O', '-otest.smi']
out = subprocess.run(cmdline_list, shell=True, capture_output=True)
print(out.returncode)
print(out.stderr)
with open('info', 'wb') as f:
    f.write(out.stderr)
