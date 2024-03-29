import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from mydblib import my_select as slc

frm = "post_office"
city = "茅野市"
prefecture = ("長野県", "新潟県", "富山県", "石川県", "福井県")

sqlstring = f"""
    SELECT prefecture, COUNT(prefecture) AS pcnt
    FROM {frm}
    WHERE prefecture IN {prefecture}
    GROUP BY prefecture
    ;
"""

postNum = slc(sqlstring)
print(postNum)
# make graph
plt.bar(postNum["prefecture"], postNum["pcnt"],
        tick_label=postNum["prefecture"])
plt.title("北信越地方県別事業所数")
plt.xlabel("県名")
plt.ylabel("登録数便番号数")
plt.savefig("./img/En0305.png")
