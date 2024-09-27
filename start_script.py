import os
import subprocess

subprocess.run(['python', os.path.join(os.getcwd(),'main.py'), 'ls', 'cd mydir', 'ls','cat file4.txt','wc file4.txt','cd','ls','exit'])
