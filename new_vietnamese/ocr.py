import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

class OCR(object):
    def ocr_from_image(self, imgPath, lang = 'vie'):
        return pytesseract.image_to_string(Image.open(imgPath), lang=lang)
