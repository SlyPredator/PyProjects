# Python code to convert an image to ASCII image.
import argparse
import math
import random
import sys

import numpy as np
from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = "@%#*+=-:. "


def getAverageL(image):

    """
    Given PIL Image, return average value of grayscale value
    """
    # Get image as numpy array
    im = np.array(image)

    # Get shape
    w, h = im.shape

    # Get average
    return np.average(im.reshape(w * h))


def covertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images
    """
    # Declare globals
    global gscale1, gscale2

    # Open image and convert to grayscale
    image = Image.open(fileName).convert("L")

    # Store dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))

    # Compute width of tile
    w = W / cols

    # Compute tile height based on aspect ratio and scale
    h = w / scale

    # Compute number of rows
    rows = int(H / h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # Check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # Ascii image is a list of character strings
    aimg = []
    # Generate list of dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)

        # Correct last tile
        if j == rows - 1:
            y2 = H

        # Append an empty string
        aimg.append("")

        for i in range(cols):

            # Crop image to tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)

            # Correct last tile
            if i == cols - 1:
                x2 = W

            # Crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # Get average luminance
            avg = int(getAverageL(img))

            # Look up ascii char
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]

            # Append ascii char to string
            aimg[j] += gsval

    # Return txt image
    return aimg


def main():
    # Create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # Add expected arguments
    parser.add_argument("--file", dest="imgFile", required=False)
    parser.add_argument("--scale", dest="scale", required=False)
    parser.add_argument("--out", dest="outFile", required=False)
    parser.add_argument("--cols", dest="cols", required=False)
    parser.add_argument("--morelevels", dest="moreLevels", action="store_true")

    # Parse args
    args = parser.parse_args()

    # Set input file
    imgFile = "img.png"
    if args.imgFile:
        imgFile = args.imgFile

    # Set output file
    outFile = "out.txt"
    if args.outFile:
        outFile = args.outFile

    # Set scale default as 0.43 which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)

    # Set cols
    cols = 120
    if args.cols:
        cols = int(args.cols)

    print("generating ASCII art...")
    # Convert image to ascii txt
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)

    # Open file
    f = open(outFile, "w")

    # Write to file
    for row in aimg:
        f.write(row + "\n")

    f.close()
    print("ASCII art written to %s" % outFile)


# call main
if __name__ == "__main__":
    main()


# Example CLI run --> "py main.py --file images.jpeg --cols 120"
