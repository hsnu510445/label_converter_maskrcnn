import numpy
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


INPUT_DIR = "origin_mask"
OUTPUT_DIR = "label_output"

files = os.listdir(INPUT_DIR)  # 得到資料夾下的所有檔名稱

for file in files:  # 遍歷資料夾
    if not os.path.isdir(file):  # 判斷是否是資料夾，不是資料夾才開啟

        # 讀原始遮罩檔
        old_mask = cv2.imread(INPUT_DIR+"/"+file)
        # img = cv2.imread(imgname,-1) ->讀二值圖的話

        # 如果是7個label以內
        # 複製圖片
        new_mask = np . ones((old_mask.shape[0], old_mask.shape[1]),  dtype="uint8")
        # 跑迴圈修改新圖片
        for x in range(old_mask.shape[1]):
            for y in range(old_mask.shape[0]):
                if sum(old_mask[y][x] == ([0, 0, 0])) == 3:
                    # 該點為[0 0 0]
                    new_mask[y][x] = 0
                    pass
                else:
                    point = old_mask[y][x].astype("bool").astype("uint8")
                    label_num = point[0]*4+point[1]*2+point[2]
                    new_mask[y][x] = label_num

        # 存出圖片
        cv2.imwrite(OUTPUT_DIR+"/label_"+file, new_mask)
