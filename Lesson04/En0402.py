import pandas as pd
from mydblib2 import my_select as slc
from scipy.stats import ttest_ind as tt, bartlett as bt

"""
SQLの設定
"""
sqlstr = f"""
SELECT *
FROM siken2
;
"""
# dataの抽出
siken = slc("webprog", sqlstr)
j_avg = siken["Jpn"].mean()
m_avg = siken["Math"].mean()
# 平均
print(f"数学平均：{m_avg.round(3)}\n国語平均：{j_avg.round(3)}")
# f検定
b_val, p_val = bt(siken['Math'], siken['Jpn'])
print(f"Bartlett p_val= {p_val.round(5)}")

# t検定
if (p_val >= 0.05):
    t_val, p_val = tt(siken['Math'], siken['Jpn'], equal_var=True)
else:
    t_val, p_val = tt(siken['Math'], siken['Jpn'], equal_var=False)

print(f"ttes p_val= {p_val.round(5)}")
