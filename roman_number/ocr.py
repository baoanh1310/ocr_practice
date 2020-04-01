"""Apply OCR for Image."""
from PIL import Image 
import pytesseract
import argparse
import cv2
import os

def main():
    """Test pytesseract package."""
    # construct the argument
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the image to be OCR")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", 
        help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    # load the image and convert it to grayscale  
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the image 
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove noise
    elif args["preprocess"] == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can apply OCR to it 
    file_name = "{}.png".format(os.getpid())
    cv2.imwrite(file_name, gray)

    # load the image as a PIL image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(file_name))
    os.remove(file_name)
    print(text)

    # show the output image 
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
