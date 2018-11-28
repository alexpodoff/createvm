"""File systems tests fixtures."""


import pytest
import os
import re
import shlex
from subprocess import call
from parsec import fs_xattrs_data


__author__ = 'vgol'
__version__ = '0.1.0'


def _create_img_default(fs, img):
    """Default function for preparing image.

    It works for ext2, ext3, ext4, ntfs.
    """
    mkfs = "/sbin/mkfs.{0} -F {1}".format(fs, img)
    call(shlex.split(mkfs))
    mount = "mount -o loop {img} /mnt".format(img=img)
    call(shlex.split(mount))


def _create_img_simple(fs, img):
    """Create image and make FS without '-F' flag.

    It works for exFAT, FAT32, minix.
    """
    mkfs = "/sbin/mkfs.{0} {1}".format(fs, img)
    call(shlex.split(mkfs))
    mount = "mount -o loop {img} /mnt".format(img=img)
    call(shlex.split(mount))


@pytest.fixture(
    scope='function',
    params=fs_xattrs_data.fs_types
)
def preparefs(request):
    """Create image with FS. Return path as str."""
    image = os.path.join('/tmp', 'image-' + request.param)
    img_size = 2000000
    with open(image, 'wb') as img, open('/dev/zero', 'rb') as zero:
        img.write(zero.read(img_size))
    if re.match('(ext[2-4]|ntfs)', request.param):
        _create_img_default(request.param, image)
    else:
        _create_img_simple(request.param, image)

    def cleaning():
        call(['umount', image])
        os.remove(image)

    request.addfinalizer(cleaning)
    return image


@pytest.fixture(scope='function')
def set_mount_point_label(request):
    """Set label to mount point. And return as was"""
    call(shlex.split("pdpl-file 1:0:0:ccnr /mnt"))

    def lbl_back():
        call(shlex.split("pdpl-file 0:0:0:0 /mnt"))

    request.addfinalizer(lbl_back)
