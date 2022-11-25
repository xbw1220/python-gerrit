from openpyxl import Workbook
import numpy as np

wb = Workbook()

ws = wb.create_sheet("che")
label = [[0],
         [1],
         [2],
         [3]
         ]
feature = [
    [0.1, 0.2, 0.3, 0.4, 0.5],
    [0.11, 0.21, 0.31, 0.41, 0.51],
    [0.6, 0.7, 0.8, 0.9, 1.00],
    [1.1, 1.2, 1.3, 1.4, 1.5],
]
# 这个地方之所以 变成numpy格式是因为在很多时候我们都是在numpy格式下计算的，模拟一下预处理
label = np.array(label)
feature = np.array(feature)

label_input = []
for l in range(len(label)):
    label_input.append(label[l][0])
ws.append(label_input)
for f in range(len(feature[0])):
    ws.append(feature[:, f].tolist())
wb.save("chehongshu.xlsx")
wb.close()