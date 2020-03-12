## Guide to run this mini-project

```console
$ git clone https://github.com/baoanh1310/ocr_practice.git
$ cd ocr_practice/new_vietnamese
$ pip install -r requirements.txt
$ sudo apt-get install tesseract-ocr
$ python main.py --image test.png
```

## Notes:

- You need to install vietnamese language for tesseract
- If you don't have, follow below instructions:
  - After you install tesseract-ocr, go to https://github.com/tesseract-ocr/tessdata/blob/master/vie.traineddata
  - Install vietnamese data
  - Move this file to your tessdata folder in your machine
