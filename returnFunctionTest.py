import math


def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume


volume_radius_10 = make_cylinder_volume_func(10)
print(volume_radius_10(5))
