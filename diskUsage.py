## 수정 해야함
import os
import collections


def getDiskSpace():
    _ntuple_diskusage = collections.namedtuple('usage', 'total used free')

    if hasattr(os, 'statvfs'):  # POSIX
        def diskUsage(path):
            st = os.statvfs(path)
            free = st.f_bavail * st.f_frsize
            total = st.f_blocks * st.f_frsize
            used = (st.f_blocks - st.f_bfree) * st.f_frsize
            return _ntuple_diskusage(total, used, free)

    elif os.name == 'nt':  # Windows
        import ctypes
        import sys

        def diskUsage(path):
            _, total, free = ctypes.c_ulonglong(), ctypes.c_ulonglong(), \
                             ctypes.c_ulonglong()
            if sys.version_info >= (3,) or isinstance(path, unicode):
                fun = ctypes.windll.kernel32.GetDiskFreeSpaceExW
            else:
                fun = ctypes.windll.kernel32.GetDiskFreeSpaceExA
            ret = fun(path, ctypes.byref(_), ctypes.byref(total),
                      ctypes.byref(free))
            if ret == 0:
                raise ctypes.WinError()
            used = total.value - free.value
            return _ntuple_diskusage(total.value, used, free.value)
    else:
        raise NotImplementedError("platform not supported")

    diskUsage.__doc__ = __doc__

    # drives = ['C:', 'D:', 'E:', 'F:']
    drives = ['C:', 'D:', 'Z:']

    disk_array = []

    for drive in drives:
        disk_usage = diskUsage(drive + '\\')
        disk_array.append({'used': disk_usage.used, 'free': disk_usage.free,
                           'drive': drive, 'total': disk_usage.total})

    return disk_array


if __name__ == '__main__':
    print(getDiskSpace())
