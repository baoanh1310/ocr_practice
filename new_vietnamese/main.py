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
    result = Converter(str=str).convert()

    end = time.time()

    print(result)
    print('Time: {}s'.format(end-start))
