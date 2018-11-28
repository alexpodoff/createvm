"""The module contains the list of required paths.

packer - absolute path to Packer directory;
packer_templates - absolute path to Packer templates directory;
packer_export - relative (from template dir) path to exported VM;
vm_group - testing VM group;
upload - where to put exported VMs.
"""


from os.path import join


__author__ = 'pod'
__version__ = '1.4'


packer = "/home/pod/packer"
packer_templates = join(packer, "templates")
packer_export = "export"
vm_group = "smolensk_unstable"
vm_group_stable = "smolensk_stable"
upload = "/srv/ftp/vm"

