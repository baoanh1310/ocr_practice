import pytesseract
from PIL import Image

class OCR(object):
    def ocr_from_image(self, imgPath, lang = 'vie'):
        return pytesseract.image_to_string(Image.open(imgPath), lang=lang)
