from selenium import webdriver
import cv2
import base64
import numpy as np
import time

URL="chrome://dino"

class Dino:
    def __init__(self):
        self.d = webdriver.Chrome()
        try:
            self.d.get("chrome://dino")
        except Exception as e:
            pass
        time.sleep(5)
        self.d.set_window_size(640, 480)
        self.d.set_window_position(0, 0)
    
    def __del__(self):
        self.d.quit()

    def fetch_one(self):
        b64_str = self.d.get_screenshot_as_base64()
        img_origin = base64.b64decode(b64_str)
        xdata=np.asarray(bytearray(img_origin), dtype=np.uint8)
        image = cv2.imdecode(xdata, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

if __name__ == "__main__":
    dino = Dino()

    begin = time.time()
    dino.fetch_one()
    end = time.time()
    print(f"timecost {end - begin}")
