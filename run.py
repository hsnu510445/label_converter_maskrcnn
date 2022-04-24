
import numpy
import cv2
import matplotlib.pyplot as plt
import numpy as np


PATH_OLD_LABEL = "origin/label_names.txt"
PATH_OLD_MASK = "origin/label.png"
PATH_NEW_LABEL = "new/label_names.txt"
PATH_NEW_MASK = "new/label_new.png"

# 讀原始標籤檔
f = open(PATH_OLD_LABEL, "r")
old_label = []
for line in f.readlines():
    old_label.append(line[:-1])  # 拿掉換行符
f.close()

# 讀轉換標籤檔
f = open(PATH_NEW_LABEL, "r")
new_label = []
for line in f.readlines():
    new_label.append(line[:-1])  # 拿掉換行符
f.close()


# 讀原始遮罩檔
old_mask = cv2.imread(PATH_OLD_MASK)

# 如果是7個label以內
# 複製圖片
new_mask = old_mask.copy()
# 跑迴圈修改新圖片
for x in range(old_mask.shape[1]):
    for y in range(old_mask.shape[0]):
        if sum(old_mask[y][x]==([0, 0, 0]))==3:
            # 該點為[0 0 0]
            pass
        else:
            point=old_mask[y][x].astype("bool").astype("uint8")
            old_label_num=point[0]*4+point[1]*2+point[2]
            new_label_num=new_label.index(old_label[old_label_num])
            new_mask[y][x]=np.array([new_label_num/4, new_label_num%4/2, new_label_num%2], dtype="uint8")*128
            
# 存出圖片
cv2.imwrite(PATH_NEW_MASK,new_mask)

