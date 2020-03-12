# USAGE
# python main.py --image test.png

import argparse
import time

from converter import *
from ocr import *

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="Path to the image for OCR")
args = vars(ap.parse_args())

if __name__ == "__main__":

    imgPath = args["image"]
    model = OCR()

    start = time.time()

    str = model.ocr_from_image(imgPath=imgPath)

    end = time.time()

    print(str)
    print('Time: {}'.format(end-start))
