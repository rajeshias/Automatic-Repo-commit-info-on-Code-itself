import time
import os
from git import Repo

repo = Repo(os.getcwd(), search_parent_directories=True)
writeRepoChanges = False

with open('./README.md', 'r') as f:
    lines = f.readlines()

with open('./README.md', 'w') as f:
    for line in lines:
        if line.startswith('//git Rajesh:'): ### <--------------------------- here
            line = "//git Rajesh: Last changes made on " + \
                time.strftime('%d, %b %Y - %I:%M %p') + "\n"
        if line.startswith(' * ') and not writeRepoChanges:
            line = "\n".join(
                [f" * ---> {item.a_path}" for item in repo.index.diff(None)]) + "\n*/\n"
            writeRepoChanges = True
            f.write(line)
            continue
        if line.startswith(' * ') and writeRepoChanges:
            continue
        if line.startswith('*/') and writeRepoChanges:
            continue
        f.write(line)


# template

# //git Rajesh: 

# /** Rajesh made changes on the following last time:
#  * 
# */
