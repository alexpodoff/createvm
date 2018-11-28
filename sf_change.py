#/usr/bin/python3

import os
import subprocess


"""Changes default path for shared folders to my path"""
home = os.environ['HOME']
folders = {
        'git': os.path.join(home, 'hard_2/git'),
        'svn': os.path.join(home, 'hard_2/svn')
    }

names = ['sudcm', 'suac', 'susrv', 'suodcm', 'suoac', 'sudcs', 'sufs', 'fiac', 'fidcm', 'fidcr1', 'fidcr2', 'fisrv']
for name in names:
    for key in folders.keys():
        subprocess.call(['VBoxManage', 'sharedfolder', 'remove',
                         name, '--name', key])
        subprocess.call(['VBoxManage', 'sharedfolder', 'add',
                         name, '--name', key, '--hostpath',
                         folders[key], '--automount'])

