"""File systems test module helpers."""


import os.path
import shlex
from subprocess import Popen, PIPE


__author__ = 'vgol'
__version__ = '0.1.0'


def mount_img(image):
    """Mount img to /mnt. Return tuple of bytes."""
    mount_image = "mount -o loop {img} /mnt".format(img=image)
    mnt = Popen(shlex.split(mount_image), stdout=PIPE, stderr=PIPE)
    output = mnt.communicate()
    return output


def get_label(file):
    """Get MAC label from file. Return str."""
    cmd = "pdp-ls -Mn {}".format(file)
    get_lbl = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    output = get_lbl.communicate()
    return output[0].decode()


def get_aud(file):
    """Get audit flags from file. Return str."""
    cmd = "getfaud {}".format(file)
    getaud = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    output = getaud.communicate()
    return output[0].decode()


def fs_from_image(img):
    """Get fs name from image path. Return str."""
    return os.path.split(img)[1][len('image-'):]
