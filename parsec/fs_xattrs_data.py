"""Data for file systems tests."""


__author__ = 'vgol'
__version__ = '0.1.0'


fs_types = [
    'ext2',
    'ext3',
    'ext4',
    'vfat',
    'ntfs',
    'minix',
    'exfat'
]
# FS from this list expected to fail test_mac.
mac_xfail = [
    'vfat',
    'ntfs',
    'minix',
    'exfat'
]
# FS from this list expected to fail test_audit.
audit_xfail = [
    'vfat',
    'minix',
    'exfat'
]
tfile = '/mnt/testfile'

# System configuration pseudo FS list.
pseudo_fs_sysconf = [
    'sysfs',
    'proc',
    'cpuset',
    'cgroup',
    'degugfs',
    'tracefs',
    'securityfs',
    'pstore',
    'parsecfs',
    'rpc-pipefs'
]

# Pseudo FS with write access.
pseudo_fs_writable = [
    'tmpfs',
    'devtmpfs',
    'ramfs',
    'hugetlbfs',
    'mqueue',
    'fusectl'
]
