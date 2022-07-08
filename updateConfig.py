import time
import os
from git import Repo

repo = Repo(os.getcwd())
writeRepoChanges = False

with open('./src/config/constants.js', 'r') as f:
    lines = f.readlines()

with open('./src/config/constants.js', 'w') as f:
    for line in lines:
        if line.startswith('//git version Rajesh:'):
            line = "//git version Rajesh: Last changes made on " + time.strftime('%d, %b %Y - %I:%M %p') + "\n"
        if line.startswith(' * ') and not writeRepoChanges:
            line = "\n".join([ f" * ---> {item.a_path}" for item in repo.index.diff(None) ]) + "\n*/\n"
            writeRepoChanges = True
            f.write(line)
            continue
        if line.startswith(' * ') and writeRepoChanges:
            continue
        if line.startswith('*/') and writeRepoChanges:
            continue
        f.write(line)
