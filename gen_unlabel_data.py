from dino import Dino
import numpy as np
import cv2
import time

def save(dirname, cnt=1, interval=0.5):
    last = None
    dino = Dino()
    begin = time.time()
    max=int(cnt)
    for i in range(max):
        gray = dino.fetch_one()
        if last is None or np.sum(last-gray) != 0:
            last = gray
        else:
            continue

        suc = cv2.imwrite(f"{dirname}/{i}.jpg", gray)
        print("save {}".format(suc))
        time.sleep(interval)

    end = time.time()
    print(f"timecost {end - begin}")

if __name__ == "__main__":
    save("./unlabel_data", 1000)
