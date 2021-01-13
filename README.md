# Cli Palettizer

A program that applies a .gpl palette to an image by finding the nearest color in the palette for each pixel using the CIECAM02-UCS color space by default (others are available as well). This provides more accurate-to-eye results than can be achieved with a run-of-the-mill graphics editor.

## Why a fork ?

This is a fork from https://github.com/PureAsbestos/Image-palettizer.

The parent repository focuses on providing a portable GUI. This fork is a barebone cli implementation tested on Linux exclusively with a lot less features (no dithering or lospec integration yet).

The goal is to be able to automate the palettization of many resources without having to manually select each of them by hand.

I chose not to contribute to the parent repository because the business logic was too tightly coupled with the GUI framework, making it hard to add a cli implementation.

## Requirements

Requires Python 3.6+ and the following packages to run from source:
- numpy
- colorspacious
- imageio
- psutil
- requests
- multiprocess

## Installation

1. `git clone https://github.com/volnt/Image-palettizer.git`.
2. `pip3 install -r requirements.txt`
3. `python3 main.py <palette.gpl> <source.png> <dest.png>` to apply `palette.gpl` on `source.png` and save it as `dest.png`

## Usage

To begin, you’ll need two things: a palette in .gpl format, and an image (png, jpeg, etc.)

You can then apply the palette on the image using `python3 main.py <palette.gpl> <source.png> <dest.png>`.

## Features

Besides the core feature that has been discussed, this program offers:

- [x] Partial parallelism for faster run time on multi-core systems
- [ ] The ability to dither with 9 common error-diffusion methods
- [ ] The ability to dither with 4 sizes of Bayer matrix (2x2, 3x3, 4x4, 8x8)
- [ ] Integration with [Lospec](https://lospec.com/palette-list) for easy retrieval and use of color palettes
- [ ] The ability to work with large images (note that *extremely* wide images may take up too much RAM)

## To-do
- [ ] Add command line arguments for dithering
- [ ] Add command line argument to load palette from lospec
