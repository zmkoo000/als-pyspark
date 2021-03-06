import ctypes
def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shitf(n, i):

    if n < 0:
        n = ctypes.c_uint32(n).value

    if i < 0:
        return -int_overflow(n << abs(i))

    return int_overflow(n >> i)