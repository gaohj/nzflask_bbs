import pytesseract
import random
from PIL import Image
from urllib import request
import time



def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    url = "https://passport.lagou.com/vcode/create?from=register&refresh=%s" % (random.random())
    while True:
        request.urlretrieve(url,'code.png')
        image = Image.open('code.png')
        text = pytesseract.image_to_string(image,lang='eng')

        print(text)
        time.sleep(2)
if __name__ == "__main__":
    main()

