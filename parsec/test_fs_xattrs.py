import pytest
import shlex
import os
from subprocess import call
from parsec import fs_xattrs, fs_xattrs_data
# noinspection PyUnresolvedReferences
from .fs_xattrs_fixtures import set_mount_point_label, preparefs


__author__ = 'vgol'
__version__ = '0.3.0'


tfile = fs_xattrs_data.tfile


def test_read_write(preparefs):
    """Try to read and write into image."""
    # Try to write.
    with open(tfile, 'wb') as tf:
        tf.write(b'this is test')
    assert os.path.exists(tfile)
    # Try to read.
    with open(tfile, 'rb') as tf:
        data = tf.read()
    assert data == b'this is test'


def test_mac(preparefs, set_mount_point_label):
    """Check MAC attributes."""
    # Mark as expected fail for no xattr fs.
    if fs_xattrs.fs_from_image(preparefs) in fs_xattrs_data.mac_xfail:
        pytest.xfail('xattrs not supported')
    with open(tfile, 'wb') as tf:
        tf.write(b'this is secret')
    assert os.path.exists(tfile)
    call(shlex.split("pdpl-file 1:0:0:0 {}".format(tfile)))
    lbl = fs_xattrs.get_label(tfile)
    assert '1:0:0x0:0x0' in lbl
    call('sync')
    call(['umount', '/mnt'])
    mount_result = fs_xattrs.mount_img(preparefs)
    assert not mount_result[1], mount_result[1].decode()
    lbl = fs_xattrs.get_label(tfile)
    assert '1:0:0x0:0x0' in lbl
    os.remove(tfile)


def test_audit(preparefs):
    """Check audit flags."""
    # Mark as expected fail for no xattr fs.
    if fs_xattrs.fs_from_image(preparefs) in fs_xattrs_data.audit_xfail:
        pytest.xfail('xattrs not supported')
    with open(tfile, 'wb') as tf:
        tf.write(b'this is for test')
    assert os.path.exists(tfile)
    call(shlex.split("setfaud -m o:o {}".format(tfile)))
    lbl = fs_xattrs.get_aud(tfile)
    assert 'o:o:o' in lbl
    call('sync')
    call(['umount', '/mnt'])
    mount_result = fs_xattrs.mount_img(preparefs)
    assert not mount_result[1], mount_result[1].decode()
    lbl = fs_xattrs.get_aud(tfile)
    assert 'o:o:o' in lbl
