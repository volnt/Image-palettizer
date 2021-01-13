from time import time

import numpy as np

# import functools
# from importlib import import_module


def load_rgb(palette, header_size=0, use_names=False):
    """
    GPL files look like that :

    GIMP Palette
    12 32 45 name1
    23 34 45 name2
    ...

    Lines that do not start with a number are comments
    They can also contain an alpha channel as a fourth column
    """
    palette_lines = palette.readlines()  # Read each line of the file.
    palette_list = []  # Initialize a list to hold the values later.
    if palette_lines[0] != "GIMP Palette\n":
        raise IOError("Not a GPL file.")
    for line in palette_lines[header_size:]:
        if line.strip()[0] in "1234567890":  # Ignore comments.
            color_val = line.split()[:3]
            palette_list.append(color_val)

    return np.array(palette_list).astype(np.uint8)


def rgb2hex(color):
    return "".join(format(channel, "x").rjust(2, "0") for channel in color)


def load_hex(*args, **kwargs):
    pal = load_rgb(*args, **kwargs)
    return np.array(["#" + rgb2hex(color) for color in pal])


def load_int(*args, **kwargs):
    pal = load_rgb(*args, **kwargs)
    return np.array([int(rgb2hex(color), 16) for color in pal])


def write_rgb(location, pal, header={"palette name": "", "description": ""}, color_names=[]):
    pal = pal.astype(np.uint8)
    lines = []
    if color_names == []:
        color_names = np.full(pal.shape[0], "")
    for triple, name in zip(pal, color_names):
        line = [str(val) + " " * (3 - len(str(val))) for val in triple]
        line.append(name)
        line = " ".join(line)
        lines.append(line)

    header_list = [
        "GIMP Palette",
        "#Palette name: " + header["palette name"],
        "#Description: " + header["description"],
        "#Colors: " + str(len(lines)),
    ]

    lines = header_list + lines

    with open(location + header["palette name"] + "_" + str(int(time())) + ".gpl", mode="w+") as f:
        f.write("\n".join(lines))
