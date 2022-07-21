# 復習問題1
import numpy as np
# 試験結果
suugaku = np.array([
    62, 79, 0, 44, 62, 31, 65, 14, 1, 54, 25, 55, 16, 67, 6, 94, 37, 41, 90, 47, 8, 27, 1, 24, 99, 28, 31,
    62, 61, 89, 18, 35, 77, 57, 18, 54, 34, 38, 12, 18, 66, 90, 19, 80, 42
])

kokugo = np.array([
    50, 100, 49, 56, 76, 56, 51, 15, 27, 28, 17, 48, 43, 29, 49, 66, 24, 37, 57, 41, 65,
    15, 0, 32, 90, 65, 39, 92, 39, 60, 10, 75, 69, 69, 44, 21, 27, 30, 4, 50, 87, 93, 19, 63, 14
])

eigo = np.array([
    56, 72, 15, 71, 44, 46, 87, 35, 21, 62, 51, 62, 45, 85, 32, 100, 24, 14, 92, 77, 17, 37, 22, 23,
    91, 53, 34, 63, 30, 64, 42, 14, 63, 70, 22, 76, 15, 67, 17, 0, 89, 87, 52, 86, 55
])

# 合計点
total = kokugo + suugaku + eigo

# 平均点，標準偏差
mean = np.mean(total)
sgm = np.std(total)
# 偏差値
hensa = (total - mean) / sgm * 10 + 50

# 結果を表形式で表示する
print("数学，国語，英語, 合計, 偏差値")
for i in range(len(total)):
    print("{:3},{:3},{:3},{:3},{:.2f}".format(suugaku[i], kokugo[i],eigo[i],total[i],hensa[i]))
# 度数分布計算
dosuu,kaikyu = np.histogram(total, bins =10 , range = (0,300))
print("度数分布{}\n階級:{}".format(dosuu,kaikyu))
# 相関行列