import struct

def inverse_sqrt_quake(x):
    """Fast inverse square root. Three Newton steps so it matches the reference cases."""
    x = float(x)
    xhalf = 0.5 * x
    i = struct.unpack(">i", struct.pack(">f", x))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack(">f", struct.pack(">i", i))[0]
    y = y * (1.5 - xhalf * y * y)
    y = y * (1.5 - xhalf * y * y)
    y = y * (1.5 - xhalf * y * y)
    return y
