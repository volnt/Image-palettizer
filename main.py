# Dependencies
import argparse
import pathlib

import numpy as np
from PIL import Image

import loadgpl
import palettizer
from constants import EXT_LIST
from imageio import imread, imwrite


def do_palettize(palette, image, *args, **kwargs):

    # For if image is grayscale
    if len(image.shape) == 2:
        image = image[..., np.newaxis].repeat(3, axis=2)

    # For if alpha data is included
    image = image[..., :3]

    return palettizer.palettize(palette, image, *args, **kwargs)


def save_image(image, name, palette_len=None):
    temp_img = Image.fromarray(image)
    w, h = temp_img.size

    if "." in name:
        ext = name.split(".")[-1].casefold()
    else:
        ext = None

    if ext in EXT_LIST:
        try:
            imwrite(name, image, quantize=palette_len)  # only works for PNGs right now
        except:
            imwrite(name, image)
    else:
        try:
            imwrite(name + ".png", image, quantize=palette_len)
        except:
            imwrite(name + ".png", image)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("palette", type=open)
    parser.add_argument("image", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()

    # lospec.palette_retriever()
    palette = loadgpl.load_rgb(args.palette)
    image = imread(args.image)

    output_image = do_palettize(palette, image)
    save_image(output_image, str(args.output), len(palette))
