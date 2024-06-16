#!/usr/bin/python
# -*- coding:utf-8 -*-
from waveshare_epd import epd7in5_V2
import sys
import os
from PIL import Image

libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)


def display_image_on_eink(image_path):
    try:
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()

        # Load the image file
        image = Image.open(image_path)
        # Resize the image to the display resolution if necessary
        if image.size != (epd7in5_V2.EPD_WIDTH, epd7in5_V2.EPD_HEIGHT):
            image = image.resize(
                (epd7in5_V2.EPD_WIDTH, epd7in5_V2.EPD_HEIGHT), Image.BILINEAR)

        # Display the image
        epd.display(epd.getbuffer(image))
        print("Image has been displayed.")

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        print("Program exited.")
        epd7in5_V2.epdconfig.module_exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <image_path>".format(sys.argv[0]))
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print("Error: The file '{}' does not exist.".format(image_path))
        sys.exit(1)

    display_image_on_eink(image_path)
